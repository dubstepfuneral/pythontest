class Item:
    def __init__(self):
        pass


class ItemList:
    def __init__(self):
        self.list = []
    
    def create(self, name, dateDue, priority):
        thing = {'name': name, 'dateDue': dateDue, 'priority': priority} # priority - High, Medium, Low
        self.list.append(thing)

    def getAll(self):
        for i in range(len(self.list)):
            ending = '' # ; or . depending whether it's the last one
            if self.list[i] == self.list[-1]:
                ending = '.'
            else:
                ending = ';'
            print(i+1, ': ', self.list[i]['name'], ', Date due: ', self.list[i]['dateDue'], ', Priority: ', self.list[i]['priority'], ending, sep='')
    
    def getByDate(self, date):
        for i in self.list:
            if i['dateDue'] == date:
                ending = '' # ; or . depending whether it's the last one
                if self.list[i] == self.list[-1]:
                    ending = '.'
                else:
                    ending = ';'
                print(i+1, ': ', self.list[i]['name'], ', Date due: ', self.list[i]['dateDue'], ', Priority: ', self.list[i]['priority'], ending, sep='')
    
    def getByPriority(self, priority):
        for i in self.list:
            if i['priority'] == priority:
                ending = '' # ; or . depending whether it's the last one
                if self.list[i] == self.list[-1]:
                    ending = '.'
                else:
                    ending = ';'
                print(i+1, ': ', self.list[i]['name'], ', Date due: ', self.list[i]['dateDue'], ', Priority: ', self.list[i]['priority'], ending, sep='')

    def deleteThing(self, thingName):
        for i in len(self.list):
            if self.list[i]['name'].lower() == thingName.lower():
                actualName = self.list[i]['name'] # in case if it's not the right by casing
                self.list.pop(i)
                print("Case named '", actualName, "' deleted.", sep='')
    
    def changeName(self, thingName, newName):
        for i in len(self.list):
            if self.list[i]['name'].lower() == thingName.lower():
                previousName = self.list[i]['name'] 
                self.list[i]['name'] = newName
                print("Name changed from '", previousName, "' to '", newName, "' successfully.")

    