#! /bin/bash
lspci | grep -E "Network | network | Ethernet | ethernet | wireless | Wireless" | cut -c9-100 
