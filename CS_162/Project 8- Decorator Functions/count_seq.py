# Author: Ty Vareka
# Date: 5/18/2020
# Description: This program uses a generator to make an indefinite list of numbers and yields the sequence as a string

def count_seq():
    '''Generator function that generates a sequence that goes on indefinitely'''
    num = '2'
    yield '2'
    while True:
        index = 0
        out = ''
        while index < len(num):
            count = 1
            ch = num[index]
            while index + 1 < len(num) and num[index] == num[index + 1]:
                count += 1
                index += 1
            out += str(count) + ch
            index += 1
        num = out
        yield out


def main():
    '''testing the program with simple parameters'''
    gen = count_seq()
    cnt = 0
    for val in gen:
        print(val)
        cnt += 1
        if cnt > 10:
            break


if __name__ == "__main__":
    main()
