from unittest import TestCase # import from standard library
from funniest.command_line import main

class TestConsole(TestCase):
	def test_basic(self):
		main()