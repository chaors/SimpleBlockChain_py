
import datetime
import hashlib

class Transaction: #交易类

    def __init__(self,
                 payer,   #付款方
                 recer,   #收款方
                 count):  #金额
        self.payer = payer
        self.recer = recer
        self.count = count
        self.timestamp = datetime.datetime.now()

    def __repr__(self):

        return str(self.payer) + " pay" + str(self.recer) + " " + str(self.count) + " in " + str(self.timestamp)


if __name__ == '__main__':

    t1 = Transaction("chaors", "yajun", 999999999)
    print("\n", t1)