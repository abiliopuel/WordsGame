import random
import time

class WordsGame:
    def __init__(self):
        self.wordsList = ['consider', 'minute', 'around', 'accord', 'evident', 'practice', 'intend', 'concern', 'commit', 'issue', 'approach', 'establish', 'utter', 'conduct', 'engage', 'obtain',
        'scarce', 'policy', 'straight', 'stock', 'apparent', 'property', 'fancy', 'concept', 'court', 'appoint', 'passage', 'vain', 'instance', 'coast', 'project']
        self.wordsInGame = []
        self.wordsAmount = 10

    def menu(self):
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


    def options(self):
        print("===================OPTIONS===================")
        print("")
        print("!words <WORDS AMOUNT> -> Change the amount of")
        print("                         words to type.")
        print("                         DEFAULT: 10 words.")
        print("!menu -> Back to main menu.")
        print("")
        print("=============================================")
        while True:
            optionsCommand = input("")
            if "!words" in optionsCommand:
                optionsCommand = optionsCommand.replace("!words", "")
                optionsCommand = optionsCommand.replace(" ", "")
                optionsCommand = int(optionsCommand)
                self.wordsAmount = optionsCommand
                print("Words amount defined to: {}.".format(self.wordsAmount))
                continue
            elif optionsCommand.upper() == "!MENU":
                return self.menu()
            else:
                print("\nPlease use the listed commands.")

    def help(self):
        print("====================HELP====================")
        print("")
        print("In this game your goal is to rewrite the")
        print("the listed words as quickly as you can.")
        print("At the end of each match, you will have")
        print("acess to your score. Here you can find your")
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

    def inGame(self):
        self.wordsInGame.clear()
        for i in range(self.wordsAmount):
            self.wordsInGame.append(self.wordsList[random.randint(0, (len(self.wordsList)-1))])
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
        wordsWritten = input("\n")
        endTime = time.time()
        wordsWritten2 = ("[{}]".format(wordsWritten))
        wordsWrittenList = wordsWritten2.strip('][').split(' ')
        wordsCorrect = 0
        char = 0

        for i in range(0, len(wordsWrittenList)):
            if wordsWrittenList[i] == self.wordsInGame[i]:
                wordsCorrect += 1
                char = char + len(wordsWrittenList[i])

        gametime = endTime-startTime
        wpm = (60*(((char/5)*wordsCorrect)/len(self.wordsInGame)))/gametime
                
        print("")
        print("================GAME ENDED================")
        print("")
        print("Your pontuation:")
        print("  WPM: {:.2f}.".format(wpm))
        print("  Accuracy: {0}/{1} ({2:.2f}%).".format(wordsCorrect, len(self.wordsInGame), (100*wordsCorrect)/len(self.wordsInGame)))
        print("  Time: {:.2f}s.".format(gametime))
        print("")
        print("!menu -> Back to main menu.")
        print("!close -> Close the game.")
        print("")
        print("==========================================")

game = WordsGame()
game.menu()