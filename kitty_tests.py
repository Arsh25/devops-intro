import unittest
from kittystuff import KittyStuff


class KittyTests(unittest.TestCase):
    def test_kitty_purr(self):
        my_kitty = KittyStuff()
        self.assertEqual(my_kitty.purr(),'purr')
        self.assertEqual(my_kitty.purr(1),'purr!')
        self.assertEqual(my_kitty.purr(2),'purr!!')
        self.assertEqual(my_kitty.purr(1), 'purr!')
        self.assertEqual(my_kitty.purr(5), 'purr!!!!!')
        self.assertEqual(my_kitty.purr(0), 'purr')

    def test_setting_happiness(self):
        my_kitty = KittyStuff()
        self.assertEqual(my_kitty.happiness, 0)
        my_kitty.set_happiness(1)
        self.assertEqual(my_kitty.happiness,1)
        my_kitty.set_happiness(-1)
        self.assertEqual(my_kitty.happiness, -1)
        my_kitty.set_happiness(100)
        self.assertEqual(my_kitty.happiness, 100)

    def test_let_owner_sleep(self):
        my_kitty = KittyStuff()
        self.assertEqual(my_kitty.let_owner_sleep(),True)
        my_kitty.set_happiness(1)
        self.assertEqual(my_kitty.let_owner_sleep(), True)
        my_kitty.set_happiness(3)
        self.assertEqual(my_kitty.let_owner_sleep(), True)
        my_kitty.set_happiness(5)
        self.assertEqual(my_kitty.let_owner_sleep(), False)
        my_kitty.set_happiness(100)
        self.assertEqual(my_kitty.let_owner_sleep(), False)
        my_kitty.set_happiness(5.5)
        self.assertEqual(my_kitty.let_owner_sleep(), False)

    def test_scratch_owner(self):
        my_kitty = KittyStuff()
        self.assertEqual(my_kitty.scratch_owner(), True)
        my_kitty.set_happiness(2)
        self.assertEqual(my_kitty.scratch_owner(), True)
        my_kitty.set_happiness(4)
        self.assertEqual(my_kitty.scratch_owner(), True)
        my_kitty.set_happiness(5)
        self.assertEqual(my_kitty.scratch_owner(), False)
        my_kitty.set_happiness(10)
        self.assertEqual(my_kitty.scratch_owner(), False)
        my_kitty.set_happiness(100)
        self.assertEqual(my_kitty.scratch_owner(), False)
        my_kitty.set_happiness(0)
        self.assertEqual(my_kitty.scratch_owner(), True)



if __name__=='__main__':
    unittest.main(failfast=False)
