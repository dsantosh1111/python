from collections import deque

# queue is a data structure, which performs first in firstout
queue = deque(["karthik", "mourya", "santosh"])
print(queue)

# adding few elemnts to queue

queue.append("dharma")

print(queue)

queue.append("vinay")

print(queue)

# removing an elemnt form queue

queue.popleft()

print(queue)

queue.popleft()

print(queue)