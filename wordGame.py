from os import remove
import random, time

class Score:

    def __init__(self, wordsList, wordsWritten, time):
        wordsCorrect = []
        for i in range(0, len(wordsWritten)):
            if wordsWritten[i] == wordsList[i]:
                wordsCorrect.append(wordsWritten[i])
        totalChars = sum(len(x) for x in wordsCorrect)
        self.wpm = 60*(totalChars/5)/time
        self.accuracy = len(wordsCorrect)/len(wordsList)
        self.time = time
        self.wordsCorrectAmount = len(wordsCorrect)
        self.wordsTotalAmount = len(wordsList)

    def getWordsCorrectAmount(self):
        return self.wordsCorrectAmount

    def getWordsTotalAmount(self):
        return self.wordsTotalAmount

    def getWpm(self):
        return self.wpm

    def getAccuracy(self):
        return self.accuracy

    def getTime(self):
        return self.time

class WordsGame:
    def __init__(self):
        self.wordsList = ['consider', 'minute', 'around', 'accord', 'evident', 'practice', 'intend', 'concern', 'commit', 'issue', 'approach', 'establish', 'utter', 'conduct', 'engage', 'obtain',
        'scarce', 'policy', 'straight', 'stock', 'apparent', 'property', 'fancy', 'concept', 'court', 'appoint', 'passage', 'vain', 'instance', 'coast', 'project']
        self.wordsInGame = []
        self.customWordsList = []
        self.wordsAmount = 10
        self.gameMode = "random"

    def setWordsAmount(self, amount):
        self.wordsAmount = amount

    def setGameMode(self, gamemode: str) -> bool:
        previousGameMode = self.gameMode
        self.gameMode = gamemode
        gameModeChanged = (previousGameMode != gamemode)
        return gameModeChanged

    def appendCustomWord(self, customWord):
        if customWord in self.customWordsList:
            return False

        self.customWordsList.append(customWord)
        return True

    def removeCustomWord(self, customWord):
        if customWord not in self.customWordsList:
            return False

        self.customWordsList.remove(customWord)
        return True

    def clearCustomList(self):
        if len(self.customWordsList) == 0:
            return False
        
        self.customWordsList.clear()
        return True

    def getCustomWordsList(self):
        return self.customWordsList

    def getWordsInGame(self):
        return self.wordsInGame

    def hasCustomList(self):
        if len(self.customWordsList) == 0:
            return False

        return True
        
    def preGameConfig(self):
        self.wordsInGame.clear()
        if self.gameMode == "random":
            for i in range(self.wordsAmount):
                self.wordsInGame.append(self.wordsList[random.randint(0, (len(self.wordsList)-1))])
        if self.gameMode == "custom":
            for i in range(self.wordsAmount):
                self.wordsInGame.append(self.customWordsList[random.randint(0, (len(self.customWordsList)-1))])

    def inGame(self, wordsWritten, startTime, endTime):
        wordsWritten = wordsWritten[0:len(self.wordsInGame)]

        return Score(self.wordsInGame, wordsWritten, endTime-startTime)

