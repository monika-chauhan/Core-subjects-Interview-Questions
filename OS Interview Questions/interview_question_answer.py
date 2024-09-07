Question1 : What is the main purpose of operating system. Discuss different types?
Answer : An operating system (OS) is system software that manages computer hardware, software resources, and provides common services for computer programs. So it manages the computer's memory, processes, devices, files, and security aspects of the system. It also allows us to communicate with the computer without knowing how to speak the computer's language. Without an operating system, a computer is not useful.
Types of Operating Systems
There are several types of Operating Systems which are mentioned below.

1.Batch Operating System
2.Multi-Programming System
3.Multi-Processing System
4.Multi-Tasking Operating System
5.Time-Sharing Operating System
6.Distributed Operating System
7.Network Operating System
8.Real-Time Operating System

1. Batch Operating System
Answer : This type of operating system does not interact with the computer directly. There is an operator which takes similar jobs having the same requirements and groups them into batches. It is the responsibility of the operator to sort jobs with similar needs. Batch Operating System is designed to manage and execute a large number of jobs efficiently by processing them in groups.

2. Multi-Programming Operating System
Answer : Multiprogramming Operating Systems can be simply illustrated as more than one program is present in the main memory and any one of them can be kept in execution. This is basically used for better utilization of resources.

3. Multi-Processing Operating System
Answer : Multi-Processing Operating System is a type of Operating System in which more than one CPU is used for the execution of resources. It betters the throughput of the System.

4. Multi-Tasking Operating System
Answer : Multitasking Operating System is simply a multiprogramming Operating System with having facility of a Round-Robin Scheduling Algorithm. It can run multiple programs simultaneously.
There are two types of Multi-Tasking Systems which are listed below.
1.Preemptive Multi-Tasking
2.Cooperative Multi-Tasking

5. Time-Sharing Operating Systems
Answer : Each task is given some time to execute so that all the tasks work smoothly. Each user gets the time of the CPU as they use a single system. These systems are also known as Multitasking Systems. The task can be from a single user or different users also. The time that each task gets to execute is called quantum. After this time interval is over OS switches over to the next task.

6. Distributed Operating System
Answer : These types of operating system is a recent advancement in the world of computer technology and are being widely accepted all over the world and, that too, at a great pace. Various autonomous interconnected computers communicate with each other using a shared communication network. Independent systems possess their own memory unit and CPU. These are referred to as loosely coupled systems or distributed systems .

7. Network Operating System
Answer : These systems run on a server and provide the capability to manage data, users, groups, security, applications, and other networking functions. These types of operating systems allow shared access to files, printers, security, applications, and other networking functions over a small private network. One more important aspect of Network Operating Systems is that all the users are well aware of the underlying configuration, of all other users within the network, their individual connections, etc. and that’s why these computers are popularly known as tightly coupled systems .

8. Real-Time Operating System
Answer : These types of OSs serve real-time systems. The time interval required to process and respond to inputs is very small. This time interval is called response time. Real-time systems are used when there are time requirements that are very strict like missile systems, air traffic control systems, robots, etc.

Question2 : What is a socket, kernel and monolithic kernel?
Answer : 
    Socket:
    A socket is defined as an endpoint for communication, A pair of processes communicating over a network employ a pair of sockets ,one for each process. A socket is identified by an IP address concatenated with a port number.
    The server waits for incoming client requests by listening to a specified port. Once a request is received, the server accepts a connection from the client socket to complete the connection.

    Kernel :
    Kernel is the central core component of an operating system that manages operations of computer and hardware. Kernel Establishes communication between user level application and hardware. Manages memory and CPU time. Decides state of incoming processes. Controls Disk, Memory, Task Management

    Monolithic Kernel (provides good performance but lots of lines of code):
    It is one of the types of kernel where all operating system services operate in kernel space. It has dependencies between system components. It has huge lines of code which is complex.
    Example : Unix, Linux, Open VMS, XTS-400 etc.


Question3 : Difference between process, program and thread? Discuss Types of process and thread?
Answer : 
Process:
Process is an instance of an executing program. For example, we write our computer programs in a text file and when we execute this program, it becomes a process which performs all the tasks mentioned in the program.

