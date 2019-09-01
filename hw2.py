
class Chat:

    chat_room = []
    robot_text = ''
    human_text = ''
    counter = 0
    conversation = {}

    def connect_human(self,human):

        self.human_name = human.name
        self.chat_room.append(self.human_name)
        
        
    
    def connect_robot(self, robot):

        self.robot_name = robot.name
        self.chat_room.append(self.human_name)

        

    
    def show_human_dialogue(self):
        for key, value in self.conversation.items():

            if 'H' in key:
                
                print(self.human_name + " said: "+ value)
            else:
                print(self.robot_name + " said: "+ value)



    def show_robot_dialogue(self):

        new_val = ''
        for key, value in self.conversation.items():

            for char in value:
                if char in 'aeouiAEOUI':
                    new_val += '0'
                else:
                    new_val += '1'

            if 'H' in key:
                
                print(self.human_name + " said: "+ new_val)
            else:
                print(self.robot_name + " said: "+ new_val)
            
            new_val = ''


        

class Human(Chat):

    def __init__(self, name):
        self.name = name

    def send(self, message):
        Chat.conversation['H'+str(Chat.counter)] = message
        
        Chat.counter += 1



class Robot(Chat):

    def __init__(self, name):
        self.name = name
    
    def send(self, message):
        Chat.conversation['R'+ str(Chat.counter)] = message
        
        Chat.counter += 1


chat = Chat()

majd = Human('MAJD')
bot = Robot('R2D2')

chat.connect_human(majd)
chat.connect_robot(bot)

majd.send('Hello Im Majd')
majd.send('24 years old')
bot.send('Im the robot')
majd.send('I dont care')
bot.send('why?')

print('Human Dialogue:\n---------')
chat.show_human_dialogue()
print('\n')
print('Robot Dialogue:\n---------')
chat.show_robot_dialogue()
#chat.show_robot_dialogue(bot)

