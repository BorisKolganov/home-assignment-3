import re
from culc import Culc
class CulcCI():
    def __init__(self):
        self.culc = Culc()


    def __parser__(self, str):
        return filter(None, re.split('([0-9]+[eE][-+]?[0-9]+){0,1}([\-\+\*\/\^])', str.replace(" ",""), 1))

    def run(self):
        print ("Welcome to culc")
        print ("You can: +, -, *, / and ^")
        while True:
            buf = ""
            try:
                buf = raw_input("Please, enter the expression: ")
            except EOFError:
                exit()
            print (self.proc(buf))


    def proc(self, exp):
        l = self.__parser__(exp)
        try:
            return {
                "+": lambda x, y: self.culc.sum(x, y),
                "-": lambda x, y: self.culc.dif(x, y),
                "*": lambda x, y: self.culc.mul(x, y),
                "/": lambda x, y: self.culc.div(x, y),
                "^": lambda x, y: self.culc.pow(x, y),
            }[l[1]](l[0], l[2])
        except:
            return "Sorry, smth wrong with your expression"
