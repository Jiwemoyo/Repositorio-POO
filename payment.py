class Payment :
    id      = int
    ammount = int
    
    def __init__(self,id,amount) -> None:
        self.ammount = amount
        self.id      = id
        
        pass