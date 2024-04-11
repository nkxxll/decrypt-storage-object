# Notes to the decryption of a storage object in optee

Discalmer this is (state now) a python program that decrypts a optee storage object after the extraction of such a file with the coresponding TSK (Trusted Applicaton Storage Key). And the "Meta File".
...for ease of use the rest of the _Studienarbeits-Programs_ also go here...

## Note

In `img` there is a picture `bug.png`. In this picture there is a bug associated with the seal-key
application that I cannot explain myself. I can read storage objects if I parse them by the command
line I cannot read them if I parse them any other way through stdin or with a file. I don't know why
the objects are definitly written to secure storage. This could be veryfied with a debug print just
before writing.

## General Preceedure

General Preceedure for decrypting a data object...

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

so 16 bytes in the "meta file" are the encrypted fek

### data

and on the encrypted file the first 12 bytes are the iv
the next 16 bytes are tag bytes the rest should be data

## problem for now

Which of the files is the "meta file" with the encrypted FEK? After running the `optee_example_secure_storage`, there are three files `0, 1, 2` that are objects and the `dirf.db` file which from my understanding only holds integrity hashes for the files in `/data/tee`.
Solution idea print the storage object id in the _secure storage ta_ and create a mapping like this...
