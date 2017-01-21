## PenTestKit
Useful tools for Penetration Testing


### Requirements
* Tested on Debian 8.x
* Python 2.x
* termcolor
* requests


### Contents
* secure-headers-checker.py - Test OWASP HTTP Secure Headers


### Download - Installation
* git clone https://github.com/maldevel/PenTestKit.git
* pip install -r requirements.txt

### Usage Examples

**secure-headers-checker.py**
```python
python secure-headers-checker.py -H http://example.com
```

```python
python secure-headers-checker.py -H https://example.com -x http://127.0.0.1:8080
```

```python
python secure-headers-checker.py -H https://127.0.0.1 -x http://127.0.0.1:8080
```


#### Credits
The secure-headers-checker.py script was inspired by [web_headers_checker.py](https://github.com/nma-io/pentest_tools/blob/master/web_headers_checker.py) from nma-io.


