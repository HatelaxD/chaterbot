# This file is for testing the code within the console.

import meaning
from ChatBot import inputRefactor
from ChatBot import messageHandler

refactorer = inputRefactor.InputRefactor()
meaning = meaning.Meaning()
messageHandler = messageHandler.MessageHandler()

while True:
    msg = input("Talk to me: ")
    refactored_input = refactorer.nonLetterRemover(msg)
    refactored_input = refactorer.tokenise(refactored_input)
    print(messageHandler.generate_response(msg, 1))
