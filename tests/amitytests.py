import unittest
from app.classes.amity import Amity
from app.classes.room import Room, Office, Lspace
from app.classes.person import Person, Staff, Fellow

class AmityTest(unittest.TestCase):

    def setUp(self):
        self.amity = Amity()
        #Staff
        self.staff1 = self.amity.add_person("staff1","Staff")
        self.staff2 = self.amity.add_person("staff2","Staff", "N")
        #Fellows
        self.fellow1 = self.amity.add_person("fellow1","Fellow","N")
        self.fellow2 = self.amity.add_person("fellow2","Fellow","Y")
        self.fellow3 = self.amity.add_person("fellow1","Fellow","Y")
        #Living spaces
        self.lspace1 = self.amity.create_room("lspace1", "lspace")
        self.lspace2 = self.amity.create_room("lspace2", "lspace")
        self.lspace3 = self.amity.create_room("lspace3", "lspace")
        #Offices
        self.office1 = self.amity.create_room("office1", "office")
        self.office2 = self.amity.create_room("office2", "office")
        self.office3 = self.amity.create_room("office3", "office")

    def test_add_person(self):
        "Add Person"
        self.assertIsInstance(self.staff1, Staff)
        self.assertIsInstance(self.amity.add_person("Ian Kingori","Staff", "N"), Staff)
        self.assertEqual(self.amity.add_person("Ian Kingori","Staff","Y"), "Error, Staff cannot be allocated a living space")

        "Tests for new fellow"
        self.assertIsInstance(self.amity.add_person("Ian Kingori","Fellow","N"), Fellow)
        self.assertIsInstance(self.amity.add_person("Ian Kingori","Fellow","Y"), Fellow)
        self.assertIsInstance(self.amity.add_person("Ian Kingori","Fellow"), Fellow)

        "Test Invalid Input"
        self.assertEqual(self.amity.add_person("Ian Kingori", "Intern", "Y" ), "Invalid role")

    def test_create_room(self):
        "Create Rooms"
        self.assertIsInstance(self.lspace1, Lspace )
        self.assertEqual(self.lspace1.name, "LSPACE1")

        "Create New Office"
        self.assertIsInstance(self.office1, Office )
        self.assertEqual(self.office1.name, "OFFICE1")

        "Invalid input"
        self.assertEqual(self.amity.create_room("test_invalid", "live-in"),  None)

    def test_search_room(self):
        "Test room search pass"
        self.assertIsInstance(self.amity.search_room("lspace1"), Lspace)

        "Test non existent room"
        self.assertFalse(self.amity.search_room("notthere") )

    def test_reallocate_person(self):
        "Reallocation"

        "Fellow LSpace Reallocation"
        self.amity.reallocate_person("fellow1", "lspace3")
        self.assertEqual(self.fellow1.lspace_allocated.name, "LSPACE3")
        self.assertTrue("FELLOW1" in self.lspace3.occupants)

        self.amity.reallocate_person("fellow1", "lspace2")
        self.assertEqual(self.fellow1.lspace_allocated.name, "LSPACE2")
        self.assertTrue("FELLOW1" in self.lspace2.occupants)
        self.assertFalse("FELLOW1" in self.lspace3.occupants)

        "Test Staff office reallocation"
        self.amity.reallocate_person("staff1", "office1")
        self.assertEqual(self.staff1.office_allocated.name, "OFFICE1")
        self.assertTrue("STAFF1" in self.office1.occupants)

        self.amity.reallocate_person("staff1", "office2")
        self.assertEqual(self.staff1.office_allocated.name, "OFFICE2")
        self.assertTrue("STAFF1" in self.office2.occupants)
        self.assertFalse("STAFF1" in self.office1.occupants)

        "Test Staff Lspace reallocation"
        self.assertEqual(self.amity.reallocate_person("staff1", "lspace1"), None)


    def test_load_people(self):
        pass

    def test_print_allocations(self):
        pass

    def test_print_unallocated(self):
        pass

    def test_print_room(self):
        pass

    def test_save_state(self):
        pass

    def test_load_state(self):
        pass




if __name__ == '__main__':
    unittest.main()
