# wcpy

A `wc` clone written with Python. It is a commandline tool that reads any number of files or from stdin and returns stats about newline count, word count, and byte count depending on flags provided.


```
usage: wcpy [-h] [-c] [-m] [-l] [--files0-from=F [FILES0_FROM=F ...]] [-L] [-w] [files ...]

Print newline, word, and byte counts for each FILE, and a total line if more than one FILE is specified. A word is a
non-zero-length sequence of characters delimited by white space.

positional arguments:
  files                 a file or many files separated by a space

options:
  -h, --help            show this help message and exit
  -c, --bytes           print the byte counts
  -m, --chars           print the character counts
  -l, --lines           print the newline counts
  --files0-from=F [FILES0_FROM=F ...]
                        read input from the files specified by NUL-terminated names in file F; If F is '-' then read
                        names from standard input
  -L, --max-line-length
                        print the maximum display width
  -w, --words           print the word counts
```