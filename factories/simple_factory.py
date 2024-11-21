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


class VeichleFactory:
    @staticmethod
    def get_car(type: str) -> Veichle:  # type: ignore

        match type.lower():
            case 'luxury':
                return LuxuryCar()
            case 'popular':
                return PopularCar()
            case 'luxury_motorcycle':
                return LuxuryMotorcycle()
            case 'popular_motorcycle':
                return LuxuryMotorcycle()
            case _:
                assert 0, "Car does'nt exists."


if __name__ == '__main__':
    from random import choice
    available_veichles = [
        'Luxury', 'Popular', 'Luxury_Motorcycle', 'Popular_motorcycle'
    ]

    for i in range(10):
        car = VeichleFactory.get_car(choice(available_veichles))
        car.get_client()
