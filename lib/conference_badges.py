def badge_maker(name):
    badge = (f"Hello, my name is {name}.")
    return badge

def batch_badge_creator(names):
    badges = [f"Hello, my name is {name}." for name in names]
    # Remember list comprehensions return lists,(now to get the for loop method working:)
    return badges


def assign_rooms(names):
    room_assignments = []
    for i, name in enumerate(names, start=1):
        room_assignments.append(f"Hello, {name}! You'll be assigned to room {i}!")
    return room_assignments

def printer(names):
    badges = batch_badge_creator(names)
    room_assignments = assign_rooms(names)
    
    for badge in badges:
        print(badge)
    for assignment in room_assignments:
        print(assignment)