import random, time

class WordsGame:
    def __init__(self):
        self.wordsList = ['consider', 'minute', 'around', 'accord', 'evident', 'practice', 'intend', 'concern', 'commit', 'issue', 'approach', 'establish', 'utter', 'conduct', 'engage', 'obtain',
        'scarce', 'policy', 'straight', 'stock', 'apparent', 'property', 'fancy', 'concept', 'court', 'appoint', 'passage', 'vain', 'instance', 'coast', 'project']
        self.wordsInGame = []
        self.customWordsList = []
        self.wordsAmount = 10
        self.gameMode = "random"
        self.wordsCorrect = 0
        self.char = 0

    def setWordsAmount(self, amount):
        self.wordsAmount = amount

    def setGameMode(self, gamemode):
        previousGameMode = self.gameMode
        self.gameMode = gamemode
        gameModeChanged = (previousGameMode == gamemode)
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

    def hasCustomList(self):
        if len(self.customWordsList) == 0:
            return False

        return True
         
    def preGameConfig(self):
        print(1000*"\n")
        self.wordsInGame.clear()
        if self.gameMode == "random":
            for i in range(self.wordsAmount):
                self.wordsInGame.append(self.wordsList[random.randint(0, (len(self.wordsList)-1))])
        if self.gameMode == "custom":
            for i in range(self.wordsAmount):
                self.wordsInGame.append(self.customWordsList[random.randint(0, (len(self.customWordsList)-1))])
        menu.preGame()

    def inGame(self):
        self.wordsCorrect = 0
        self.char = 0
        self.startTime = time.time()
        wordsWritten = input("\n").split(" ")
        self.endTime = time.time()
        
        while len(wordsWritten) > len(self.wordsInGame):
            correctList = len(wordsWritten) - len(self.wordsInGame)
            wordsWritten.remove(wordsWritten[-correctList])
        for i in range(0, len(wordsWritten)):
            if wordsWritten[i] == self.wordsInGame[i]:
                self.wordsCorrect += 1
                self.char = self.char + len(wordsWritten[i])
        
        menu.endMenu()

class Menu:

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
            startCommand = input("")
            startCommand = startCommand.lower()
            if startCommand == "!start":
                return game.preGameConfig()
            if startCommand == "!options":
                return self.optionsMenu()
            if startCommand == "!help":
                return self.helpMenu()
            elif startCommand == "!close":
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
            optionsCommand = input("")
            optionsCommand = optionsCommand.lower()
            #!words
            if optionsCommand[0:6] == "!words":
                optionsCommand = optionsCommand.replace("!words ", "")
                if optionsCommand.isnumeric():
                    optionsCommand = int(optionsCommand)
                    game.setWordsAmount(optionsCommand)
                    print("Words amount defined to: {}.".format(game.wordsAmount))
                    continue
                elif not optionsCommand.isnumeric():
                    print("The actual amount of words in your game is: {}.".format(game.wordsAmount))
            #!menu
            elif optionsCommand == "!menu":
                return self.mainMenu()
            #!custom
            elif optionsCommand == "!custom":
                return self.customMenu()
            #!mode
            elif optionsCommand[0:5] == "!mode":
                optionsCommand = optionsCommand.replace("!mode ", "")
                if optionsCommand == "random":
                    if game.setGameMode("random"):
                        print("You changed the game mode to random words.")
                    else:
                        print("The game mode is already on random words mode.")
                elif optionsCommand == "custom":
                    if len(game.customWordsList) == 0:
                        print("You don't have a custom words list or you removed all words from your custom list.\nPlease do !custom and manage it.")
                    else:
                        if game.setGameMode("custom"):
                            print("The game mode is already on custom words mode.")
                        else:
                            print("You changed the game mode to custom words.")
                else:
                    print("The actual mode is: {}.".format(game.gameMode))
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
            customCommand = input("")
            customCommand = customCommand.lower()
            #!add
            if customCommand[0:4] == "!add":
                customCommand = customCommand.replace("!add ", "")
                if not customCommand.isnumeric():
                    if " " in customCommand:
                        print("Please add one word at a time.")
                    else:
                        if game.appendCustomWord(customCommand):
                            print("Added the \"{}\" word to your custom list.".format(customCommand))
                        else:
                            print("The word \"{}\" is already on your custom list.".format(customCommand))
                else:
                    print("Please don't use digits on your custom words.")
            #!remove
            elif customCommand[0:7] == "!remove":
                customCommand = customCommand.replace("!remove ", "")
                if " " not in customCommand:
                    if game.removeCustomWord(customCommand):
                        print("Removed the \"{}\" word from your custom list.".format(customCommand))
                    else:
                        print("This word is not on your custom list.")
                else:
                    print("Please remove one word at a time.")
            #!clear
            elif customCommand == "!clear":
                if game.clearCustomList():
                    print("You cleared your custom list.")
                else:
                    print("You don't have a custom words list to clear.\nPlease use the commands in menu to manage it.")
            #!list
            elif customCommand == "!list":
                if game.hasCustomList():
                    print("This is your custom list:")
                    print(game.getCustomWordsList())
                else:
                    print("You don't have a custom list. Use the commands in the menu to manage it.")
            #!menu
            elif customCommand == "!menu":
                return self.mainMenu()
            #!options
            elif customCommand == "!options":
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
            helpCommand = input("")
            if helpCommand.upper() == "!MENU":
                return self.mainMenu()
            else:
                print("\nPlease use the listed commands.")

    def preGame(self):
        print(game.wordsInGame)
        print("\nStarting in..")
        time.sleep(0.1)
        print("3")
        time.sleep(0.1)
        print("2")
        time.sleep(0.1)
        print("1")
        time.sleep(0.1)
        print("\nSTART TYPING...\n")
        game.inGame()


    def endMenu(self):
        print(1000*"\n")
        print("================GAME ENDED================")
        print("")
        print("Your pontuation:")
        print("  WPM: {:.2f}.".format(score.WPM()))
        print("  Accuracy: {0}/{1} ({2}%).".format(score.accuracyWordsCorrect(), score.accuracyWordsInGame(), score.accuracyPorcentage()))
        print("  Time: {:.2f}s.".format(score.scoretime()))
        print("")
        print("!menu -> Back to main menu.")
        print("!close -> Close the game.")
        print("!more -> More info about this match.")
        print("")
        print("==========================================")
        while True:
            endCommand = input("")
            if endCommand.upper() == "!MENU":
                return self.mainMenu()
            elif endCommand.upper() == "!CLOSE":
                print("Closing the game.")
                exit()
            else:
                print("\nPlease use the listed commands.")

class Score:

    def WPM(self):
        wpm = ((60*(((game.char/5)*(game.wordsCorrect)/len(game.wordsInGame))))/(game.endTime - game.startTime))
        return wpm

    def accuracyWordsCorrect(self):
        return game.wordsCorrect

    def accuracyWordsInGame(self):
        return len(game.wordsInGame)

    def accuracyPorcentage(self):
        porcentage = (100*game.wordsCorrect/len(game.wordsInGame))
        return porcentage

    def scoretime(self):
        return (game.endTime - game.startTime)

menu = Menu()
score = Score()
game = WordsGame()
menu.mainMenu()