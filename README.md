# sweetmorse

Morse code tools from read to write, analog to digital.

[![Build Status](https://travis-ci.org/Jdsleppy/sweetmorse.svg?branch=master)](https://travis-ci.org/Jdsleppy/sweetmorse)

### Compatibility

Targets Python3, tested against against Python 3.3-3.6.

### Crash course

See a crash course at https://github.com/Jdsleppy/sweetmorse

> Currently `sweetmorse` is only available on the testing version of PYPI.org.  As such, `pip install` won't work out-of-the-box just quite yet.
```
$ pip install sweetmorse
```

Use it from code:
```python
>>> from sweetmorse.morse import Morse
>>> m = Morse.from_plain_text("SOS")
>>> m.human_readable
'... ___ ...'
>>> m.binary
'101010001110111011100010101'
```
You get an executable that reads from standard in and performs conversions between `sweetmorse`'s formats:
```
$ echo "Hello, Morse World!" | sweetmorse PLAIN HUMAN_READABLE > output.txt
$ cat output.txt
.... . ._.. ._.. ___ --..--   __ ___ ._. ... .   .__ ___ ._. ._.. _.. _._.__
$ cat output.txt | sweetmorse HUMAN_READABLE BINARY
101010100010001011101010001011101010001110111011100011101110101011101110000000111011100011101110111000101110100010101000100000001011101110001110111011100010111010001011101010001110101
```

You can do the same with the main module, provided everything's in your `PYTHONPATH`:
```
$ echo "Hello, Morse World!" | python sweetmorse/main.py PLAIN HUMAN_READABLE
.... . ._.. ._.. ___ --..--   __ ___ ._. ... .   .__ ___ ._. ._.. _.. _._.__
```
