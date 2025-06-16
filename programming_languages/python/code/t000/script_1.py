def say_hello(name=""):
    print(f"Hello {name.title()}!")

def main():
    name = input("Введите своё имя: ")
    say_hello(name=name)

if __name__ == "__main__":
    main()
    print(f"__name__ script_1.py is {__name__}")