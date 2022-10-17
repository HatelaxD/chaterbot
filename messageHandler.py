class MessageHandler:
    import inputRefactor
    import meaning
    import random as random
    import webscraping
    import requests

    def __init__(self):

        # TODO put this to database THOMAS
        self.greetings = ["Hello! ", "Hi! ", "Sup bro ", "Hey ", "I'm here to help you :) ", "Good bean! "]
        self.feeling = ["I do not have feelings", "I feel like Pablo"]
        self.thanks = ['No problem bro!',
                       'I am robot, my existance is pointless, so you do not have to thank me, because I do not fell '
                       'nothing!',
                       'Ez pz', 'I am just learning to love you in the future :)',
                       'Hey you just wasted 10 sec of your life to say thanks to computer program, you weirdo!',
                       'Ok, Ok,',
                       'Hakuna Matata!']
        self.refactorer = self.inputRefactor.InputRefactor()
        self.meaningH = self.meaning.Meaning()
        self.informer = self.webscraping.GetWebInfo()

    def generate_response(self, message, author):
        response_ref = self.refactorer.nonLetterRemover(message)
        response_ref = self.refactorer.tokenise(response_ref)
        response_list = self.meaningH.predict(response_ref, message)
        if response_list[0] is "Greeting":
            response = self.random.choice(self.greetings) + str(author) + '!'
        elif response_list[0] is "Feeling":
            response = self.random.choice(self.feeling)
        elif response_list[0] is "Thanks":
            response = self.random.choice(self.thanks)
        elif response_list[0] is None:
            response = "Sorry I don't understand your message :/"
        elif response_list[1] is None:
            response = "Do you mean?"
            if response_list[0] is "Craft_question":
                if len(response_list[3]) > 0:
                    response = "Do you mean: How do I craft " + ' or '.join(response_list[3]) + '?'
                else:
                    response = "Sorry I do not know what do you want to craft | here is list of items that you can " \
                               "ask me about: https://www.minecraftcraftingguide.net/ "
            elif response_list[0] is "Item_question":
                response = "Do you mean: What can I do with " + ' or '.join(response_list[3]) + '?'
        elif response_list[0] is "Craft_question":
            itemData = self.requests.get("http://51.83.46.159:8000/items/" + str(response_list[1]['id']) + "?format=json").json()
            response = "Here is how to create " + str(itemData['itemTitle'])  + ' | ' + str(itemData['itemIngredients']) + ' | https://' + str(itemData['craftingURL'])
        else:
            itemData = self.requests.get("http://51.83.46.159:8000/items/" + str(response_list[1]['id']) + "?format=json").json()
            response = str(itemData['itemDescription'])

        return response




cookies = {
    "sb": "xasyYmAoy1tRpMGYvLxgkHBF",
    "fr": "0NxayJuewRHQ30OX3.AWVJwIYNh0Tt8AJv6kSwDamhkoM.BiMrVd.Iu.AAA.0.0.BiMtVZ.AWXMVaiHrpQ",
    "c_user": "",
    "datr": "xasyYs51GC0Lq5H5lvXTl5zA",
    "xs": ""
}


client = ChatBot("",
                 "", session_cookies=cookies)
print(client.isLoggedIn())

try:
    client.listen()
except:
    time.sleep(3)
    client.listen()

