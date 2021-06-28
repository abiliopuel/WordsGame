import random
import time

class WordsGame:
    def __init__(self):
        self.wordsList = ['consider', 'minute', 'around', 'accord', 'evident', 'practice', 'intend', 'concern', 'commit', 'issue', 'approach', 'establish', 'utter', 'conduct', 'engage', 'obtain',
        'scarce', 'policy', 'straight', 'stock', 'apparent', 'property', 'fancy', 'concept', 'court', 'appoint', 'passage', 'vain', 'instance', 'coast', 'project']
        self.wordsInGame = []
        self.customWordsList = []
        self.wordsAmount = 10
        self.gameMode = "random"

    def menu(self):
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
            startCommand = input("")
            if startCommand.upper() == "!START":
                return self.inGame()
            if startCommand.upper() == "!OPTIONS":
                return self.options()
            if startCommand.upper() == "!HELP":
                return self.help()
            elif startCommand.upper() == "!CLOSE":
                print("Closing the game.")
                exit()
            else:
                print("\nPlease use the listed commands.")

    def setWordsAmount(self, amount):
        self.wordsAmount = amount

    def setGameMode(self, gamemode):
        previousGameMode = self.gameMode
        self.gameMode = gamemode
        gameModeChanged = (previousGameMode == gamemode)
        return gameModeChanged

    def options(self):
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
            optionsCommand = input("")
            #!words
            if optionsCommand[0:6].upper() == "!WORDS":
                optionsCommand = optionsCommand.replace("!words ", "")
                if optionsCommand.isnumeric():
                    optionsCommand = int(optionsCommand)
                    self.setWordsAmount(optionsCommand)
                    print("Words amount defined to: {}.".format(self.wordsAmount))
                    continue
                elif not optionsCommand.isnumeric():
                    print("The actual amount of words in your game is: {}.".format(self.wordsAmount))
            #!menu
            elif optionsCommand.upper() == "!MENU":
                return self.menu()
            #!custom
            elif optionsCommand.upper() == "!CUSTOM":
                return self.custom()
            #!mode
            elif optionsCommand[0:5].upper() == "!MODE":
                optionsCommand = optionsCommand.replace("!mode ", "")
                if optionsCommand.upper() == "RANDOM":
                    if self.setGameMode("random"):
                        print("You changed the game mode to random words.")
                    else:
                        print("The game mode is already on random words mode.")
                elif optionsCommand.upper() == "CUSTOM":
                    if len(self.customWordsList) == 0:
                        print("You don't have a custom words list or you removed all words from your custom list.\nPlease do !custom and manage it.")
                    else:
                        if self.setGameMode("custom"):
                            print("The game mode is already on custom words mode.")
                        else:
                            print("You changed the game mode to custom words.")
                else:
                    print("The actual mode is: {}.".format(self.gameMode))
            else:
                print("Please use the listed commands.")

    def help(self):
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
            helpCommand = input("")
            if helpCommand.upper() == "!MENU":
                return self.menu()
            else:
                print("\nPlease use the listed commands.")

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

    def showCustomList(self):
        if len(self.customWordsList) == 0:
            return False

        print("This is your custom list:")
        print(self.customWordsList)
        return True
         

    def custom(self):
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
            customCommand = input("")
            #!add
            if customCommand[0:4].upper() == "!ADD":
                customCommand = customCommand.replace("!add ", "")
                if not customCommand.isnumeric():
                    if " " in customCommand:
                        print("Please add one word at a time.")
                    else:
                        if self.appendCustomWord(customCommand):
                            print("Added the \"{}\" word to your custom list.".format(customCommand))
                        else:
                            print("The word \"{}\" is already on your custom list.".format(customCommand))
                else:
                    print("Please don't use digits on your custom words.")
            #!remove
            elif customCommand[0:7].upper() == "!REMOVE":
                customCommand = customCommand.replace("!remove ", "")
                if " " not in customCommand:
                    if self.removeCustomWord(customCommand):
                        print("Removed the \"{}\" word from your custom list.".format(customCommand))
                    else:
                        print("This word is not on your custom list.")
                else:
                    print("Please remove one word at a time.")
            #!clear
            elif customCommand.upper() == "!CLEAR":
                if self.clearCustomList():
                    print("You cleared your custom list.")
                else:
                    print("You don't have a custom words list to clear.\nPlease use the commands in menu to manage it.")
            #!list
            elif customCommand.upper() == "!LIST":
                if not self.showCustomList():
                    print("You don't have a custom list. Use the commands in the menu to manage it.")
            #!menu
            elif customCommand.upper() == "!MENU":
                return self.menu()
            #!options
            elif customCommand.upper() == "!OPTIONS":
                return self.options()
            else:
                print("Please use the listed commands.")

    def inGame(self):
        print(1000*"\n")
        self.wordsInGame.clear()
        if self.gameMode == "random":
            for i in range(self.wordsAmount):
                self.wordsInGame.append(self.wordsList[random.randint(0, (len(self.wordsList)-1))])
        if self.gameMode == "custom":
            for i in range(self.wordsAmount):
                self.wordsInGame.append(self.customWordsList[random.randint(0, (len(self.customWordsList)-1))])
        print(self.wordsInGame)
        print("\nStarting in..")
        time.sleep(1)
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)
        print("\nSTART TYPING...\n")

        startTime = time.time()
        wordsWritten = input("\n").split(" ")
        endTime = time.time()
        wordsCorrect = 0
        char = 0

        for i in range(0, len(wordsWritten)):
            if wordsWritten[i] == self.wordsInGame[i]:
                wordsCorrect += 1
                char = char + len(wordsWritten[i])

        gametime = endTime-startTime
        wpm = ((60*(((char/5)*wordsCorrect)/len(self.wordsInGame)))/gametime)
                
        print(1000*"\n")
        print("================GAME ENDED================")
        print("")
        print("Your pontuation:")
        print("  WPM: {:.2f}.".format(wpm))
        print("  Accuracy: {0}/{1} ({2:.2f}%).".format(wordsCorrect, len(self.wordsInGame), (100*wordsCorrect)/len(self.wordsInGame)))
        print("  Time: {:.2f}s.".format(gametime))
        print("")
        print("!menu -> Back to main menu.")
        print("!close -> Close the game.")
        print("!more -> More info about this match.")
        print("")
        print("==========================================")
        while True:
            endCommand = input("")
            if endCommand.upper() == "!MENU":
                return self.menu()
            elif endCommand.upper() == "!CLOSE":
                print("Closing the game.")
                exit()
            else:
                print("\nPlease use the listed commands.")

class Menu:
    def __init__(self):
        self.game = WordsGame()



game = WordsGame()
game.menu()