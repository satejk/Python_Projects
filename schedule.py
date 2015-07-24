__author__ = 'satej'

from math import *

import sys

class Queue:

    #items = []

    def __init__(self):

        self.items = []



    def isEmpty(self):
        return self.items == []



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
            for j in range(len(self.items[i])):

                print self.items[i][j],
            
            print
        print



class Task_info:
    # task_count = 0

    def __init__(self, name, compute, period):
        self.name = name
        self.compute = compute
        self.period = period
        #Task_info.task_count += 1

    def getTaskname(self):
        return self.name

    def getComputetime(self):
        return self.compute

    def getPeriod(self):
        return self.period

    def displayTaskinfo(self):
        print "Task name:", self.name
        print "Task compute time:", self.compute
        print "Task period:", self.period
        print

list1 = []

list2 = []

list3 = []


# list4 = []
# list5 = []

superlist = [list1 , list2 , list3]
print superlist

number_of_tasks = 3
print "Enter task set information for %d tasks:" % number_of_tasks
task_set_user = []
for i in range (number_of_tasks):

    #get input from user for task name , compute time and period
    task_name = raw_input("Enter the name of the %dth task" % (i+1))
    compute_time = int(raw_input("Enter the Compute time of the %dth task" % (i+1)))
    period_time = int(raw_input("Enter the Period  of the %dth task" % (i+1)))

    superlist[i].append(task_name)
    superlist[i].append(int(compute_time))
    superlist[i].append(int(period_time))

    
   
    # append the task to task_set_user
    task_t = Task_info(task_name,compute_time,period_time)

    task_set_user.append(task_t)



print "*****************************************"

print superlist

print "Task set user information"

task_set_user[0].displayTaskinfo()
task_set_user[1].displayTaskinfo()
task_set_user[2].displayTaskinfo()






'''
# task set 1
task_set_1 = []
#task_info(name, computime , period)
task1 = Task_info("A", 1, 8)
task_set_1.append(task1)
task2 = Task_info("B", 2, 5)
task_set_1.append(task2)
task3 = Task_info("C", 2, 10)
task_set_1.append(task3)

#task set 2
task_set_2 = []

task1 = Task_info("A", 5, 5)
task_set_2.append(task1)
task2 = Task_info("B", 1, 1)
task_set_2.append(task2)
task3 = Task_info("C", 2, 2)
task_set_2.append(task3)


#print task_set_1

print "Task set 1 information"

task_set_1[0].displayTaskinfo()
task_set_1[1].displayTaskinfo()
task_set_1[2].displayTaskinfo()

print "*****************************************"

print "Task set 2 information"

task_set_2[0].displayTaskinfo()
task_set_2[1].displayTaskinfo()
task_set_2[2].displayTaskinfo()

#setlist = [1,2,3]
'''

#function to calculate the nth root
def nroot(n, x):
    count = 0
    initx = 1;  #initial guess

    while count < 10:
        initx = float((1 / float(n)) * ((n - 1) * float(initx) + (x / float(pow(initx, (n - 1)))) ))

        count += 1

    return initx


def utilization(task_set):
    sum_task = 0
    lenght = len(task_set)

    for i in range(lenght):
        c = float(task_set[i].getComputetime())
        t = float(task_set[i].getPeriod())

        sum_task += (c / t)

    rhs = lenght * (nroot(lenght, 2) - 1)

    if (sum_task <= rhs):

        print "task set is schedulable"
        print "%f < %f " % (sum_task, rhs)
    else:
        print "task is not schedulable"
        print "%f > %f " % (sum_task, rhs)






def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def lcm(a, b):
    return a * b / gcd(a, b)


def LCM_list(list):

    list_lcm = []

    for i in range(len(list)):
        list_lcm.append(list[i].getPeriod())


    return reduce(lcm, list_lcm)




utilization(task_set_user)

print




#schedule for task_set_1

LCM_time =  LCM_list(task_set_user)

print LCM_time




print "..........super list keeda..............."
print superlist






def list_sort(superlist2):

    for i in range((len(superlist2) ) ):
        print superlist2[i]
        for j in  range((len(superlist2) )):

            if(superlist2[i][1] > superlist2[j][1]):
                print superlist2[i][1]
                print superlist2[j][1]
                temp_list = []
                temp_list = superlist2[i]
                superlist2[i] = superlist2[j]
                superlist2[j] = temp_list




list_sort(superlist)

print "sorted list"
print superlist



print "...................scheduler............"




def wait_state():
    print "wait_state"

def ready_state():
    print "ready_state"

def running_state():
    print "running_state"




time = 0
while(time < LCM_time):


    wait_state()

    ready_state()

    running_state()

    time += 1



display = []


for x in range((number_of_tasks + 1)):
    display.append(["."] * LCM_time)


for i in range(LCM_time):
    display[3][i] = "%d" % ( i + 1 )

def print_display(display):
    task_bound = number_of_tasks + 1
    for i in range(task_bound):
        for j in range(LCM_time):

            if(i < (number_of_tasks) and j > 8):

                print " "+display[i][j],
            else:

                print display[i][j],


        print

    print


print_display(display)