Program:
Program is a set of instructions to perform a certain task. Eg: chrome.exe, notepad.exe

Thread:
Answer : Thread is a path of execution within a process. A thread is also known as a lightweight process. The idea is to achieve parallelism by dividing a process into multiple threads. For example,Word processor uses multiple threads: one thread to format the text, another thread to process inputs.


Question4 : Define virtual memory , thrashing, threads.
Answer : 
Virtual Memory:
A computer can address more memory than the amount physically installed on the system. This extra memory is actually called virtual memory and it is a section of a hard disk that's set up to emulate the computer's RAM.
The main visible advantage of this scheme is that programs can be larger than physical memory. Virtual memory serves two purposes. First, it allows us to extend the use of physical memory by using a disk. Second, it allows us to have memory protection, because each virtual address is translated to a physical address.

Thrashing:
Thrashing is a condition or a situation when the system is spending a major portion of its time in servicing the page faults, but the actual processing done is very negligible. High degree of multiprogramming(if number of processes keeps on increasing in the memory), lack of frames (if a process is allocated too few frames, then there will be too many and too frequent page faults) causes Thrashing.

Threads:
A thread is a single sequential flow of execution of tasks of a process so it is also known as thread of execution or thread of control.

Question5 : What is RAID ? Different Types.
Answer : RAID, or “Redundant Arrays of Independent Disks” is a technique which makes use of a combination of multiple disks instead of using a single disk for increased performance, data redundancy or both.Data redundancy, although taking up extra space, adds to disk reliability. This means, in case of disk failure, if the same data is also backed up onto another disk, we can retrieve the data and go on with the operation.

Question6 : What is deadlock ? Different condition to achieve a dedalock.
Answer : A Deadlock is a situation where each of the computer processes waits for a resource which is being assigned to some other process. In this situation, none of the processes gets executed since the resource it needs is held by some other process which is also waiting for some other resource to be released.

    How deadlock is achieved: Deadlock happens when Mutual exclusion, hold and wait, No preemption and circular wait occurs simultaneously.
    Necessary Conditions for deadlock:
    Mutual Exclusion
    Hold and Wait
    No preemption
    Circular Wait

Question7 : What s fragmentation ? types of fragmentation.
Answer : Fragmentation:
    An unwanted problem in the operating system in which the processes are loaded and unloaded from memory, and free memory space is fragmented. Processes can't be assigned to memory blocks due to their small size, and the memory blocks stay unused. It is also necessary to understand that as programs are loaded and deleted from memory, they generate free space or a hole in the memory. These small blocks cannot be allotted to new arriving processes, resulting in inefficient memory use.
    The conditions of fragmentation depend on the memory allocation system. As the process is loaded and unloaded from memory, these areas are fragmented into small pieces of memory that cannot be allocated to incoming processes. It is called fragmentation.

    Types of fragmentation:
    1. Internal
    2. External

Question8 : What is spooling?
Answer : SPOOL is an acronym for simultaneous peripheral operations online. Spooling is a process in which data is temporarily held to be used and executed by a device, program, or system.
        In spooling, there is no interaction between the I/O devices and the CPU. That means there is no need for the CPU to wait for the I/O operations to take place. Such operations take a long time to finish executing, so the CPU will not wait for them to finish.
        The biggest example of Spooling is printing. The documents which are to be printed are stored in the SPOOL and then added to the queue for printing. During this time, many processes can perform their operations and use the CPU without waiting while the printer executes the printing process on the documents one-by-one.

Question9 : What is Semaphore and mutex(Difference might be asked)? define Binary Semaphore.

Question10 : Belady's Anomaly?
Answer : Bélády’s anomaly is the name given to the phenomenon where increasing the number of page frames results in an increase in the number of page faults for a given memory access pattern.
        Solution to fix Belady’s Anomaly:
        Implementing alternative page replacement algo helps eliminate Belady’s Anomaly.. Use of stack based algorithms, such as Optimal Page Replacement Algorithm and Least Recently Used (LRU) algorithm, can eliminate the issue of increased page faults as these algorithms assign priority to pages

