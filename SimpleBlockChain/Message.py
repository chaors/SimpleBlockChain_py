#交易链的简单实现

import datetime
import hashlib
from Transaction import Transaction

class ChaorsMessage: #交易记录类

    def __init__(self, data):

        self.data = data   # 交易信息

        self.hash = None  #自身哈希
        self.prev_hash = None  #上一个交易记录的哈希
        self.timestamp = datetime.datetime.now()
        self.payload_hash = self._hash_payload()

    def _hash_payload(self):  #交易哈希

        return hashlib.sha256((str(self.timestamp) + str(self.data)).encode("utf-8")).hexdigest()

    def _hash_message(self):  #交易记录哈希，锁定交易(哈希再哈希)

        return hashlib.sha256((str(self.prev_hash) + str(self.payload_hash)).encode("utf-8")).hexdigest()

    def seal(self):  #密封

        self.hash = self._hash_message()  #对应数据锁定

    def validate(self):  #验证

        if self.payload_hash != self._hash_payload():
            raise InvalidMessage("交易数据与时间被修改" + str(self))

        if self.hash != self._hash_message():  #判断消息链
            raise InvalidMessage("交易的哈希链接被修改" + str(self))

        return "data ok" + str(self)

    def __repr__(self):  #返回对象基本信息

        mystr = "hash:{}, prev_hash:{}, data:{}".format(self.hash, self.prev_hash, self.data)
        return mystr

    def link(self, message):  #链接
        self.prev_hash = message.hash

class InvalidMessage(Exception):  #异常处理类

    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)

if __name__ == '__main__':  #单独模块测试

    try:

        t1 = Transaction("chaors", "yajun", 999999999)
        t2 = Transaction("chaors2", "yajun2", 999999999)
        t3 = Transaction("chaors4", "yajun4", 999999999)

        m1 = ChaorsMessage(t1)
        m2 = ChaorsMessage(t2)
        m3 = ChaorsMessage(t3)

        #交易密封
        m1.seal()
        #交易哈希只有密封之后才能link
        m2.link(m1)

        m2.seal()
        m3.link(m2)
        m3.seal()

        print(m1)
        print(m2)
        print(m3)

        m1.validate()
        m2.validate()
        m3.validate()

        #篡改数据
        # m2.data = "hahahaha"
        # m2.validate()
        #
        m2.prev_hash = "kkkkk"
        # print(m2)
        m2.validate()

    except InvalidMessage as e:
        print(e)

