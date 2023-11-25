def roll_call_dwarves(dwarves):
    for index, dwarf in enumerate((dwarves)):
        print(f"{index + 1}. {dwarf}")

def summon_captain_planet(calls):
    planet_calls = [f"{call.capitalize()}!" for call in calls]
    return planet_calls

def long_planeteer_calls(calls):
    for call in calls:
        if(len(call) > 4):
            return True
        elif(len(call) <= 4 and call == calls[-1]):
            return False
        

def find_the_cheese(snacks):
    cheese = ['cheddar', 'gouda', 'camembert']
    for snack in snacks:
        if(snack in cheese):
            return snack
    return None