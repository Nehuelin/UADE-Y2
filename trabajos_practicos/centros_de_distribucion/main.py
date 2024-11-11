import heapq
import sys
from collections import defaultdict, namedtuple

# File paths
RUTAS_FILE = "rutas.txt"
CLIENTES_Y_CENTROS_FILE = "clientesYCentros.txt"

# Structures for data
Edge = namedtuple("Edge", ["origin", "destination", "cost"])
Factory = namedtuple("Factory", ["id", "delivery_cost", "fixed_cost"])
Client = namedtuple("Client", ["id", "production_volume"])

def parse_rutas(file_path):
    """Parse the rutas.txt file to extract graph edges."""
    edges = []
    with open(file_path, "r") as file:
        lines = file.readlines()
        total_connections = int(lines[0].strip(","))
        for line in lines[1:]:
            origin, destination, cost = map(int, line.strip().split())
            edges.append(Edge(origin, destination, cost))
    return edges

def parse_clientes_y_centros(file_path):
    """Parse clientesYCentros.txt to extract factory and client data."""
    factories = []
    clients = []
    with open(file_path, "r") as file:
        lines = file.readlines()
        num_clients = int(lines[0].strip(","))
        num_factories = int(lines[1].strip(","))
        
        # Read factories
        for i in range(2, 2 + num_factories):
            factory_id, delivery_cost, fixed_cost = map(int, lines[i].strip().split())
            factories.append(Factory(factory_id, delivery_cost, fixed_cost))
        
        # Read clients
        for i in range(2 + num_factories, 2 + num_factories + num_clients):
            client_id, production_volume = map(int, lines[i].strip().split())
            clients.append(Client(client_id, production_volume))
    
    return factories, clients

def build_graph(edges):
    """Build an adjacency list representation of the graph."""
    graph = defaultdict(list)
    for edge in edges:
        graph[edge.origin].append((edge.destination, edge.cost))
        graph[edge.destination].append((edge.origin, edge.cost))  # Undirected graph
    return graph

def dijkstra(graph, start):
    """Compute the shortest path costs from start to all other nodes using Dijkstra's algorithm."""
    distances = {node: float("inf") for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

def calculate_cost(factories, clients, graph):
    """Calculate total costs for each factory location."""
    total_costs = []
    for factory in factories:
        distances = dijkstra(graph, factory.id)
        total_cost = factory.fixed_cost  # Start with annual fixed cost
        
        for client in clients:
            delivery_cost = factory.delivery_cost * client.production_volume
            transport_cost = distances.get(client.id, float("inf"))
            total_cost += delivery_cost + transport_cost
        
        total_costs.append((factory.id, total_cost))
    
    return total_costs

def find_optimal_factory_location():
    # Parse input files
    edges = parse_rutas(RUTAS_FILE)
    factories, clients = parse_clientes_y_centros(CLIENTES_Y_CENTROS_FILE)
    
    # Build the graph
    graph = build_graph(edges)
    
    # Calculate the total cost for each factory
    total_costs = calculate_cost(factories, clients, graph)
    
    # Find the factory with the minimal cost
    optimal_factory = min(total_costs, key=lambda x: x[1])
    return optimal_factory

if __name__ == "__main__":
    optimal_factory = find_optimal_factory_location()
    print(f"Optimal Factory Location: Factory {optimal_factory[0]} with total cost: {optimal_factory[1]}")
