
## Taxi_v3
# Observations:
There are 500 discrete states since there are 25 taxi positions, 5 possible locations of the passenger (including the case when the passenger is in the taxi), and 4 destination locations.
# Passenger locations:

    0: R(ed)
    1: G(reen)
    2: Y(ellow)
    3: B(lue)
    4: in taxi 


# Destinations:

    0: R(ed)
    1: G(reen)
    2: Y(ellow)
    3: B(lue) 


# Actions:
There are 6 discrete deterministic actions:

    0: move south
    1: move north
    2: move east
    3: move west
    4: pickup passenger
    5: drop off passenger 


# Rewards:

    There is a default per-step reward of -1,
    except for delivering the passenger, which is +20,
    or executing "pickup" and "drop-off" actions illegally, which is -10. 
