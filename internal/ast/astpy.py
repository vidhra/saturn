import os
import ast
import networkx as nx
import matplotlib.pyplot as plt

def extract_functions_and_classes_from_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as source_file:
            source_code = source_file.read()
        tree = ast.parse(source_code, filename=file_path)
        names = []
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                names.append(f"Class: {node.name}")
                for body_item in node.body:
                    if isinstance(body_item, ast.FunctionDef):
                        names.append(f"{node.name}.{body_item.name}")
            elif isinstance(node, ast.FunctionDef):
                names.append(node.name)
        return names
    except Exception as e:
        print(f"Error parsing file {file_path}: {e}")
        return []

def build_graph(directory_path):
    G = nx.DiGraph()
    directory_path = os.path.normpath(directory_path)
    root_node = os.path.basename(directory_path)
    if not root_node:
        root_node = os.path.basename(os.path.abspath(directory_path))
    G.add_node(root_node, type='folder')
    print(f"Root node: {root_node}")

    for dirpath, dirnames, filenames in os.walk(directory_path):
        rel_dir = os.path.relpath(dirpath, directory_path)
        print(f"\nProcessing directory: {dirpath}")
        print(f"Relative directory: {rel_dir}")

        if rel_dir == '.':
            parent_node = root_node
            print(f"At root directory: {parent_node}")
        else:
            parent_node = os.path.basename(rel_dir)
            parent_path = os.path.dirname(rel_dir)
            if parent_path == '.':
                parent_parent_node = root_node
            else:
                parent_parent_node = os.path.basename(parent_path)
            if not parent_node or not parent_parent_node:
                continue
            G.add_node(parent_node, type='folder')
            G.add_edge(parent_parent_node, parent_node)
            print(f"Parent node: {parent_parent_node} -> {parent_node}")

        for dirname in dirnames:
            if not dirname:
                continue
            print(f"Found subdirectory: {dirname}")
            G.add_node(dirname, type='folder')
            G.add_edge(parent_node, dirname)

        for filename in filenames:
            if filename.endswith('.py'):
                if not filename:
                    continue
                print(f"Found Python file: {filename}")
                file_path = os.path.join(dirpath, filename)
                names = extract_functions_and_classes_from_file(file_path)
                if names:
                    file_node = filename
                    G.add_node(file_node, type='file')
                    G.add_edge(parent_node, file_node)
                    for name in names:
                        if not name:
                            continue
                        G.add_node(name, type='function_or_class')
                        G.add_edge(file_node, name)
                    print(f"Found in {filename}: {names}")
                else:
                    print(f"No functions or classes found in {filename}")
    return G

def visualize_graph(G):
    # Use spring layout for positioning nodes
    pos = nx.spring_layout(G, k=0.15, iterations=20)
    
    # Prepare node colors based on node types
    node_types = nx.get_node_attributes(G, 'type')
    color_map = []
    for node in G.nodes():
        node_type = node_types.get(node, 'unknown')
        if node_type == 'folder':
            color_map.append('#FFA500')  # Sunny Orange
        elif node_type == 'file':
            color_map.append('#FFA500')  # Sunny Orange
        elif node_type == 'function_or_class':
            color_map.append('#FFA500')  # Sunny Orange
        else:
            color_map.append('#FFA500')  # Sunny Orange
    
    # Set up plot with black background
    plt.figure(figsize=(15, 15), facecolor='black')
    ax = plt.gca()
    ax.set_facecolor('black')
    
    # Draw the graph
    nx.draw_networkx(
        G,
        pos,
        with_labels=False,
        node_color=color_map,
        edge_color='white',
        node_size=500,
        arrows=True,
        arrowstyle='-|>',
        arrowsize=10,
        width=1.0
    )
    
    # Draw labels separately to adjust font size and color
    labels = {node: node for node in G.nodes()}
    nx.draw_networkx_labels(G, pos, labels=labels, font_size=6, font_color='white')
    
    plt.title('Directory Structure and Functions', color='white')
    plt.axis('off')
    plt.show()

if __name__ == "__main__":
    # Replace with your directory path
    directory_path = 'C:/Users/AMD/vidhra/internal/ast/google-cloud-python/packages/google-cloud-run/google/cloud/run_v2/services/jobs'
    
    # Build the graph
    G = build_graph(directory_path)

    # After building the graph
    print("\nGraph construction complete.")
    print(f"Number of nodes: {G.number_of_nodes()}")
    print(f"Number of edges: {G.number_of_edges()}")

    # Visualize the graph
    visualize_graph(G)
