import unittest
'''
the file in /tests/homework/b_in_proc_out/tests_in_proc_out
has the test functions
'''
#from tests.homework.b_in_proc_out import tests_in_proc_out
#from tests.examples.a_example import tests_devprocess
#from tests.examples.b_input_process_output import tests_input_process_output
#from tests.homework.b_in_proc_out import tests_in_proc_out (Homework 1)
#from tests.homework.c_decisions import tests_decisions # Homework 3
#from tests.examples.h_strings import tests_strings (Lecture)
#from tests.homework.d_repetition import tests_repetition (Homework 4)
#from tests.examples.g_lists_and_tuples import tests_lists_and_tuples (Lecture)
#from tests.homework.h_strings import tests_strings (HW5)
#from tests.examples.i_dictionaries_sets import tests_dictionaries_and_sets (Lecture)
#from tests.homework.i_dictionaries_sets import tests_dictionaries_and_sets (HW6)

from tests.homework.h_strings import tests_strings
suite = unittest.TestLoader().loadTestsFromModule(tests_strings)
unittest.TextTestRunner(verbosity=2).run(suite)
