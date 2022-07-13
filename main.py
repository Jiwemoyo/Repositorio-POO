from account import Account
from car import Car
from payment import Payment


if __name__ == "__main__":
    
    car = Car()
    car.id          = 1
    car.brand       = "Toyota"
    car.driver      = "Sebas"
    car.passager    = 4
    
    car2 = Car()
    car2.id          = 2
    car2.brand       = "Renault"
    car2.driver      = "Luis"
    car2.passager    = 5
    
    car3=Car()
    car2.id          = 3
    car2.brand       = "Andino"
    car2.driver      = "Ana"
    car2.passager    = 4
    

    account = Account()
    account.id          = 1
    account.name        = "Carlos"
    account.document    = 17549846
    account.mail        = "mail@gma"
    
    account2 = Account()
    account2.id          = 2
    account2.name        = "Paola"
    account2.document    = 1723502
    account2.mail        = "Pao@gma"
    
    print(vars(account2))