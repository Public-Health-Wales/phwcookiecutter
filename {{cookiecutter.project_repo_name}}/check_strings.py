import re
import sys


def check_strings(files_to_check, strings_to_avoid_file):
    with open(strings_to_avoid_file, "r") as f:
        strings_to_avoid = [line.strip() for line in f.readlines()]

    for file_to_check in files_to_check:
        with open(file_to_check, "r") as f:
            content = f.read()

            for string_to_avoid in strings_to_avoid:
                if re.search(string_to_avoid, content):
                    print(
                        f"""Found string to avoid '{string_to_avoid}' in
                        file '{file_to_check}'"""
                    )
                    sys.exit(1)


if __name__ == "__main__":
    check_strings(sys.argv[1:], ".nocommitstrings")
