# Notes to the decryption of a storage object in optee

Discalmer this is (state now) a python program that decrypts a optee storage object after the extraction of such a file with the coresponding TSK (Trusted Applicaton Storage Key). And the "Meta File".
...for ease of use the rest of the _Studienarbeits-Programs_ also go here...

## Notes

`./scripts/prefix_len_test.py` shows a test for how long the prefix in the file is.

### gegeben

TSK
Encrypted FEK
block data
block iv
tag

### gesucht

decrypted data

### "pseudo code"

```
def getpassword(tsk, encrypted_fek):
    fek = aes.ecb_decrypt(tsk, encrypted_fek)
    return fek

def decrypt(iv, tag, data, password):
    verifyed, decrypted_data = aes.gcm_decrypt(iv, tag, data, password)
    return decrypted_data
```

### meta

So 16 bytes in the "meta file" are the encrypted FEK.

### data

and on the encrypted file the first 12 bytes are the iv
the next 16 bytes are tag bytes the rest should be data

## problem for now

Which of the files is the "meta file" with the encrypted FEK? After running the `optee_example_secure_storage`, there are three files `0, 1, 2` that are objects and the `dirf.db` file which from my understanding only holds integrity hashes for the files in `/data/tee`.
Solution idea print the storage object id in the _secure storage ta_ and create a mapping like this...
