import heapq

class Router:
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.graph = {i: {} for i in range(num_nodes)}  # adjacency list

    def set_edge(self, src, dest, cost):
        # Add link in both directions
        self.graph[src][dest] = cost
        self.graph[dest][src] = cost

    def dijkstra(self, start):
        distances = [float('inf')] * self.num_nodes
        distances[start] = 0
        pq = [(0, start)]  # priority queue (min-heap)

        while pq:
            current_dist, current_node = heapq.heappop(pq)

            for neighbor, weight in self.graph[current_node].items():
                distance = current_dist + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))

        return distances

    def print_routing_table(self):
        print("\nLink State Routing Tables (using Dijkstra’s Algorithm):")
        for i in range(self.num_nodes):
            distances = self.dijkstra(i)
            print(f"\nRouter {i + 1}:")
            for j, d in enumerate(distances):
                if d == float('inf'):
                    print(f"  To Router {j + 1}: No path")
                else:
                    print(f"  To Router {j + 1}: Cost = {d}")

def get_user_input():
    num_nodes = int(input("Enter the number of routers: "))
    router = Router(num_nodes)

    print("\nEnter the cost of the links (enter -1 if no direct link exists):")
    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            cost = int(input(f"Cost between Router {i + 1} and Router {j + 1}: "))
            if cost != -1:
                router.set_edge(i, j, cost)
    return router

if __name__ == "__main__":
    router = get_user_input()
    print("\nCalculating shortest paths using Link State Routing...")
    router.print_routing_table()
