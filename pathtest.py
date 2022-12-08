from pathlib import Path


def paths():
    paths
    home = Path.home() / ".ruwfs"
    image_dir = home / "images"
    archive_dir = image_dir / "archive"
    tmp_dir = home / "tmp"
    paths = paths.append([home, image_dir, archive_dir, tmp_dir])

    # for path in paths:
    #     if not path.exists():
    #         path.mkdir(parents=True)

    obuffer = paths[0][3] / "outputs.json"
    cached_outputs = paths[0][3] / "cached_outputs.json"

    paths = paths.append([obuffer, cached_outputs])

    for i in paths():
        print(i)


def main():
    paths()
    # paths = paths()[0]
    # files = paths()[1]

    # print(paths)
    # print(files)


# for path in paths:
#     if not path.exists():
#         path.mkdir(parents=True) # make the directory and all parent directories

# for file in image_dir.glob("*.jpg"):
#     file.rename(archive_dir / file.name)

# if obuffer.is_file():
#     print("yes")
# else:
#     print("no")

if __name__ == "__main__":
    main()
