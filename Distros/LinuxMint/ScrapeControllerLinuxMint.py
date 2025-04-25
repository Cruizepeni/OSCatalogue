import sys
import subprocess
import json
from pathlib import Path

TOOLS_DIR = Path(__file__).parents[2] / 'Tools'
sys.path.append(str(TOOLS_DIR))
from OSCatalogueCurator import write_os_entry

SCRIPT_NAME = "LinuxMint"
SCRAPERS = {
    "ScrapeLinuxMintCinnamon64bit.py": True,
    "ScrapeLinuxMintMATE64bit.py": True,
    "ScrapeLinuxMintXFCE64bit.py": True
}

def get_wiki_dates():
    initial = "Unknown"
    latest  = "Unknown"
    try:
        import requests
        from bs4 import BeautifulSoup
        resp = requests.get("https://en.wikipedia.org/wiki/Linux_Mint", timeout=10)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, 'html.parser')
        infobox = soup.find("table", class_="infobox")
        if infobox:
            for row in infobox.find_all("tr"):
                th = row.find("th")
                td = row.find("td")
                if not th or not td:
                    continue
                text = td.get_text(separator=" ").strip().replace('\xa0',' ')
                if "Initial release" in th.text:
                    initial = text
                elif "Latest release" in th.text:
                    latest = text
    except:
        pass
    return initial, latest

def run_scraper(script_name):
    key = script_name[:-3]
    print(f"[STARTING {key}]")
    path = Path(__file__).parent / script_name
    if not path.exists():
        print(f"[FAILED {key}]")
        print(f"[FINISHED {key}]")
        return None
    p = subprocess.run([sys.executable, str(path)], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if p.returncode != 0:
        print(f"[FAILED {key}]")
        if p.stderr:
            print(p.stderr.strip())
        print(f"[FINISHED {key}]")
        return None
    try:
        data = json.loads(p.stdout)
        print(f"[COMPLETE {key}]")
        print(f"[FINISHED {key}]")
        return data
    except:
        print(f"[FAILED {key}]")
        if p.stdout:
            print(p.stdout.strip())
        print(f"[FINISHED {key}]")
        return None

def main():
    print(f"[STARTING {SCRIPT_NAME}]")
    initial, latest = get_wiki_dates()
    write_os_entry(
        ["Linux Distros","Linux Mint"],
        {
            "name": "Linux Mint",
            "icon": "https://raw.githubusercontent.com/Cruizepeni/ProjectHomelabIcons/main/OperatingSystems/IconLinuxMint.svg",
            "description": "Linux Mint is a community-driven Linux distribution based on Ubuntu or Debian that strives to be a modern, elegant and comfortable operating system which is both powerful and easy to use.",
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
            "initial_release": initial,
            "latest_release": latest,
            "based_on": ["Ubuntu","Debian"]
        }
    )
    for script, enabled in SCRAPERS.items():
        if enabled:
            data = run_scraper(script)
            if data:
                write_os_entry(
                    ["Linux Distros","Linux Mint","versions",data["name"]],
                    data
                )
    print(f"[COMPLETE {SCRIPT_NAME}]")
    print(f"[FINISHED {SCRIPT_NAME}]")

if __name__=="__main__":
    main()
