def main():
    string = input()
    string = convert(string)
    print(string)

def convert(sstring):
    sstring= sstring.replace(":)", "🙂").replace(":(", "🙁")
    return sstring


main()