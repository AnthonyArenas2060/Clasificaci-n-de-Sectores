import streamlit as st
import pandas as pd
import numpy as np

st.title("Clasificación de Sectores - Admetricks")

# 📂 Subir archivo
uploaded_file = st.file_uploader("Carga tu archivo Excel (.xlsx)", type=["xlsx"])

if uploaded_file is not None:
    # Leer el archivo
    data2 = pd.read_excel(uploaded_file, sheet_name=0)

    # Mostrar primeras filas
    st.subheader("Vista previa del archivo:")
    st.dataframe(data2.head())

    # Definir condiciones y resultados
    condiciones = [
        data2['Industria/Sector'].str.contains('transporte|viajes|turismo', case=False, na=False),
        data2['Industria/Sector'].str.contains('tiendas|restaurantes', case=False, na=False),
        data2['Industria/Sector'].str.contains('textil|vestimenta', case=False, na=False),
        data2['Industria/Sector'].str.contains('telecomunicaciones|internet|otros', case=False, na=False),
        data2['Industria/Sector'].str.contains('empresas|empresariales', case=False, na=False),
        data2['Industria/Sector'].str.contains('servicios&públicos|privados', case=False, na=False),
        data2['Industria/Sector'].str.contains('salud', case=False, na=False),
        data2['Industria/Sector'].str.contains('religión y esoterismo|chef', case=False, na=False),
        data2['Industria/Sector'].str.contains('objetos personales', case=False, na=False),
        data2['Industria/Sector'].str.contains('mascotas', case=False, na=False),
        data2['Industria/Sector'].str.contains('limpieza', case=False, na=False),
        data2['Industria/Sector'].str.contains('juegos y apuestas|eventos', case=False, na=False),
        data2['Industria/Sector'].str.contains('informática y equipos de oficina', case=False, na=False),
        data2['Industria/Sector'].str.contains('industrial, material de trabajo, agropecuario', case=False, na=False),
        data2['Industria/Sector'].str.contains('hogar', case=False, na=False),
        data2['Industria/Sector'].str.contains('finanzas', case=False, na=False),
        data2['Industria/Sector'].str.contains('energía', case=False, na=False),
        data2['Industria/Sector'].str.contains('educación y formación', case=False, na=False),
        data2['Industria/Sector'].str.contains('deportes y tiempo libre', case=False, na=False),
        data2['Industria/Sector'].str.contains('cultura', case=False, na=False),
        data2['Industria/Sector'].str.contains('construcción', case=False, na=False),
        data2['Industria/Sector'].str.contains('belleza e higiene', case=False, na=False),
        data2['Industria/Sector'].str.contains('bebidas', case=False, na=False),
        data2['Industria/Sector'].str.contains('automoción', case=False, na=False),
        data2['Industria/Sector'].str.contains('alimentación', case=False, na=False),
        data2['Industria/Sector'].str.contains('medios de comunicación', case=False, na=False)
    ]

    resultados = [
        'TURISMO',
        'COMERCIO',
        'ROPA/CALZADO/TELAS/TEJIDO',
        'TELECOMUNICACIONES',
        'GRUPOS EMPRESARIALES',
        'SERVICIOS SOCIALES/GOBIERNO',
        'SALUD/HIGIENE PERSONAL/COSMETICOS',
        'ARTE Y CULTURA',
        'OBJETOS PERSONALES/JUGUETES',
        'AGROPECUARIA/ANIMALES DOMESTICOS',
        'LIMPIEZA E HIGIENE DOMESTICA',
        'LOTERIAS Y JUEGOS DE AZAR',
        'EQUIPO/MATERIAL OFICINA/ESCUELA',
        'MAQUINAS/MATERIAS PRIMAS/REFACCIONES/ACCESORIOS INDUSTRIALES',
        'LIMPIEZA E HIGIENE DOMESTICA',
        'FINANCIERO Y SEGUROS',
        'MAQUINAS/MATERIAS PRIMAS/REFACCIONES/ACCESORIOS INDUSTRIALES',
        'EDUCACION Y MEDIOS DE COMUNICACION',
        'DEPORTES Y PASATIEMPOS',
        'ARTE Y CULTURA',
        'INDUSTRIA DE CONSTRUCCION',
        'SALUD/HIGIENE PERSONAL/COSMETICOS',
        'BEBIDAS',
        'AUTOMOTRIZ Y AFINES',
        'ALIMENTOS',
        'EDUCACION Y MEDIOS DE COMUNICACION'
    ]

    # Clasificación
    data2['Categoria'] = np.select(condiciones, resultados, default='Otros')

    st.success("✅ Clasificación completada")

    # Filtro interactivo
    categorias = sorted(data2['Categoria'].unique())
    categoria_sel = st.selectbox("Filtra por categoría:", options=["Todas"] + categorias)

    if categoria_sel != "Todas":
        df_filtrado = data2[data2['Categoria'] == categoria_sel]
    else:
        df_filtrado = data2

    st.subheader("Resultados Clasificados:")
    st.dataframe(df_filtrado)

    # Descargar resultados
    st.download_button(
        label="⬇️ Descargar resultados clasificados",
        data=df_filtrado.to_csv(index=False).encode('utf-8-sig'),
        file_name="sectores_clasificados.csv",
        mime="text/csv"
    )

else:
    st.info("👆 Carga un archivo Excel para comenzar.")
