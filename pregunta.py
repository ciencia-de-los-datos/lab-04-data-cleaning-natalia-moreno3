"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd
from functools import reduce
import sweetviz as sv

def clean_col(df, col_name):
    df = df.copy()
    # df[col_name] = df[col_name].str.strip()
    df[col_name] = df[col_name].str.lower()
    df[col_name] = df[col_name].str.replace('_', ' ')
    df[col_name] = df[col_name].str.replace('-', ' ')
    # df[col_name] = df[col_name].str.translate(
    #     str.maketrans("", "", "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~")
    # )
    # df[col_name] = df[col_name].str.strip()

    return df

def format_date(date):
    chain = date.split('/')
    if len(chain[0]) == 4:
        formated_date = '/'.join(reversed(chain))
    else:
        formated_date = date
    return formated_date

def clean_data():
    df = pd.read_csv("solicitudes_credito.csv",index_col=0, sep=";")

    cols_to_clean = ['sexo', 'tipo_de_emprendimiento', 'barrio',
                 'línea_credito', 'idea_negocio']

    for col in cols_to_clean:
        df = clean_col(df=df, col_name=col)

    df["comuna_ciudadano"] = df["comuna_ciudadano"].astype(int)

    df['monto_del_credito'] = df['monto_del_credito'].str.strip('$')
    df['monto_del_credito'] = df['monto_del_credito'].str.replace(',', '')
    df['monto_del_credito'] = df['monto_del_credito'].str.replace(' ', '')
    df["monto_del_credito"] = df["monto_del_credito"].astype(float)
    df["monto_del_credito"] = df["monto_del_credito"].astype(int)

    df["fecha_de_beneficio"] = df["fecha_de_beneficio"].map(format_date)

    df.dropna(inplace=True)
    df.drop_duplicates(inplace=True)

    return df
