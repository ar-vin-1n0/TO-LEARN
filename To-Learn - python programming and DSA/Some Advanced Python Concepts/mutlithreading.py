#what is a process

#process is an independent running program
#eg chrome,pycharm,instagram etc ---- each are separate processes

#Each process has:
#its own memory
#own variables
#own resources
#own execution environment


#Chrome Process
    #memory
    #threads

#VS Code Process
   #memory
   #threads

#features of a process
#
#isolated memory  --	safer
#independent	-- separate programs
#heavier	--  more resources
#true parallelism


#What Is a Thread?

#Thread is a smaller execution unit inside process

#A process can contain multiple threads

#eg
#Chrome browser process may have

#UI thread
#rendering thread
#network thread
#JavaScript thread

#all inside SAME process

#One Process
# ├── Thread 1
# ├── Thread 2
# └── Thread 3
#Shared Memory

#| Feature        | Process |   Thread |

#| memory        | separate  |  shared          |
#| speed         | slower    |  faster          |
#| communication | expensive |  easier          |
#| isolation     | strong    |  weak            |
#| crash impact  | isolated  |  affects process |

#why threads ----> Threads allow program to do multiple tasks seemingly simultaneously

#Music player:

#one thread plays audio
#another updates UI
#another handles clicks

#without freezing

#threading module in python

from threading import Thread
import time

def task():

    for i in range(5):

        print("Task running")

        time.sleep(1)

#creating a thread

t = Thread(target=task)

#t.start() #----> creates separate thread execution.

#Main Thread
#      +
#Worker Thread



#MULTI THREADING

def task_b(name):

    for i in range(5):

        print(name)

        time.sleep(1)


t1 =Thread(
    target=task_b,
    args=("Thread 1",)
)

t2 =Thread(
    target=task_b,
    args=("Thread 2",)           #args=("Thread 1",) --> Tuple with arguments passed to function.
)


t1.start()
t2.start()

#Threads execute concurrently OS rapidly switches between them
#Thread scheduling depends on operating system CPU timing execution speed So output order NOT guaranteed


#join()

t1.join()
t2.join()

print("Done")

#main thread wait for worker threads to finish "Done" prints atlast

#Thread means execution path inside a program When Python program runs,instructions execute line-by-line that execution flow is called thread
#When Python program starts,Python automatically creates one default thread called main thread
#This is the ORIGINAL thread running your program.

#Program Starts
#      ↓
#Main Thread Created
#      ↓
#Code Executes

#t1 and t2 are the worker thread

def task_c():

    print("Working")

t1 = Thread(target=task_c)

t1.start()

print("Main thread running")

#Main Thread
#    ├── Worker Thread t1
#both run concurrently

#with out join()

def work():

    time.sleep(3)

    print("Worker finished")

t1 = Thread(target=work)

t1.start()

print("Done")

#Done
#Worker finished

#Main thread DOES NOT wait.It continues immediately.

#without join()

#Main thread:
#start t1
#↓
#immediately continue
#↓
#print("Done")

#t1.join()means “main thread waits until t1 finishes”


#with join()
#Main Thread:
#start t1
#↓
#WAIT
#↓
#worker finishes
#↓
#continue
#↓
#Done

#Any thread can wait for another thread.Not just main thread.



#Shared Memory

#Threads share variables.

counter = 0

#all thread can access counter

#Shared Memory
#     │
# ┌───┴───┐
# │       │
# T1      T2

def work():

    global counter

    counter += 1

#Both threads modify SAME counter


#import threading

shared = []

def task_d():

    shared.append("hello")

t1 = Thread(target=task_d)
t2 = Thread(target=task_d)

t1.start()
t2.start()

t1.join()
t2.join()

print(shared)

#All threads can:
#read
#modify
#append
#same list.


#Why Shared Memory Dangerous?
# Because multiple threads may modify same data simultaneously This causes race conditions



#Race Conditions

#What is Race Condition?

#Race condition happens when:multiple threads modify shared data unsafely
#leading to:
#corrupted data
#unpredictable behavior

#take counter
#1. read counter
#2. add 1
#3. write result back

#Thread 1 Reads
#counter = 0
#Before Writing Back

#Thread 2 ALSO reads:
#counter = 0
#Then Both Write

#Both may write:1
#instead of: 2
#Update lost.

#This is race condition

#eg
counterA = 0

def increment():

    global counterA

    for i in range(100000):

        counterA += 1

t1 = Thread(target=increment)
t2 = Thread(target=increment)

t1.start()
t2.start()

t1.join()
t2.join()

print(counter)

#expected 200000
#output different in every run

#Threads overwrite each other’s updates


#Thread1 reads counter = 5
#Thread2 reads counter = 5

#Thread1 writes 6
#Thread2 writes 6

#Expected 7
#Actual 6



#Critical Section

#Critical section = code accessing shared resources

#Example:
#counter += 1
#because multiple threads touching same data.

#Critical Sections Must Be Protected Otherwise race conditions happen

#When thread enters:

#with lock:

