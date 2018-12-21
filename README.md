# eth-ecies-py
Encrypt and decrypt messages with Ethereum private and public key in python

```
myAccount = pyelliptic.ECC(privkey=pk,pubkey=vk,curve=curve)
ciphertext = myAccount.encrypt(cleartext,vk)
```

```
myAccount = pyelliptic.ECC(privkey=pk,pubkey=vk,curve=curve)
decrypted = myAccount.decrypt(ciphertext)
```

# Encrypt message for another user
```
myAccount = pyelliptic.ECC(privkey=pk,pubkey=vk,curve=curve)
ciphertext = myAccount.encrypt(cleartext,publicKeyOfUser)
```

