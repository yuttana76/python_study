class Mammals:
    members = []

    #Constructior for this class
    def __init__(self):
        self.members = ['Tiger', 'Elephant', 'Wild Cat']

    def printmembers(self):
        print('Print members of Mammal class !')
        for member in self.members:
            print('\t%s' % member)
