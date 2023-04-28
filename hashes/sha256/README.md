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
   $ zokrates compute-witness -a 3326615074 3321839972 2942831500 4205177069 824241919 2311385863 3299277482 3763981840 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 5
   ```

4. generate proof:
    ```sh
    $ zokrates generate-proof --proving-scheme gm17 --backend ark
    ```

5. verify proof:
    ```sh
    $ zokrates verify
    ```