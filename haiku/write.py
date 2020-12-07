'''
write.py (haiku_generator)

Evan Meade, 2019

This is the main code for generating haikus. It is contained
within the Writer class.
'''

import random
# import hashlib
# from PIL import Image
# import io


# def set_seed(loc):
#     img = Image.open(loc)
#     m = hashlib.sha256()
#     with io.BytesIO() as mem:
#         img.save(mem, 'PNG')
#         data = mem.getvalue()
#         m.update(data)
#     random.seed(m.digest())


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
        self.f1 = open("word_lists/one.txt", "r")
        self.f2 = open("word_lists/two.txt", "r")
        self.f3 = open("word_lists/three.txt", "r")
        self.f4 = open("word_lists/four.txt", "r")
        self.f5 = open("word_lists/five.txt", "r")
        self.f6 = open("word_lists/six.txt", "r")
        self.f7 = open("word_lists/seven.txt", "r")

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


class Writer:
    def __init__(self):
        self.wb = WordBank()

    def chop(self, total):
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


    def gen_line(self, size):
        bins = self.chop(size)
        line = ''
        for x in bins:
            line = line + self.wb.pull_word(x).rstrip() + ' '
        return line[:len(line) - 1]


    def gen_haiku(self, *args):
        # set_seed(file_path)
        lengths = [a for a in args]
        haiku = []

        for l in lengths:
            haiku.append(self.gen_line(l))
        return haiku


def main():
    # seed_file = 'media/test.jpg'
    wb = WordBank()
    print(gen_haiku(wb))


if __name__ == "__main__":
    main()
