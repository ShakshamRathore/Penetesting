## PenTestKit

Useful tools for Penetration Testing.


### Requirements

* Tested on Debian 8.x
* Python 2.x
* termcolor
* requests
* Nessus
* Nmap
* Nikto
* sslscan


### Contents

#### Vulnerability Scanner
* **nessus-helper.py** - Nessus helper

#### Web
* **secure-headers-checker.py** - Test OWASP HTTP Secure Headers.
* **nikto-scan-http.sh** - Scan HTTP service using nikto.
* **nikto-scan-https.sh** - Scan HTTPS service using nikto.

#### SSL
* **ssl-scan.sh** - Query SSL services using sslscan.

#### TCP
* **tcp-scan-full.sh** - Scan all 65535 TCP ports.
* **tcp-scan-full-delay.sh** - Scan all 65535 TCP ports. Send packets no faster than 1 per second.
* **tcp-scan-services.sh** - Identify services running on a list of open TCP ports.
* **tcp-scan-services-1000.sh** - Identify services running on 1000 most common TCP ports.

#### UDP
* **udp-scan-1000.sh** - Scan 1000 most common UDP ports.
* **udp-scan-services.sh** - Identify services running on a list of open UDP ports.
* **udp-scan-services-1000.sh** - Identify services running on 1000 most common UDP ports.


### Download - Installation

* git clone https://github.com/maldevel/PenTestKit.git
* pip install -r requirements.txt


### Usage Examples

#### Vulnerability Scanner
##### nessus-helper.py
```bash
python nessus-helper.py -n https://<nessus.scanner.url>:8834 -u <nessus_username> -l
```

#### Web
##### secure-headers-checker.py
```bash
python secure-headers-checker.py -H http://example.com
```
```bash
python secure-headers-checker.py -H https://example.com -x http://127.0.0.1:8080
```
```bash
python secure-headers-checker.py -H http://127.0.0.1
```

##### nikto-scan-http.sh
```bash
./nikto-scan-http.sh 10.10.10.1 80
```

##### nikto-scan-https.sh
```bash
./nikto-scan-https.sh 10.10.10.1 443
```

#### SSL
##### ssl-scan.sh
```bash
./ssl-scan.sh 10.10.10.1
```

#### TCP
##### tcp-scan-full.sh
```bash
./tcp-scan-full.sh 10.10.10.1
```

##### tcp-scan-full-delay.sh
```bash
./tcp-scan-full-delay.sh 10.10.10.1
```

##### tcp-scan-services.sh
```bash
./tcp-scan-services.sh 10.10.10.1 22,80,443
```

##### tcp-scan-services-1000.sh
```bash
./tcp-scan-services-1000.sh 10.10.10.1
```

#### UDP
##### udp-scan-1000.sh
```bash
./udp-scan-1000.sh 10.10.10.1
```

##### udp-scan-services.sh
```bash
./udp-scan-services.sh 10.10.10.1 68,111,137
```

##### udp-scan-services-1000.sh
```bash
./udp-scan-services-1000.sh 10.10.10.1
```


#### Credits

[web_headers_checker.py](https://github.com/nma-io/pentest_tools/blob/master/web_headers_checker.py) from nma-io.
[AutoNessus](https://github.com/redteamsecurity/AutoNessus) from redteamsecurity.

