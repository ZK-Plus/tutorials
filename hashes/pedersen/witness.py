from zokrates_pycrypto.gadgets.pedersenHasher import PedersenHasher

preimage = bytes.fromhex("1616")
# create an instance with personalisation string
hasher = PedersenHasher(b"test")
# hash payload
digest = hasher.hash_bytes(preimage)
print(digest)
# x:2685288813799964008676827085163841323150845457335242286797566359029072666741,
# y:3621301112689898657718575625160907319236763714743560759856749092648347440543

# write ZoKrates DSL code to disk
path = "pedersen.code"
hasher.write_dsl_code(path)

# write witness arguments to disk
path = "pedersen_witness.txt"
witness = hasher.gen_dsl_witness_bytes(preimage)
with open(path, "w+") as f:
    f.write(" ".join(witness))