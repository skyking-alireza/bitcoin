import hashlib
import binascii
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
    # Process pairs. For odd length, the last is skipped
    for i in range(0, len(hashList) - 1, 2):
        newHashList.append(hashIt(hashList[i], hashList[i + 1]))
    if len(hashList) % 2 == 1:  # odd, hash last item twice
        newHashList.append(hashIt(hashList[-1], hashList[-1]))
    return merkleCalculator(newHashList)
txHashes = [
    "338bbd00b893c384eb2b11e70f3875447297c5f20815499e787867df4538e48d",
    "1ad1138c6064dd17d0a4d12016d629c18f15fc9d1472412945f9c91a696689c7",
    "c77834d14d66729014b06fcf45c5f82af4bdd9d816e787f01bfa525cfa147014",
    "bb3d83398d7517fe643b2421d795e73c342b6a478ef53acdaab35dbdffbbcdb5",
    "38d563caf0e9ed103515cab09e40e49da0ccb8c0765ce304f9556e5bc62e8ff5",
    "8fc0507359d0122fa14b5887034d857bd69c8bc0e74c8dd428c2fc098595c285",
    "9db9fe6d011c1c7e997418aeec78ccb659648cfc915b2ff1154cabb41359ac70",
    "3c72fdb7e38e4437faa9e5789df6b51505de014b062361ef47578244d5025628"
]
def CalculatedMerkleRoot():
    return (str(merkleCalculator(txHashes), 'utf-8'))