"""
License: Apache
Organization: UNIR
Asignature: Gestion de proyectos
"""

import os
import sys

DEFAULT_FILENAME = "words.txt"
DEFAULT_DUPLICATES = False


def sort_list(items, ascending=True, remove_duplicates=False):
    if not isinstance(items, list):
        raise RuntimeError(f"Cannot order {type(items)}")

    if remove_duplicates:
        items = list(set(items))

    return sorted(items, reverse=(not ascending))


if __name__ == "__main__":
    filename = DEFAULT_FILENAME
    remove_duplicates = DEFAULT_DUPLICATES

    if len(sys.argv) == 3:
        filename = sys.argv[1]
        remove_duplicates = sys.argv[2].lower() == "yes"
    else:
        print("You must pass the file as the first parameter")
        print("The second parameter indicates if you want to remove duplicates ('yes' or 'no')")
        sys.exit(1)

    print(f"Will read the words from {filename}")
    file_path = os.path.join(".", filename)
    
    if os.path.isfile(file_path):
        word_list = []
        with open(file_path, "r") as file:
            for line in file:
                word_list.append(line.strip())
    else:
        print(f"Filename {filename} doesn't exist")
        word_list = ["ravenclaw", "gryffindor", "slytherin", "hufflepuff"]

    sorted_list = sort_list(word_list, ascending=True, remove_duplicates=remove_duplicates)

    print(sorted_list)
