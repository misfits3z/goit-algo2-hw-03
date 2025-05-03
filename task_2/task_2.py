import csv
import timeit
from BTrees.OOBTree import OOBTree

"""Час виконання 100 запитів для OOBTree: 0.281176 секунд
   Час виконання 100 запитів для dict: 1.037853 секунд"""

# Функція для завантаження даних із CSV
def load_data(file_path):
    data = []
    with open(file_path, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            row["ID"] = int(row["ID"])
            row["Price"] = float(row["Price"])
            data.append(row)
    return data


# Функція для додавання товарів у OOBTree
def add_item_to_tree(tree, item):
    tree[(item["Price"], item["ID"])] = {
        "Name": item["Name"],
        "Category": item["Category"],
    }


# Функція для додавання товарів у dict
def add_item_to_dict(dictionary, item):
    dictionary[item["ID"]] = {
        "Name": item["Name"],
        "Category": item["Category"],
        "Price": item["Price"],
    }


def range_query_tree(tree, min_price, max_price):
    return [
        value for key, value in tree.items((min_price, 0), (max_price, float("inf")))
    ]


def range_query_dict(dictionary, min_price, max_price):
    return [
        value
        for key, value in dictionary.items()
        if min_price <= value["Price"] <= max_price
    ]


def main():
    # Завантаження даних
    file_path = "task_2/generated_items_data.csv"
    data = load_data(file_path)

    # Ініціалізація структур даних
    tree = OOBTree()
    dictionary = {}

    # Додавання даних у структури
    for item in data:
        add_item_to_tree(tree, item)
        add_item_to_dict(dictionary, item)

    # Визначення діапазону цін
    min_price = 50.0
    max_price = 150.0

    # Вимірювання часу виконання діапазонного запиту для OOBTree
    tree_time = timeit.timeit(
        lambda: range_query_tree(tree, min_price, max_price), number=100
    )

    # Вимірювання часу виконання діапазонного запиту для dict
    dict_time = timeit.timeit(
        lambda: range_query_dict(dictionary, min_price, max_price), number=100
    )

    # Виведення результатів
    print(f"Час виконання 100 запитів для OOBTree: {tree_time:.6f} секунд")
    print(f"Час виконання 100 запитів для dict: {dict_time:.6f} секунд")


if __name__ == "__main__":
    main()
