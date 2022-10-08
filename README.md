# 🐝 Beencrypted
 
If you want to encrypt your strings and want to have the Bee Movie script in your code, then this is the Python package for you!
With this package, you can encrypt strings to the first part of the Bee Movie script and decrypt it back.

▶️ This project is still under development and obviously don't use this as your secure encryption

[Installation and use](https://github.com/Agent-Kwabbel/Beencrypted#installation-and-use)

[Examples](https://github.com/Agent-Kwabbel/Beencrypted#examples)

[Characters](https://github.com/Agent-Kwabbel/Beencrypted#characters)

[Contribution](https://github.com/Agent-Kwabbel/Beencrypted#contribution)

### Installation and use

##### Use pip

Use pip to install it:

```
pip install beencrypted
```

See this project on [PyPi](https://pypi.org/project/beencrypted/).

##### Download

If you want to download and use the package you can download the ```beencrypted/``` folder and place it in your project.

#### Usage

Import the package

```python
import beencrypted

#import only encrypt or decrypt
from beencrypted import encrypt
from beencrypted import decrypt

#import with other name
import beencrypted as bc
from beencrypted import encrypt as encr
```

### Examples

##### Encrypt
```python
from beencrypt

string = "Barry B Benson"
print(beencrypted.encrypt(string))
```

##### Decrypt
```python
from beencrypt

string = "ToAccordingItsItsLittleCareToCareToLawsShouldWingsBeShould"
print(beencrypted.decrypt(string))
```
### Characters

Beencryption only supports the Latin alphabet, numbers and some basic symbols. Decrypted strings will not have capitals. Letters or symbols that are not supported will have been replaced with "Barry" in the encrypted string and will be lost in decryption.

```abcdefghijklmnopqrstuvwxyz1234567890 .,-:;/?!```

### Contribution

If you feel like contributing feel free to open issues and give feedback. I'm open to pull requests and you can contact me on Discord with Fabe#1754

<sub>And yes, this is a meme project :)</sub>
