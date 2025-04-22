import json
import os
from pathlib import Path
import portalocker

JSON_FILENAME = 'OSCatalogue.json'

def get_catalogue_path():
    return Path(__file__).parent.parent / JSON_FILENAME

def write_os_entry(category_path, entry_data):
    json_path = get_catalogue_path()
    os.makedirs(json_path.parent, exist_ok=True)
    if not json_path.exists() or os.path.getsize(json_path) == 0:
        with open(json_path, 'w') as f:
            json.dump({'RaspberryPi Distros': {}, 'Linux Distros': {}, 'Help': {}, 'Errors': {}}, f, indent=2)
    with portalocker.Lock(str(json_path), mode='r+', timeout=5) as f:
        try:
            f.seek(0)
            data = json.load(f)
        except:
            data = {'RaspberryPi Distros': {}, 'Linux Distros': {}, 'Help': {}, 'Errors': {}}
        ref = data
        for key in category_path[:-1]:
            ref = ref.setdefault(key, {})
        ref[category_path[-1]] = entry_data
        f.seek(0)
        f.truncate()
        json.dump(data, f, indent=2)
