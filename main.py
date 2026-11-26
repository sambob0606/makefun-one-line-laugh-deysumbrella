"""One Line, One Laugh — writes a single funny line to /output/entry.txt."""

import os

LINE = (
    "I finally organized my junk drawer; now I still can't find anything, "
    "but at least I can lose it alphabetically."
)


def main() -> None:
    out_dir = "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(LINE + "\n")
    except OSError:
        os.makedirs("output", exist_ok=True)
        with open(os.path.join("output", "entry.txt"), "w", encoding="utf-8") as f:
            f.write(LINE + "\n")


if __name__ == "__main__":
    main()
