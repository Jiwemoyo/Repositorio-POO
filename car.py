from account import Account


class Car :
    id          = int
    driver      = Account(",")
    passager    = int
    brand       = str
    model       = str
    license     = str
    
    def __init__(self,license,driver):
        self.license    =license
        self.driver     =driver
        pass