import sys
import requests
import json
import re
from bs4 import BeautifulSoup

def get_remote_file_size(url):
    try:
        head = requests.head(url, allow_redirects=True, timeout=10)
        size_bytes = int(head.headers.get("Content-Length", 0))
        return f"{round(size_bytes / (1024**2), 2)} MB" if size_bytes else ""
    except:
        return ""

def main():
    resp = requests.get("https://mirror.rackspace.com/archlinux/iso/latest/", timeout=10)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")
    iso_link = ""
    version = ""
    for a in soup.find_all("a", href=True):
        href = a["href"]
        if href.startswith("archlinux-") and href.endswith("-x86_64.iso"):
            iso_link = "https://mirror.rackspace.com/archlinux/iso/latest/" + href
            m = re.search(r"archlinux-([\d\.]+)-x86_64\.iso", href)
            if m:
                version = m.group(1)
            break
    if not iso_link:
        sys.exit(1)
    size = get_remote_file_size(iso_link)
    data = {
        "name": f"Arch Linux {version} x86_64",
        "version": version,
        "download_url": iso_link,
        "size": size,
        "arch": "x86_64",
        "icon": "https://raw.githubusercontent.com/Cruizepeni/ProjectHomelabIcons/main/OperatingSystems/IconArchLinux.svg",
        "description": "Arch Linux is a lightweight, flexible Linux distribution with a rolling release model and a DIY ethos.",
        "homepage": "https://archlinux.org/",
        "documentation": [
            "https://wiki.archlinux.org/"
        ],
        "wikis": [
            "https://en.wikipedia.org/wiki/Arch_Linux",
            "https://simple.wikipedia.org/wiki/Arch_Linux",
            "https://linux.fandom.com/wiki/Arch_Linux",
            "https://wiki.archlinux.org/",
            "https://archlinuxarm.org/wiki"
        ],
        "install_guides": [
            "https://wiki.archlinux.org/title/Installation_guide",
            "https://www.reddit.com/r/archlinux/comments/17s5ggz/modern_arch_linux_installation_guide_ideal_for/",
            "https://phoenixnap.com/kb/arch-linux-install",
            "https://itsfoss.com/install-arch-linux/",
            "https://www.freecodecamp.org/news/how-to-install-arch-linux/",
            "https://github.com/silentz/arch-linux-install-guide",
            "https://www.linux.org/threads/getting-started-with-arch-linux-a-beginners-installation-guide.53535/",
            "https://www.youtube.com/watch?v=FxeriGuJKTM",
            "https://www.youtube.com/watch?v=8YE1LlTxfMQ",
            "https://www.youtube.com/watch?v=LiG2wMkcrFE"
        ],
        "distrowatch": [
            "https://distrowatch.com/table.php?distribution=arch"
        ],
        "github_repos": [
            "https://github.com/archlinux",
            "https://github.com/archlinux/archinstall",
            "https://github.com/archlinux/arch-install-scripts",
            "https://github.com/archlinux/aurweb",
            "https://github.com/archlinux/archweb"
        ],
        "forums": [
            "https://bbs.archlinux.org/",
            "https://www.reddit.com/r/archlinux/",
            "https://archlinuxarm.org/forum/",
            "https://bbs.archlinux32.org/"
        ],
        "mailing_lists": [
            "https://lists.archlinux.org/mailman3/lists/"
        ],
        "type": "Rolling Release",
        "based_on": [
            "Independent"
        ],
        "checksum": "",
        "torrent_url": "https://archlinux.org/releng/releases/2025.04.01/torrent/",
        "magnet_link": "magnet:?xt=urn:btih:f0d8c74420b1f845c9b892e44cf595f79b56687b&dn=archlinux-2025.04.01-x86_64.iso",
        "hardware_requirements": {
            "minimum": {
                "cpu": "x86-64 compatible CPU",
                "ram": "512 MB",
                "storage": "2 GB",
                "graphics": "VGA-capable",
                "network": "Ethernet or Wi-Fi"
            },
            "recommended": {
                "cpu": "Dual-core 2 GHz",
                "ram": "4 GB",
                "storage": "20 GB SSD",
                "graphics": "GPU with 3D support",
                "network": "Ethernet or Wi-Fi"
            }
        }
    }
    print(json.dumps(data))

if __name__ == "__main__":
    main()
