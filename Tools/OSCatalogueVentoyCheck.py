import os
import requests
import re
import shutil
from pathlib import Path

VENTOY_DIR = Path(__file__).resolve().parent / "Ventoy"
GITHUB_API_RELEASES_URL = "https://api.github.com/repos/ventoy/Ventoy/releases/latest"

def ensure_directory(path):
    if not path.exists():
        path.mkdir(parents=True)

def get_latest_version():
    response = requests.get(GITHUB_API_RELEASES_URL)
    if response.status_code == 200:
        data = response.json()
        tag = data.get("tag_name")
        if tag and tag.startswith("v"):
            return tag[1:]
    raise Exception("Could not determine latest Ventoy version.")

def download_ventoy_files(version):
    base_url = f"https://github.com/ventoy/Ventoy/releases/download/v{version}"
    linux_filename = f"ventoy-{version}-linux.tar.gz"
    windows_filename = f"ventoy-{version}-windows.zip"
    linux_url = f"{base_url}/{linux_filename}"
    windows_url = f"{base_url}/{windows_filename}"

    linux_dest = VENTOY_DIR / linux_filename
    windows_dest = VENTOY_DIR / windows_filename

    print("[VENTOY DOWNLOADING]")
    download_file(linux_url, linux_dest)
    download_file(windows_url, windows_dest)

def download_file(url, destination):
    with requests.get(url, stream=True) as r:
        if r.status_code == 200:
            with open(destination, "wb") as f:
                shutil.copyfileobj(r.raw, f)
        else:
            raise Exception(f"Failed to download {url}")

def get_current_version():
    linux_files = list(VENTOY_DIR.glob("ventoy-*-linux.tar.gz"))
    windows_files = list(VENTOY_DIR.glob("ventoy-*-windows.zip"))
    if linux_files and windows_files:
        linux_version = re.search(r"ventoy-([0-9.]+)-linux", linux_files[0].name)
        windows_version = re.search(r"ventoy-([0-9.]+)-windows", windows_files[0].name)
        if linux_version and windows_version:
            if linux_version.group(1) == windows_version.group(1):
                return linux_version.group(1)
    return None

def cleanup_old_versions():
    for file in VENTOY_DIR.glob("ventoy-*.tar.gz"):
        file.unlink()
    for file in VENTOY_DIR.glob("ventoy-*.zip"):
        file.unlink()

def main():
    ensure_directory(VENTOY_DIR)
    current_version = get_current_version()
    latest_version = get_latest_version()

    print("[VENTOY CHECKED]")

    if current_version == latest_version:
        print("[VENTOY UP TO DATE]")
        return

    cleanup_old_versions()
    download_ventoy_files(latest_version)
    print("[VENTOY UPDATED]")

if __name__ == "__main__":
    main()
