import json
from pathlib import Path

def get_catalogue_path():
    return Path(__file__).parent.parent / 'OSCatalogue.json'

def find_unknowns(data, path=''):
    unknowns = []
    if isinstance(data, dict):
        for k, v in data.items():
            new_path = f"{path}/{k}" if path else k
            if isinstance(v, str) and v.lower() == 'unknown':
                unknowns.append(new_path)
            else:
                unknowns.extend(find_unknowns(v, new_path))
    elif isinstance(data, list):
        for idx, item in enumerate(data):
            unknowns.extend(find_unknowns(item, f"{path}[{idx}]"))
    return unknowns

def main():
    print("[STARTING OSCatalogueErrorManager]")
    path = get_catalogue_path()
    with open(path) as f:
        data = json.load(f)

    errors = find_unknowns(data)
    if errors:
        for e in errors:
            print(f"[WARNING {e}]")

    data['Errors'] = errors
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)

    print("[FINISHED OSCatalogueErrorManager]")

if __name__ == '__main__':
    main()
