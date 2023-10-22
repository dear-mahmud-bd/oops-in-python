class Family:
    def __init__(self, address) -> None:
        self.address = address

class School:
    def __init__(self, id, konClassE) -> None:
        self.id = id
        self.konClassE = konClassE

class Sports:
    def __init__(self, game) -> None:
        self.game = game

class Student(Family, School, Sports):
    def __init__(self, address, id, konClassE, game) -> None:
        School.__init__(self, id, konClassE)
        Sports.__init__(self, game)
        Family.__init__(self, address)