class Menu:

    def __init__(self):
        self.game = WordsGame()

    def mainMenu(self):
        print(1000*"\n")
        print("================TYPE FAST GAME================")
        print("")
        print("!start -> Start the game.")
        print("!options -> Change some options of the game.")
        print("!help -> Some information of the game.")
        print("!close -> Close the game.")
        print("")
        print("=============================================")
        while True:
            startCommand = Command()
            if startCommand.command == "!start":
                self.game.preGameConfig()
                self.preGame()
                startTime = time.time()
                inputWords = input("\n").split(" ")
                endTime = time.time()
                gameScore = self.game.inGame(inputWords, startTime, endTime)
                return self.endMenu(gameScore)
            if startCommand.command == "!options":
                return self.optionsMenu()
            if startCommand.command == "!help":
                return self.helpMenu()
            elif startCommand.command == "!close":
                print("Closing the game.")
                exit()
            else:
                print("\nPlease use the listed commands.")

    def optionsMenu(self):
        print(1000*"\n")
        print("=====================OPTIONS=====================")
        print("")
        print("!words <WORDS AMOUNT> -> Change the amount of")
        print("                         words of list random")
        print("                         DEFAULT: 10 words.")
        print("")
        print("!custom -> Manage your custom list with your own")
        print("           words.")
        print("")
        print("!mode <RANDOM/CUSTOM> -> Change the mode")
        print("                         between your custom")
        print("                         list or a random list.")
        print("")
        print("!menu -> Back to main menu.")
        print("")
        print("=================================================")
        while True:
            optionsCommand = Command()
            if optionsCommand.command == "!words":
                if optionsCommand.hasArgs() and optionsCommand.args[0].isnumeric():
                    wordsAmount = int(optionsCommand.args[0])
                    self.game.setWordsAmount(wordsAmount)
                    print("Words amount defined to: {}.".format(self.game.wordsAmount))
                    continue
                else:
                    print("The actual amount of words in your game is: {}.".format(self.game.wordsAmount))
            elif optionsCommand.command == "!menu":
                return self.mainMenu()
            elif optionsCommand.command == "!custom":
                return self.customMenu()
            elif optionsCommand.command == "!mode":
                if optionsCommand.hasArgs() and optionsCommand.args[0] == "random":
                    if self.game.setGameMode("random"):
                        print("You changed the game mode to random words.")
                    else:
                        print("The game mode is already on random words mode.")
                elif optionsCommand.hasArgs() and optionsCommand.args[0] == "custom":
                    if len(self.game.customWordsList) == 0:
                        print("You don't have a custom words list or you removed all words from your custom list.\nPlease do !custom and manage it.")
                    else:
                        if self.game.setGameMode("custom"):
                            print("The game mode is already on custom words mode.")
                        else:
                            print("You changed the game mode to custom words.")
                else:
                    print("The actual mode is: {}.".format(self.game.gameMode))
            else:
                print("Please use the listed commands.")

    def customMenu(self):
        print(1000*"\n")
        print("=====================CUSTOM=====================")
        print("")
        print("!add <WORD> -> Add a word to your custom list.")
        print("!remove <WORD> -> Remove a word from you")
        print("                  custom list.")
        print("")
        print("!clear -> Remove all the words from your custom")
        print("          list.")
        print("")
        print("!list -> List your actual list of words.")
        print("!options -> Back to options menu.")
        print("!menu -> Back to main menu.")
        print("")
        print("=====================CUSTOM=====================")
        while True:
            customCommand = Command()
            if customCommand.command == "!add":
                addedWordsList = []
                for word in customCommand.args:
                    if self.game.appendCustomWord(word):
                        addedWordsList.append(word)
                    else:
                        print("The word \"{}\" is already on your custom list.".format(word))
                print("Added the {} words to your custom list.".format(addedWordsList))
            elif customCommand.command == "!remove":
                removedWordsList = []
                for removedWord in customCommand.args:
                    if self.game.removeCustomWord(removedWord):
                        removedWordsList.append(removedWord)
                    else:
                        print("The word \"{}\" is not on your custom list.".format(removedWord))
                print("Removed the {} words from your custom list.".format(removedWordsList))
            elif customCommand.command == "!clear":
                if self.game.clearCustomList():
                    print("You cleared your custom list.")
                else:
                    print("You don't have a custom words list to clear.\nPlease use the commands in menu to manage it.")
            elif customCommand.command == "!list":
                if self.game.hasCustomList():
                    print("This is your custom list:")
                    print(self.game.getCustomWordsList())
                else:
                    print("You don't have a custom list. Use the commands in the menu to manage it.")
            elif customCommand.command == "!menu":
                return self.mainMenu()
            elif customCommand.command == "!options":
                return self.optionsMenu()
            else:
                print("Please use the listed commands.")

    def helpMenu(self):
        print(1000*"\n")
        print("====================HELP====================")
        print("")
        print("In this game your goal is to rewrite the")
        print("listed words as quickly as you can.")
        print("At the end of each match, you will have")
        print("acess to your score. There you can find your")
        print("WPM(Words per minute), time and accuracy.")
        print("")
        print("!menu -> Back to main menu.")
        print("")
        print("===============================================")
        while True:
            helpCommand = Command()
            if helpCommand.command == "!menu":
                return self.mainMenu()
            else:
                print("\nPlease use the listed commands.")

    def preGame(self):
        print(self.game.getWordsInGame())
        print("\nStarting in..")
        time.sleep(0.5)
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)
        print("\nSTART TYPING...\n")

    def endMenu(self, score: Score):
        #print(1000*"\n")
        print("================GAME ENDED================")
        print("")
        print("Your pontuation:")
        print("  WPM: {:.2f}.".format(score.getWpm()))
        print("  Accuracy: {0}/{1} ({2}%).".format(score.getWordsCorrectAmount(), score.getWordsTotalAmount(), 100*score.getAccuracy()))
        print("  Time: {:.2f}s.".format(score.getTime()))
        print("")
        print("!menu -> Back to main menu.")
        print("!close -> Close the game.")
        print("!more -> More info about this match.")
        print("")
        print("==========================================")
        while True:
            endCommand = Command()
            if endCommand.command == "!menu":
                return self.mainMenu()
            elif endCommand.command == "!close":
                print("Closing the game.")
                exit()
            else:
                print("\nPlease use the listed commands.")

class Command:

    def __init__(self):
        a = input().split(" ")
        self.command = a[0].lower()
        self.args = a[1:]

    def hasArgs(self) -> bool:
        return len(self.args) > 0

Menu().mainMenu()