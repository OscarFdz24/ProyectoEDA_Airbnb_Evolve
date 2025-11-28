import pandas as pd
#Aqui definiremos una función para limpiar las columnas monetarias del dataset, las cuales son pasadas por parámetro junto al dataframe
def clean_monetary_columns(df,monetary_columns):
    df_cleaned = df.copy()
    
    # Bucle que itera en la lista pasada por parametro
    for col in monetary_columns:
        # Comprobamos que la columna existe en el dataframe, y en el caso de que exista realizamos las siguientes operaciones
        if col in df_cleaned.columns:
            df_cleaned[col] = (
                df_cleaned[col].astype(str)       # Convierto el objeto a String para poder operar
                .str.replace(r'[^0-9\.\-]', '', regex=True)         # Elimino los simbolos cambiandolos por un espacio en blanco
                .str.strip()        # Los elimino de los laterales
            )
            # Convertimos las columnas a tipo numérico
            df_cleaned[col] = pd.to_numeric(df_cleaned[col], errors="coerce")
    return df_cleaned

def clean_categorical_values(df):
    df_cleaned = df.copy()
    # Ahora limpiaremos y normalizaremos los valores categóricos de la columna neighbourhood_group
    if "neighbourhood_group" in df_cleaned.columns:
        df_cleaned["neighbourhood_group"] =  df_cleaned["neighbourhood_group"].replace(
            {
                "brookln" : "Brooklyn",
                "manhatan": "Manhattan"
            }
        )
        # Reemplazar valores nulos por "Unknown"
        df_cleaned["neighbourhood_group"] = df_cleaned["neighbourhood_group"].fillna("Unknown")
    
    # Inputamos los nulos de la columna "host_identity_verified"
    if "host_identity_verified" in df_cleaned.columns:
        # Aqui decido remplazar el valor de verified por confirmed para la comparativa en el análisis avanzado
        df_cleaned["host_identity_verified"] = df_cleaned["host_identity_verified"].replace({
        "verified": "confirmed"
        })
        df_cleaned["host_identity_verified"] = df_cleaned["host_identity_verified"].fillna("Unknown")
    
    # Inputamos también los nombres de la columna "neighbourhood"
    df_cleaned["neighbourhood"] = (
        df_cleaned["neighbourhood"]
        .astype(str)
        .str.split(",", n=1).str[0]
        .str.strip()
    )
    
    # Convertimos la columna "instant_bookable" a Booleano 
    if "instant_bookable" in df_cleaned.columns:
            df_cleaned["instant_bookable"] =  df_cleaned["instant_bookable"].replace(
            {
                "False" : False,
                "True": True
            }
            )
            
    df_cleaned["instant_bookable"] = df_cleaned["instant_bookable"].astype("boolean")
    
    # Convertimos columnas a category
    categorical_cols = [
        "host_identity_verified",
        "neighbourhood_group",
        "neighbourhood",
        "country",
        "country_code",
        "cancellation_policy",
        "room_type"
    ]

    for col in categorical_cols:
        if col in df_cleaned.columns:
            df_cleaned[col] = df_cleaned[col].astype("category")
    return df_cleaned

# Aqui definimos una función destinada a normalizar los nombres de las columnas para que sean más legibles.
# En estas funciones, siempre trabajaremos sobre una copia del df pasado por parámetro
def normalize_column_names(df):
    df_cleaned = df.copy()
    df_cleaned.columns = (
        df_cleaned.columns
        .str.lower()
        .str.strip()
        .str.replace(" ", "_")
        .str.replace('[^0-9a-zA-Z_]', '', regex=True)
    )
    return df_cleaned

def format_dates(df):
    df_cleaned = df.copy()
    # Lo siguiente que realizaremos será formatear las fechas de la columna "last review"
    if "last_review" in df_cleaned.columns:
        df_cleaned['last_review'] = pd.to_datetime(df_cleaned['last_review'], errors='coerce')
    return df_cleaned

def convert_numeric_types(df, int_cols=None, float_cols=None):
    df_cleaned = df.copy()

    # Columnas que deben ser enteros
    if int_cols:
        for col in int_cols:
            if col in df_cleaned.columns:
                df_cleaned[col] = pd.to_numeric(df_cleaned[col], errors="coerce").astype("Int64")

    # Columnas que deben ser float
    if float_cols:
        for col in float_cols:
            if col in df_cleaned.columns:
                df_cleaned[col] = pd.to_numeric(df_cleaned[col], errors="coerce")

    return df_cleaned