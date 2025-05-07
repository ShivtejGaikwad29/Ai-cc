# job scheduling by priority queue

processes = [
    ('P1',0,2),
    ('P2',1,3),
    ('P3',1,5),
    ('P4',2,6),
    ('P5',2,4)
]

def jobscheduling(joblist):
    jobs = sorted(joblist,key=lambda x:x[1])
    n = len(jobs)
    time = 0
    current_queue = []
    order = []

    def add_to_current_queue():
        for job in jobs:
            if(job[1]==time):
                current_queue.append(job)
    
    def choose_job():
        choice = None
        for job in current_queue:
            if(choice == None or job[2] > choice[2]):
                choice = job
        if(choice) : current_queue.remove(choice)
        return choice
    
    while(len(order) < n):
        add_to_current_queue()
        cur = choose_job()
        if(cur) : order.append(cur[0])
        time = time+1
    return order

print(jobscheduling(processes))



