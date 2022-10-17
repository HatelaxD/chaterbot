from mcpi.minecraft import Minecraft
import time
import messageHandler

mc = Minecraft.create("51.83.46.159", 4711)
print("Connection success")

messageHandler = messageHandler.MessageHandler()


class Connection:
    def edited_on_message(self, message):
        player_ID = message.entityId
        message = message.message
        if message.lower() == "sven stop":
            mc.setBlock(9, -66, 8, 30)  # off
            mc.setBlock(9, -66, 8, 0)
            Connection.start()
            return

        if 'Sven' in message:
            response = "SVEN: " + messageHandler.generate_response(message, player_ID)
            mc.postToChat(response)

    @classmethod
    def start(self):
        '''function to control on/off of chatbot (controlls hotbar ingame)'''
        start_up = False
        while start_up == False:
            for posts in mc.events.pollChatPosts():
                if posts.message.lower() == "sven start":
                    start_up = True
                    mc.setBlock(7, -66, 8, 30)  # on turns on bossbar
                    mc.setBlock(7, -66, 8, 0)


connection = Connection()
connection.start()
while True:
    for posts in mc.events.pollChatPosts():
        connection.edited_on_message(posts)
    time.sleep(1)
