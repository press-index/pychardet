# Fast universal encoding detection in Python
This library is a python binding to [universal chardet](https://github.com/BYVoid/uchardet).
## Example
### Python 3
```python
>>> from pychardet import detect
>>> detect('El castellano es la lengua española'.encode('iso-8859-1'))
{'encoding': 'iso-8859-1', 'confidence': 0.8775989413261414}
```
### Python 2
```python
>>> from pychardet import detect
>>> detect(u"Réseau Démographie de l'Agence universitaire de la francophonie".encode('utf8'))
{'encoding': 'utf-8', 'confidence': 0.7524999976158142}
```
## Installation

### Requirements
[Cython](http://docs.cython.org/src/quickstart/install.html)

### From github source
```bash
$ pip install git+https://github.com/PRESS-INDEX/pychardet.git
```