import unittest
'''
the file in /tests/homework/b_in_proc_out/tests_in_proc_out
has the test functions
'''
#from tests.homework.b_in_proc_out import tests_in_proc_out
#from tests.examples.a_example import tests_devprocess
#from tests.examples.b_input_process_output import tests_input_process_output
#from tests.homework.b_in_proc_out import tests_in_proc_out (Homework 1)

from tests.homework.c_decisions import tests_decisions # Homework 3
suite = unittest.TestLoader().loadTestsFromModule(tests_decisions)
unittest.TextTestRunner(verbosity=2).run(suite)
