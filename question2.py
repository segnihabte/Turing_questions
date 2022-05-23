class Welcome:

        def __init__(self,name):
            self.name=name

        def say_hello(self):
                print('Welcome to',self.name)

cw = Welcome('Turing')
cw.say_hello()