def bytes_to_u32(val: bytes) -> [int]:
    b0 = [str(int.from_bytes(val[i:i+4], "big")) for i in range(0,len(val), 4)]
    return " ".join(b0)


print(f"preimage as u32 array: {bytes_to_u32(preimage)}")
print(f"hash as u32 array: {bytes_to_u32(hashed_msg)}")
