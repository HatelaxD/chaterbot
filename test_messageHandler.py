import unittest as unittest
from ChatBot import messageHandler

messageHandler = messageHandler.MessageHandler()

# To create these tests, the source code of messageHandler.py was modified to always return the first element rather
# than a random choice each time.
# specifically lines 30, 32 and 34.


class test_messageHandler(unittest.TestCase):
    def test_greeting(self):
        # Test greetings work
        self.assertEqual(messageHandler.generate_response("Hello", 1), messageHandler.greetings[0] + str(1) + "!")
        self.assertEqual(messageHandler.generate_response("Hi.", 1), messageHandler.greetings[0] + str(1) + "!")
        self.assertEqual(messageHandler.generate_response("Hi", 1), messageHandler.greetings[0] + str(1) + "!")
        self.assertEqual(messageHandler.generate_response("HI", 1), messageHandler.greetings[0] + str(1) + "!")
        self.assertEqual(messageHandler.generate_response("hi", 1), messageHandler.greetings[0] + str(1) + "!")
        self.assertEqual(messageHandler.generate_response("Good day", 1), messageHandler.greetings[0] + str(1) + "!")
        self.assertNotEqual(messageHandler.generate_response("123", 1), messageHandler.greetings[0] + str(1) + "!")
        self.assertNotEqual(messageHandler.generate_response("@£!@£!@£", 1), messageHandler.greetings[0] + str(1) + "!")
        self.assertNotEqual(messageHandler.generate_response("word", 1), messageHandler.greetings[0] + str(1) + "!")
        self.assertNotEqual(messageHandler.generate_response("+_!@£*£A", 1), messageHandler.greetings[0] + str(1) + "!")
        self.assertNotEqual(messageHandler.generate_response(" ", 1), messageHandler.greetings[0] +
        str(1) + "!")

    def test_feeling(self):
        # Test feeling messages work
        self.assertEqual(messageHandler.generate_response("Sven how are you?", 1), messageHandler.feeling[0])
        self.assertEqual(messageHandler.generate_response("Sven how are you", 1), messageHandler.feeling[0])
        self.assertEqual(messageHandler.generate_response("Sven how do you do?", 1), messageHandler.feeling[0])
        self.assertEqual(messageHandler.generate_response("Sven how do you do", 1), messageHandler.feeling[0])
        self.assertEqual(messageHandler.generate_response("Sven do you feel?", 1), messageHandler.feeling[0])
        self.assertEqual(messageHandler.generate_response("Sven feel?", 1), messageHandler.feeling[0])
        self.assertNotEqual(messageHandler.generate_response("Hello", 1), messageHandler.feeling[0])
        self.assertNotEqual(messageHandler.generate_response("+_!@£*£A", 1), messageHandler.feeling[0])
        self.assertNotEqual(messageHandler.generate_response("@@'@!AS", 1), messageHandler.feeling[0])
        self.assertNotEqual(messageHandler.generate_response("random word", 1), messageHandler.feeling[0])
        self.assertNotEqual(messageHandler.generate_response(" ", 1), messageHandler.feeling[0])

    def test_thanks(self):
        # Test thanks messages work
        self.assertEqual(messageHandler.generate_response("Sven thanks.", 1), messageHandler.thanks[0])
        self.assertEqual(messageHandler.generate_response("Sven thank you", 1), messageHandler.thanks[0])
        self.assertEqual(messageHandler.generate_response("Sven nice one", 1), messageHandler.thanks[0])
        self.assertEqual(messageHandler.generate_response("Sven thank", 1), messageHandler.thanks[0])
        self.assertEqual(messageHandler.generate_response("Sven thanks you?", 1), messageHandler.thanks[0])
        self.assertNotEqual(messageHandler.generate_response("Hello", 1), messageHandler.thanks[0])
        self.assertNotEqual(messageHandler.generate_response("Sven how are you?.", 1), messageHandler.thanks[0])
        self.assertNotEqual(messageHandler.generate_response("@!£!@£A@$", 1), messageHandler.thanks[0])
        self.assertNotEqual(messageHandler.generate_response("((!@£aaa@@", 1), messageHandler.thanks[0])
        self.assertNotEqual(messageHandler.generate_response(" ", 1), messageHandler.thanks[0])















