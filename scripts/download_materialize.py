# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "requests",
# ]
# ///

from pathlib import Path
import requests
import tarfile


def main() -> None:
    workshop_root = Path(__file__).parent.parent
    materialize_dir = workshop_root / "materialize2"
    materialize_dir.mkdir(exist_ok=True)
    urls = [
        "https://aryn-public.s3.us-east-1.amazonaws.com/haystack_documents/alldocs-partitioned.tar.xz",
        "https://aryn-public.s3.us-east-1.amazonaws.com/haystack_documents/about-to-ingest.tar.xz"
    ]
    for url in urls:
        print(f"GET {url} and unpack it")
        resp = requests.get(url, stream=True)
        with tarfile.open(fileobj=resp.raw, mode='r|xz') as tf:
            tf.extractall(materialize_dir)


if __name__ == "__main__":
    main()
