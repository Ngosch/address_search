# sample01を呼び出し、double関数を使う
from sample01 import double


def main():
    number = 5
    print(f"{number}の2倍は{double(number)}")


if __name__ == "__main__":
    main()
