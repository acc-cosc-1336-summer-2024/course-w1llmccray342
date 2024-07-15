import unittest

from src.homework.j_classes.class_a import Die

class Test_Config(unittest.TestCase):
        
    def test_Die_get_rolled_value(self):
        dice_no = 0
        
        # Create three objects
        my_first_dice = Die()
        my_second_dice = Die()
        my_third_dice = Die()

        # Store 3 dice objects into a list
        my_dice = [my_first_dice, my_second_dice, my_third_dice]

        # For each dice present in my_dice we create a empty list:
        for dice in my_dice:
            my_dice_to_test = []
            dice_no += 1

            # Inner loop to roll three dice and append them to a test list
            for i in range(3):
                my_temporary_dice = dice.roll()
                my_dice_to_test.append(my_temporary_dice)

                 # For each dice in my test list we want to check that each value is within the range of 1, 6 if anything else is
                 # Detected we should receive an assertion error.
            
            for my_dice in my_dice_to_test:
                # Check that the rolled_value is in the range 1, 6
                # self should be included to check get_rolled_value
                self.assertEqual(True, Die.get_rolled_value(self, my_dice) in range(1, 7))
                self.assertEqual(False, Die.get_rolled_value(self, my_dice) in range(8, 99))                
                


           
      
