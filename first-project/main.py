def main():
    hello()
    name = input("What is your name? ")
    hello(name)


def hello(to="world"):
    print("hello,", to)


main()




