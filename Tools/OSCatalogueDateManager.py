import json
import re
from pathlib import Path
from datetime import datetime
try:
    from dateutil import parser as dateparser
except:
    dateparser = None

def get_catalogue_path():
    return Path(__file__).parent.parent / 'OSCatalogue.json'

def normalize_date(raw):
    m = re.search(r'\(\s*(\d{4}-\d{2}-\d{2})\s*\)', raw)
    if m:
        return datetime.fromisoformat(m.group(1)).strftime('%d/%m/%Y')
    m2 = re.search(r'(\d{1,2}\s+\w+\s+\d{4})', raw)
    if m2 and dateparser:
        try:
            dt = dateparser.parse(m2.group(1))
            return dt.strftime('%d/%m/%Y')
        except:
            pass
    return raw

def process_versions(node):
    if isinstance(node, dict):
        if 'initial_release' in node:
            node['initial_release'] = normalize_date(node['initial_release'])
        if 'latest_release' in node:
            node['latest_release'] = normalize_date(node['latest_release'])
        for v in node.values():
            process_versions(v)
    elif isinstance(node, list):
        for item in node:
            process_versions(item)

def main():
    print("[STARTING OSCatalogueDateManager]")
    path = get_catalogue_path()
    data = json.loads(path.read_text())

    for section in ['RaspberryPi Distros', 'Linux Distros']:
        if section in data:
            process_versions(data[section])

    path.write_text(json.dumps(data, indent=2))
    print("[FINISHED OSCatalogueDateManager]")

if __name__ == '__main__':
    main()
