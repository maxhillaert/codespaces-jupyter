"""Blabl"""

import os
import requests
from tqdm import tqdm

def download_if_not_exist(url: str, filename: str) -> None:
    """Download a file if it does not exist
    Args:
        url (str): URL to download from
        filename (str): Filename to save to
    """
    if not os.path.exists(filename):
        response = requests.get(url, allow_redirects=True, timeout=60)
        total = int(response.headers.get('content-length', 0))
        with open(filename, 'wb') as file, tqdm(
                desc=filename,
                total=total,
                unit='iB',
                unit_scale=True,
                unit_divisor=1024,
        ) as prog_bar:
            for data in response.iter_content(chunk_size=1024):
                size = file.write(data)
                prog_bar.update(size)
    else:
        print(f"File {filename} already exits")
