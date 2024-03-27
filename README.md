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
