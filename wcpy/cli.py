from argparse import ArgumentParser
from math import inf as infinity


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


def get_file_stats(file):
    with open(file, "r", encoding="utf-8") as f:
        contents = f.read()
        chars = bytes = len(contents)
        words = len(contents.split(" "))

        lines = 0
        max_line_length = -infinity
        for line in contents.splitlines():
            line_length = len(line)

            if line_length > max_line_length:
                max_line_length = line_length

            lines += 1

        return {
            "lines": lines,
            "words": words,
            "chars": chars,
            "bytes": bytes,
            "max_line_length": max_line_length,
            "file_name": file,
        }


def cli():
    try:
        args = get_parsed_args()

        if args.files:
            output = get_file_stats(args.files[0])
            pretty_print_string = ""

            for key in output:
                pretty_print_string += f" {output[key]}"

            pretty_print_string.rstrip()

            print(pretty_print_string)
    except Exception as e:
        print(e)
        exit(1)


if __name__ == "__main__":
    cli()
