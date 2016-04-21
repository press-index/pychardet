# Universal encoding detection in Python
This library is python binding to [uchardet](https://github.com/BYVoid/uchardet)
## Example
### Python 3
```python
>>> from pychardet import detect
>>> detect(b'hello')
{'encoding': 'ascii', 'confidence': 1.0}
```
### Python 2
```python
>>> from pychardet import detect
>>> detect('hello')
{'encoding': 'ascii', 'confidence': 1.0}
```
## Installation

### Requirements
[Cython](http://docs.cython.org/src/quickstart/install.html)

### From github source
```bash
$ pip install git+https://github.com/PRESS-INDEX/pychardet.git
```