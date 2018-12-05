import unittest

from app.api.v1.models.verification import Verification

class TestVerification(unittest.TestCase):
	"""
	class to test verification
	"""
	def setUp(self):
		self.obj = Verification()

	def tearDown(self):
		self.obj = None

	# test empty data
	def test_is_empty(self):
		test = self.obj.is_empty(['','Pot-holes'])
		self.assertEqual(test,0)

	# if data is not emoty
	def test_not_empty(self):
		test = self.obj.is_empty(['scott','scott'])
		self.assertFalse(test)

	# test if white space
	def test_is_whitespace(self):
		test = self.obj.is_whitespace(['  ','Broken sewer'])
		self.assertEqual(test,0)

	# test if not whitespace
	def test_not_whitespace(self):
		test = self.obj.is_whitespace(['Road closure','Illegal structure'])
		self.assertFalse(test)

	def test_that_email_works(self):
	    with self.client:
	        response = self.client.post('login', { username: 'steve', password: '1234' })
			assertEquals(current_user.username, 'steve')