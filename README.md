## PenTestKit

Useful tools for Penetration Testing.


### Requirements

* Tested on Debian 8.x
* Python 2.x
* termcolor
* requests
* Burp
* Nessus
* Nmap
* Nikto
* sslscan
* dirb
* netdiscover
* curl
* netcat (nc)


### Contents


#### System
* **os-web-headers.sh** - Check web headers for OS details.
* **banner-grabbing.sh** - Banner grabbing - Check web headers for OS details.


#### Vulnerability Scanner
* **nessus-helper.py** - Nessus helper


#### Web
* **secure-headers-checker.py** - Test OWASP HTTP Secure Headers.
* **nikto-scan-http.sh** - Scan HTTP service using nikto.
* **nikto-scan-https.sh** - Scan HTTPS service using nikto.
* **dir-scanner.sh** - Web content scanning using dirb.
* **content-type-checker.py** - Test supported Content-Types using requests from Burp.
* **curl-get.sh** - Make GET requests using curl.
* **curl-post.sh** - Make POST requests using curl.
* **curl-delete.sh** - Make DELETE requests using curl.
* **curl-put.sh** - Make PUT requests using curl.
* **curl-options.sh** - Make OPTIONS requests using curl.


#### SSL
* **ssl-scan.sh** - Query SSL services using sslscan.


#### Live hosts
* **discover-live-hosts.sh** - Discover live hosts.
* **discover-local-live-hosts.sh** - Discover local network's live hosts using netdiscover.


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


#### System
##### os-web-headers.sh
```bash
./os-web-headers.sh example.com 443
```

##### banner-grabbing.sh
```bash
./banner-grabbing.sh example.com 443
```


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
./nikto-scan-http.sh example.com 80
```

##### nikto-scan-https.sh
```bash
./nikto-scan-https.sh example.com 443
```

##### dir-scanner.sh
```bash
./dir-scanner.sh http://example.com
```

##### content-type-checker.py
```bash
python content-type-checker.py -t lists/common-content-types.list -r requests/myrequest.req -o results.txt -x http://127.0.0.1:8080
```

##### curl-get.sh
```bash
./curl-get.sh 'Accept: application/json' 'Cookie: blah blah' 'http://127.0.0.1:8080' 'https://example.com'
```

##### curl-post.sh
```bash
./curl-post.sh 'Accept: application/json' 'Content-Type: application/x-www-form-urlencoded' 'Cookie: blah blah' 'param1=value1&param2=value2' 'http://127.0.0.1:8080' 'https://example.com'
```

##### curl-delete.sh
```bash
./curl-delete.sh 'Accept: application/json' 'Cookie: blah blah' 'http://127.0.0.1:8080' 'https://example.com'
```

##### curl-put.sh
```bash
./curl-put.sh 'Accept: application/json' 'Content-Type: application/json' 'Cookie: blah blah' '{"param1":"value1","param2":"value2"}' 'http://127.0.0.1:8080' 'https://example.com'
```

##### curl-options.sh
```bash
./curl-options.sh http://127.0.0.1:8080 https://example.com:8443
```


#### SSL
##### ssl-scan.sh
```bash
./ssl-scan.sh example.com
```


#### Live hosts
#####discover-live-hosts.sh
```bash
sudo ./discover-live-hosts.sh 10.10.10.0/24
```

#####discover-local-live-hosts.sh
```bash
sudo ./discover-local-live-hosts.sh eth0 10.10.10.0/24
```


#### TCP
##### tcp-scan-full.sh
```bash
./tcp-scan-full.sh example.com
```

##### tcp-scan-full-delay.sh
```bash
./tcp-scan-full-delay.sh example.com
```

##### tcp-scan-services.sh
```bash
./tcp-scan-services.sh example.com 22,80,443
```

##### tcp-scan-services-1000.sh
```bash
./tcp-scan-services-1000.sh example.com
```


#### UDP
##### udp-scan-1000.sh
```bash
./udp-scan-1000.sh example.com
```

##### udp-scan-services.sh
```bash
./udp-scan-services.sh example.com 68,111,137
```

##### udp-scan-services-1000.sh
```bash
./udp-scan-services-1000.sh example.com
```


#### Request Sample
```bash
POST uri HTTP/1.1
Host: example.com
Accept: **************
Accept-Language: en
Content-Type: ************
Cookie: *************
Content-Length: ******

post data blah blah
```


#### Credits

* [web_headers_checker.py](https://github.com/nma-io/pentest_tools/blob/master/web_headers_checker.py) from nma-io.
* [AutoNessus](https://github.com/redteamsecurity/AutoNessus) from redteamsecurity.

