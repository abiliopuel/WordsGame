import random
import time

class WordsGame:
    def __init__(self):
        self.words_list = ['consider', 'minute', 'around', 'accord', 'evident', 'practice', 'intend', 'concern', 'commit', 'issue', 'approach', 'establish', 'utter', 'conduct', 'engage', 'obtain',
        'scarce', 'policy', 'straight', 'stock', 'apparent', 'property', 'fancy', 'concept', 'court', 'appoint', 'passage', 'vain', 'instance', 'coast', 'project']
        self.words_in_game = []
        self.words_amount = 10

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
            start_command = input("")
            if start_command.upper() == "!START":
                return self.inGame()
            if start_command.upper() == "!OPTIONS":
                return self.options()
            if start_command.upper() == "!HELP":
                return self.helpp()
            elif start_command.upper() == "!CLOSE":
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
            options_command = input("")
            if "!words" in options_command:
                options_command = options_command.replace("!words", "")
                options_command = options_command.replace(" ", "")
                options_command = int(options_command)
                self.words_amount = options_command
                print("Words amount defined to: {}.".format(self.words_amount))
                continue
            elif options_command.upper() == "!MENU":
                return self.menu()
            else:
                print("\nPlease use the listed commands.")

    def helpp(self):
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
            help_command = input("")
            if help_command.upper() == "!MENU":
                return self.menu()
            else:
                print("\nPlease use the listed commands.")

    def inGame(self):
        self.words_in_game.clear()
        for i in range(self.words_amount):
            self.words_in_game.append(self.words_list[random.randint(0, (len(self.words_list)-1))])
        print(self.words_in_game)
        print("\nStarting in..")
        time.sleep(1)
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)
        print("\nSTART TYPING...\n")

        start_time = time.time()
        words_writed = input("\n")
        end_time = time.time()
        words_writed2 = ("[{}]".format(words_writed))
        words_writed_list = words_writed2.strip('][').split(' ')
        words_correct = 0
        char = 0

        for i in range(0, len(words_writed_list)):
            if words_writed_list[i] == self.words_in_game[i]:
                words_correct += 1
                char = char + len(words_writed_list[i])

        gametime = end_time-start_time
        wpm = (60*(((char/5)*words_correct)/len(self.words_in_game)))/gametime
                
        print("")
        print("================GAME ENDED================")
        print("")
        print("Your pontuation:")
        print("  WPM: {:.2f}.".format(wpm))
        print("  Accuracy: {0}/{1} ({2:.2f}%).".format(words_correct, len(self.words_in_game), (100*words_correct)/len(self.words_in_game)))
        print("  Time: {:.2f}s.".format(gametime))
        print("")
        print("!menu -> Back to main menu.")
        print("!close -> Close the game.")
        print("")
        print("==========================================")

game = WordsGame()
game.menu()