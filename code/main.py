from funciones import leer_datos, filtrar_calcular_media
import pandas as pd

def main():
    df = leer_datos("datos_examen.csv")
    media=filtrar_calcular_media(df,'Ana')
    print(media)

if __name__ == "__main__":
    main()