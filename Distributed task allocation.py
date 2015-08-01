__author__ = 'satej'
"""
 * This file is part of my Distributed Real Time Systems LAB.
 *
 *
 *
 * Copyright (C) 2015 satej v. khandeparkar <satejk5@gmail.com> , Halmstad University.
 *
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; version 2 of the License.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc.
 *
 * be warned, this file is to used for education purpose only
 */
"""



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

list4 = []


list5 = []

list6 = []

list7 = []

list8 = []



number_of_tasks = 8

superlist = [list1 , list2 , list3 , list4 , list5 , list6, list7, list8]
#superlist = [list1 , list2 , list3 ]
display = []



#print superlist
print "*****************************Distributed task allocation SIMULATION TOOL*********************************"
print
print
print "Task simulation  menu:"


print
task_set_user = []

while(1):
    select = int(raw_input("Enter 1 for Default test case and 2 for user input : "))
    if(select == 2):

        print "Enter task set information for %d tasks:" % number_of_tasks

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

        break

    elif(select == 1):
            # task set 1


        #task_info(name, computime , period)
        task1 = Task_info("A", 5, 10)
        task_set_user.append(task1)
        superlist[0].append("A")
        superlist[0].append(int(5))
        superlist[0].append(int(10))
        task2 = Task_info("B", 7, 21)
        task_set_user.append(task2)
        superlist[1].append("B")
        superlist[1].append(int(7))
        superlist[1].append(int(21))

        task3 = Task_info("C", 3, 22)
        task_set_user.append(task3)
        superlist[2].append("C")
        superlist[2].append(int(3))
        superlist[2].append(int(22))

        task4 = Task_info("D", 1, 24)
        task_set_user.append(task4)
        superlist[3].append("D")
        superlist[3].append(int(1))
        superlist[3].append(int(24))
        task5 = Task_info("E", 10, 30)
        task_set_user.append(task5)
        superlist[4].append("E")
        superlist[4].append(int(10))
        superlist[4].append(int(30))

        task6 = Task_info("F", 16, 40)
        task_set_user.append(task6)
        superlist[5].append("F")
        superlist[5].append(int(16))
        superlist[5].append(int(40))

        task7 = Task_info("G", 1, 50)
        task_set_user.append(task7)
        superlist[6].append("G")
        superlist[6].append(int(1))
        superlist[6].append(int(50))
        task8 = Task_info("H", 3, 55)
        task_set_user.append(task8)
        superlist[7].append("H")
        superlist[7].append(int(3))
        superlist[7].append(int(55))

        break

    else:
        print "Please enter valid input 1 or 2"


print
print

print "***********************************************"

#print superlist

print
print "Task set user information"



print superlist

for i in range(number_of_tasks):
    task_set_user[i].displayTaskinfo()


print "************************************************"

#print 0%10






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
        list_lcm.append(list[i][2])


    return reduce(lcm, list_lcm)








#schedule for task_set_1






#print "..........super list keeda..............."
#print superlist






def list_sort(superlist2):
    #print superlist
    for i in range((len(superlist2) ) ):
        #print superlist2[i]
        for j in  range((len(superlist2) )):
            #sort in ascending order
            if(superlist2[i][1] < superlist2[j][1]):
                #print superlist2[i][1]
                #print superlist2[j][1]
                temp_list = []
                temp_list = superlist2[i]
                superlist2[i] = superlist2[j]
                superlist2[j] = temp_list



def list_sort_mod(superlist2):
    #print superlist
    for i in range((len(superlist2) ) ):
        #print superlist2[i]
        for j in  range((len(superlist2) )):
            #sort in ascending order
            if(superlist2[i][1] < superlist2[j][1] or len(superlist2[j]) == 0 or len(superlist2[i]) == 0):
                #print superlist2[i][1]
                #print superlist2[j][1]

                temp_list = superlist2[i]
                superlist2[i] = superlist2[j]
                superlist2[j] = temp_list


list_sort(superlist)

#print "sorted list"
#print superlist





def display_init(task_set):
    LCM_time = LCM_list(task_set)
    global display
    display = []
    number_of_tasks = len(task_set)
    task_bound = number_of_tasks + 1
    for x in range(task_bound):
        display.append(["."] * LCM_time)

    for i in range(task_bound):
        for j in range(LCM_time):

            if((j % task_set[0][2]) == 0):

                display[i][(j-1)] = "|"

            else:
                display[i][j] = "."

    for i in range(LCM_time):
        display[number_of_tasks][i] = "%d" % ( i + 1 )


    print "Intializaing display...."
#---------display init function-------------


def print_display(display , task_set):
    LCM_time = LCM_list(task_set)
    number_of_tasks = len(task_set)
    task_bound = number_of_tasks + 1
    for i in range(task_bound):
        for j in range(LCM_time):

            if(i < (number_of_tasks) and j > 8 and j <= 99):

                print " "+display[i][j],

            elif(i < (number_of_tasks) and j > 99):
                print "  " + display[i][j],
            else:

                print display[i][j],


        print

    print
print

#LCM_time =  LCM_list(task_set_user)


#print "LCM time :" + str(LCM_time)

utilization(task_set_user)


#distributed task allocation algorithm

#(nroot(lenght, 2) - 1)

