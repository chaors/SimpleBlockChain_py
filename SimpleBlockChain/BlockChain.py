import datetime
import hashlib

from Block import Block
from Block import InvalidBlock
from Message import ChaorsMessage
from Message import InvalidMessage
from Transaction import Transaction

class BlockChain:

    def __init__(self):
        self.blocklist = []

    def add_block(self, block):
        if len(self.blocklist) > 0:
            block.prev_hash = self.blocklist[-1].hash
        block.seal()
        block.validate()
        self.blocklist.append(block)

    def validate(self):

        for i, block in enumerate(self.blocklist):
            try:
                block.validate()
            except InvalidBlock as e:
                print(e)
                raise InvalidBlockChain("第{}区块校验错误".format(i))

    def __repr__(self):
        return "BlockChain:{}".format(len(self.blocklist))

class InvalidBlockChain(Exception):  # 异常处理类

    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)

if __name__ == '__main__':
    try:
        t1 = Transaction("chaors", "yajun", 999999999)
        t2 = Transaction("chaors2", "yajun2", 999999999)
        t3 = Transaction("chaors4", "yajun4", 999999999)

        m1 = ChaorsMessage(t1)
        m2 = ChaorsMessage(t2)
        m3 = ChaorsMessage(t3)

        block1 = Block(m1, m2, m3)
        block1.seal()

        t21 = Transaction("chaors", "yajun", 999999999)
        t22 = Transaction("chaors2", "yajun2", 999999999)

        m21 = ChaorsMessage(t21)
        m22 = ChaorsMessage(t22)

        block2 = Block(m21, m22)
        block2.seal()

        t31 = Transaction("chaors", "yajun", 999999999)
        t32 = Transaction("chaors2", "yajun2", 999999999)
        t33 = Transaction("chaors4", "yajun4", 999999999)
        t34 = Transaction("chaors8", "yajun8", 999999999)

        m31 = ChaorsMessage(t31)
        m32 = ChaorsMessage(t32)
        m33 = ChaorsMessage(t33)
        m34 = ChaorsMessage(t34)

        block3 = Block(m31, m32, m33, m34)
        block3.seal()

        mychain = BlockChain()
        mychain.add_block(block1)
        mychain.add_block(block2)
        mychain.add_block(block3)

        print(mychain)
        #篡改区块
        block3.messagelist[1] = m33
        # m31.data = "lkjioh"
        mychain.validate()

    except InvalidBlockChain as e:
        print(e)