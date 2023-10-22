import secrets
import string
import random

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
    

    def password(self, length, mode="basic", ascii_only=None):
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
        elif mode == "ascii_only":
            if ascii_only == "uppercase":
                pass_chars = string.ascii_uppercase
            elif ascii_only == "lowercase":
                pass_chars = string.ascii_lowercase
            elif ascii_only == "letters":
                pass_chars = string.ascii_letters
            elif ascii_only == "ex_characters":
                pass_chars = ex_characters
            elif ascii_only == "digits":
                pass_chars = string.digits
            elif ascii_only == "symbols":
                pass_chars = string.punctuation
            else:
                pass_chars = ascii_only
        else:
            error("The mode is not defined.", function="randomPass")
            return "QUIT"
        password = ''.join(secrets.choice(pass_chars) for x in range(length))
        return password
    
    def writeFile(self, file="myfile.txt", passwords=None):
        global written, password
        f = open(file, 'w')
        if passwords ==None:
            written = password
        else:
            written = passwords
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
