# Calculo-de-comisiones-pendientes
En este script calculo las posibles combinaciones para que me den un numero determinado

Dada la necesidad especifica en mi empresa actual.

Reclamo de pago de comisiones pendientes.
para poder gestionar el pago de comisiones pendientes dentro de la emopresa se necesita idenfiticar cual o cuales expedientes o IDs no se han pagado, aproximadamente se realizan entre 80 y 100 pagos.
de los cuales algunos rebota, oh no se realizan por cuestiones administrativas, lo cual hace muy dificil identifcar cual o cuales expedientes estan faltantes de pago.

para el facil calculo de pagos pendientes de mi equipo ya que tenemos que identificar especificamente cual o cuales IDs o ordenes no se ah realizado el pago
cree este script que tomando en cuenta:

Monto_Pagado:= 800
Monto_a_pagar= 1000
monto_pagado - monto_a_pagar = targer_number
## se calcula el valor determinado que se le da al script en targer_number
Targer_number = 200

una vez dado el targer_number, se carga el archivo de excel identificando la columna "comisiones" y realiza el calculo de cual o cuales IDs, dan la sumataria exacta o mas proxima al targer_number.
