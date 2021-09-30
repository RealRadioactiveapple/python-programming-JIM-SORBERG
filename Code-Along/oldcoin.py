class Oldcoinstash:
    def __init__(self,owner: str) -> None:
        #this attributs are public
        self.owner = owner 

        # private - by convention use underscore prefix
        self._riksdaller = 0
        self._skilling = 0

    def deposit(self, riksdaller:float = 0, skilling:float = 0):
        if riksdaller < 0 or skilling < 0:
            raise ValueError(f"stop deposting negativ values. {riksdaller}riksdaler or {skilling} not okey")

        self._riksdaller += riksdaller
        self._skilling += skilling

    def withdraw (self, riksdaller:float = 0, skilling:float = 0):
        if riksdaller > self._riksdaller or skilling > self._skilling:
            raise ValueError("you have no money")
        self._skilling -= skilling
        self._riksdaller -= riksdaller

    def check_balance(self) -> str:
        return f"coins:{self._riksdaller} and {self._skilling}"

    def __repr__(self) -> str:
        return f"Oldcoinstash(owner = '{self.owner}')"