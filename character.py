class Character():
    def __init__(self, name, description):
        self.name=name
        self.description=description
        self.conversation=None

    def describe(self):
        print(f'{self.name} is here! \n{self.description}')
    
    def set_conversation(self, conversation):
        self.conversation=conversation
    
    def talk(self):
        print(f'[{self.name} says]: {self.conversation}')

    def fight(self):
        print(f'{self.name} does not want to fight with you')

class Enemy(Character):
    def __init__(self, name, description):
        super().__init__(name, description)
        self.weakness=None
        
    def set_weakness(self, weakness):
        self.weakness=weakness
    
    def get_weakness(self):
        print(f"{self.name}'s weakness is {self.weakness}")
    
    def fight(self, weapon):
        if weapon == self.weakness:
            print(f'You killed {self.name} with your {weapon}')
            return True
        else:
            print(f'{self.name} crushed you')
            return False