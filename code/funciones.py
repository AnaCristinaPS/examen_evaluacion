import pandas as pd
import os

def leer_datos(path):
    """
    En esta funcion se lee un archivo de formato cvs en formato pandas
    y a la columna TS en donde estan las fechas se las convierte a datetime
    """
    df=pd.read_csv(path)
    df['TS']=pd.to_datetime(df['TS'])
    return df

def filtrar_calcular_media(df,alumno:str):
    """
    Teniendo como un input el dataframe y el nombre del alumno
    La funcion filtra el tag de acuerdo al alumna y calcula la media de la columna valor
    """
    df=df.loc[df['Tag'].str.startswith("Examen_"+alumno)]
    media=round(df['Value'].mean(),2)
    return media
