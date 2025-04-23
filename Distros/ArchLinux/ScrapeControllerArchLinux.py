import sys
import subprocess
import json
from pathlib import Path

TOOLS_DIR = Path(__file__).parents[2] / 'Tools'
sys.path.append(str(TOOLS_DIR))
from OSCatalogueCurator import write_os_entry

SCRIPT_NAME = "ArchLinux"
SCRAPERS = {
    "ScrapeArchLinux64bit.py": True,
    "ScrapeArchLinuxArm.py": False,
    "ScrapeArchLinuxPPC.py": True,
    "ScrapeArchLinux32bit.py": False
}

def run_scraper(script):
    key = script[:-3]
    print(f"[STARTING {key}]")
    path = Path(__file__).parent / script
    if not path.exists():
        print(f"[FAILED {key}]")
        return None
    p = subprocess.run(
        [sys.executable, str(path)],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    if p.returncode != 0:
        print(f"[FAILED {key}]")
        if p.stderr:
            print(p.stderr.strip())
        return None
    try:
        return json.loads(p.stdout)
    except:
        print(f"[FAILED {key}]")
        if p.stdout:
            print(p.stdout.strip())
        return None

def main():
    print(f"[STARTING {SCRIPT_NAME}]")
    write_os_entry(
        ["Linux Distros", "Arch Linux"],
        {
            "name": "Arch Linux",
            "icon": "https://raw.githubusercontent.com/Cruizepeni/ProjectHomelabIcons/main/OperatingSystems/IconArchLinux.svg",
            "description": "Arch Linux is a lightweight, flexible Linux distribution with a rolling release model and a DIY ethos.",
            "homepage": "https://archlinux.org/",
            "documentation": ["https://wiki.archlinux.org/"],
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
            "distrowatch": ["https://distrowatch.com/table.php?distribution=arch"],
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
            "mailing_lists": ["https://lists.archlinux.org/mailman3/lists/"],
            "initial_release": "11/03/2002",
            "latest_release": "",
            "based_on": ["Independent"]
        }
    )
    for script, enabled in SCRAPERS.items():
        if not enabled:
            continue
        data = run_scraper(script)
        if data:
            write_os_entry(
                ["Linux Distros", "Arch Linux", "versions", data["name"]],
                data
            )
            write_os_entry(
                ["Linux Distros", "Arch Linux", "latest_release"],
                data["version"]
            )
    print(f"[COMPLETE {SCRIPT_NAME}]")
    print(f"[FINISHED {SCRIPT_NAME}]")

if __name__ == "__main__":
    main()
