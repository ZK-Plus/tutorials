import hashlib


def sha3(preimage: bytearray):
    return hashlib.sha3_512(preimage).digest()

def sha3_to_u8_array(val: bytearray) -> list[str]:
    array_arrays = [val[i] for i in range(0, len(val))]
    u32_array = [str(x) for x in array_arrays]
    return u32_array

msg = (5).to_bytes(32, "big", signed=False)
root = sha3(msg)

print(*sha3_to_u8_array(root), *sha3_to_u8_array(msg))

