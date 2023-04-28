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
   $ zokrates compute-witness -a 6 195 173 103 172 169 108 58 114 105 178 230 75 24 7 155 253 57 244 117 158 206 107 106 181 198 130 99 86 109 111 81 81 61 55 244 242 113 7 33 65 196 140 219 27 112 249 77 30 1 180 66 2 214 56 101 230 241 179 102 173 145 232 184 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 5
   ```

4. generate proof:
    ```sh
    $ zokrates generate-proof --proving-scheme gm17 --backend ark
    ```

5. verify proof:
    ```sh
    $ zokrates verify
    ```