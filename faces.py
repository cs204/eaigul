def main():
    s = input()
    s2 = convert(s)
    print(s2)

def convert(s):
    s2 = s.replace(":)", "🙂")
    s3 = s2.replace(":(", "🙁")
    return s3

main()
