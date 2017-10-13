class MyClass:
    variable =''
    def function(self):
        print('This is the message %s' %(self.variable))

myClass = MyClass()
myClass.variable = 'Hi !'
myClass.function()

'''
Exercise
We have a class defined for vehicles. Create two new vehicles called car1 and car2. 
Set car1 to be a red convertible worth $60,000.00 with a name of Fer, 
and car2 to be a blue van named Jump worth $10,000.00.
'''
print('***** Start Exercixe !!!')
class Vehicle:
    name = ''
    kind = 'car'
    color = ''
    value = 100.00
    #def setValue(name,kind,color,value):

    def description(self):
        desc = ' %s is a %s %s worth $%.2f ' %(self.name,self.color,self.kind,self.value)
        return desc

car1 = Vehicle()
car1.name = 'Fer'
car1.color = 'red'
car1.kind = 'convertible'
car1.value=60000

car2 = Vehicle()
car2.name = 'Jump'
car2.color = 'blue'
car2.kind = 'van'
car2.value=10000

print(car1.description())
print(car2.description())

