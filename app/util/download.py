"""Blabl"""

import os
import requests


def download_if_not_exist(url: str, filename: str) -> None:
    """Download a file if it does not exist
    Args:
        url (str): URL to download from
        filename (str): Filename to save to
    """
    if not os.path.exists(filename):
        response = requests.get(url, allow_redirects=True, timeout=60)
        print(f"Downloading {filename}")
        open(filename, 'wb').write(response.content)
    else:
        print(f"File {filename} already exits")
