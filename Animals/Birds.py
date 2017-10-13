class Birds:
    members = []

    def __init__(self):
        self.members = ['Sparrow', 'Robin', 'Duck']

    def printMembers(self):
        print('Print members of Birds class!')
        for member in self.members:
            print('\t%s' % member)
