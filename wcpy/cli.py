from argparse import ArgumentParser


def get_parsed_args():
    parser = ArgumentParser(
        description=(
            "Print newline, word, and byte counts for each FILE, and a total line if more than one FILE is"
            " specified. A word is a non-zero-length sequence of characters delimited by white space."
        )
    )

    parser.add_argument("files", nargs="*", help="a file or many files separated by a space")
    parser.add_argument("-c", "--bytes", help="print the byte counts", action="store_true")
    parser.add_argument("-m", "--chars", help="print the character counts", action="store_true")
    parser.add_argument("-l", "--lines", help="print the newline counts", action="store_true")

    parser.add_argument(
        "--files0-from=F",
        nargs="*",
        help=(
            "read input from the files specified by NUL-terminated names in file F; If F is '-' then read names"
            " from standard input"
        ),
    )

    parser.add_argument("-L", "--max-line-length", help="print the maximum display width", action="store_true")

    parser.add_argument("-w", "--words", help="print the word counts", action="store_true")

    return parser.parse_args()


def cli():
    try:
        args = get_parsed_args()

        print(args)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    cli()
