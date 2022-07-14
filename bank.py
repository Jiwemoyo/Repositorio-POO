from payment import Payment

class Bank(Payment):
    bank            = str
    identification  = str
    numberAccount   = int
    
    def __init__(self, id, ammount, bank, identification, numberAccount):
        super().__init__(id, ammount)
        self.bank           = bank
        self.identification = identification
        self.numberAccount  = numberAccount