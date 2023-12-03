# 🐝 Beencrypted
 
Beencrypted is the ideal Python package for those looking to encrypt strings using the Bee Movie script. This unique package enables the conversion of strings into segments of the Bee Movie script, which can then be decrypted back to their original form.

▶️ Please note that this project is currently in development, and will propably never get out of it or even get worked on. And if it isn't clear, this is obviously not intended for secure encryption purposes.

[Installation and use](https://github.com/Agent-Kwabbel/Beencrypted#installation-and-use)

[Examples](https://github.com/Agent-Kwabbel/Beencrypted#examples)

[Characters](https://github.com/Agent-Kwabbel/Beencrypted#characters)

[Contribution](https://github.com/Agent-Kwabbel/Beencrypted#contribution)

### Installation and use

##### Use pip

To install, simply use pip:

```
pip install beencrypted
```

You can also find this project on [PyPi](https://pypi.org/project/beencrypted/).

##### Manual Download

Alternatively, download the ```beencrypted/``` folder and include it in your project.

#### Usage

Start by importing the package:

```python
import beencrypted
```

### Examples

##### Encrypting a String
```python
from beencrypt

string = "Barry B Benson"
print(beencrypted.encrypt(string))
```

##### Decrypting a String
```python
from beencrypt

string = "ToAccordingItsItsLittleCareToCareToLawsShouldWingsBeShould"
print(beencrypted.decrypt(string))
```
### Supported Characters

Beencryption supports the Latin alphabet, numbers, and some basic symbols. Decrypted strings will not include capital letters. Unsupported letters or symbols will be replaced with "Barry" in the encrypted string and will not be recoverable after decryption.

```abcdefghijklmnopqrstuvwxyz1234567890 .,-:;/?!```

### Future plans

Yeah, I know my code isn't the most optimal. Better yet, it's suboptimal. However, there exists an optimized version of this project, supporting the biggest range of Unicode standard characters that is possible with The Bee Movie script. This optimized version has not been uploaded to PyPi yet. If discovered, I will certainly make it available.