#it says:"Nobody else can enter this section until I'm done."
# other threads WAIT.
#This protected section is called:Critical Section


#LOCKS

#Locks solve race conditions

import threading

counter = 0

lock = threading.Lock()

def increment():

    global counter

    for i in range(100000):

        with lock:

            counter += 1


#Lock ensures only ONE thread enters critical section at a time

#Thread1 enters lock
#↓
#Thread2 waits
#↓
#Thread1 exits
#↓
#Thread2 enters

#internally python

#lock.acquire()

#try:
#    counter += 1

#finally:
#    lock.release()

#Without locks shared data becomes corrupted



# Deadlocks

#Deadlock = threads waiting forever Program freezes


#Thread1 holds LockA
#Thread1 waiting for LockB

#Thread2 holds LockB
#Thread2 waiting for LockA

#Thread1 ← waiting
#Thread2 ← waiting
#No progress possible

#Why Deadlocks Dangerous?
#Application may:
#freeze
#stop responding
#require restart
#VERY serious backend issue.



#Thread Communication

#Threads communicate easily because shared memory
#All threads can modify same list
shared = []

def task(n):

    shared.append(n)

threads = []

for i in range(5):

    t = threading.Thread(
        target=task,
        args=(i,)
    )

    threads.append(t)

    t.start()

for t in threads:
    t.join()

print(shared)



# Threading Good for I/O Tasks

#I/O operations are usually SLOW compared to CPU speed
#CPU can do billions of operations per second BUT internet request may take 2 seconds

#threading help cpu to work concurrently when waiting for a request

def download(name):

    print(f"{name} started")

    time.sleep(3)

    print(f"{name} completed")

tA = threading.Thread(
    target=download,
    args=("File1",)
)

tB = threading.Thread(
    target=download,
    args=("File2",)
)

#Main Process
# ├── Thread 1 → File1
# └── Thread 2 → File2

tA.start()
tB.start()

 #Thread 1 starts: File1 started
 #Thread 1 reaches: time.sleep(3) Now thread waits
 #While Thread 1 waits: CPU becomes available
 #OS scheduler runs Thread 2. File2 started
 #Thread 2 also waits
 #Result Both waiting simultaneously

#File1 waits 3 sec
#↓
#File2 waits 3 sec

#Total: 6 seconds

#Both overlap:

#Thread1 waiting + Thread2 waiting

# Total: 3 seconds



#Python GIL - Global Interpreter Lock

#In CPython: only ONE thread executes Python bytecode at a time

#Even with: 10 threads
#Python interpreter allows: only one active Python executor at exact instant.

#Python memory management is complex.
#GIL simplifies:
#garbage collection
#reference counting
#interpreter safety
#Makes Python easier and safer internally.

#Threads are BAD for: CPU-heavy parallel computation

#Task Type	Threads Helpful?
#I/O-bound	YES
#CPU-bound	NO (mostly)

#when thread performs i/o python gil releases
#While one thread waits: another thread can execute
#This is WHY threading excellent for I/O tasks.

#Task Type	Best Tool
#I/O-bound	threading
#CPU-bound	multiprocessing


#multi processing

#Why Multiprocessing Solves GIL
#Processes have:
#separate Python interpreters
#Each process has OWN GIL

#Process 1 → GIL 1
#Process 2 → GIL 2
#Now multiple CPU cores truly work simultaneously
#actual parallel execution occurs


#Thread Pools

#Managing threads manually becomes difficult.
#Suppose:
#1000 downloads
#Creating 1000 threads manually BAD idea.

#Problems with Too Many Threads
#memory waste
#context switching overhead
#slower performance
#system instability

#ThreadPoolExecutor

#Instead of creating infinite threads reuse limited worker threads

#eg
from concurrent.futures import ThreadPoolExecutor

def task(x):

    time.sleep(2)

    return x * 2

with ThreadPoolExecutor(
    max_workers=3
) as executor:

    results = executor.map(
        task,
        [1,2,3,4,5]
    )

    print(list(results))

#Pool Creates 3 reusable worker threads

#Worker1 → task1
#Worker2 → task2
#Worker3 → task3

#When worker finishes: takes next task

#Context Switching

#OS rapidly switches between threads.

#This called:context switching

#OS saves:
#registers
#execution position
#stack state
#for paused thread.
#Then resumes another thread.

#T1 running
#↓
#pause/save state
#↓
#T2 running
#↓
#pause/save state
#↓
#T1 resumes


#Real Backend Example — Full Visualization

#Suppose web server receives:100 requests

#Each request does:

#database query
#API call
#file access

#Most time spent:waiting

#Without Threads
#Request1 waits
#↓
#Request2 waits
#↓
#Request3 waits

#With Threads
#all requests overlap waiting
#Much faster server responsiveness

#Threading Purpose
#efficiently use waiting time

#GIL Meaning
#only one thread executes Python bytecode at instant

#Threads Excellent For
#I/O-bound waiting tasks

#Threads BAD For
#heavy CPU computation

#Thread Pool
#reuse worker threads efficiently