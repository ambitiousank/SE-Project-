import re
import unittest

def validateEmail(email):
	str = ["iiitb.org", "iiitb.ac.in"] # TODO: take this input from config file
	str = "|".join(str)
	if len(email) > 5: 
		if re.match("^[a-zA-Z0-9\\-\\.]+@+("+ str +")$", email) != None:
			return True
	return False
	
	
def validateName(name):
	if len(name) > 1 and len(name) < 31: #max allowed 30 
		if re.match("^[a-zA-Z]*$", name) != None:
			return True
	return False
	
def validateMobile(number):
	if len(str(number)) == 10 and (isinstance(number,long) or isinstance(number,int)): #max allowed 10 
		if re.match("^[0-9]*$", str(number)) != None:
			return True
	return False


class TestValidations(unittest.TestCase):

	def testValidateEmail(self):
		self.assertTrue(validateEmail("manAa12.oj@iiitb.org"))
		self.assertFalse(validateEmail("@iiitb.org"))
		self.assertTrue(validateEmail("manoj@iiitb.ac.in"))
		self.assertFalse(validateEmail("manoj@iiitb.ac"))
		self.assertTrue(validateEmail("manoj.batra@iiitb.org"))
		self.assertFalse(validateEmail("manoj.batra@gmail.org"))
		self.assertFalse(validateEmail("manoj.batra@iiitb.sc"))
		self.assertFalse(validateEmail("manoj.batra@iiitb.org.org"))
	
	def testValidateMobile(self):
		self.assertTrue(validateMobile(1234567890))
		self.assertFalse(validateMobile(123-123123))
		self.assertTrue(validateMobile(9036365260))
		self.assertFalse(validateMobile("1234567891"))
		self.assertTrue(validateMobile(1010101010))
		self.assertFalse(validateMobile(123))
		self.assertFalse(validateMobile(11234567890))
		self.assertFalse(validateMobile(90123123123))
	
	def testValidateName(self):
		self.assertFalse(validateName("manAa12"))
		self.assertFalse(validateName("iiitb.org"))
		self.assertFalse(validateName("j@i"))
		self.assertTrue(validateName("manoj"))
		self.assertFalse(validateName("manoj batra"))
		self.assertTrue(validateName("manojbatragmailorg"))
		self.assertFalse(validateName(""))
		self.assertFalse(validateName(" "))

suite = unittest.TestLoader().loadTestsFromTestCase(TestValidations)
unittest.TextTestRunner(verbosity=2).run(suite)