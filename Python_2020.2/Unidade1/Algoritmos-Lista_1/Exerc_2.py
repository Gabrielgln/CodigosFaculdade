#Faça um programa que calcule a média de consumo (em km/l) de combustível de um veículo. O usuário deve informar o KM inicial (ex. 12500 km), o KM final (ex. 12700 km) e quantos litros foram gastos no percurso.

km1 = float(input('quantos km inicial:'))
km2 = float(input('quantos km final:'))
litro = float(input('quantos litros gastos:'))
kmt = km2-km1
consumototal = kmt/litro
print('consumo é:', consumototal)
