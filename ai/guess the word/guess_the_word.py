from random import choice
from main import speak
class Game:
    def __init__(self,words_list):
        self.words_list = words_list
        
    @classmethod
    def fromWords(cls, data):
        return cls(data.split("\n"))

    def randomword(self):
        self.main_word = choice(self.words_list)
        self.store_word = self.main_word

    def usword(self):
        self.user_word = input(f"Enter any {len(self.main_word)} letter word:")
        
        
    def analyse(self):
        if len(self.user_word) == len(self.main_word):
            for index,letter in enumerate(self.user_word):
                
                if letter == self.main_word[index]:
                    print(f"{letter} = GREEN")
                    self.remove_letter(letter)
                else:
                    if self.analyse_yellow(letter):
                        print(f"{letter} = YELLOW")
                        self.remove_letter(letter)
                    else:
                        print(f"{letter} = RED")
        else:
            print("INVALID INPUT")
        self.main_word = self.store_word

    def analyse_yellow(self, letter):
        for main_letter_word in self.main_word:
            if letter == main_letter_word:
                return True

    def remove_letter(self,letter):
        letter_in = self.main_word.find(letter)
        if letter_in == 0:
            self.main_word = f" {self.main_word[1:]} "
        elif letter_in == len(self.main_word)-1:
            self.main_word =f"{self.main_word[0:len(self.main_word)-1]} "
        else:
            self.main_word = f"{self.main_word[0:letter_in]} {self.main_word[letter_in+1:]}"
     
with open("guess the word/word_list.txt", "r") as f:
    all_words = f.read()
game = Game.fromWords(all_words)
game.randomword()
while True:
    game.usword()
    if game.user_word == game.main_word:
        speak("You got it right")
        break
    elif game.user_word == "QUIT":
        speak(f"The correct word is {game.main_word}")
        break
    else:
        game.analyse()