import math
NumberOfTasks = int(input("Please enter total NUMBER of tasks: "))
task = [dict() for x in range(NumberOfTasks)]

busyInterval =[]
timeDemand =[]
worstCaseRT = []
finalworstCaseRT = []
ListExecutionTime = []
finalBusyInterval =[]
noOfInstances = []
instance = []

for i in range (NumberOfTasks):
    
    period = float(input("Please enter PERIOD for task "+str(i+1)+": "))
    executionTime = float(input("Please enter EXECUTION TIME for task "+str(i+1)+": "))
    deadline = float(input("Please enter DEADLINE for task "+str(i+1)+": "))
    
    task[i] = ({'period':period,'executionTime':executionTime, 'deadline':deadline})
task = sorted(task, key = lambda i:i['deadline'])
print(task)

utilizationratio = 0
for a in range (NumberOfTasks):
    utilizationratio = utilizationratio + task[a]['executionTime']/task[a]['period']
print("Utilization ratio:",utilizationratio)

if(utilizationratio>1):
    print('tasks are not schedulable')
else:
    t = 0;
    for i in range (NumberOfTasks):
        t= t + task[i]['executionTime']
        ListExecutionTime.append(t)
    print("List Execution Time",ListExecutionTime)

    totalInstances = 0;
    for h in range(NumberOfTasks):
        i = 0;
        t = ListExecutionTime[h]
        busyInterval.clear()
        while True:
            
            sum = 0;                   
            for k in range(h+1):
                sum= sum +(math.ceil(t/task[k]['period'])*task[k]['executionTime'])
            t = sum
            busyInterval.append(t)
            if (i and (busyInterval[i] == busyInterval[i-1])):
                break
            i = i+1
        finalBusyInterval.append(busyInterval[i])
        noOfInstances.append(math.ceil(finalBusyInterval[h] / task[h]['period']));
        totalInstances = totalInstances + noOfInstances[h]
    print("final BusyInterval: ",finalBusyInterval)


#######################################################################


    #noOfInstances = math.ceil(finalBusyInterval / task[NumberOfTasks-1]['period']);
    count = 0; 
    for p in range(NumberOfTasks):
        #instance = [dict() for x in range(noOfInstances[p])]
        instance.clear();
        finalworstCaseRT.clear();
        releaseTime = 0
        for ri in range(noOfInstances[p]):
            instance.append(releaseTime);
            releaseTime = releaseTime + task[p]['period']
        
        for k in range(noOfInstances[p]):
            t = task[p]['executionTime']
            #print('Initial Value of t: '+str(t))
            i = 0;
            worstCaseRT.clear();
            while True:
                sum = 0
           
                sumHp = 0
                for m in range(p):
                    sumHp = sumHp + (math.ceil((t+instance[k])/task[m]['period']))*task[m]['executionTime']
                #print('High Priority sum : '+str(sumHp))
                sum = sum + sumHp + (k+1)*task[p]['executionTime']-instance[k];
                t = sum;
                worstCaseRT.append(t)
                if (i and (worstCaseRT[i] == worstCaseRT[i-1])):
                    break
                i = i+1
            finalworstCaseRT.append(worstCaseRT[i]);
    
               
        for w in range(noOfInstances[p]):
            if (finalworstCaseRT[w] > task[p]['deadline']):
                print('task ' +str(p+1)+' job '+str(w+1)+" is not schedulable")
            else:
                count = count + 1
                print('task ' +str(p+1)+' job '+str(w+1)+" is schedulable")
        
    if (count == totalInstances):
        print('tasks are schedulable')
    else:
        print('tasks are not schedulable')
    
