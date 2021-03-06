## Metasploit installation - Debian 9

```bash
apt-get install default-jre default-jdk software-properties-common
add-apt-repository "deb http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main"
apt-get update
apt-get install oracle-java8-installer
apt-get install build-essential libreadline-dev libssl-dev libpq5 libpq-dev libreadline5 libsqlite3-dev libpcap-dev git-core autoconf postgresql pgadmin3 curl zlib1g-dev libxml2-dev libxslt1-dev libyaml-dev
```

```bash
curl -sSL https://rvm.io/mpapis.asc | gpg --import -
curl -L https://get.rvm.io | bash -s stable
```

```bash
source /usr/local/rvm/scripts/rvm
echo "source /usr/local/rvm/scripts/rvm" >> ~/.bashrc
source ~/.bashrc
```

```bash
RUBYVERSION=$(wget https://raw.githubusercontent.com/rapid7/metasploit-framework/master/.ruby-version -q -O - )
rvm install $RUBYVERSION
rvm use $RUBYVERSION --default
cd ~
apt-get install rbenv
git clone git://github.com/sstephenson/rbenv.git .rbenv
git clone git://github.com/sstephenson/rbenv.git .rbenv
echo 'eval "$(rbenv init -)"' >> ~/.bashrc
exec $SHELL
```

```bash
git clone git://github.com/sstephenson/ruby-build.git ~/.rbenv/plugins/ruby-build
echo 'export PATH="$HOME/.rbenv/plugins/ruby-build/bin:$PATH"' >> ~/.bashrc
git clone git://github.com/dcarley/rbenv-sudo.git ~/.rbenv/plugins/rbenv-sudo
exec $SHELL
```

```bash
RUBYVERSION=$(wget https://raw.githubusercontent.com/rapid7/metasploit-framework/master/.ruby-version -q -O - )
rbenv install $RUBYVERSION
rbenv global $RUBYVERSION
mkdir ~/dev
cd ~/dev
```

```bash
git clone https://github.com/nmap/nmap.git
./configure
make
make install
make clean
```

```bash
su postgres
createuser msf -P -S -R -D
createdb -O msf msf
psql -c "ALTER USER msf WITH ENCRYPTED PASSWORD 'mypassword';"
exit
```

```bash
cd /opt/
git clone https://github.com/rapid7/metasploit-framework.git
cd metasploit-framework/
rvm --default use ruby-${RUBYVERSION}@metasploit-framework
gem install bundler
apt-get install patch ruby-dev liblzma-dev
gem install nokogiri -v '1.6.7.1'
bundle install
bash -c 'for MSF in $(ls msf*); do ln -s /opt/metasploit-framework/$MSF /usr/local/bin/$MSF;done'
nano /opt/metasploit-framework/config/database.yml
```

### datebase.yml contents

```
production:
 adapter: postgresql
 database: msf
 username: msf
 password: mypassword
 host: 127.0.0.1
 port: 5432
 pool: 75
 timeout: 5
```

### The end

```bash
sh -c "echo export MSF_DATABASE_CONFIG=/opt/metasploit-framework/config/database.yml >> /etc/profile"
source /etc/profile
msfconsole
```

