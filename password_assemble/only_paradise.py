import make_password

strong = make_password.setup()
password = strong.password(30, mode="ascii_only", ascii_only="-ー￣_")
strong.writeFile()
