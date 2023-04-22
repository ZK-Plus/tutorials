# preimage sha256

1. compile proof 
    ```sh
    $ zokrates compile -i hash.zok
    ```

2. and run setup:
    ```sh
    $ zokrates setup --proving-scheme gm17 --backend ark
    ```

3. compute witness:
   ```sh
   $ zokrates compute-witness -a 3573006668 1328011836 262565714 1315389030 201875398 2228137404 3732152073 1554944195 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 5
   ```

4. generate proof:
    ```sh
    $ zokrates generate-proof --proving-scheme gm17 --backend ark
    ```

5. verify proof:
    ```sh
    $ zokrates verify
    ```