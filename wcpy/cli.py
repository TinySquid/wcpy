from argparse import ArgumentParser

from tabulate import tabulate


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

        words = len(contents.split())

        lines = contents.count("\n") + contents.count("\r\n")

        max_line_length = 0
        for line in contents.splitlines():
            line_length = len(line)

            if line_length > max_line_length:
                max_line_length = line_length

        # return [lines, words, chars, bytes, max_line_length, file]
        return {
            "lines": lines,
            "words": words,
            "chars": chars,
            "bytes": bytes,
            "max_line_length": max_line_length,
            "file_name": file,
        }


def format_stats_line_to_args(stats, args):
    stat_line = []

    if args.lines:
        stat_line.append(stats["lines"])
    if args.words:
        stat_line.append(stats["words"])
    if args.chars:
        stat_line.append(stats["chars"])
    if args.bytes:
        stat_line.append(stats["bytes"])
    if args.max_line_length:
        stat_line.append(stats["max_line_length"])

    if "file_name" in stats:
        stat_line.append(stats["file_name"])
    else:
        stat_line.append("total")

    return stat_line


def sum_total_stats(stats):
    totals = {"lines": 0, "words": 0, "chars": 0, "bytes": 0, "max_line_length": 0}

    for s in stats:
        totals["lines"] += s["lines"]
        totals["words"] += s["words"]
        totals["chars"] += s["chars"]
        totals["bytes"] += s["bytes"]

        if s["max_line_length"] > totals["max_line_length"]:
            totals["max_line_length"] = s["max_line_length"]

    return totals


def pretty_print_stats(stats, args):
    table = []

    for s in stats:
        stat_line = format_stats_line_to_args(s, args)
        table.append(stat_line)

    if len(stats) > 1:
        totals = sum_total_stats(stats)
        table.append(format_stats_line_to_args(totals, args))

    print(tabulate(table, tablefmt="plain"))


def cli():
    try:
        args = get_parsed_args()

        if args.files:
            stats = []

            for file in args.files:
                stats.append(get_file_stats(file))

            pretty_print_stats(stats, args)
    except Exception as e:
        print(e)
        exit(1)


if __name__ == "__main__":
    cli()
