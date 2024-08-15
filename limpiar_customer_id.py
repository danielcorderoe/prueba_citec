def limpiar_customer_id(df):
    """
    Esta función rellena los valores nulos en la columna 'CustomerID' con 1
    y convierte la columna a tipo entero.
    
    Parámetros:
    df (pd.DataFrame): El DataFrame que contiene la columna 'CustomerID'.
    
    Retorna:
    pd.DataFrame: El DataFrame con la columna 'CustomerID' limpiada.
    """
    df['CustomerID'] = df['CustomerID'].fillna(1)
    df['CustomerID'] = df['CustomerID'].astype(int)
    df['CustomerID'] = df['CustomerID'].astype(str)
    df.drop_duplicates()
    # Nombre del día, mes, año
    df['Dia']  = df['InvoiceDate'].dt.strftime('%A')
    df['MesN'] = df['InvoiceDate'].dt.month
    df['Mes']  = df['InvoiceDate'].dt.month_name()
    df['Año']  = df['InvoiceDate'].dt.year

    return df
