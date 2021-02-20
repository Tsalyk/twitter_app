import json
from pprint import pprint


def main(path_to_file: str) -> None:
    """
    Main function. Launches all process
    """
    data = read_json(path_to_file)
    navigation_on_json(data)


def read_json(path_to_file: str) -> dict or list:
    """
    Reads json and converts in Python object
    """
    with open(path_to_file, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


def navigation_on_json(data: dict or list) -> None:
    """
    Navigates through json data
    """
    if isinstance(data, list):
        print(f"It is list object!\nIt containes {len(data)} elements.\n")
        answer = input("Would you like to see it? (Yes/No): ")
        print()

        if answer.lower() == "yes":
            for ind, el in enumerate(data):
                pprint(f"Index: {ind} — Element: {el}")
                print()
            print()

        ind = int(input("Please enter an index which you'd like to "
                        f"view (range [0:{len(data)-1}]): "))

        while not 0 <= ind <= len(data):
            ind = int(input("Please enter an index in "
                            f"range [0:{len(data)-1})]: "))

        print()
        return navigation_on_json(data[ind])


    elif isinstance(data, dict):
        print("It is dict object!\nIt consists of "
              f"forward keys: {data.keys()}")
        key = input("Please enter a key which you'd like to view: ")

        while key not in data:
            key = input("Please enter a key which is in dict: ")

        print()
        return navigation_on_json(data[key])

    else:
        print(f"It is final data: {data}")
        return None