import secrets
import string
import random
import sys

written = ""
a = ""
pass_chars = ""
ex_characters = "..__:!"
password = ""

def error(contain, function=None):
    print("Location: "+function+"() Error has occured: "+contain)


class setup:
    def symbol_replace(self, strings):
        import re
        global pass_chars
        time = 0
        symbol = 0
        pattern = r'[!_:.]+'
        sentence = strings
        #strings = strings[:1]
        for i in range(len(sentence)):
            try:
                match = re.search(pattern, strings[i])

                if match:
                    if symbol > 0:
                        sentence = sentence.replace(sentence[i], '')
                        time = time + 1
                    symbol = 2
                symbol = symbol - 1
            except:
                break
        pass_chars = string.ascii_letters
        r = self.password(time, mode="basic")
        sentence = sentence + r

        return sentence
    

    def password(self, length, mode="basic"):
        global pass_chars, password
        if mode == "basic":#You can set new app in there.
            pass
        elif mode == "micro":
            pass_chars = string.ascii_letters + ex_characters
            password = ''.join(secrets.choice(pass_chars) for x in range(length))
            password = self.symbol_replace(password)
            return password
        elif mode == "cute":
            pass_chars = string.ascii_lowercase + string.digits + '___'
        else:
            error("The mode is not defined.", function="randomPass")
            return "QUIT"
        password = ''.join(secrets.choice(pass_chars) for x in range(length))
        return password
    
    def writeFile(self, file="myfile.txt",
                  length=None):
        global written, password
        f = open(file, 'w')
        written = password
        f.write(written)

        f.close()
        print("Password: "+written)

    def ask(self):
        global a, pass_chars
        a = input("Use symbols?[y/n]: ")
        if a == "n":    
            pass_chars = string.ascii_letters
        else:
            pass_chars = string.ascii_letters + string.digits+string.punctuation

def main():
    strong = setup()
    strong.ask()
    strong.password(length=random.randint(8, 12))
    strong.writeFile()

if __name__ == '__main__':
    main()
