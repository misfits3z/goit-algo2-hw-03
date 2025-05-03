
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

node_names = {
    0: "Термінал 1",
    1: "Склад 1",
    2: "Склад 2",
    3: "Склад 3",
    4: "Термінал 2",
    5: "Склад 4",
    6: "Магазин 1",
    7: "Магазин 2",
    8: "Магазин 3",
    9: "Магазин 4",
    10: "Магазин 5",
    11: "Магазин 6",
    12: "Магазин 7",
    13: "Магазин 8",
    14: "Магазин 9",
    15: "Магазин 10",
    16: "Магазин 11",
    17: "Магазин 12",
    18: "Магазин 13",
    19: "Магазин 14",
    20: "Джерело",
    21: "Стік",
}

# Перейменовані ребра з назвами
edges_named = [
    (node_names[0], node_names[1], 25),
    (node_names[0], node_names[2], 20),
    (node_names[0], node_names[3], 15),
    (node_names[4], node_names[3], 15),
    (node_names[4], node_names[5], 30),
    (node_names[4], node_names[2], 10),
    (node_names[1], node_names[6], 15),
    (node_names[1], node_names[7], 10),
    (node_names[1], node_names[8], 20),
    (node_names[2], node_names[9], 15),
    (node_names[2], node_names[10], 10),
    (node_names[2], node_names[11], 25),
    (node_names[3], node_names[12], 20),
    (node_names[3], node_names[13], 15),
    (node_names[3], node_names[14], 10),
    (node_names[5], node_names[15], 20),
    (node_names[5], node_names[16], 10),
    (node_names[5], node_names[17], 15),
    (node_names[5], node_names[18], 5),
    (node_names[5], node_names[19], 10),
    (node_names[20], node_names[0], 60),
    (node_names[20], node_names[4], 55),
]

# Додаємо зв'язки до стоку
for i in range(6, 20):
    edges_named.append((node_names[i], node_names[21], 30))

# Створення графа
G_named = nx.DiGraph()
G_named.add_weighted_edges_from(edges_named)

# Нова позиція вузлів
pos_named = {
    node_names[6]: (0, 4),
    node_names[7]: (1, 4),
    node_names[8]: (2, 4),
    node_names[9]: (4, 4),
    node_names[10]: (5, 4),
    node_names[11]: (6, 4),
    node_names[1]: (1, 3),
    node_names[2]: (5, 3),
    node_names[0]: (1, 2),
    node_names[4]: (5, 2),
    node_names[3]: (1, 1),
    node_names[5]: (5, 1),
    node_names[12]: (0, 0),
    node_names[13]: (1, 0),
    node_names[14]: (2, 0),
    node_names[15]: (3, 0),
    node_names[16]: (4, 0),
    node_names[17]: (5, 0),
    node_names[18]: (6, 0),
    node_names[19]: (7, 0),
    node_names[20]: (3, 5),
    node_names[21]: (3, -1),
}

# Візуалізація
plt.figure(figsize=(14, 8))
nx.draw(
    G_named,
    pos_named,
    with_labels=True,
    node_size=2000,
    node_color="lightblue",
    font_size=9,
    font_weight="bold",
    arrows=True,
)

edge_labels_named = nx.get_edge_attributes(G_named, "weight")
nx.draw_networkx_edge_labels(G_named, pos_named, edge_labels=edge_labels_named)

plt.title("Іменований граф постачання")
plt.tight_layout()
plt.show()

capacity_matrix = nx.to_numpy_array(G_named, dtype=int)
print("Матриця пропускної здатності:")
print(capacity_matrix.astype(int))
