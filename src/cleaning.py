import pandas as pd

# Limpia columnas monetarias eliminando símbolos y convirtiendo a numérico
def clean_monetary_columns(df, monetary_columns):
    df_cleaned = df.copy()
    
    for col in monetary_columns:
        if col in df_cleaned.columns:
            df_cleaned[col] = (
                df_cleaned[col].astype(str)  # Asegura formato string
                .str.replace(r'[^0-9\.\-]', '', regex=True)  # Mantiene solo números, puntos y signos
                .str.strip()
            )
            df_cleaned[col] = pd.to_numeric(df_cleaned[col], errors="coerce")  # Convierte a numérico
    return df_cleaned


# Limpia y normaliza valores categóricos específicos
def clean_categorical_values(df):
    df_cleaned = df.copy()

    # Estándar en nombres de grupos de barrio
    if "neighbourhood_group" in df_cleaned.columns:
        df_cleaned["neighbourhood_group"] = df_cleaned["neighbourhood_group"].replace({
            "brookln": "Brooklyn",
            "manhatan": "Manhattan"
        }).fillna("Unknown")

    # Unifica el valor de verificación del anfitrión
    if "host_identity_verified" in df_cleaned.columns:
        df_cleaned["host_identity_verified"] = df_cleaned["host_identity_verified"].replace({
            "verified": "confirmed"
        }).fillna("Unknown")

    # Mantiene solo el nombre principal del barrio si viene con coma
    df_cleaned["neighbourhood"] = (
        df_cleaned["neighbourhood"].astype(str)
        .str.split(",", n=1).str[0].str.strip()
    )

    # Convierte valores texto a booleano
    if "instant_bookable" in df_cleaned.columns:
        df_cleaned["instant_bookable"] = df_cleaned["instant_bookable"].replace({
            "False": False,
            "True": True
        }).astype("boolean")

    # Convierte varias columnas a categoría (optimiza y normaliza)
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


# Normaliza nombres de columnas para consistencia
def normalize_column_names(df):
    df_cleaned = df.copy()
    df_cleaned.columns = (
        df_cleaned.columns.str.lower()     # Minúsculas
        .str.strip()                       # Sin espacios externos
        .str.replace(" ", "_")             # Reemplazo por guiones bajos
        .str.replace('[^0-9a-zA-Z_]', '', regex=True)  # Elimina caracteres especiales
    )
    return df_cleaned


# Convierte "last_review" en formato fecha
def format_dates(df):
    df_cleaned = df.copy()
    if "last_review" in df_cleaned.columns:
        df_cleaned["last_review"] = pd.to_datetime(df_cleaned["last_review"], errors="coerce")
    return df_cleaned


# Convierte columnas a tipo entero o flotante según indicación
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