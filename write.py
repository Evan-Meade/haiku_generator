import random
import hashlib
from PIL import Image
import io


def set_seed(loc):
    img = Image.open(loc)
    m = hashlib.sha256()
    with io.BytesIO() as mem:
        img.save(mem, 'PNG')
        data = mem.getvalue()
        m.update(data)
    random.seed(m.digest())


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
        if syl == 1:
            return self.l1[random.randint(0, len(self.l1) - 1)]
        elif syl == 2:
            return self.l2[random.randint(0, len(self.l2) - 1)]
        elif syl == 3:
            return self.l3[random.randint(0, len(self.l3) - 1)]
        elif syl == 4:
            return self.l4[random.randint(0, len(self.l4) - 1)]
        elif syl == 5:
            return self.l5[random.randint(0, len(self.l5) - 1)]
        elif syl == 6:
            return self.l6[random.randint(0, len(self.l6) - 1)]
        elif syl == 7:
            return self.l7[random.randint(0, len(self.l7) - 1)]
        else:
            return ""


def chop(total):
    weights = [10, 50, 40, 20, 15, 12, 10]
    upper = sum(weights) - 1
    bounds = []
    ret = []
    for x in weights:
        bounds.append(sum(bounds) + x)
    while total > 0:
        r = random.randint(0, upper)
        bins = 1
        for x in range(1, len(bounds)):
            bins = x
            if r < bounds[x]:
                break
        if bins <= total:
            ret.append(bins)
            total -= bins
    return ret


def gen_line(wb, size):
    bins = chop(size)
    line = ''
    for x in bins:
        line = line + wb.pull_word(x).rstrip() + ' '
    return line[:len(line) - 1]


def gen_haiku(wb):
    return gen_line(wb, 5) + '\n' + gen_line(wb, 7) + '\n' + gen_line(wb, 5)


def main():
    set_seed('media/test2.jpg')
    wb = WordBank()
    print(gen_haiku(wb))


if __name__ == "__main__":
    main()
