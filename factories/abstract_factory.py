'''
Abstract Factory é um padrão de criação que fornece uma
interface para criar famílias de objetos relacionados ou dependentes
sem especificar suas classes concretas. Geralmente Abstract Factory
conta com um ou mais Factory Methods para criar seus objetos.

Uma diferença importante entre Factory Method e Abstract Factory é que
o Factory Method usa herança, enquanto Abstract Factory usa a composição.

Princípio: programe para interfaces, não para implementações.
'''


from abc import ABC, abstractmethod


class PopularVeichle(ABC):

    @abstractmethod
    def get_client(self) -> None:
        pass


class LuxuryVeichle(ABC):
    @abstractmethod
    def get_client(self) -> None:
        pass


class ZNLuxuryCar(LuxuryVeichle):
    def get_client(self) -> None:
        print('ZN Luxury car is getting the client...')
        return super().get_client()


class ZNPopularCar(PopularVeichle):
    def get_client(self) -> None:
        print('ZN Popular car is getting the client...')
        return super().get_client()


class ZNLuxuryMotorcycle(LuxuryVeichle):
    def get_client(self) -> None:
        print('ZN Luxury Motorcicyle is getting the client...')
        return super().get_client()


class ZNPopularMotorcycle(PopularVeichle):
    def get_client(self) -> None:
        print('ZN Popular Motorcicyle is getting the client...')
        return super().get_client()


class ZSLuxuryCar(LuxuryVeichle):
    def get_client(self) -> None:
        print('ZS Luxury car is getting the client...')
        return super().get_client()


class ZSPopularCar(PopularVeichle):
    def get_client(self) -> None:
        print('ZS Popular car is getting the client...')
        return super().get_client()


class ZSLuxuryMotorcycle(LuxuryVeichle):
    def get_client(self) -> None:
        print('ZS Luxury Motorcicyle is getting the client...')
        return super().get_client()


class ZSPopularMotorcycle(PopularVeichle):
    def get_client(self) -> None:
        print('ZS Popular Motorcicyle is getting the client...')
        return super().get_client()


class VeichleFactory(ABC):
    @staticmethod
    @abstractmethod
    def get_luxury_car() -> LuxuryVeichle:
        pass

    @staticmethod
    @abstractmethod
    def get_popular_car() -> PopularVeichle:
        pass

    @staticmethod
    @abstractmethod
    def get_luxury_motorcycle() -> LuxuryVeichle:
        pass

    @staticmethod
    @abstractmethod
    def get_popular_motorcycle() -> PopularVeichle:
        pass


class ZNVeichleFactory(VeichleFactory):
    @staticmethod
    def get_luxury_car() -> LuxuryVeichle:
        return ZNLuxuryCar()

    @staticmethod
    def get_popular_car() -> PopularVeichle:
        return ZNPopularCar()

    @staticmethod
    def get_luxury_motorcycle() -> LuxuryVeichle:
        return ZNLuxuryMotorcycle()

    @staticmethod
    def get_popular_motorcycle() -> PopularVeichle:
        return ZNPopularMotorcycle()


class ZSVeichleFactory(VeichleFactory):
    @staticmethod
    def get_luxury_car() -> LuxuryVeichle:
        return ZSLuxuryCar()

    @staticmethod
    def get_popular_car() -> PopularVeichle:
        return ZSPopularCar()

    @staticmethod
    def get_luxury_motorcycle() -> LuxuryVeichle:
        return ZSLuxuryMotorcycle()

    @staticmethod
    def get_popular_motorcycle() -> PopularVeichle:
        return ZSPopularMotorcycle()


class Subsidiary:
    def get_clients(self):
        for factory in [ZNVeichleFactory(), ZSVeichleFactory()]:
            popular_car = factory.get_popular_car()
            popular_car.get_client()

            luxury_car = factory.get_luxury_car()
            luxury_car.get_client()

            popular_motorcycle = factory.get_popular_motorcycle()
            popular_motorcycle.get_client()

            luxury_motorcycle = factory.get_luxury_motorcycle()
            luxury_motorcycle.get_client()


if __name__ == '__main__':
    subsidiary = Subsidiary()
    subsidiary.get_clients()
