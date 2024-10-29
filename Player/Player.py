import abc

class PlayerClass(abc.ABC):
    '''Player class interface'''

    def __init__(self:object) -> None:
        pass
     
    @abc.abstractmethod
    def Move(self:object) -> None:
        pass

    def Eat(self:object) -> None:
        pass