import json
import re
import shutil
from pathlib import Path
import requests
import zipfile
import io

def load_settings():
    return json.loads(Path(__file__).parent.parent.joinpath('settings.json').read_text())

def main():
    print("[UPDATE STARTING]")
    try:
        settings = load_settings()
        url = settings.get('update_from')
        m = re.match(r'https://github.com/([^/]+/[^/]+)/tree/([^/]+)/(.+)', url)
        if not m:
            print("[UPDATE FAILED]")
            return

        repo, branch, subpath = m.groups()
        zip_url = f'https://github.com/{repo}/archive/refs/heads/{branch}.zip'
        r = requests.get(zip_url)
        r.raise_for_status()

        z = zipfile.ZipFile(io.BytesIO(r.content))
        prefix = f"{repo.split('/')[1]}-{branch}/{subpath.rstrip('/')}/"
        dest = Path(__file__).parent.parent / 'Distros'
        shutil.rmtree(dest, ignore_errors=True)

        for member in z.namelist():
            if member.startswith(prefix) and not member.endswith('/'):
                rel = member[len(prefix):]
                target = dest / rel
                target.parent.mkdir(parents=True, exist_ok=True)
                with z.open(member) as src, open(target, 'wb') as out:
                    out.write(src.read())

        print("[UPDATE FINISHED]")
    except Exception:
        print("[UPDATE FAILED]")

if __name__ == '__main__':
    main()