Question11 : Starving and Aging in OS?
Answer : Starving/Starvation(also called Lived lock): Starvation is the problem that occurs when low priority processes get jammed for an unspecified time as the high priority processes keep executing. So starvation happens if a method is indefinitely delayed.
        Solution to Starvation : Ageing is a technique of gradually increasing the priority of processes that wait in the system for a long time.


Question12 : Why does thrashing occur?
Answer : High degree of multiprogramming(if number of processes keeps on increasing in the memory) , lack of frames(if a process is allocated too few frames, then there will be too many and too frequent page faults.) causes Thrashing.

Question13 : What is paging and why do we need it?
Answer : Paging is a memory management scheme that eliminates the need for contiguous allocation of physical memory. This scheme permits the physical address space of a process to be non – contiguous.
        Paging is used for faster access to data. When a program needs a page, it is available in the main memory(RAM) as the OS copies a certain number of pages from your storage device to main memory. Paging allows the physical address space of a process to be noncontiguous.

Question14 : Demand paging , Segmentation.
Answer : Demand paging is a method of virtual memory management which is based on the principle that pages should only be brought into memory if the executing process demands them. This is often referred to as lazy evaluation as only those pages demanded by the process are swapped from secondary storage to main memory.
    So demand paging works opposite to the principle of loading all pages immediately.

    Segmentation is a memory management technique in which the memory is divided into the variable size parts. Each part is known as a segment which can be allocated to a process.
    The details about each segment are stored in a table called a segment table. Segment table is stored in one (or many) of the segments.
    Segment table contains mainly two information about segment:
    Base: It is the base address of the segment
    Limit: It is the length of the segment.

Question15 : Real Time operating system , types of RTOS.
Answer : A real-time operating system (RTOS) is a special-purpose operating system used in computers that has strict time constraints for any job to be performed and is intended to serve real time applications that possess data as it comes in , typically without buffer delays.
        Types of RTOS:
        1.Hard RTOS
        2.Firm RTOS
        4.Soft RTOS

Question16 : Difference between main memory and secondary memory.

Question17 : what is Staic Binding and Dynamic Binding ?
Answer : Static binding happens when the code is compiled, while dynamic bind happens when the code is executed at run time.
    Static Binding:
    When a compiler acknowledges all the information required to call a function or all the values of the variables during compile time, it is called “static binding”. As all the required information is known before runtime, it increases the program efficiency and it also enhances the speed of execution of a program. Static Binding makes a program very efficient, but it declines the program flexibility, as ‘values of variable’ and ‘function calling’ are predefined in the program. Static binding is implemented in a program at the time of coding. Overloading a function or an operator is the example of compile time polymorphism i.e. static binding.

    Dynamic Binding: Calling a function or assigning a value to a variable, at run-time is called “Dynamic Binding”. Dynamic binding can be associated with run time ‘polymorphism’ and ‘inheritance’ in OOP. Dynamic binding makes the execution of a program flexible as it can decide what value should be assigned to the variable and which function should be called, at the time of program execution. But as this information is provided at run time it makes the execution slower as compared to static binding.

Question18 : FCFS Scheduling?
Answer : Abstract
In FCFS, the process that requires CPU first is allocated CPU first. 
It is a non-preemptive scheduling algorithm.
Scope
This article talks about FCFS scheduling in detail.

Definition
FCFS (First-Come-First-Serve) is the simplest scheduling algorithm. The basic idea is the process that comes first is scheduled first. It follows the principle of FIFO (First-in-First-Out). It is a non-preemptive algorithm.

Let’s look at this problem

           PROCESS	          ARRIVAL TIME	          BURST TIME
              P0	                  0	                    10
              P1	                  1	                    6
              P2	                  3	                    2
              P3	                  5	                    4
Only the processes in the ready queue are to be considered. Since there is no preemption, once the job starts it is going to run until its completion. Now let’s look at the Gantt chart:


Now let’s compute each type of time using concepts and formulae.

PROCESS	ARRIVAL TIME	BURST TIME	COMPLETION         TIME	TURN AROUND TIME	WAITING TIME
P0	        0	        10	          10	                    10	                    0
P1	        1	        6	          16	                    15	                    9
P2	        3	        2	          18	                    15	                    13
P3	        5	        4	          22	                    17	                    13
*Turnaround time = Completion time - Arrival time

