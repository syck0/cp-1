import unittest
from app.classes.amity import Amity
from app.classes.room import Room, Office, Lspace
from app.classes.person import Person, Staff, Fellow

class AmityTest(unittest.TestCase):

    def setUp(self):
        self.amity = Amity()
        self.staff = self.amity.add_person("staff1","Staff")
        self.fellow = self.amity.add_person("fellow1","Fellow","N")

    def test_add_person(self):
        "Tests for new staff"
        self.assertIsInstance(self.amity.add_person("Ian Kingori","Staff","N"), Staff)
        self.assertIsInstance(self.amity.add_person("Ian Kingori","Staff"), Staff)
        self.assertEqual(self.amity.add_person("Ian Kingori","Staff","Y"), "Error, Staff cannot be allocated a living space")

        "Tests for new fellow"
        self.assertIsInstance(self.amity.add_person("Ian Kingori","Fellow","N"), Fellow)
        self.assertIsInstance(self.amity.add_person("Ian Kingori","Fellow","Y"), Fellow)
        self.assertIsInstance(self.amity.add_person("Ian Kingori","Fellow"), Fellow)

        "Test Invalid Input"
        self.assertEqual(self.amity.add_person("Ian Kingori", "Intern", "Y" ), "Invalid role")

    def test_create_room(self):
        pass

    def test_reallocate_person(self):
        pass

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
