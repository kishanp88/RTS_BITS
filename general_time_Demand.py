# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import math
NumberOfTasks = int(input("Please enter total NUMBER of tasks: "))
task = [dict() for x in range(NumberOfTasks)]

busyInterval =[]
timeDemand =[]
worstCaseRT = []
finalworstCaseRT = []
for i in range (NumberOfTasks):
    
    period = float(input("Please enter PERIOD for task "+str(i+1)+": "))
    executionTime = float(input("Please enter EXECUTION TIME for task "+str(i+1)+": "))
    deadline = float(input("Please enter DEADLINE for task "+str(i+1)+": "))
    
    task[i] = ({'period':period,'executionTime':executionTime, 'deadline':deadline})
task = sorted(task, key = lambda i:i['deadline'])
print(task)
t = 0;
for i in range (NumberOfTasks):
    t= t + task[i]['executionTime']

i = 0;
while True:
    
    sum = 0;                   
    for k in range(NumberOfTasks):
        sum= sum +(math.ceil(t/task[k]['period'])*task[k]['executionTime'])
    t = sum
    busyInterval.append(t)
    if (i and (busyInterval[i] == busyInterval[i-1])):
        break
    i = i+1
finalBusyInterval =   busyInterval[i];  
print("BusyInterval: "+str(busyInterval[i]))

#######################################################################

noOfInstances = math.ceil(finalBusyInterval / task[NumberOfTasks-1]['period']);

instance = [dict() for x in range(noOfInstances)]
releaseTime = 0
for ri in range(noOfInstances):
    instance[ri]['releaseTime'] = releaseTime;
    releaseTime = releaseTime + task[NumberOfTasks-1]['period']

for k in range(noOfInstances):
    t = task[NumberOfTasks-1]['executionTime']
    #print('Initial Value of t: '+str(t))
    i = 0;
    worstCaseRT.clear();
    while True:
        sum = 0
   
        sumHp = 0
        for m in range(NumberOfTasks-1):
            sumHp = sumHp + (math.ceil((t+instance[k]['releaseTime'])/task[m]['period']))*task[m]['executionTime']
        #print('High Priority sum : '+str(sumHp))
        sum = sum + sumHp + (k+1)*task[NumberOfTasks-1]['executionTime']-instance[k]['releaseTime'];
        t = sum;
        worstCaseRT.append(t)
        if (i and (worstCaseRT[i] == worstCaseRT[i-1])):
            break
        i = i+1
    finalworstCaseRT.append(worstCaseRT[i]);

count = 0;        
for w in range(noOfInstances):
    if (finalworstCaseRT[w] > task[NumberOfTasks-1]['deadline']):
        print('task ' +str(NumberOfTasks)+' job '+str(w+1)+"is not schedulable")
    else:
        count = count + 1
        print('task ' +str(NumberOfTasks)+' job '+str(w+1)+"is schedulable")

if (count == noOfInstances):
    print('tasks are schedulable')
else:
    print('tasks are not schedulable')
        
