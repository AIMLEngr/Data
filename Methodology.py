import matplotlib.pyplot as plt
import networkx as nx

# Create a directed graph
graph = nx.DiGraph()

# Define the nodes
nodes = [
    ('Requirement Analysis', '2'), ('Data Collection and Preprocessing', '3'),
    ('Model Architecture Design', '4'), ('Model Training and Optimization', '5'),
    ('Annotation and Labeling', '6'), ('Model Evaluation', '7'),
    ('Clinical Integration', '8'), ('Ethical Considerations', '9'),
    ('Deployment and Scalability', '')
]

# Add the nodes to the graph
graph.add_nodes_from(nodes)

# Define the edges
edges = [('Requirement Analysis', 'Data Collection and Preprocessing'),
         ('Data Collection and Preprocessing', 'Model Architecture Design'),
         ('Model Architecture Design', 'Model Training and Optimization'),
         ('Model Training and Optimization', 'Annotation and Labeling'),
         ('Annotation and Labeling', 'Model Evaluation'),
         ('Model Evaluation', 'Clinical Integration'),
         ('Clinical Integration', 'Ethical Considerations'),
         ('Ethical Considerations', 'Deployment and Scalability')]

# Add the edges to the graph
graph.add_edges_from(edges)

# Set the position of the nodes
pos = nx.spring_layout(graph)

# Draw the nodes and edges
nx.draw_networkx_nodes(graph, pos)
nx.draw_networkx_edges(graph, pos, arrowstyle='->')

# Add labels to the nodes
node_labels = {node[0]: node[0] for node in nodes}
nx.draw_networkx_labels(graph, pos, labels=node_labels)

# Remove axes
plt.axis('off')

# Save the figure as a JPEG image
plt.savefig('f:/proj/methodology.jpeg')

# Create a text file of the methodology
methodology_text = '''Modified Waterfall Methodology:

1. Requirement Analysis
2. Data Collection and Preprocessing
3. Model Architecture Design
4. Model Training and Optimization
5. Annotation and Labeling
6. Model Evaluation
7. Clinical Integration
8. Ethical Considerations
9. Deployment and Scalability'''

with open('f:/proj/methodology.txt', 'w') as file:
    file.write(methodology_text)