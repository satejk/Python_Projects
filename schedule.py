__author__ = 'satkha14'






class Queue:

    items = []

    def __int__(self):

        self.items = []



    def isEmpty(self):
        return (self.items == [])



    def enqueue(self,item):

        self.items.insert(0,item)


    def dequeue(self):
        return self.items.pop()

    def size(self):

        return len(self.items)


    def print_queue(self):

        print self.items

    def contents(self):

        for i in range(len(self.items)):
            print self.items[i],

        print





q = Queue()


print q.isEmpty()

q.enqueue(5)

q.print_queue()

q.enqueue(12)
q.enqueue(20)
q.enqueue(30)

q.print_queue()
q.contents()

task = q.dequeue()
print task
q.contents()

q.enqueue(5)

q.contents()






