import nmap

# Create a single instance of PortScanner
nm = nmap.PortScanner()

target = "45.33.32.156"
options = "-sV -sC"  # Adjust options as needed

# Perform the scan using the created instance
nm.scan(target, arguments=options)

# Iterate over the scan results
for host in nm.all_hosts():
    print("Host: %s (%s)" % (host, nm[host].hostname()))
    print("State: %s" % nm[host].state())
    for protocol in nm[host].all_protocols():
        print("Protocols: %s" % protocol)
        port_info = nm[host][protocol]
        for port, state in port_info.items():
            print("Port: %s\tState: %s" % (port, state))
