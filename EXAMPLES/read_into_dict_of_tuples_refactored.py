"""
Read and display knight information from a file. 

Needs knights.txt for input.
"""
from pprint import pprint
DATA_FILE = "../DATA/knights.txt"  # treat this as read-only


def main():
    """
    Program entry point
    """
    data = read_data()
    pretty_print(data)
    print()
    print_names_and_titles(data)
    print()
    print(f"get_attribute(data, 'Robin', 2): {get_attribute(data, 'Robin', 2)}")


def read_data():
    """
    Read data from knights.txt into a dictionary.
    """
    knight_info = {}  # create empty dict

    with open(DATA_FILE, encoding="utf-8") as knights_in:
        for line in knights_in:
            name, title, color, quest, comment = line.rstrip('\n\r').split(":")
            # create new dict element with name as key and a tuple of the other fields as the value
            knight_info[name] = title, color, quest, comment
    return knight_info


def pretty_print(info):
    """
    Pretty-print the dictionary of knight data
    """
    pprint(info)


#   key   value
def print_names_and_titles(data):
    """
    For each knight, print the title and the name
    """
    for name, info in data.items():
        print(info[0], name)


def get_attribute(data, knight, attr_index):
    """
    Get one attribute from a particular knight
    """
    return data[knight][attr_index]


if __name__ == "__main__":
    main()
