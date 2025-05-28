import glob


if __name__ == "__main__":
    print(
        glob.glob(
            "**/??dex.html",
            root_dir="53-glob/public",
            recursive=True,
            include_hidden=True,  # python 3.11
        )
    )  # ['index.html', 'categories/index.html']
    """
    ** -> unlimited files | unlimited Folders
    ?? -> Any Character instead of each "?" (Unix path expansion rules)
    ~ is not expanded

    load all the files at once
    """

    # * -> matches everything
    print(
        glob.glob("**/*.html", root_dir="53-glob", recursive=True)
    )  # ['public/index.html', 'public/landing.html', 'public/categories/index.html']

    # [] -> matches ant character in the sequence ex. [al] [la]
    print(
        glob.glob("**/[la]*.html", root_dir="53-glob", recursive=True)
    )  # ['public/landing.html']
    print(
        glob.glob("**/[al]*.html", root_dir="53-glob", recursive=True)
    )  # ['public/landing.html']
    print(
        glob.glob("**/[la][a]*.html", root_dir="53-glob", recursive=True)
    )  # ['public/landing.html']

    # [!] -> matches ant character not in the sequence
    print(
        glob.glob("**/[!la]*.html", root_dir="53-glob", recursive=True)
    )  # ['public/index.html', 'public/categories/index.html']

    # generator version
    globs = glob.iglob(
        "**/*.html",
        root_dir="53-glob/public",
        recursive=True,
        include_hidden=True,
    )
    print(globs)  # <itertools.chain object at 0x105263700>
    # print(next(globs))
    # print(globs.__next__())
    # print(next(globs))

    # load into memory one by one (much more memory efficient)
    for i, file in enumerate(globs):
        print(i, file, sep=":")
