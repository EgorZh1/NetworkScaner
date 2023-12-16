import VulnScan
import NetScan

def main():
    NetScan.netscan()

    scanner = VulnScan.VulnerabilityScanner()
    scanner.scan()
    scanner.report_vulnerabilities()

# call main
if __name__ == "__main__":
    main()


