#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
一个unittest学习用例
"""

import unittest

class MyTest(unittest.TestCase):
	def setUp(self):
		self.a = 1
		self.b = 2

	def test_assert_equal(self):
		"""a == b"""
		self.assertEqual(self.a, 1)
		self.assertEqual(self.b, 2)

	def test_fial_if_equal(self):
		"""a != b"""
		self.failIfEqual(self.a, self.b)

	def test_assert_not_equal(self):
		"""a != b"""
		self.assertNotEqual(self.a, self.b)

	def test_assert_true(self):
		"""bool(x) is True"""
		self.assertTrue(self.a==1)
		self.assertTrue(self.b==2)

	def test_assert_false(self):
		"""bool(x) is false"""
		self.assertFalse(self.a==self.b)

	def test_assert_is(self):
		class A(object):
			pass

		a = A()
		b = a
		c = A()
		self.assertIs(a, b)

		self.assertIsNot(a, c)

	def test_is_none(self):
		def _a():
			return
		_b = _a()	
		self.assertIsNone(_b)
		self.assertIsNotNone({})

	def test_in_and_not_in(self):
		_list = [1, 2, 'haha']
		self.assertIn(1, _list)
		self.assertNotIn(3, _list)

	def test_is_inc_and_not_inc(self):
		class _A(object):
			pass

		a = _A()
		self.assertIsInstance(a, _A)
		_D = type("D", (object, ), {'x': 1})
		self.assertNotIsInstance(a, _D)

	def test_raise(self):
		def _a(num):
			if num <= 0:
				raise TypeError("TypeError")
			else:
				return True

		self.assertRaises(TypeError, _a(1))

if __name__ == '__main__':
	print __doc__
	unittest.main()