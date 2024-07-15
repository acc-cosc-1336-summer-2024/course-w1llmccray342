import unittest

from src.homework.j_classes.class_a import Die

class Test_Config(unittest.TestCase):
        
    def test_Die_get_rolled_value(self):
        my_first_dice = Die()
        my_second_dice = Die()
        my_third_dice = Die()

        my_first_dice_roll = my_first_dice.roll()
        my_second_dice_roll = my_second_dice.roll()
        my_third_dice_roll = my_third_dice.roll()

        my_dice_to_test = [my_first_dice_roll, my_second_dice_roll, my_third_dice_roll]

        for dice in my_dice_to_test:
            self.assertEqual( 1 >= dice.get_rolled_value(dice) <= 6)