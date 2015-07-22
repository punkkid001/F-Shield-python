# -*- coding : utf-8 -*-

class example:
    def __init__(self, username):
        self.username=username
        print("Your name is %s"%username)
        print("\n")

    def textViewer(self, sentence):
        print("Hi %s"%self.username)
        print("***** Text Viewer *****")
        print(sentence)
        print("***** End Of Text *****")
        print("\n")

class new_example:
    def __init__(self, username):
        self.username=username

    def printName(self):
        print("%s, you can print your name\n"%self.username)
