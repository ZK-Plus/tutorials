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

## Compile and generate the recursive proof
Once we have a valid proof and the verification key from the Merkle Root proof, we need to compile the recursive proof and parse the arguments of `merkle_tree/proof.json` and `merkle_tree/verification.key` to generate a valid witness in the "parent" proof. 
For that:

1. Open a new terminal window on your terminal and run the command below from the root of this tutorial. This will generate the valid arguments to generate a valid witness and the final proof. The arguments for the recursive proof will be stored in `gm17.json`.
    ```sh
    $ echo "[\n$(cat merkle_proof/proof.json | jq '{proof, inputs}'), $(cat merkle_proof/verification.key | jq 'del(.scheme,.curve)')\n]" > jq > gm17.json
    ```

2. Back in the docker container, go back to the parent directory of this tutorial:
    ```sh
    $ cd ..
    ```

3. Compile & setup the recursive proof with the curve `bw6_761`, `gm17` proving-scheme and `ark` as backend
   ```sh
   $ zokrates compile --curve bw6_761 -i recursive_proof.zok
   $ zokrates setup --proving-scheme gm17 --backend ark
   ```

4. Open a new terminal window on your terminal and run the command below outside of docker. This will generate the valid arguments to generate a valid witness and the final proof. The arguments for the recursive proof will be stored in `gm17.json`.
    ```sh
    $ echo "[\n$(cat merkle_proof/proof.json | jq '{proof, inputs}'), $(cat merkle_proof/verification.key | jq 'del(.scheme,.curve)')\n]" > jq > gm17.json
    ```

5. Compute a valid witness from the `gm17.json` file and generate the json proof.
To be found in `proof.json`.
   ```sh
   $ zokrates compute-witness --abi --stdin < gm17.json
   $ zokrates generate-proof --proving-scheme gm17 --backend ark
   ```

