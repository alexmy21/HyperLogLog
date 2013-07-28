from HLL import HyperLogLog
import unittest

class TestRegisterFunctions(unittest.TestCase):

    def setUp():
	self.k = 5
	self.hll = HyperLopLog(5)

    def test_set_last_register(self):
	self.hll.set_register(self.k - 1, 1)
	self.assertTrue(self.registers()[self.k - 1] == 1)

    def test_set_first_register(self):
	self.hll.set_register(0, 1)
	self.assertTrue(self.registers()[0] == 1)

    def test_registers_returns_bytesarray(self):
	self.assertTrue(self.registers() is bytesarray)

    def test_registesr_returns_correct_length_bytes_array(self):
	self.assertTrue(len(self.registers()) == pow(2, self.k))

class TestCardinalityEstimation(unittest.TestCase):

    def setUp(self):
	""" """

    def test_add_adds_an_element_to_a_random_register(self):
        """ """

    def test_small_range_correction(self):
	""" """

    def test_medium_range_no_correction(self):
	""" """

    def test_large_range_correction(self):
 	""" """

    def test_the_larger_rank_is_used_when_comparing_elements(self):
        """ """

class TestHyperLogLogConstructor(self):

    def setUp(self):
	""" """

    def test_non_power_of_2_size_is_invalid(self):
	""" """


    def test_negative_size_is_invalid(self):
    	""" """

    def test_size_2_is_valid(self):
        """ """

    def test_all_registers_initialized_to_zero(self):
        """ """

    def test_size_param_correctly_determines_the_number_of_registers(self):
        """ """

    def test_seed_can_be_set(self):
        """ """

class TestMerging(self):

    def setUp(self):
	""" """

    def test_only_same_size_HyperLogLogs_can_be_merged(self):
        """ """

    def test_merge(self):
        """ """



if __name__ == '__main__':
    unittest.main()









"""
import HLL
n = HLL.HyperLogLog(12, 314)

path='/usr/share/dict/words'
f = open(path, 'r')
i = 0
for line in f.readlines():
    tokens = line.split(' ')
    for token in tokens:
        if i % 100 is 0:
            print n.murmur3_hash(token)
        n.add(token)

print dir(n)
print n.cardinality()
n.set_register(100,0)
n.set_register(200,0)
n.set_register(300,0)
n.set_register(300,0)



print n.cardinality()


#YT343axlkepskkde0
# intersection(hyperloglog)
# hash(data)
# fold()
# union(hyperloglog)
# set all registers(val)
# check to see is VARARGS has a single arg component for hyperloglog_methods
"""