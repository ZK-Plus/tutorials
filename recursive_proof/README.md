# Nested Proofs

In this tutorial we will verify the correctnes of a zk-SNARK inside another zokrates program.

## Set Up

Lets start by running an interactive container locally were zokrates is installed.

```sh
$ docker run -it -v "$(pwd)":/home/zokrates/src zokrates/zokrates:0.8.3
$ cd src
```

Check the [zokrates docs](https://zokrates.github.io/) for other installation options appart from Docker.

## Compile & generate the Merkle Tree proof
First of all we need to create a zk-SNARK proof with zokrates, whose correctness will be later verify by another zokrates program.
For this tutorial we have chosen a Merkle Root proof proof as the sample proof for out nested proof program.
The following instructions guide to genera a valid Merkle Root proof, which will be later used as witness inputs in a subsequent proof.

1. Go to the proof's subfolder
    ```sh
    $ cd merkle_proof
    ```

2. Compile the Merkle Root proof with the curve `bls12_377` 
   ```sh
   $ zokrates compile -i merkle_proof.zok -o merkle_proof --curve bls12_377
   ```

    the output of the comand should be some similar to this:
    ```sh
    Compiling merkle_proof.zok

    Compiled code written to 'merkle_proof'
    Number of constraints: 169763
    ```

3. Run the setup with the `gm17` proving-scheme and `ark` as backend
   ```sh
   $ zokrates setup --proving-scheme gm17 --backend ark -i merkle_proof
   ```

4. The file `merkle_proof/witness.json` contains the arguments of generated valid merkle root. Use this file to generate a valid witness, and subsequently a valid proof: 
   ```sh
   $ zokrates compute-witness --abi -i merkle_proof --stdin < witness.json
   $ zokrates generate-proof --proving-scheme gm17 --backend ark -i merkle_proof
   ```

After successfully running all the previous command you will find the resulting SNARK in `proof.json` file.

