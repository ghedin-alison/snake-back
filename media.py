def media_acumulada():
    valores = []

    def calcula_media(valor):
        valores.append(valor)
        return sum(valores) / len(valores)
    return calcula_media


media = media_acumulada()
media(2)
media(2)
media(2)
media(2)
media(2)

print(media(500))

