## PenTestKit

Useful tools for Penetration Testing.


### Requirements

* Tested on Debian 8.x
* Python 2.x
* termcolor
* requests


### Contents

* secure-headers-checker.py - Test OWASP HTTP Secure Headers.
* tcp-scan-full.sh - Scan all 65535 TCP ports.
* tcp-scan-services.sh - Scan services on open TCP ports.
* udp-scan-1000.sh - Scan 1000 most common UDP ports.d
* udp-scan-services.sh - Scan services on open UDP ports.


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

**tcp-scan-full.sh**
```bash
./tcp-scan-full.sh 10.10.10.1
```

**tcp-scan-services.sh**
```bash
./tcp-scan-services.sh 22,80,443 10.10.10.1
```

**udp-scan-1000.sh**
```bash
./udp-scan-1000.sh 10.10.10.1
```

**udp-scan-services.sh**
```bash
./udp-scan-services.sh 68,111,137 10.10.10.1
```


#### Credits

[web_headers_checker.py](https://github.com/nma-io/pentest_tools/blob/master/web_headers_checker.py) from nma-io.


