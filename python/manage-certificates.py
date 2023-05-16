#!/usr/bin/env python3

'''
This script is manage SSL certificates on a Linux Machine
Author: Manoj Kesavulu
Email: manoj.kesavulu@dcu.ie
"date: 2023-05-16 13:12:02"
'''

import os
import sys

# check which Linux OS is running
def check_os():
    if os.path.exists("/etc/redhat-release"):
        os_type = "redhat"
    elif os.path.exists("/etc/debian_version"):
        os_type = "debian"
    # check if it is an arch based system
    elif os.path.exists("/etc/arch-release"):
        os_type = "arch"
    else:
        print("Unsupported Linux OS")
        sys.exit(1)
    return os_type


# store the list of certificates on a variable
def get_certificates():
    os_type = check_os()
    if os_type == "redhat":
        certificates = os.popen("ls /etc/pki/tls/certs").read()
    elif os_type == "debian" or os_type == "arch":
        certificates = os.popen("ls /etc/ssl/certs | sed 's/_/ /g; s/.pem$//'").read()
    else:
        print("Unsupported Linux OS")
        sys.exit(1)
    return certificates

# check which SSL certificates are trusted on the system
def get_trusted_certificates():
    trusted_certificates = os.popen("trust list | grep -oP 'label: \K.*'").read()
    return trusted_certificates

# check which SSL certificates are not trusted on the system
def get_untrusted_certificates():
    certificates = get_certificates()
    trusted_certificates = get_trusted_certificates()
    untrusted_certificates = []
    for cert in certificates.split():
        if cert not in trusted_certificates:
            untrusted_certificates.append(cert)
    return untrusted_certificates

# main function
def main():
    #print("SSL Certificates on the system:")
    #print(get_certificates())
    #print("SSL Certificates trusted on the system:")
    #print(get_trusted_certificates())
    #print("SSL Certificates not trusted on the system:")
    print(get_untrusted_certificates())

if __name__ == "__main__":
    main()


