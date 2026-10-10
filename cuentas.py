class CuentaBancaria:
    def __init__(self, numero_cuenta: str, titular: str):
        self.numero_cuenta = numero_cuenta
        self.titular = titular
        self.__saldo = 0.0

    def depositar(self, monto: float):
        if monto <= 0:
            raise ValueError(
                "El monto a depositar debe ser mayor a 0."
            )

        self._ajustar_saldo(monto)

    def retirar(self, monto: float):
        if monto <= 0:
            raise ValueError(
                "El monto a retirar debe ser mayor a 0."
            )

        if monto > self.__saldo:
            raise ValueError(
                "Saldo insuficiente."
            )

        self._ajustar_saldo(-monto)

    def consultar_saldo(self) -> float:
        return self.__saldo

    def _ajustar_saldo(self, variacion: float) -> None:
        self.__saldo += variacion

    def __str__(self):
        return (
            f"Número de cuenta: {self.numero_cuenta} | "
            f"Titular: {self.titular} | "
            f"Saldo: S/ {self.__saldo:.2f}"
        )


class CuentaAhorros(CuentaBancaria):
    def __init__(
        self,
        numero_cuenta: str,
        titular: str,
        tasa_interes: float
    ):
        super().__init__(numero_cuenta, titular)
        self.tasa_interes = tasa_interes

    def calcular_interes(self) -> float:
        return (
            self.consultar_saldo()
            * self.tasa_interes
            / 100
        )

    def __str__(self):
        return (
            f"{super().__str__()} | "
            f"Tasa de interés: {self.tasa_interes}% | "
            f"Interés anual: S/ {self.calcular_interes():.2f}"
        )


class CuentaCorriente(CuentaBancaria):
    def __init__(
        self,
        numero_cuenta: str,
        titular: str,
        limite_sobregiro: float
    ):
        super().__init__(numero_cuenta, titular)

        if limite_sobregiro < 0:
            raise ValueError(
                "El límite de sobregiro no puede ser negativo."
            )

        self.limite_sobregiro = limite_sobregiro

    def retirar(self, monto: float):
        if monto <= 0:
            raise ValueError(
                "El monto a retirar debe ser mayor a 0."
            )

        saldo_disponible = (
            self.consultar_saldo()
            + self.limite_sobregiro
        )

        if monto > saldo_disponible:
            raise ValueError(
                "Se excedió el límite de sobregiro."
            )

        self._ajustar_saldo(-monto)

    def permite_sobregiro(self) -> bool:
        return self.consultar_saldo() < 0

    def __str__(self):
        return (
            f"{super().__str__()} | "
            f"Límite de sobregiro: S/ "
            f"{self.limite_sobregiro:.2f}"
        )


cuenta_bancaria = CuentaBancaria(
    "000-000001",
    "Bryan Cahuana"
)
cuenta_ahorros = CuentaAhorros(
    "001-123456",
    "Bryan Cahuana",
    4.5
)

cuenta_corriente = CuentaCorriente(
    "002-654321",
    "Bryan Cahuana",
    500.0
)

print("=== CUENTA BANCARIA ===")
cuenta_bancaria.depositar(500)
cuenta_bancaria.retirar(100)
print(cuenta_bancaria)

try:
    cuenta_bancaria.depositar(0)
except ValueError as error:
    print(f"Error de depósito esperado: {error}")

print("=== CUENTA DE AHORROS ===")

cuenta_ahorros.depositar(1000)

print(cuenta_ahorros)

cuenta_ahorros.retirar(200)

print(cuenta_ahorros)

print(
    f"Interés anual: "
    f"S/ {cuenta_ahorros.calcular_interes():.2f}"
)


print("\n=== CUENTA CORRIENTE ===")

cuenta_corriente.depositar(300)

print(cuenta_corriente)

cuenta_corriente.retirar(500)

print(cuenta_corriente)

print(
    f"¿Está usando sobregiro?: "
    f"{cuenta_corriente.permite_sobregiro()}"
)

try:
    cuenta_corriente.retirar(301)
except ValueError as error:
    print(f"Error de sobregiro esperado: {error}")