#
# Python MEGA-downloader
# Copyright (C) 2025 Felix Patryjas [schwienernitzel]
# pfelix0803@gmail.com
#

import os
import sys
from mega import Mega

def download_from_mega(link, output_folder="."):
    try:
        mega = Mega()
        mega_client = mega.login()

        print("Downloading...")
        file_path = mega_client.download_url(link, dest_path=output_folder)
        print(f"Success! File saved in {file_path}")

    except Exception as e:
        print(f"An error occurred while downloading the file: {e}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python download.py <mega_link> [output_folder]")
        sys.exit(1)

    link = sys.argv[1]
    output_folder = sys.argv[2] if len(sys.argv) > 2 else "."

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    download_from_mega(link, output_folder)

if __name__ == "__main__":
    main()
