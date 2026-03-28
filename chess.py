import chess 
import chess.syzygy
import chess.svg
import networkx as nx
import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def download_syzygy345(save_folder):
    url = "http://tablebase.sesse.net/syzygy/3-4-5/"

    # This header tells the server you are a browser, not a bot
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    print(f"Connecting to {url}...")
    try:
        # Pass the HEADERS here
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Failed to connect: {e}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    links = [urljoin(url, a['href']) for a in soup.find_all('a', href=True) 
             if a['href'].endswith(('.rtbw', '.rtbz'))]

    print(f"Found {len(links)} files. starting download...")

    for i, file_url in enumerate(links, 1):
        filename = os.path.basename(file_url)
        file_path = os.path.join(save_folder, filename)

        if os.path.exists(file_path):
            print(f"[{i}/{len(links)}] Skipping {filename}")
            continue

        try:
            # Pass HEADERS here too for the actual file download
            with requests.get(file_url, headers=HEADERS, stream=True, timeout=30) as r:
                r.raise_for_status()
                with open(file_path, 'wb') as f:
                    for chunk in r.iter_content(chunk_size=16384):
                        f.write(chunk)
            print(f"[{i}/{len(links)}] Finished: {filename}")
        except Exception as e:
            print(f"[{i}/{len(links)}] Error downloading {filename}: {e}")

if __name__=="__main__":
    download_syzygy345("syzygy_345")
    