import pyelliptic
from web3.auto import w3
import cointool

def get_public_from_private(pk):
        return cointool.privtopub(pk)

acct = w3.eth.account.create("Brain words !")
pk = acct.privateKey
vk = get_public_from_private(pk)

print("Private key ",pk)
print("Public key ",vk)

curve = 'secp256k1'
cleartext = "Text to encrypt"

myAccount = pyelliptic.ECC(privkey=pk,pubkey=vk,curve=curve)
ciphertext = myAccount.encrypt(cleartext,vk)

print("Cipher text ",ciphertext)

decrypted = myAccount.decrypt(ciphertext)

print("Decrypted text ",decrypted)



