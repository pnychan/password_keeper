import make_password
written = ""
strong = make_password.setup()
strong.password(15, mode="micro")
strong.writeFile()

