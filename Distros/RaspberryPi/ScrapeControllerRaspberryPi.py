import sys
from pathlib import Path
import requests

# point at OSCatalogue/Tools regardless of cwd
TOOLS_DIR = Path(__file__).parent.parent.parent / 'Tools'
sys.path.append(str(TOOLS_DIR))

from OSCatalogueCurator import write_os_entry

SCRIPT_NAME = "RaspberryPi"

def main():
    print(f"[STARTING {SCRIPT_NAME}]")
    try:
        url = "https://downloads.raspberrypi.org/os_list_imagingutility_v4.json"
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        rpi_data = resp.json()

        write_os_entry(
            ["RaspberryPi Distros"],
            rpi_data
        )

        print(f"[COMPLETE {SCRIPT_NAME}]")
    except Exception as e:
        print(f"[FAILED {SCRIPT_NAME}] {e}")
    finally:
        print(f"[FINISHED {SCRIPT_NAME}]")

if __name__ == "__main__":
    main()
