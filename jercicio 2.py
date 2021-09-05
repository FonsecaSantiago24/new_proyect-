#programa para calcular media aritmetica 

n1=int(input("digite el valor 1: "))
n2=int(input("digite el valor 2: "))
n3=int(input("digite el valor 3: "))

#calculo de la media aritmetica
media_aritmetica=(n1+n2+n3)/3
print("el valor de la media aritmetica es: ",media_aritmetica)

print("______________________________________________________")


#programa para calcular valor de la compra con descuento (valor final ) 

precio=int(input("digite el valor de la compra: "))
descuento=float(input("digite el valor del descuento: "))
#calculo
valor_final=precio-(descuento*precio)/100
print("el valor final a pagar es de:",valor_final)

