from pathlib import Path

p = Path.home() / ".ruwfs"
image_dir = p / "images"
archive_dir = image_dir / "archive"
tmp_dir = p / "tmp"
obuffer = tmp_dir / "outputs.json"

paths = [p, image_dir, archive_dir, tmp_dir]

# for path in paths:
#     if not path.exists():
#         path.mkdir(parents=True) # make the directory and all parent directories

for file in image_dir.glob("*.jpg"):
    file.rename(archive_dir / file.name)

if obuffer.is_file():
    print("yes")
else:
    print("no")
