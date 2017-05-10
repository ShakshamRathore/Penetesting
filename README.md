## PenTestKit

Useful tools for Penetration Testing.

### Requirements

* Tested on Debian 8.x
* Python 2.x
* termcolor
* requests
* Burp Pro
* Nessus
* Nmap
* Nikto
* sslscan
* dirb
* netdiscover
* curl
* netcat (nc)

### Contents

#### Burp

[Stunnel - Burp Pro](burp/stunnel.md)

#### Fuzzing

* **json.sh** - Merge all fuzzdb-project json payloads into one file.
* **lfi.sh** - Merge all fuzzdb-project lfi payloads into one file.
* **create-cmd.sh** - Create specific command injection payloads using fuzzdb-project os-command template.
* **os-cmd-execution-linux.sh** - Merge all fuzzdb-project linux os-command-execution payloads into one file.
* **os-cmd-execution-osx.sh** - Merge all fuzzdb-project osx os-command-execution payloads into one file.
* **os-cmd-execution-windows.sh** - Merge all fuzzdb-project windows os-command-execution payloads into one file.
* **os-cmd-execution-unix.sh** - Merge all fuzzdb-project unix os-command-execution payloads into one file.
* **path-traversal.sh** - Merge all fuzzdb-project path-traversal payloads into one file.
* **sqli-blind.sh** - Merge all fuzzdb-project sqli blind payloads into one file.
* **sqli-detect.sh** - Merge all fuzzdb-project sqli detect payloads into one file.
* **sqli-exploit.sh** - Merge all fuzzdb-project sqli exploit payloads into one file.
* **xml.sh** - Merge all fuzzdb-project xml payloads into one file.
* **xpath.sh** - Merge all fuzzdb-project xpath payloads into one file.
* **xss.sh** - Merge all fuzzdb-project xss payloads into one file.
* **email.sh** - Merge all fuzzdb-project email payloads into one file.
* **html-js.sh** - Merge all fuzzdb-project html and javascript payloads into one file.
* **unicode.sh** - Merge all fuzzdb-project unicode payloads into one file.

#### System

* **web-headers-null.sh** - Check web headers for OS details. Send null.
* **banner-grabbing.sh** - Banner grabbing - Check web headers for OS details.
* **web-headers-malformed.sh** - Check web headers for OS details. Malformed request.
* **web-headers-malformed-2.sh** - Check web headers for OS details. Malformed request.

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
* **robots.sh** - Retrieve robots.txt. HTTP.
* **robots-ssl.sh** - Retrieve robots.txt. HTTPS.

#### SSL

* **ssl-scan.sh** - Query SSL services using sslscan.

#### Live hosts

* **discover-live-hosts.sh** - Discover live hosts.
* **discover-local-live-hosts-1.sh** - Discover local network's live hosts using netdiscover.
* **discover-local-live-hosts-2.sh** - Discover local network's live hosts using arp-scan.
* **passive-discover-local-live-hosts.sh** - Discover local network's live hosts passively using p0f.

#### ICS/SCADA Live hosts/Assets

* **discover-local-live-hosts-scada.sh** - Discover local network's live hosts during ICS/SCADA PT using arp-scan.
* **passive-discover-local-live-hosts.sh** - Discover local network's live hosts passively using p0f.

#### Port-Scanning - TCP

* **tcp-ports-scan-1000.sh** - Scan 1000 most common TCP ports.
* **tcp-ports-scan-1000-delay.sh** - Scan 1000 most common TCP ports. Send packets no faster than 1 per second.
* **tcp-ports-scan-full.sh** - Scan all 65535 TCP ports.
* **tcp-ports-scan-full-delay.sh** - Scan all 65535 TCP ports. Send packets no faster than 1 per second.
* **tcp-services-scan.sh** - Identify services running on a list of open TCP ports.
* **tcp-services-scan-1000.sh** - Identify services running on 1000 most common TCP ports.

#### Port-Scanning - UDP

