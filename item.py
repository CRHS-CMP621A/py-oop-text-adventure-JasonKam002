class Item():
    def __init__(self, name):
        self.name=name
        self.description=None

    def getname(self):
        print(f'{self.name}')

    def set_description(self, description):
        self.description=description


