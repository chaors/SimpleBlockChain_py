#通过哈希来挖掘区块

from hashlib import sha256

if __name__ == '__main__':
    x = 11
    y = 0

    #f'{x*y}' 将x*y的结果转化为字符串 encode("utf-8") 默认utf-8，可以不写
    #当x*y的结果的前三位是=都是0的时候找到目标哈希值
    # while sha256(f'{x*y}'.encode("utf-8")).hexdigest()[-3:] != "000":
    # while sha256(f'{x*y}'.encode("utf-8")).hexdigest()[-5:] != "01010":
    while sha256(f'{x*y}'.encode("utf-8")).hexdigest()[:8] != "00001111":
        y += 1
        print(y)

    print("y = {}".format(y))