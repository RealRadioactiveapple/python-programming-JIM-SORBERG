from plotter import PlotVectors

class Vector:
    """a class to represent a eucliden vector magnitude and direction """

    def __init__(self, *numbers: float) -> None:
        #print(numbers)
        for number in numbers:
            if not isinstance(number, (float,int)):
                raise TypeError(f"{number} must be a float or int not {type(number)}")
        if len(numbers) <= 0:
            raise ValueError("vectors cant be empty")

        self._numbers = tuple(float(number) for number in numbers)


    @property
    def numbers(self) -> tuple:
        return self._numbers
    #(2,3) + (1,1,1) not okey
    #(2,3) + (1,1)= (3,4) is okey
    def __add__(self, other: "Vector") -> "Vector":
        if self.validate_vector(other):
            numbers = (a+b for a,b in zip(self.numbers, other.numbers))
            return Vector(*numbers)

    def __sub__(self, other: "Vector") -> "Vector":
         if self.validate_vector(other):
            numbers = (a-b for a,b in zip(self.numbers, other.numbers))
            return Vector(*numbers)

    def __mul__(self, value: float) -> "Vector":
        if not isinstance(value,(float, int)):
            raise TypeError(f"it most be a number")
        
        numbers = (value * a for a in self.numbers)
        return Vector(*numbers)

    def __rmul__(self, value: float):
        return self*value


    def __len__ (self) -> int:
        """retun number of components in a vector not the euclidean lenght"""
        return len(self.numbers)
    
    def validate_vector(self, other: "Vector") -> bool:
        """validate thet two vectors have the same dimensions"""
        if not isinstance(other, Vector) or len(other) != len(self):
            raise TypeError("both most be a vector and same lenght")
        return len(self) == len(other)

    def __repr__(self) -> str:
        return f"vector {self.numbers}"
    
    def __str__(self) -> str:
        return f"{self.numbers}"

    def __getitem__(self, item: int) ->float:
        return self.numbers[item]

    def __eq__(self, other) -> bool:
        if not self.validate_vector(other):
            return False
        
        for num1, num2 in zip(self.numbers, other.numbers):
            if num1 != num2:
                return False
        return True

    def plot(self, *others: "Vector") -> None:
        # TODO: error checking
        # composition -> vector has a PlotVector object
        plot_vector = PlotVectors(self, *others)
        
        plot_vector.plot()
        


# v1 = (1,1), v2 = (1,1,3,4,5,6,)S
