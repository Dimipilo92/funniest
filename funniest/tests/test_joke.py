from unittest import TestCase # standard unittest class

import funniest

class TestJoke(TestCase): # extends TestCase class
	def test_is_string(self):
		s = funniest.joke()
		self.assertTrue(isinstance(s, basestring))