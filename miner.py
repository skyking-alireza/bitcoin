import pip
pip.main(['install','python-bitcoinrpc'])
import hashlib
from binascii import unhexlify, hexlify
import random
import time
import binascii
from bitcoinrpc.authproxy import AuthServiceProxy
rpc_connection = AuthServiceProxy("http://address:port"%('username', 'password'))
best_block_hash = rpc_connection.listtransactions()
print(best_block_hash)
def hashIt(firstTxHash, secondTxHash):
    unhex_reverse_first = binascii.unhexlify(firstTxHash)[::-1]
    unhex_reverse_second = binascii.unhexlify(secondTxHash)[::-1]
    concat_inputs = unhex_reverse_first + unhex_reverse_second
    first_hash_inputs = hashlib.sha256(concat_inputs).digest()
    final_hash_inputs = hashlib.sha256(first_hash_inputs).digest()
    return binascii.hexlify(final_hash_inputs[::-1])
def merkleCalculator(hashList):
    if len(hashList) == 1:
        return hashList[0]
    newHashList = []
    for i in range(0, len(hashList) - 1, 2):
        newHashList.append(hashIt(hashList[i], hashList[i + 1]))
    if len(hashList) % 2 == 1:  # odd, hash last item twice
        newHashList.append(hashIt(hashList[-1], hashList[-1]))
    return merkleCalculator(newHashList)
def CalculatedMerkleRoot(txHashes):
    return (str(merkleCalculator(txHashes), 'utf-8'))
def int2lehex(value, width):
    return int(value , 16).to_bytes(width, byteorder='little').hex()
def int2varinthex(value):
    if int(value , 16) < int("0xfd" , 16) :
        return int2lehex(value, 1)
    elif int(value , 16) <= int('0xffff' , 16):
        return "fd" + int2lehex(value, 2)
    elif int(value , 16) <= int('0xffffffff' , 16):
        return "fe" + int2lehex(value, 4)
    else:
        return "ff" + int2lehex(value, 8)
f = lambda n:n.to_bytes(4,"little").hex()
best_block_hash = rpc_connection.listtransactions()
getblocktemplate = rpc_connection.getblocktemplate({"rules": ["segwit"]})
version = f(getblocktemplate['version'])
bits = hexlify(bytes.fromhex(getblocktemplate['bits'])[::-1]).decode("utf-8")
def block_bits2target(bits):
    bits = bytes.fromhex(bits)
    shift = bits[0] - 3
    value = bits[1:]
    target = value + b"\x00" * shift
    target = b"\x00" * (32 - len(target)) + target
    return target
target = hexlify(block_bits2target(getblocktemplate['bits'])).decode("utf-8")
txidsBEbinary = []
for tttt in  best_block_hash:
    txidsBEbinary.append(tttt['txid'])
kmlistroot = CalculatedMerkleRoot(txidsBEbinary)
txidsBEbinary2 = []
for tttt in  best_block_hash:
    txidsBEbinary2.append(rpc_connection.gettransaction(tttt['txid'])['hex'])
txidsBEbinary2 = "".join(txidsBEbinary2[::-1])
cccccc = int2varinthex(hex(len(txidsBEbinary) + 1))
coinbase = "01000000010000000000000000000000000000000000000000000000000000000000000000ffffffff4503ec59062f48616f4254432f53756e204368756e2059753a205a6875616e67205975616e2c2077696c6c20796f75206d61727279206d653f2f06fcc9cacc19c5f278560300ffffffff0143649d260000000076a914380ab03fd34c3c6e70b2eb8bd34e812ed9d9ec3088ac00000000"
while True:
    header_hex = (version + getblocktemplate['previousblockhash'][::-1]  + kmlistroot[::-1] + f(int(time.time())) + bits + f(random.randint(1000000000,3999999999)))
    header_bin = unhexlify(header_hex)
    hash = hashlib.sha256(hashlib.sha256(header_bin).digest()).digest()
    finalhash = hexlify(hash[::-1]).decode("utf-8")
    if int(finalhash, 16) < int(target , 16):
        print(header_hex .cccccc .coinbase .txidsBEbinary2)
        print(finalhash)
        print(rpc_connection.submitblock(header_hex .cccccc .coinbase .txidsBEbinary2))
