import hashlib
import poseidon


# def sha256(preimage: bytearray):
#     return hashlib.poseidon(preimage).digest()

# def sha3_to_u8_array(val: bytearray) -> list[str]:
#     array_arrays = [val[i] for i in range(0, len(val))]
#     u32_array = [str(x) for x in array_arrays]
#     return u32_array

# msg = (5).to_bytes(32, "big", signed=False)
# root = sha256(msg)

# print(*sha3_to_u8_array(root), *sha3_to_u8_array(msg))

security_level = 128
input_rate = 3
t_opt = 4
full_round = 8
partial_round = 56
alpha = 5
poseidon_pre_generated = poseidon.OptimizedPoseidon(poseidon.HashType.CONSTINPUTLEN, poseidon.parameters.prime_255, 
                                                security_level, alpha, input_rate, t_opt,
                                                full_round=full_round, partial_round=partial_round,
                                                rc_list=poseidon.parameters.round_constants_neptune, 
                                                mds_matrix=poseidon.parameters.matrix_neptune)

input_vec_2 = [x for x in range(0, t_opt - 1)]
print("Input: ", input_vec_2)
poseidon_output = poseidon_pre_generated.run_hash(input_vec_2)
print("Output: ", int(poseidon_output))

