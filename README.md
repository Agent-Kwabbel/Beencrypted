# 🐝 Beecrypted
 
If you want to encrypt your strings and want to have the Bee Movie script in your code than this is the Python package for you!
With this package you can encrypt strings to the first part of the Bee Movie scipt and decrypt it back.

### Examples

##### Encryption
```python
from beencrypt

string = "Barry B Benson"
print(beencrypt.encrypt(string))
```

##### Decryption
```python
from beencrypt

string = "ToAccordingItsItsLittleCareToCareToLawsShouldWingsBeShould"
print(beencrypt.decrypt(string))
```
### Characters

Beencryption only supports the latin alphabet, numbers and some basic symbols. Decrypted strings will not have capitals. Letters or symbols that are not supported will have been replaced with "Barry" in the encrypted string and will be lost in decryption.