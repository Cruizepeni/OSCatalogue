import json
import subprocess
import sys
from pathlib import Path

def load_settings():
    return json.loads((Path(__file__).parent.parent / 'OSCatalogueSettings.json').read_text())

def ensure_initial_json():
    catalog_path = Path(__file__).parent.parent / 'OSCatalogue.json'
    if not catalog_path.exists():
        initial = {
            "RaspberryPi Distros": {},
            "Linux Distros": {},
            "Help": {},
            "Errors": []
        }
        catalog_path.write_text(json.dumps(initial, indent=2))
        print("[COMPLETE Initial JSON setup]")

def find_controllers(settings):
    controllers = []
    for distro, enabled in settings.get('distros', {}).items():
        if not enabled:
            continue
        module_key = distro.replace(" ", "").replace(".", "")
        script_name = f"ScrapeController{module_key}.py"
        script_path = Path(__file__).parent.parent / 'Distros' / module_key / script_name
        controllers.append((module_key, script_path))
    return controllers

def run_controllers_parallel(controllers):
    procs = []
    for name, path in controllers:
        print(f"[STARTING {name}]")
        p = subprocess.Popen(
            [sys.executable, str(path)],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        procs.append((name, p))

    for name, p in procs:
        stdout, stderr = p.communicate()
        if p.returncode == 0:
            print(f"[COMPLETE {name}]")
        else:
            print(f"[FAILED {name}]")
            if stdout:
                print("--- stdout ---")
                print(stdout.strip())
            if stderr:
                print("--- stderr ---")
                print(stderr.strip())
        print(f"[FINISHED {name}]")

def main():
    print("[STARTING OSCatalogueMaster]")

    ensure_initial_json()

    settings = load_settings()
    if settings.get('scrape_distros', False):
        controllers = find_controllers(settings)
        run_controllers_parallel(controllers)

    # post‑processing
    subprocess.run([sys.executable, str(Path(__file__).parent / 'OSCatalogueDateManager.py')])
    subprocess.run([sys.executable, str(Path(__file__).parent / 'OSCatalogueErrorManager.py')])

    print("[FINISHED OSCatalogueMaster]")

if __name__ == '__main__':
    main()
