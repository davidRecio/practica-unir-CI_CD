"""
License: Apache
Organization: UNIR
Asignature:Gestion de proyectos
"""

import os
import sys

DEFAULT_FILENAME = "words.txt"
DEFAULT_DUPLICATES = False
DEFAULT_ASCENDING = True

def sort_list(items, ascending=True):
    if not isinstance(items, list):
        raise RuntimeError(f"Cannot order {type(items)}")

    return sorted(items, reverse=(not ascending))

def remove_duplicates_from_list(items):
    return list(set(items))

if __name__ == "__main__":
    filename = DEFAULT_FILENAME
    remove_duplicates = DEFAULT_DUPLICATES
    ascending = DEFAULT_ASCENDING

    if len(sys.argv) == 4:
        filename = sys.argv[1]
        remove_duplicates = sys.argv[2].lower() == "yes"
        ascending = sys.argv[3].lower() == "asc"
    else:
        print("Uso: python script.py <fichero> <eliminar_duplicados: yes/no> <orden: asc/desc>")
        print("You must pass the file as the first parameter")
        print("The second parameter indicates if you want to remove duplicates")
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

    if remove_duplicates:
        word_list = remove_duplicates_from_list(word_list)

    sorted_words = sort_list(word_list, ascending=ascending)
    print(sorted_words)
