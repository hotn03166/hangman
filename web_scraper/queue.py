import time
import random

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

def similate_line(till_show, max_time):
    pq = Queue()
    tix_sold = []

    for i in range(100):
        pq.enqueue('person' + str(i))

    t_end = time.time() + till_show
    now = time.time()

    while now < t_end and not pq.is_empty():
        now = time.time()
        r = random.randint(0, max_time)
        
        time.sleep(r)
        
        person = pq.dequeue()
        print(person)
        tix_sold.append(person)
        
    return tix_sold
    

q = Queue()
print(q.is_empty())


for i in range(5):
    q.enqueue(i)
print(q.size())


while q.size():
    print(q.dequeue())
print('\n' + str(q.size()))


# チケット行列
sold = similate_line(100, 1)
print(sold)
