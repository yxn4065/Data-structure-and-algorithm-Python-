# -*- coding: utf-8 -*-
# @Author : yxn
# @Date : 2022/2/5 15:07 
# @IDE : PyCharm(2021.3.1) Python3.98
import hashlib

"""Python自带MD5和SHA系列的散列函数
库：hashlib
包括了md5/sha1/sha224/sha256/
sha384/sha512等6种散列函数
"""


def hash(astring, tablesize):
    sum = 0
    for pos in range(len(astring)):
        sum += ord(astring[pos])
    return sum % tablesize


class HashTable:
    """映射抽象数据类型 ADT Map"""
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def hashfunction(self, key):
        """求余数进行散列"""
        return key % self.size

    def rehash(self, oldhash):
        return (oldhash + 1) % self.size

    def put(self, key, data):
        hashvalue = self.hashfunction(key)

        # key不存在,未冲突
        if self.slots[hashvalue] is None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        # key存在,替换val
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data
            else:
                nextslot = self.rehash(hashvalue)

                # 冲突解决:线性探测再散列(直到找到空槽或者key)
                while self.slots[nextslot] is not None \
                        and self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot)

                if self.slots[nextslot] is None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                else:
                    self.data[nextslot] = data

    def get(self, key):
        # 标记散列值为查找起点
        startslot = self.hashfunction(key)
        data = None
        stop = False
        found = False
        position = startslot
        # 找key,直到空槽或者回到起点
        while self.slots[position] is not None \
                and found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:  # 未找到key,再散列继续找
                position = self.rehash(position)
                if position == startslot:
                    stop = True  # 回到起点,停
        return data

    # 通过特殊方法实现[]访问
    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)


if __name__ == '__main__':
    t1 = "hello world!".encode("utf-8")
    a = hashlib.md5(t1).hexdigest()
    t2 = "this is part #2".encode("utf-8")
    m = hashlib.md5()
    m.update(t2)
    print(a)
    print(m.hexdigest())
    print("*" * 20)
    print(hash("cat", 11))
