rodas = int(input("Digite a quantidade de rodas do veículo: "))
peso = float(input("Digite o peso bruto do veículo em quilogramas: "))
pessoas = int(input("Digite a quantidade de pessoas no veículo: "))

if rodas <= 3:
    print("A categoria de habilitação recomendada é A")
elif rodas >= 4 and pessoas <= 8 and peso <= 3500:
    print("A categoria de habilitação recomendada é B")
elif rodas >= 4 and peso > 3500 and peso <= 6000:
    print("A categoria de habilitação recomendada é C")
elif rodas >= 4 and pessoas > 8:
    print("A categoria de habilitação recomendada é D")
elif rodas >= 4 and peso > 6000:
    print("A categoria de habilitação recomendada é E")
else:
    print("Não foi possível determinar a categoria de habilitação recomendada")
