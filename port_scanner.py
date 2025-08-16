#!/usr/bin/env python3
import nmap

def nmap_scan(target, ports="1-100"):
    """Advanced scan using Nmap (requires root for SYN scans)."""
    scanner = nmap.PortScanner()
    
    print(f"🔍 Scanning {target} (ports {ports})...")
    scanner.scan(target, ports, arguments='-T4')  # -T4 for faster scan
    
    if not scanner.all_hosts():
        print("❌ Target not reachable")
        return
    
    host = scanner[target]
    print(f"\n📊 Scan results for {target}:")
    print(f"Status: {host.state()}")

    for proto in host.all_protocols():
        print(f"\nProtocol: {proto}")
        ports = host[proto].keys()
        for port in sorted(ports):
            state = host[proto][port]["state"]
            if state == "open":
                service = host[proto][port].get("name", "unknown")
                print(f"✅ Port {port} ({service}) is {state}")

if __name__ == "__main__":
    target = input("Enter target IP/hostname: ")
    nmap_scan(target)
