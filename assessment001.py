from time import sleep
import random

class Plane:
    def __init__(self, priority, flightNumber, planeRequest):       # Plane Constructor
        self.priority = priority
        self.flightNumber = flightNumber
        self.planeRequest = planeRequest
    def getPriority(self):          # getting the priority of a plane
        return self.priority

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