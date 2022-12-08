import subprocess
import os
import requests
import json
import time
import random
from pathlib import Path


def main():
    home = Path.home() / ".ruwfs"
    image_dir = home / "images"
    archive_dir = image_dir / "archive"
    tmp_dir = home / "tmp"
    obuffer = tmp_dir / "outputs.json"
    paths = [home, image_dir, archive_dir, tmp_dir]

    with open(obuffer, "r") as f:
        outputs = json.load(f)

    # output_list = outputs[0]["name"]
    output_list = []

    for i in range(len(outputs)):
        output_list.append(outputs[i]["name"])
    print(output_list)


if __name__ == "__main__":
    main()
