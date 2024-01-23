import unittest
import string

def encrypt(message):
    abc = string.ascii_letters + string.punctuation + string.digits+ " "
    encrypted_message="".join([abc[abc.find(char)+1] if len(abc)>(abc.find(char)+1) else abc[0] for idx, char in enumerate(message)])
    return encrypted_message

class TestEncryption(unittest.TestCase):
    def setUp(self):
        self.my_message="Hi Hello @# 33"    
    def test_inputExists(self):
        self.assertIsNotNone(self.my_message)

    def test_inputType(self):
        self.assertIsInstance(self.my_message,str)

    def test_funcReturnsSomething(self):
        self.assertIsNotNone(encrypt(self.my_message))

    def test_lenIO(self):
        self.assertEqual(len(self.my_message),len(encrypt(self.my_message)))

    #WE are checking wether the first i.e input msg is revealed withing the output msg.
    def test_differentIO(self):
        self.assertNotIn(self.my_message,encrypt(self.my_message))

    def test_outputType(self):
        self.assertIsInstance(encrypt(self.my_message),str)

    def test_shiftedCipher(self):
        abc = string.ascii_letters + string.punctuation + string.digits+ " "
        encrypted_message="".join([abc[abc.find(char)+1] if len(abc)>(abc.find(char)+1) else abc[0] for idx, char in enumerate(self.my_message)])
        print(encrypted_message)
        self.assertEqual(encrypted_message,encrypt(self.my_message))

if __name__ == "__main__":
    unittest.main()