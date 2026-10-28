import ipaddress
import platform
import subprocess


def check_host(ip_address):
    try:
        address = ipaddress.ip_address(ip_address)

        if not address.is_private:
            print("Warning: This is not a private IP address.")

        count_flag = "-n" if platform.system() == "Windows" else "-c"

        result = subprocess.run(
            ["ping", count_flag, "2", str(address)],
            capture_output=True,
            text=True,
            timeout=10,
        )

        if result.returncode == 0:
            print(f"[+] {address} is reachable.")
        else:
            print(f"[-] No ping response from {address}.")

    except ValueError:
        print("[!] Invalid IP address.")

    except subprocess.TimeoutExpired:
        print("[!] The request timed out.")


def main():
    print("=" * 40)
    print("       SAFE NETWORK AUDITOR")
    print("=" * 40)
    print("Use only on networks you are authorized to test.")

    target = input("Enter a target IP address: ").strip()
    check_host(target)


if __name__ == "__main__":
    main()