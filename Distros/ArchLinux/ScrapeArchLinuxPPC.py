import requests
import json

URL = "https://archlinuxpower.org/iso/archpower-current-powerpc.iso"

head = requests.head(URL, allow_redirects=True, timeout=10)
head.raise_for_status()
size_bytes = head.headers.get("Content-Length", "0")
size = f"{int(size_bytes) / 1024**2:.2f} MB" if size_bytes.isdigit() else ""

data = {
    "name": "Arch Linux PPC current",
    "version": "current",
    "download_url": URL,
    "size": size,
    "arch": "powerpc",
    "icon": "https://raw.githubusercontent.com/Cruizepeni/ProjectHomelabIcons/main/OperatingSystems/IconArchLinux.svg",
    "description": "Arch Linux PPC is an unofficial port of Arch Linux for PowerPC architectures, including 32-bit and 64-bit variants.",
    "homepage": "https://archlinuxpower.org/",
    "documentation": ["https://archlinuxpower.org/wiki"],
    "wikis": [
        "https://archlinuxpower.org/wiki",
        "https://en.wikipedia.org/wiki/PowerPC"
    ],
    "install_guides": [
        "https://archlinuxpower.org/wiki/Installation_Guide",
        "https://www.reddit.com/r/archlinux/comments/kqa7l2/i_made_arch_linux_for_powerpc/"
    ],
    "distrowatch": [],
    "github_repos": ["https://github.com/kth5/archpower"],
    "forums": [
        "https://bbs.archlinux.org/viewtopic.php?id=264109",
        "https://www.reddit.com/r/archlinux/comments/kqa7l2/i_made_arch_linux_for_powerpc/"
    ],
    "mailing_lists": [],
    "type": "Unofficial community port",
    "based_on": ["Arch Linux"],
    "checksum": "",
    "torrent_url": "",
    "magnet_link": "",
    "hardware_requirements": {
        "minimum": {
            "cpu": "PowerPC 604 or newer",
            "ram": "64 MB",
            "storage": "2 GB",
            "graphics": "VGA-compatible",
            "network": "Ethernet or Wi-Fi"
        },
        "recommended": {
            "cpu": "PowerPC G4 or G5",
            "ram": "512 MB",
            "storage": "10 GB SSD",
            "graphics": "GPU with 3D support",
            "network": "Ethernet or Wi-Fi"
        }
    }
}

print(json.dumps(data))