def task_distribution(procs , superlist):

    megalist = [[] for x in range(procs)]

    print megalist

    Ui = 0

    for i in range(len(superlist)):

        Ui = (float(superlist[i][1])/superlist[i][2])
        #print str(Ui) + superlist[i][0]
        for j in range(procs):
            #print j
            if( (nroot((j+2),2) - 1 )< Ui <=  (nroot((j+1),2) - 1 )) :

                megalist[j].append(superlist[i])

            elif(j == (procs - 1)):
                    if( 0   < Ui <=  (nroot((j+1),2) - 1 )):


                        megalist[j].append(superlist[i])

            else:
                #print j
                #print "Task not allocated" + str(superlist[i])
                pass

    for i in range(procs):

        print megalist[i]

    return megalist



def list_util(list):

    sum_util = 0
    u = 0
    for i in range(len(list)):
        #print list[i]
        #if(len(list[i]) != 0):
        u = float((float(list[i][1])/float(list[i][2])))
        sum_util += u

    #print sum_util

    return sum_util


#--------------------------------------

def util_sort(superlist):

    for i in range(len(superlist)):

        ui = list_util(superlist[i])

        for j in range(len(superlist)):

            uj = list_util(superlist[j])

            if((ui < uj )):  #or (len(superlist[i]) == 0) or (len(superlist[j]) == 0)) :

                temp_list = superlist[i]
                superlist[i] = superlist[j]
                superlist[j] = temp_list


    return superlist


def distributed_task_alloc(procs , superlist):

    megalist = [[] for x in range(procs)]
    sorted_megalist = [[] for x in range(procs)]

    print megalist

    list_sort(superlist)


    for i in range(len(superlist)):

        megalist = util_sort(megalist)
        #print megalist

        if(list_util(megalist[0]) < 0.7):
            megalist[0].append(superlist[i])

        else:
            print "Task not allocated " + str(superlist[i])





    for i in range(procs):
        print

        print megalist[i]
        print list_util(megalist[i])
        print
    return megalist



print


print "...................RATE MONOTONIC scheduler Graph ........................"



#task_timers.append( 0 for x in range(number_of_tasks))



def wait_state(time, task_display_time,wait_queue,ready_queue , task_timers):
    wq_range= len(wait_queue)
    #print "wait state"
    #global time
    #global task_display_time
    #global wait_queue
    #global  ready_queue
    if (len(wait_queue) != 0 ):
        list_sort(wait_queue)
        # check for time % period = 0
        task = 0
        while task < (wq_range):
            #task +=1
            if(len(wait_queue) != 0):
                #print "task"
                #print task
                if (( time %wait_queue[task][2])== 0):
                    #print (time % wait_queue[task][2])
                    #engueue
                    ready_queue.append(wait_queue[task])
                    task_display_time = 0 #reset at entry of higher priority task
                    #print ready_queue
                    #dequeue
                    wait_queue.pop(task)
                    #print wait_queue

                    wq_range  =    len(wait_queue)
                    task = 0

                else:
                    task +=1

            else:
                break

    else:
        pass

    #print "wait_queue"
    #print wait_queue
    #print "ready_queue"
    #print ready_queue

def ready_state(ready_queue):
    #print "ready_state"
    # sort the ready queue
    #global ready_queue
    list_sort(ready_queue)



def running_state(time,task_display_time,wait_queue, ready_queue,task_timers,superlist):
    #print "running_state"
    #global task_display_time
    #global wait_queue
    #global ready_queue
    #get the running task from ready queue
    number_of_tasks = len(superlist)
    if(len(ready_queue) != 0):

        running_task = ready_queue[0]

        display[superlist.index(running_task)][time] = running_task[0]


        #task_display_time += 1
        for i in range(number_of_tasks):


            if(running_task == superlist[i]):
                task_timers[i] +=1

                if (task_timers[i] == running_task[1]):
                    #engueue in wait_queue
                    wait_queue.append(running_task)
                    #dequeue from ready_queue

                    ready_queue.pop(0)

                    task_timers[i] = 0
                    #task_display_time = 0
                else:
                    pass
            else:
                pass



#display_init()

def simulator(superlist):
    #print superlist

    LCM_time = LCM_list(superlist)
    wait_queue = []

    ready_queue = []


    #wait_temp = []


    #append all the tasks to wait_queue

    for tasks in superlist:
        wait_queue.append(tasks)

    #print "wait_queue"
    #print wait_queue

    time = 0 # simulation time

    task_display_time = 0

    task_timers = [0,0,0,0,0,0,0,0]

    while(time < LCM_time):


        #print time

        wait_state(time, task_display_time,wait_queue,ready_queue,task_timers)

        ready_state(ready_queue)

        running_state(time ,task_display_time,wait_queue, ready_queue,task_timers,superlist)

        time += 1


#call wrapper functions
def Distributed_task_allocation(proc, list):

    megalist = task_distribution(proc,list)

    for i in range(len(megalist)):
       print "PROCESSOR" + " " + str(i + 1)
       print
       print megalist[i]
       if((len(megalist[i]) > 0) and (LCM_list(megalist[i]) < 1000) ):


            display_init(megalist[i])

            simulator(megalist[i])
            print_display(display,megalist[i])

       else:
           print "list is either empty or LCM is > 1000"


    print
    print
    print "********************* Distributed task allocation *****************************************"


    megalist2 = distributed_task_alloc(proc,list)

    for i in range(len(megalist2)):
       print "PROCESSOR" + " " + str(i + 1)
       print
       print megalist2[i]
       if((len(megalist2[i]) > 0) and (LCM_list(megalist2[i]) < 1000) ):


            display_init(megalist2[i])

            simulator(megalist2[i])
            print_display(display,megalist2[i])

       else:
           print "list is either empty or LCM is > 1000"



Distributed_task_allocation(8,superlist)