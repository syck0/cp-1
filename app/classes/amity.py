import random
from .room import Office, Lspace
from .person import Staff, Fellow


class Amity():
    def __init__(self):
        self.staff = []
        self.rooms = []
        self.fellows = []
        self.people = []
        self.lspace_unallocated = []
        self.office_unallocated = []

    def add_person(self, name, role, wants_accomadation = 'N'):
        if role.upper() == 'STAFF':
            if wants_accomadation == 'Y':
                print("Error, Staff cannot be allocated a living space")
                return "Error, Staff cannot be allocated a living space"
            office = self.select_random_room(Office)
            person = Staff(name, office )
            self.allocate_room(person, office)
            self.people.append(person)
            print(person.name + " added successfully")

        elif role.upper() == 'FELLOW':
            lspace = None
            office = None
            if wants_accomadation:
                lspace = self.select_random_room(Lspace)
            office = self.select_random_room(Office)
            person = Fellow(name, office, lspace)
            self.people.append(person)
            self.allocate_room(person, office)
            self.allocate_room(person, lspace)
            print(person.name + " added successfully")
        else:
            person = "Invalid role"

        return person

    def allocate_room(self, person, room):
        if room is not None and room.check_availability():
            room.occupants.append(person.name.upper())
            room.number_of_occupants += 1

    def deallocate_room(self, person, room):
        if room is not None:
            room.occupants.remove(person.name.upper())
            room.number_of_occupants -= 1

    #Randomly allocates rooms
    def select_random_room(self, room_type):
        available_rooms = []
        selected_room = None
        for room in self.rooms:
            if type(room) == room_type:
                if(room.check_availability()):
                    available_rooms.append(room)
        number_available = len(available_rooms)
        if number_available > 0:
            selected_room = random.sample(available_rooms, 1)[0]
        else:
            #TODO:Implement waiting list
            print("There are no vacancies")
        return selected_room


    def create_room(self, name, room_type):
        room = None
        if room_type.upper() == 'OFFICE':
            room = Office(name)
            self.rooms.append(room)
            message = room.name+" office created successfully"

        elif room_type.upper() == 'LSPACE':
            room = Lspace(name)

            self.rooms.append(room)
            message = room.name+" lspace created successfully"

        else:
            message = "Invalid room type"
        print(message)
        return room

    #Search for person
    def search_person(self, person_name):
        for person in self.people:
            if person.name == person_name.upper():
                return person
        return None



    #Search for room given name and class, returns room instance or false
    def search_room(self, room_name):
        for room in self.rooms:
            if (room.name).upper() == room_name.upper():
                    return room
        return False


    #Print Allocations to screen
    def print_allocations(self, file_name = False):
        for room in self.rooms:
            if not file_name:
                print("\n")
                print(room.name)
                print ("-------------------------------------")
                print(', '.join(str(name) for name in room.occupants))
                print("\n")
            else:
                file = open(file_name + ".txt", 'a')
                file.write(room.name + "\n")
                file.write("-------------------------------------\n")
                file.write(', '.join(str(name) for name in room.occupants))
                file.write("\n\n")
                file.closed

    #realocates to a specific room
    def reallocate_person(self, name, room_name):
        new_room = self.search_room(room_name)
        if new_room == False:
            print("Room Does Not Exist")
        else:
            person = self.search_person(name)
            if (person is not None):
                if type(new_room) == Office:
                    self.deallocate_room(person, person.office_allocated)
                    person.office_allocated = new_room
                    self.allocate_room(person, new_room)
                elif type(new_room) == Lspace:
                    if type(person) == Fellow:
                        self.deallocate_room(person, person.lspace_allocated)
                        person.lspace_allocated = new_room
                        self.allocate_room(person, new_room)

                    else:
                        print("Staff Cannot be alocated an LSPACE")
