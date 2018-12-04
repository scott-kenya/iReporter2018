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

	

	# # test correct product payload
	# def test_is_incident_payload(self):
	# 	payload=(items,['title','type','location','status','Images','Videos','comment'])
	# 	test = self.obj.is_incident_payload(payload)
	# 	self.assertTrue(test)

	# # test incorrect payload
	# def test_not_payload(self):
	# 	payload = {'Title':'Broken bridge','createdOn':12/12/2019,'createdBy':'scott francis',
	# 	'type':'redflag','location':'N32-345 E87-098','name': 'draft','images':'red.jpg',
	# 	'videos':'red.mpeg','comments':'awesome'}
	# 	test = self.obj.is_incident_payload(payload)
	# 	self.assertFalse(test)

if __name__ == '__main__':
	unittest.main()