*Waiting time = Turnaround time - Burst time 

So average turnaround time is = (10+15+15+17)/4  = 57/4 = 14.25

Average waiting time = (0+9+13+13)/4 = 35/4 = 8.75

Note :

The lower the average turnaround time, the better it is.
The lower the average waiting time, the better it is.
The higher the CPU utilization, the better it is.
The higher the throughput, the better it is
The average waiting time under FCFS policy is generally not minimal.
Some important points :
It is very simple and easy to implement.
It is non-preemptive. Once you assign a process to a processor you cannot take the processor back.
It results in a convoy effect. Suppose there are many IO-bound processes and one CPU-bound process. The IO-bound process has to wait for the CPU-bound process when the CPU-bound process acquires the CPU. This slows down the operating system. Each process should get a CPU for an equal amount of time but this algorithm does not follow this principle. 
The average waiting time is not optimal.
Summary
FCFS is the simplest scheduling algorithm. The implementation of the FCFS policy is easily managed with the FIFO queue.
It is a non-preemptive scheduling algorithm. It results in poor performance and low throughput.

Question19 : SJF Scheduling?
Abstract
In SJF(Shortest Job First)  scheduling, the process which has the shortest burst time is scheduled first but if two processes have the same burst time then FCFS is used to break the tie. It is a non-preemptive scheduling algorithm.

Scope 
This article talks about SJF scheduling in detail.

Definition
The problem in FCFS scheduling was if there is a job that is CPU bound and it has come first and has been scheduled on CPU, the other jobs which take less time to have to wait for this long job. It decreases throughput and increases average waiting time. The idea of the shortest job first algorithm is to consider the jobs in increasing order of their CPU burst time. This algorithm is non-preemptive. Being a non-preemptive algorithm, the first process assigned to the CPU is executed till completion then the process whose burst time is minimum is assigned next to the CPU and hence it continues. 

Let’s understand the following problem :

PROCESS 	ARRIVAL TIME 	BURST TIME
        P0	            0	          5
        P1	            1	          4
        P2	            2	          3
        P3	            3	          8
The Gantt chart of the following problem is:


Final Chart

PROCESS	    ARRIVAL TIME 	BURST TIME	COMPLETION TIME 	TURN AROUND TIME	WAITINGTIME 
P0	            0	          5	              5	                    5	            0
P1	            1	          4	              12	                11	            7
P2	            2	          3	              8	                    6	            3
P3	            3	          8	              20               	    17	            9
* Turn around time = Completion time - Arrival time 

*Waiting time = Turn around time - Burst time 

So Average turn around time = (5+11+6+17)/4 = 39/4

And average waiting time = (0+7+3+9)/4 = 19/4

Some important points 
This algorithm gives a minimum average waiting time so it is an optimal algorithm.
It is a greedy algorithm.
If the shorter processes keep coming one after the other, it may cause starvation. This problem can be solved using the concept of aging. 
This algorithm assumes that the operating system knows the burst time of every process in the ready queue which is an impractical thing because it is not possible to guess the CPU burst time of every job or process.
Summary
SJF(Shortest Job first) is a non-preemptive algorithm. In this, the process which has the shortest CPU burst time is scheduled first. This algorithm has the minimum average time among all the scheduling algorithms.

Question20 : SRTF Scheduling?
SRTF Scheduling is a preemptive version of SJF scheduling. In SRTF, the execution of the process can be stopped after a certain amount of time. At the arrival of every process, the short term scheduler schedules the process with the least remaining burst time among the list of available processes and the running process.


Question21 : LRTF Scheduling?
Answer : This is a preemptive version of Longest Job First (LJF) scheduling algorithm. In this scheduling algorithm, we find the process with the maximum remaining time and then process it. We check for the maximum remaining time after some interval of time(say 1 unit each) to check if another process having more Burst Time arrived up to that time.

Question22 : Priority Scheduling?
Answer : Priority Scheduling is a method of scheduling processes that is based on priority. In this algorithm, the scheduler selects the tasks to work as per the priority.
        The processes with higher priority should be carried out first, whereas jobs with equal priorities are carried out on a round-robin or FCFS basis. Priority depends upon memory requirements, time requirements, etc.

