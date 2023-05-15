class Frame:
    def __init__(self, slots, inherits=None):
        self.slots = slots
        self.inherits = inherits or []

    def __getitem__(self, key):
        for slot in self.slots:
            if slot[0] == key:
                return slot[1]
        for parent in self.inherits:
            val = parent[key]
            if val is not None:
                return val
        return None

    def __setitem__(self, key, value):
        for i, slot in enumerate(self.slots):
            if slot[0] == key:
                self.slots[i] = (key, value)
                return
        self.slots.append((key, value))

    def add_parent(self, parent):
        self.inherits.append(parent)

class Situation(Frame):
    pass

class Event(Frame):
    pass

class Action(Frame):
    pass

if __name__ == '__main__':
    walk = Action([('agent', 'John'), ('verb', 'walk'), ('destination', 'park')])
    print(walk['agent'])  # Output: John

    picnic = Situation([('agent', 'John'), ('verb', 'picnic'), ('location', 'park')])
    print(picnic['location'])  # Output: park

    meeting = Event([('participants', ['John', 'Mary', 'Joe']), ('verb', 'meet'), ('location', 'office')])
    print(meeting['participants'])  # Output: ['John', 'Mary', 'Joe']
