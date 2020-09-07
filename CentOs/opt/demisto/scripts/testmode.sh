# Demisto TEST Mode script
# Purpose: Sets IP-TABLES in the demisto server to prevent getting incidents
# Used for BCP testing and recovery testing where another demisto is already running the service
# Needs to be updated after adding incident creation integrations
# To disbale: just flusch ip-tables again (sudo iptables -F)

# Flush
  sudo iptables -F
# Zero Counters
  sudo iptables -Z

# Allow Loopback
  sudo iptables -A INPUT -i lo -j ACCEPT
  sudo iptables -A OUTPUT -o lo -j ACCEPT

# Accept incomming and outgoing SSH # Just to be sure we have ssh in case a wrong iptables filter
  sudo iptables -A INPUT -p tcp --dport 22 -m conntrack --ctstate NEW -j ACCEPT
  sudo iptables -A OUTPUT -p tcp --dport 22 -m conntrack --ctstate NEW -j ACCEPT

# Accept outgoing DNS # Just to be sure we have dns in case a wrong iptables filter
  sudo iptables -A OUTPUT -p tcp --dport 53 -m conntrack --ctstate NEW -j ACCEPT
  sudo iptables -A OUTPUT -p udp --dport 53 -m conntrack --ctstate NEW -j ACCEPT

# Accept outgoing LDAP # Just to be sure we can login in case a wrong iptables filter
  sudo iptables -A OUTPUT -p tcp --dport 389 -m conntrack --ctstate NEW -j ACCEPT
  sudo iptables -A OUTPUT -p udp --dport 389 -m conntrack --ctstate NEW -j ACCEPT
  sudo iptables -A OUTPUT -p tcp --dport 636 -m conntrack --ctstate NEW -j ACCEPT
  sudo iptables -A OUTPUT -p udp --dport 636 -m conntrack --ctstate NEW -j ACCEPT

### Block Demisto ( Samples )
  # sudo iptables -A OUTPUT -d SiemServer01.local.lan -j DROP
  # sudo iptables -A OUTPUT -d SplunkServer.dmz.lan -j DROP

