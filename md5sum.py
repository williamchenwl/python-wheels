import hashlib
import sys
import select

def file_hash(file):

    now_hash = hashlib.md5()

    while True:
        bin = file.read(8096)
        if not bin:
            break
        else:
            now_hash.update(bin)

    hex = now_hash.hexdigest()

    return hex


def calc(filename):
    try:
        fp = open(filename, 'rb')
    except:
        print('wrong file name, file doesn''t exist')

    res = file_hash(fp)
    fp.close()
    print(res)

if __name__ == '__main__':
    file_name = input()
    calc(file_name)
