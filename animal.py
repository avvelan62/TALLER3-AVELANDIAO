from abc import abstractmethod
from ianimal import IAnimal


class Animal(IAnimal):

    def __init__(self, nombre: str, edad: int, peso: float) -> None:
        """
        Constructor de la clase
        Args:
            nombre (str): nombre del animal
            edad (int): edad del animal
            peso (float): peso del animal
        """
        self._nombre = nombre
        self._edad = edad
        self._peso = peso
        self.kilos_comidos = 0

    # Métodos
    def comer(self, kilos: float) -> None:
        """Método para comer

        Args:
            kilos (float): Kilos comidos por el animal
        """
        self.kilos_comidos += kilos

    def obtener_kilos_comidos(self) -> float:
        """Obtiene los kilos comidos

        Returns:
            float: Cantidad de kilos comidos
        """
        return self.kilos_comidos

    @abstractmethod
    def hacer_sonido():
        """Método abstracto para hacer sonido
        """
        pass

    def obtener_nombre(self):
        """Obtiene el nombre del animal

        Returns:
            str: Nombre del animal
        """
        return self._nombre

    def obtener_peso(self):
        """Obtiene el peso del animal

        Returns:
            float: Peso del animal
        """
        return self._peso

    def obtener_edad(self):
        """Obtiene la edad del animal

        Returns:
            int: Edad del animal
        """
        return self._edad
