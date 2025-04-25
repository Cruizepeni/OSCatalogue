import requests
import json

def get_remote_file_size(url):
    try:
        h = requests.head(url, allow_redirects=True, timeout=10)
        b = h.headers.get("Content-Length","0")
        return f"{int(b)/(1024**2):.2f} MB" if b.isdigit() else ""
    except:
        return ""

url = "https://mirror.rackspace.com/linuxmint/iso/stable/22.1/linuxmint-22.1-cinnamon-64bit.iso"
version = "22.1"
size = get_remote_file_size(url)
data = {
    "name": "Linux Mint 22.1 Cinnamon Edition",
    "version": version,
    "download_url": url,
    "size": size,
    "arch": "x86_64",
    "icon": "https://raw.githubusercontent.com/Cruizepeni/ProjectHomelabIcons/main/OperatingSystems/IconLinuxMint.svg",
    "description": "Linux Mint Cinnamon offers a modern, full-featured desktop environment with rich visual effects and a sleek user interface.",
    "homepage": "https://www.linuxmint.com/",
    "documentation": [
        "https://linuxmint.com/documentation.php",
        "https://linuxmint-user-guide.readthedocs.io/"
    ],
    "wikis": [
        "https://en.wikipedia.org/wiki/Linux_Mint",
        "https://linux.fandom.com/wiki/Linux_Mint",
        "https://betawiki.net/wiki/Linux_Mint",
        "https://simple.wikipedia.org/wiki/Linux_Mint",
        "https://wiki.openstreetmap.org/wiki/LinuxMint"
    ],
    "install_guides": [
        "https://linuxmint-installation-guide.readthedocs.io/",
        "https://itsfoss.com/install-linux-mint/",
        "https://www.linux.org/threads/installing-mint-22-1-linux-to-your-computer.55346/",
        "https://forums.linuxmint.com/viewtopic.php?t=424975",
        "https://www.youtube.com/watch?v=2mUI3CMjmMc"
    ],
    "distrowatch": ["https://distrowatch.com/table.php?distribution=mint"],
    "github_repos": [
        "https://github.com/linuxmint",
        "https://github.com/linuxmint/cinnamon",
        "https://github.com/linuxmint/mintupdate",
        "https://github.com/linuxmint/mintbackup",
        "https://github.com/linuxmint/timeshift"
    ],
    "forums": [
        "https://forums.linuxmint.com/",
        "https://www.reddit.com/r/linuxmint/",
        "https://community.linuxmint.com/",
        "https://forums.linuxmint.com/viewforum.php?f=46"
    ],
    "mailing_lists": [],
    "type": "Desktop",
    "based_on": ["Ubuntu"],
    "checksum": "ccf482436df954c0ad6d41123a49fde79352ca71f7a684a97d5e0a0c39d7f39f",
    "torrent_url": "https://www.linuxmint.com/torrents/linuxmint-22.1-cinnamon-64bit.iso.torrent",
    "magnet_link": "",
    "hardware_requirements": {
        "minimum": {
            "cpu": "64-bit dual-core CPU (2 GHz or higher)",
            "ram": "2 GB",
            "storage": "20 GB",
            "graphics": "1024×768 capable GPU",
            "network": "Ethernet or Wi-Fi"
        },
        "recommended": {
            "cpu": "64-bit quad-core CPU (2.4 GHz or higher)",
            "ram": "4 GB or more",
            "storage": "100 GB SSD",
            "graphics": "Dedicated GPU with 3D acceleration",
            "network": "Linux-compatible Ethernet or Wi-Fi"
        }
    }
}
print(json.dumps(data))