* **udp-ports-scan-1000.sh** - Scan 1000 most common UDP ports.
* **udp-services-scan.sh** - Identify services running on a list of open UDP ports.
* **udp-services-scan-1000.sh** - Identify services running on 1000 most common UDP ports.

### Download - Installation

* git clone https://github.com/maldevel/PenTestKit.git
* pip install -r requirements.txt

### Usage Examples

#### Fuzzing

##### json.sh

```bash
./json.sh
```

##### lfi.sh

```bash
./lfi.sh
```

##### create-cmd.sh

```bash
./create-cmd.sh <command>
```

##### os-cmd-execution-linux.sh

```bash
./os-cmd-execution-linux.sh
```

##### os-cmd-execution-osx.sh

```bash
./os-cmd-execution-osx.sh
```

##### os-cmd-execution-windows.sh

```bash
./os-cmd-execution-windows.sh
```

##### os-cmd-execution-unix.sh

```bash
./os-cmd-execution-unix.sh
```

##### path-traversal.sh

```bash
./path-traversal.sh
```

##### sqli-blind.sh

```bash
./sqli-blind.sh
```

##### sqli-detect.sh

```bash
./sqli-detect.sh
```

##### sqli-exploit.sh

```bash
./sqli-exploit.sh
```

##### xml.sh

```bash
./xml.sh
```

##### xpath.sh

```bash
./xpath.sh
```

##### xss.sh

```bash
./xss.sh
```

##### email.sh

```bash
./email.sh
```

##### html-js.sh

```bash
./html-js.sh
```

##### unicode.sh

```bash
./unicode.sh
```

#### System

##### web-headers-null.sh

```bash
./web-headers-null.sh example.com 443
```

##### banner-grabbing.sh

```bash
./banner-grabbing.sh example.com 443
```

##### web-headers-malformed.sh

```bash
./web-headers-malformed.sh example.com 443
```

##### web-headers-malformed-2.sh

```bash
./web-headers-malformed-2.sh example.com 443
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

```bash
python content-type-checker.py -t ../fuzzdb/attack/mimetypes/MimeTypes.txt -r requests/myrequest.req -o results.txt -x http://127.0.0.1:8080
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

##### robots.sh

```bash
./robots.sh example.com
```

##### robots-ssl.sh

```bash
./robots-ssl.sh example.com
```

#### SSL

##### ssl-scan.sh

```bash
./ssl-scan.sh example.com
```

#### Live hosts

##### discover-live-hosts.sh

```bash
sudo ./discover-live-hosts.sh 192.168.1.0/24
```

##### discover-local-live-hosts-1.sh

```bash
sudo ./discover-local-live-hosts-1.sh eth0 192.168.1.0/24
```

##### discover-local-live-hosts-2.sh

```bash
sudo ./discover-local-live-hosts-2.sh eth0 192.168.1.0/24
```

##### passive-discover-local-live-hosts.sh

```bash
sudo ./passive-discover-local-live-hosts.sh eth0
```

##### discover-local-live-hosts-scada.sh

```bash
sudo ./discover-local-live-hosts-scada.sh eth0 192.168.1.0/24
```

#### TCP

##### tcp-ports-scan-1000.sh

```bash
./tcp-ports-scan-1000.sh example.com
```

##### tcp-ports-scan-1000-delay.sh

```bash
./tcp-ports-scan-1000-delay.sh example.com
```

##### tcp-ports-scan-full.sh

```bash
./tcp-ports-scan-full.sh example.com
```

##### tcp-ports-scan-full-delay.sh

```bash
./tcp-ports-scan-full-delay.sh example.com
```

##### tcp-services-scan.sh

```bash
./tcp-services-scan.sh example.com 22,80,443
```

##### tcp-services-scan-1000.sh
```bash
./tcp-services-scan-1000.sh example.com
```

#### UDP

##### udp-ports-scan-1000.sh

```bash
./udp-ports-scan-1000.sh example.com
```

##### udp-services-scan.sh

```bash
./udp-services-scan.sh example.com 68,111,137
```

##### udp-services-scan-1000.sh

```bash
./udp-services-scan-1000.sh example.com
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

