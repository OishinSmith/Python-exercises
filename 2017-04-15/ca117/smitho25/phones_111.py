phone = (r"\b08[5,6][\s\,-]\d{7}\b")


def main():
    
    import re
    import sys
    phone_regex = re.compile(phone)

    s = sys.stdin.read()

    phonelist = phone_regex.findall(s)
    for n in phonelist:
        print(n)

if __name__ == '__main__':
    main()

