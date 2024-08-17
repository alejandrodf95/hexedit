#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# A simple script to modify hexadecimal values in files.
# Author: alejandrodf95 / https://github.com/alejandrodf95
# Date: 2024-8-17

import os

FILE_NAME = "file.exe"
ORIGINAL_STRING = "750541c6463a11488d8d"
NEW_STRING = "eb0541c6463a11488d8d"


def edit_exe(exe_file):
    with open(exe_file, "rb") as f:
        data = f.read()
        hex_data = data.hex()

        if ORIGINAL_STRING in hex_data:
            modified_hex_data = hex_data.replace(ORIGINAL_STRING, NEW_STRING)
            modified_data = bytes.fromhex(modified_hex_data)

            with open(exe_file, "wb") as f:
                f.write(modified_data)

        else:
            raise ValueError(
                f"The string '{ORIGINAL_STRING}' was not found in the file."
            )


def main():
    try:
        if os.path.exists(FILE_NAME):
            edit_exe(FILE_NAME)
            print(f"The file '{FILE_NAME}' has been modified.")
        else:
            raise ValueError(
                f"Error: The file '{FILE_NAME}' is not found in the directory."
            )
    except ValueError as ve:
        print(ve)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
