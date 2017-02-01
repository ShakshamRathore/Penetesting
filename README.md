## PenTestKit

Useful tools for Penetration Testing.


### Requirements

* Tested on Debian 8.x
* Python 2.x
* termcolor
* requests


### Contents

* secure-headers-checker.py - Test OWASP HTTP Secure Headers.
* full-tcp-scan.sh - Scan all 65535 TCP ports.
* tcp-services-scan.sh - Scan services on discovered open TCP ports.


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
python secure-headers-checker.py -H http://127.0.0.1
```

**full-tcp-scan.sh**
```bash
./full-tcp-scan.sh 10.10.10.1
```

**tcp-services-scan.sh**
```bash
./tcp-services-scan.sh 22,80,443 10.10.10.1
```


#### Credits

[web_headers_checker.py](https://github.com/nma-io/pentest_tools/blob/master/web_headers_checker.py) from nma-io.


