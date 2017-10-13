def my_function():
    print('Hello python function.')

def my_function_args(name,greeting):
    print('Hello %s ,I would like to say %s' %(name,greeting))

def my_summary(a,b):
    print('The summary result of %d and %d is %d ' %(a,b,a+b))

my_function()
my_function_args('BOM','HI !')
my_summary(5,5)

#Exercise
#In this exercise you'll use an existing function, and while adding your own to create a fully functional program.
#Add a function named list_benefits() that returns the following list of strings: "More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"
#Add a function named build_sentence(info) which receives a single argument containing a string and returns a sentence starting with the given string and ending with the string " is a benefit of functions!"
#Run and see all the functions work together!
print('***** Start Exercixe !!!')
def list_benefits():
    benefits=[]
    benefits.append('More organized code')
    benefits.append('More readable code')
    benefits.append('Easier code reuse')
    benefits.append('Allowing programmers to share and connect code together')
    return benefits

def build_sentense(benefit):
    return " %s is a benefit of functions!" %(benefit)

def name_benefit_of_function():
    listBenefits = list_benefits()
    for benefit in listBenefits:
        print(build_sentense(benefit))

name_benefit_of_function()