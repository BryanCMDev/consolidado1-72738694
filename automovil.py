class Automovil:
    def __init__(
        self,
        marca: str,
        modelo: str,
        velocidad_max: float,
        nivel_combustible: float,
        año_fabricacion: int
    ):
        self.marca = marca
        self.modelo = modelo
        self._velocidad_max = velocidad_max
        self._nivel_combustible = nivel_combustible
        self._año_fabricacion = año_fabricacion

    @property
    def año_fabricacion(self):
        return self._año_fabricacion

    @año_fabricacion.setter
    def año_fabricacion(self, año):
        if año < 1886 or año > 2026:
            raise ValueError(
                "El año debe estar entre 1886 y 2026."
            )

        self._año_fabricacion = año

    @property
    def nivel_combustible(self):
        return self._nivel_combustible

    @nivel_combustible.setter
    def nivel_combustible(self, nivel):
        if nivel < 0.0 or nivel > 100.0:
            raise ValueError(
                "El nivel de combustible debe estar entre 0 y 100."
            )

        self._nivel_combustible = nivel

    @property
    def velocidad_max(self):
        return self._velocidad_max

    @velocidad_max.setter
    def velocidad_max(self, velocidad):
        if velocidad <= 0:
            raise ValueError(
                "La velocidad máxima debe ser mayor a 0."
            )

        self._velocidad_max = velocidad

    def tiempo_llegada(self, distancia_km: float) -> float:
        return distancia_km / self.velocidad_max

    def __str__(self):
        return (
            f"Marca: {self.marca}\n"
            f"Modelo: {self.modelo}\n"
            f"Velocidad máxima: {self.velocidad_max} km/h\n"
            f"Combustible: {self.nivel_combustible}%\n"
            f"Año de fabricación: {self.año_fabricacion}"
        )


automovil = Automovil(
    "Toyota",
    "Corolla",
    180.0,
    75.0,
    2022
)

print(automovil)

print(
    f"Tiempo para recorrer 360 km: "
    f"{automovil.tiempo_llegada(360):.2f} horas"
)

automovil.nivel_combustible = 50
print(f"Nuevo combustible: {automovil.nivel_combustible}%")

try:
    automovil.año_fabricacion = 1800
except ValueError as error:
    print(f"Error de validación: {error}")