# Consolidado 1 — Construcción de Software

## Propósito

Práctica de programación orientada a objetos en Python. El proyecto modela
planetas, automóviles y productos bancarios, incluyendo propiedades,
herencia, encapsulamiento y validación de datos.

**Autor:** Bryan Alexander Cahuana Mendoza

**Código de estudiante:** [Completar por el estudiante]

## Archivos

- [`planeta.py`](./planeta.py): define `Planeta`, calcula la densidad con la
  masa y el volumen esférico, clasifica planetas exteriores y muestra dos
  ejemplos.
- [`automovil.py`](./automovil.py): define `Automovil`, valida velocidad
  máxima, combustible y año mediante propiedades, y calcula el tiempo de
  viaje.
- [`cuentas.py`](./cuentas.py): define `CuentaBancaria`, `CuentaAhorros` y
  `CuentaCorriente`, con depósitos, retiros, cálculo de intereses y
  sobregiro.

## Requisitos y ejecución en Windows

Se necesita Git para clonar el repositorio y Python 3 con el lanzador `py`.
Comprueba que el lanzador esté disponible:

```powershell
py --version
```

Desde la carpeta del proyecto, ejecuta cada programa por separado:

```powershell
py planeta.py
py automovil.py
py cuentas.py
```

## Clases y funcionalidades

### `Planeta`

Recibe `nombre`, `masa` (kg), `radio` (m), `distancia_al_sol` (UA) y
`tiene_vida` (opcional, inicialmente `False`). `calcular_densidad()` calcula
masa / ((4/3) × π × radio³), y `es_planeta_exterior()` solo devuelve `True`
para distancias mayores que 5.2 UA. La masa y el radio deben ser finitos y
mayores que cero. El ejemplo de Júpiter usa exactamente 5.2 UA y se muestra
como planeta interior de acuerdo con el límite solicitado.

### `Automovil`

Expone `marca` y `modelo`; las propiedades `velocidad_max`,
`nivel_combustible` y `año_fabricacion` validan también los valores recibidos
al crear el objeto. La velocidad debe ser mayor que cero, el combustible
debe estar entre 0 y 100, y el año entre 1886 y 2026, inclusive.
`tiempo_llegada(distancia_km)` devuelve distancia / velocidad máxima.

### Cuentas bancarias

- `CuentaBancaria` inicia con saldo cero y ofrece `depositar`,
  `retirar` y `consultar_saldo`. Los montos de depósito y retiro deben ser
  positivos, y la cuenta base no permite retirar más del saldo.
- `CuentaAhorros` hereda de `CuentaBancaria`; `calcular_interes()` obtiene
  saldo × tasa de interés / 100.
- `CuentaCorriente` permite un saldo negativo hasta el límite de sobregiro,
  rechaza límites negativos y expone `permite_sobregiro()` para indicar si
  el saldo es negativo.

Los ejemplos impresos muestran depósitos, retiros, cálculo de intereses y
uso del sobregiro. Los errores esperados se capturan para que la ejecución
continúe.

## Clonar el repositorio

En PowerShell, ejecuta:

```powershell
git clone https://github.com/BryanCMDev/consolidado1-72738694.git
cd consolidado1-72738694
```

Después, usa los comandos de ejecución indicados arriba. Para comprobar las
ramas disponibles en GitHub, ejecuta `git branch -a` dentro del repositorio.