import random


def set_seed(img):
    random.seed(100)


class WordBank:
    f1 = None
    f2 = None
    f3 = None
    f4 = None
    f5 = None
    f6 = None
    f7 = None

    l1 = []
    l2 = []
    l3 = []
    l4 = []
    l5 = []
    l6 = []
    l7 = []

    def __init__(self):
        self.f1 = open("one.txt", "r")
        self.f2 = open("two.txt", "r")
        self.f3 = open("three.txt", "r")
        self.f4 = open("four.txt", "r")
        self.f5 = open("five.txt", "r")
        self.f6 = open("six.txt", "r")
        self.f7 = open("seven.txt", "r")

        for x in self.f1:
            self.l1.append(x)

        for x in self.f2:
            self.l2.append(x)

        for x in self.f3:
            self.l3.append(x)

        for x in self.f4:
            self.l4.append(x)

        for x in self.f5:
            self.l5.append(x)

        for x in self.f6:
            self.l6.append(x)

        for x in self.f7:
            self.l7.append(x)

    def pull_word(self, syl):
        pass


def main():
    pass


if __name__ == "__main__":
    main()
