class Person:
    '''Represent a person'''
    population = 0

    def __init__(self,name):
        '''Initializes the person's data.'''
        self.name=name
        print '(Initializing the %s)' % self.name
        Person.population+=1

    def __del__(self):
        '''I am dying.'''
        print '%s says bye.' % self.name
        Person.population-=1
        if Person.population==0:
            print 'I am the last one.'
        else :
            print 'There are still %d people left.' % Person.population
    def sayHi(self):
        '''Greeting by the person.

        Really , that's all it does.'''
        print 'Hi, my name is %s' % self.name
    def howMany(self):
        '''Print the current population.'''
        if Person.population == 1:
            print 'I am the only person here.'
        else :
            print 'We have %d persons here.' % Person.population


swaroop = Person('Swaroop')
print swaroop.__del__.__doc__
#swaroop.sayHi()
#swaroop.howMany()

#kalam = Person('Abdul Kalam')
#kalam.sayHi()
#kalam.howMany()

#swaroop.sayHi()
#swaroop.howMany()
#del(swaroop)
#del(kalam)

class Student(Person):
    '''I am a student.'''
    def __init__(self,name):
        Person.__init__(self,name)
        print '(Initialized a student)'
    def sayHi(self):
        print 'Hi, I am %s , a student.' % self.name
andy= Student('Andy')
andy.sayHi()
andy.howMany()
print andy.__del__.__doc__
