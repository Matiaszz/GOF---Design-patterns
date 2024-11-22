'''
Factory method é um padrão de criação que permite definir uma interface para
criar objetos, mas deixa as subclasses decidirem quais objetos criar.
O Factory method permite adiar a instanciação para as subclasses,
garantindo o baixo acoplamento entre classes.
'''

from abc import ABC, abstractmethod


class Veichle(ABC):

    @abstractmethod
    def get_client(self) -> None:
        print()


class LuxuryCar(Veichle):
    def get_client(self) -> None:
        print('Luxury car is getting the client...')
        return super().get_client()


class PopularCar(Veichle):
    def get_client(self) -> None:
        print('Popular car is getting the client...')
        return super().get_client()


class LuxuryMotorcycle(Veichle):
    def get_client(self) -> None:
        print('Luxury Motorcicyle is getting the client...')
        return super().get_client()


class PopularMotorcycle(Veichle):
    def get_client(self) -> None:
        print('Popular Motorcicyle is getting the client...')
        return super().get_client()


class VeichleFactory(ABC):

    def __init__(self, type):
        self.car = self.get_car(type)

    @staticmethod
    @abstractmethod
    def get_car(type: str) -> Veichle:  # type: ignore
        pass

    def get_client(self):
        self.car.get_client()


class ZNVeichleFactory(VeichleFactory):
    @staticmethod
    def get_car(type: str) -> Veichle:  # type: ignore

        match type.lower():
            case 'luxury_car':
                return LuxuryCar()
            case 'popular_car':
                return PopularCar()
            case 'luxury_motorcycle':
                return LuxuryMotorcycle()
            case 'popular_motorcycle':
                return LuxuryMotorcycle()
            case _:
                assert 0, "Car does'nt exists."


class ZSVeichleFactory(VeichleFactory):
    @staticmethod
    def get_car(type: str) -> Veichle:  # type: ignore

        match type.lower():
            case 'popular_car':
                return PopularCar()
            case _:
                assert 0, "Car doesn't exists."


if __name__ == '__main__':
    from random import choice
    print('''
===================
    NORTH ZONE
===================
''')
    available_veichles_ZN = [
        'Luxury_car', 'Popular_car', 'Luxury_Motorcycle', 'Popular_motorcycle'
    ]

    for i in range(10):
        carzn = ZNVeichleFactory(choice(available_veichles_ZN))
        carzn.get_client()

    print('''
===================
    SOUTH ZONE
===================
''')
    for i in range(10):
        available_veichles_ZS = [
            'Popular_car',
        ]
        carzs = ZSVeichleFactory(choice(available_veichles_ZS))
        carzs.get_client()
