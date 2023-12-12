otv = input("Приветствие: ").lower()
if otv.startswith("здравствуйте"):
    print("$0")
elif otv.startswith("з"):
    print("$20")
else:
     print("$100")