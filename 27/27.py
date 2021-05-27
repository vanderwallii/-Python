from heapq import *

class signals:

    def __init__(self, object):

        self.object = object

    def __lt__(self, a):

        return self.object.__gt__(a.object)

    def __repr__(self):

        return self.__str__()
        
    def __str__(self):
        
        return str(self.object)

heap = []
heapify(heap)
min_signals = 5
num_of_signals = input("Введите количество сигналов -  ")
num = map(int, input("Введите несколько чисел -  ").split(" "))


for val in num:

    val = signals(val)
    
    if len(heap) >= min_signals and val > max(heap):

        heappushpop(heap, val)

    elif len(heap) < min_signals:

        heappush(heap, val)
        
    print(' '.join(map(str, sorted(heap))))