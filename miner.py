import hashlib
from binascii import unhexlify, hexlify
import random
import time
from mk import CalculatedMerkleRoot
f = lambda n:n.to_bytes(4,"little").hex()
uuu = 0
ttt = int(time.time()) + 10
while True:
    header_hex = (f(536870916) +
     "00000000000000000050a8aa526627fc754992acd9ba19e2357e68478810f0dc"[::-1]  +
     "40087ab3b2ba8f2c74f025e0cb0f47cc23a92da74188b36651a4a74d3c457a16"[::-1] +
     f(int(time.time())) +
     f(386794504) +
     f(random.randint(1000000000,3999999999)))
    header_bin = unhexlify(header_hex)
    hash = hashlib.sha256(hashlib.sha256(header_bin).digest()).digest()
    finalhash = hexlify(hash[::-1]).decode("utf-8")
    uuu += 1
    if ttt == int(time.time()):
        print(uuu)
        break
    if int(finalhash, 16) < int("0000000000000000000e04080000000000000000000000000000000000000000" , 16):
        print(finalhash)
