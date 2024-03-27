# data-structures
Repo for the assessment of Data Structures and Algorithms course 

## Subject

Produce an annotated software design that addresses the data
needs of an appropriate business problem.

## Scenario

A small airport, with low traffic, needs to maintain landings and takeoffs. To do so, it
maintains two queues where planes requesting to land or to takeoff are added,
respectively.
Planes should not wait long time on air until landing, so a takeoff will be allowed only if
the landing queue is empty.
It is possible that a plane requesting landing may have a problem (malfunction, low
level of fuel, etc). In this case the landing will be given highest priority and allowed to
land before any other landing request in the queue.
  a. Define the appropriate data structures to implement this application.
  b. Implement a simulation that will randomly add requests (landing, takeoff,
     emergency landing) and give allowance to the proper action.

### Example output:

```bash
Flight 345 requests landing
Flight 190 requests landing
Flight 188 requests takeoff
CONTROL: 345 land
Flight 621 requests emergency landing
CONTROL: 621 land
Flight 511 requests takeoff
CONTROL: 190 land
CONTROL: 188 takeoff
CONTROL: 511 takeoff
Flight 810 requests takeoff
CONTROL: 810 takeoff
```

## Necessary libraries

```python
from time import sleep
import random
```

## Code explanation

First we create a Plane Class to store our plane details like this:

```python
class Plane:
    def __init__(self, priority, flightNumber, planeRequest):       # Plane Constructor
        self.priority = priority
        self.flightNumber = flightNumber
        self.planeRequest = planeRequest
    def getPriority(self):          # getting the priority of a plane
        return self.priority
```
Then we create the Priority Queue that will process the orders:

```python
class PriorityQueue:
    def __init__(self):         # Priority Queue Constructor
        self.queue = []

    def is_Empty(self):         # If queue is empty, return True
        return not self.queue
    
    def sortQueue(func):        # Sort queue by priority Decorator
        def inner(self, *args, **kwargs):
            returnedVal = func(self, *args, **kwargs)
                                                                        #The queue is sorted after the function is called
            self.queue.sort(key=lambda x: x.priority, reverse=False)    #using the lambda function to get the priority from the Class
            
            return returnedVal
        return inner

    @sortQueue          # add a plane to the queue and sort it 
    def put(self, value):
        self.queue.insert(0,value)

    @sortQueue
    def get(self):
        if not self.is_Empty():
            plane = self.queue.pop(-1)      # the priority plane is last in the queue and dequeued with get()
            self.sortQueue()
            return plane
        else:
            print("No planes left in queue")

    def size(self):             # returning the length of the queue
        return len(self.queue)
```
The function sortQueue(func) is a decorator function that wraps any function
that it decorates in order to sort the Queue after every function call.
The way we sort it is by using a lamba function to get the priority from the
Plane object and use it as our key in the sort() func
```python
self.queue.sort(key=lambda x: x.priority, reverse=False)
```

On the Main program, we initialize the repetions of the While loop, 
the While loop variable, the Priority Queue and a list of choices 
to choose randomly, a list of landing choices, the value of the 
1st process and finally the dictionary of emergencies.

```python
reps = 0
running = True
flights = PriorityQueue()

choices = [1, 2, 2]
landingchoices = ["landing", "takeoff", "emergency landing"]
process = 2 # 1st process

emergency = {
    2: "Low Fuel",
    3: "Engine Problems",
    4: "Passenger Emergency",
    5: "Airborne Attack"
}
```

Finally, the While loop consists of an if statement to run process 1,
that processess a flight and process 2, that adds a new random flight 
request.
We also check if the size of the list is larger than 15 so the program
can terminate after every flight is processed or the reps are larger 
than 50.

```python
while running == True:
    
    if process == 1:                 # processing orders 
        plane = flights.get()
        if not flights.is_Empty():
            if plane.getPriority() == 0:
                print(f"CONTROL: {plane.flightNumber} takeoff")
            else:
                print(f"CONTROL: {plane.flightNumber} land")
        elif flights.is_Empty() and reps > 20:
            running = False

    elif process == 2:                                          # adding new orders
        
        planeRequest = random.choice(landingchoices)
        flightNumber = random.randint(100, 999)

        if planeRequest == "takeoff":
            print(f"Flight {flightNumber} requests {planeRequest}")
            flights.put(Plane(priority=0, flightNumber=flightNumber, planeRequest=planeRequest))

        elif planeRequest == "landing":
            print(f"Flight {flightNumber} requests {planeRequest}")
            flights.put(Plane(priority=1, flightNumber=flightNumber, planeRequest=planeRequest))
        
        else:
            planeEmergency = random.randint(2,5)
            print(f"Flight {flightNumber} requests {planeRequest} - Reason: {emergency[planeEmergency]}")
            flights.put(Plane(priority=planeEmergency, flightNumber=flightNumber, planeRequest=planeRequest))
    else:
        continue

    reps += 1

    if flights.size() > 15:     # we limit the process to be only 1 so the program can end
        choices.clear()
        choices.append(1) 
    
    process = random.choice(choices)    # we put the next process in the end instead of the begginning so the 1st process is always a request

    if reps > 50:
        running = False
    
    sleep(0.1)
```





