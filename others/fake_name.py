from faker import Faker
 
#----------------------------------------------------------------------
def create_names():

    fake = Faker('it_IT')
    for i in range(10):
        print(fake.name())
 

create_names()