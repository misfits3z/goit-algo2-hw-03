from bfs import edmonds_karp
from graph import capacity_matrix

if __name__ == "__main__":

    source = 20  # Джерело 1
    sink = 21  # Споживач 3

    max_flow, flow_matrix = edmonds_karp(capacity_matrix, source, sink)

    print(f"Максимальний потік: {max_flow}")
    print(f"Матриця потоку: {flow_matrix}")
    for row in flow_matrix:
        print(row)
