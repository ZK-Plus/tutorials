raw_msg = "This is my secret message"
msg = hashlib.sha512(raw_msg.encode("utf-8")).digest()

# sk = PrivateKey.from_rand()
# Seeded for debug purpose
key = FQ(1997011358982923168928344992199991480689546837621580239342656433234255379025)
sk = PrivateKey(key)
sig = sk.sign(msg)

pk = PublicKey.from_private(sk)
is_verified = pk.verify(sig, msg)
print(is_verified)

path = 'zokrates_inputs.txt'
write_signature_for_zokrates_cli(pk, sig, msg, path)