Question23 : Round Robin Scheduling?
Answer : In Round-robin scheduling, each ready task runs turn by turn only in a cyclic queue for a limited time slice. This algorithm also offers starvation free execution of processes. Widely used preemptive scheduling method in traditional OS. All the jobs get a fair allocation of CPU. Cons include : Finding a correct time quantum is a quite difficult task in this system, Round-robin scheduling doesn’t give special priority to more important tasks.

Question24 : Producer Consumer Problem?
Answer : About Producer-Consumer problem: The Producer-Consumer problem is a classic problem that is used for multi-process synchronisation i.e. synchronisation between more than one processes.
The job of the Producer is to generate the data, put it into the buffer, and again start generating data. While the job of the Consumer is to consume the data from the buffer.
What's the problem here?
1.The following are the problems that might occur in the Producer-Consumer:
2.The producer should produce data only when the buffer is not full. If the buffer is full, then the producer shouldn't be allowed to put any data into the buffer.
3.The consumer should consume data only when the buffer is not empty. If the buffer is empty, then the consumer shouldn't be allowed to take any data from the buffer.
4.The producer and consumer should not access the buffer at the same time.
Solution : We can solve this problem by using semaphores.

Question25 : Banker's Alglorithm?
Answer : It is a banker algorithm used to avoid deadlock and allocate resources safely to each process in the computer system. The 'S-State' examines all possible tests or activities before deciding whether the allocation should be allowed to each process. It also helps the operating system to successfully share the resources between all the processes. The banker's algorithm is named because it checks whether a person should be sanctioned a loan amount or not to help the bank system safely simulate allocation resources.

Question26 : Explain Cache?
Answer : Cache memory is an extremely fast memory type that acts as a buffer between RAM and the CPU. It holds frequently requested data and instructions so that they are immediately available to the CPU when needed.


Question27 : What is cache maping? 
Answer : Cache mapping represents which word of the main memory will be placed at which location of the main memory. It represents the mapping between the cache addresses and the main memory addresses referring to the same unit of information.
There are three types of mapping 
1.Direct mapping
2.Associative mapping
3.Set associative mapping

Direct mapping :
While transferring the data from main memory to cache memory, it uses the formula KmodN to replace any line. Where K indicates main memory block no. and N indicates no. of cache lines. 

Associative mapping :
While transferring the data from main memory to cache lines, it checks the availability of the line. If the line is free, immediately data is transferred without any formulae (rules). If the line is not available, with the help of a replacement algorithm any one of the lines is replaced by the new data.
The main idea was to avoid high conflict miss, any block of main memory can be placed anywhere in cache memory.


Question28 : Difference between direct mapping and associative mapping?
Answer : In direct mapping, only one possible place in the cache is available for each block in the main memory.
In associative mapping, any place in the cache is available for each block in the main memory.


Question28 : Difference betweem multitasking and multiprocessing?
Answer : Multitasking: It is an extension of multiprogramming. In multitasking, a specific time slot is given to each process to run. This increases responsiveness. 
        Multiprocessing : It is an operating system that supports multiple processors. It makes the computer run faster because all the programs are distributed to various processors.
MULTITASKING:	                                        
1.The simultaneous execution of more than one task is known as multitasking.	
2.Only one CPU is required	
3.Only one job is executed at a time	
4.It takes a moderate amount of time	
5.It is economical	
6.It has more than one number of users	
7.It has moderate throughput	
8.Multitasking’s efficiency is moderate 	
9.It is classified into two: Single user multitasking and multiple user multitasking 	
10.It has more than one user tasks 
 
MULTIPROCESSING
1.In multiprocessing, we use more than one processor which executes several sets of instructions parallel.
2.More than one CPU is required.
3.More than one job is executed at a time.
4.It takes less time
5.It is also economical
6.It has either one or more users 
7.It has a maximum throughput
8.Multiprocessing’s efficiency is maximum
9.It is classified into two: Symmetric multiprocessing and asymmetric multiprocessing.
10.It has one or more than one user tasks 