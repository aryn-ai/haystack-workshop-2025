# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "requests",
#     "tqdm",
# ]
# ///

from pathlib import Path
import requests
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm

def main() -> None:
    workshop_root = Path(__file__).parent.parent
    p = workshop_root / "s3_download_list_http.txt"
    file_dir = workshop_root / "files" / "earnings_calls"
    file_dir.mkdir(exist_ok=True, parents=True)
    with open(p, "r") as f:
        urls = [u.strip() for u in f.readlines()]

    sess = requests.Session()
    with ThreadPoolExecutor(max_workers=10) as tpe:
        futures = [(url, tpe.submit(sess.get, url)) for url in urls]
        for url, fut in tqdm(futures):
            fn = url[url.rfind("/") + 1:]
            resp = fut.result()
            with open(file_dir / fn, 'wb') as f:
                f.write(resp.content)


if __name__ == "__main__":
    main()
