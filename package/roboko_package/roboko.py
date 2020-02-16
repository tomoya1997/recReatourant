import sys
import pathlib
from ..csv_file.csv import Csv as csv_file

currentdir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(currentdir)+"/../csv_file/")

class Roboko():

    def confirm(self, word):
        inputContents = input(word)
        if not inputContents:
            return self.confirm(word)
        else:
            return inputContents

    def greet(self):
        print("==========================================")
        print("こんにちわ！私の名前はロボ子です！！あなたのお名前は?")
        print("==========================================")
        self.name = self.confirm('Enter your name: ')

    def ask(self):
        print("==========================================")
        print(self.name + "さん。どこのレストランがお好きですか？")
        print("==========================================")
        self.restaurant = self.confirm('Enter your favarite restaurant name:　')
        
                            
    def suggest(self, restaurants):
        for r in restaurants:
            print("==========================================")
            print("私のオススメのレストランは" + r[0] + "です。")
            print("このレストランは好きですか？ [Yes/No]")
            print("==========================================")
            r = self.confirm("y or n:　").capitalize()
            f = ["Y", "Yes"]
            if r in f:
                break


    def toThank(self):
        print(self.name + "さん。ありがとうございました。良い一日を！さようなら！！")
