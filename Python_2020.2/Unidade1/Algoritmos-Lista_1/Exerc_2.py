#Fa�a um programa que calcule a m�dia de consumo (em km/l) de combust�vel de um ve�culo. O usu�rio deve informar o KM inicial (ex. 12500 km), o KM final (ex. 12700 km) e quantos litros foram gastos no percurso.

km1 = float(input('quantos km inicial:'))
km2 = float(input('quantos km final:'))
litro = float(input('quantos litros gastos:'))
kmt = km2-km1
consumototal = kmt/litro
print('consumo �:', consumototal)
