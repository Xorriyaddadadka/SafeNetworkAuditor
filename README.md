# Safe Network Auditor

A lightweight Python tool for checking the reachability of an IP address on an authorized network.

## Features

- IP address validation
- Host reachability checks using ping
- Windows and Linux compatibility
- No third-party Python dependencies

## Requirements

- Python 3.10 or later
- Windows or Linux

## Usage

Run the tool with:

```bash
python src/main.py
```

Enter the IP address of a device you own or are authorized to test.

## Limitations

A failed ping does not necessarily mean that a host is offline. Firewalls may block ICMP requests.

## Disclaimer

Use this tool only on systems and networks you own or have explicit permission to test.