import json
import time
from password_assemble import make_password

index = 0
label_list = []
name_list = []

wrong = False

def add(site=None, mailadress=None, password=None, user=None, filename="password_info.json"):
    info = {}
    if len(label_list) == 0:
        info = {"サイト": site, "ユーザー名": user, "パスワード": password}
    elif len(label_list) == 1:
         info = {"サイト": site, "ユーザー名": user, "パスワード": password, label_list[0]: name_list[0]}
    else:
         info = {"サイト": site, "ユーザー名": user, "パスワード": password, label_list[0]: name_list[0], label_list[1]: name_list[1]}
    with open(filename, "r+", encoding="utf-8") as file:
        file_content = json.load(file)
        file_content[mailadress].append(info)
        file.seek(0)
        json.dump(file_content, file, indent=4, ensure_ascii=False)

print("パスワードキーパーへようこそ ^^")
time.sleep(0.5)

def password():
    strong = make_password.setup()
    return strong.password(15, mode="micro")

customer_info = input("メールアドレスを教えてください： ")
with open('password_info.json', encoding="utf-8") as f:
    j = json.load(f)
try:
    name = j[customer_info]
except :
    wrong = True
    while wrong:
            print("メールアドレスが間違っています")
            time.sleep(0.5)
            customer_info = input("メールアドレスを教えてください： ")
            try:
                name = j[customer_info]
                wrong = False
            except :
                wrong = True
print(f"おかえりなさい、{customer_info}!")
time.sleep(0.5)
site = input("サイトの名前はなんですか？： ")
username = input("ユーザー名を教えてください： ")
a = input("強力なパスワードを提案しますか？[y/n]: ")
if a == 'n':
    strong_password = input("貴方のパスワードを教えてください： ")
    time.sleep(0.5)
else:
    time.sleep(0.5)
    strong_password = password()
    print("強力なパスワード（コピーしてください）： ", strong_password)
    time.sleep(3)
a = input("他の情報を入れますか？（リンク、筆名など）[y/n]: ")

if a == 'y':
     while a == 'y' and index <= 2:
          lbl = input("ラベルを教えてください： ")
          contain = input("内容を教えてください： ")
          index = index + 1
          label_list.append(lbl)
          name_list.append(name)
          
          time.sleep(0.5)
          if index != 2:
              a = input("他の情報を入れますか？（リンク、筆名など）[y/n]: ")
        

print("またお越しください🙌")
time.sleep(1.5)
add(site=site, mailadress=customer_info, password=strong_password, user=username)


     





