import threading, time, random, queue
n = 3
job_list = map(lambda x: (random.randrange(8)), range(8))
job_queue = queue.Queue()
threads_queue = queue.Queue(3)

for i in job_list:
    job_queue.put(i)

for i in list(job_queue.queue):
    print(i, end=" ")

print('\n')


def threadSleep():
    sleepTime = job_queue.get()
    print("I'm Thread-{}. I'm sleeping for {} seconds".format(threading.current_thread().getName(), sleepTime ))
    # print(threading.current_thread().getName() + 'on sleep ON')
    time.sleep(sleepTime)
    # print(threading.current_thread().getName() + 'sleep OFF')
    threads_queue.put(threading.Thread(name=threading.current_thread().getName(), target=threadSleep))


for x in range(1, n+1):
    t = threading.Thread(name=str(x), target=threadSleep)
    threads_queue.put(t)

begin =  time.time()
while not job_queue.empty():
    th = threads_queue.get()
    th.start()

th.join()
end = time.time()
print("Total time : {}".format(end-begin))