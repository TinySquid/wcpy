import argparse

def main():
  try:
    parser = argparse.ArgumentParser()
    parser.add_argument("files", nargs='*')
    args = parser.parse_args()
    print(args.files)

  except Exception as e:
    print(e)


if __name__ == "__main__":
  main()