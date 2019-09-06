class Party:
    # observers = []
    # invitation = {}
    def __init__(self, party_name, friends=None, day=None, time=None):
        if friends is None:
            self.friends=[]
        else : 
            self.friends = friends

        if day is None:
            self.day=""
        else : 
            self.day= day

        if time is None:
            self.time=""
        else : 
            self.time= time
                
        self.party_name = party_name

    def add_friend(self,friend):
        self.friends.append(friend.name)

    def delete_friend(self,friend):
        self.friends.remove(friend.name)

    def send_invititation(self, day, time):
        
        self.day = day 
        self.time = time
        
        return day + " " + "at" + time
class Friend(Party):

    def __init__(self, name):
        self.name = name
        
    
    def show_invite(self):
        pass


party = Party("Midnight Pub")
party2 = Party('khhader')

nick = Friend("Nick")
john = Friend("John")
lucy = Friend("Lucy")
chuck = Friend("Chuck")
 
party.add_friend(nick)
party.add_friend(john)
party.add_friend(lucy)
party.send_invititation('Friday','12:00')
party2.add_friend(nick)

nick.show_invite()

print(party.__dict__)
print(party2.__dict__)
