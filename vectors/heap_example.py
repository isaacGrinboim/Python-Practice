import heapq

# Define a class for the node
class Node:
    def __init__(self, name, age, hobby, phone):
        self.name = name
        self.age = age
        self.hobby = hobby
        self.phone = phone

# Create a list of nodes
nodes = [
    Node("Alice", 25, "Reading", 1234567890),
    Node("Bob", 30, "Gaming", 9876543210),
    Node("Charlie", 22, "Painting", 5551234567),
    Node("David", 28, "Cooking", 1112223333),
    Node("Eve", 24, "Swimming", 4445556666)
]

# Use a lambda function as the sorting key for age
heap = []
for node in nodes:
    heapq.heappush(heap, (node.age, node))

print( [ node[0] for node in heap])

index_to_remove = None
for i, (age, node) in enumerate(heap):
    if age == 30:
        index_to_remove = i
        break
if index_to_remove is not None:
    # Swap the element to be removed with the last element
    heap[index_to_remove], heap[-1] = heap[-1], heap[index_to_remove]
    
    # Pop the last element (the one to be removed)
    _, removed_node = heap.pop()

    # Restore the heap property
    heapq._siftup(heap, index_to_remove) 

print( [ node[0] for node in heap])


# # Pop nodes from the heap and verify the prioritization by age
# prev_age = float('-inf')
# while heap:
#     age, node = heapq.heappop(heap)
#     if age < prev_age:
#         print("Heap is not prioritized by age.")
#         break
#     prev_age = age
#     print(f"Name: {node.name}, Age: {node.age}, Hobby: {node.hobby}, Phone: {node.phone}")
# else:
#     print("Heap is correctly prioritized by age.")
