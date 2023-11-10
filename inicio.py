import streamlit as st
from PIL import Image
import io
import pandas as pd

imagen_ironman = "OIG.jpg"
imagen1 = Image.open(imagen_ironman)

imagen_picka = "OIG (1).jpg"
imagen2 = Image.open(imagen_picka)

imagen_capi = "OIG (2).jpg"
imagen3 = Image.open(imagen_capi)

def pagina_inicio():
    
    st.title("Interfaz de Inicio de Apuntado")
    st.write("¡Bienvenido a la página de inicio! donde puedes seleccionar el modo de juego que desees ya sea si quieres jugar con bots o con otros jugadores")
    modo_juego = st.selectbox("Selecciona el modo de juego que deseas",["Jugador vs jugador","Jugador vs bots"])
    if modo_juego == "Jugador vs jugador":
        num_jugadores = st.selectbox("Seleccione la cantidad de jugadores que van a participar del juego",[2,3,4,5])
    diseño_cartas = st.selectbox("Selecciona el diseño de cartas que deseas **usar**",["Pickachu","Ironman","Capibara"])

    colum1, colum2=st.columns(2)
    with colum1.expander("**Ayuda a usuario** (reglas de juego)"):
        st.markdown("https://es.wikipedia.org/wiki/51_(juego_de_naipes)")
    
    boton_inicio = colum2.button("**Iniciar**")
    col1,col2,col3=st.columns(3)
    col1.image(imagen2, caption="Pickachu", use_column_width=False)
    col2.image(imagen1, caption="Ironman", use_column_width=False)
    col3.image(imagen3, caption="Capibara", use_column_width=False)
    
    if boton_inicio:
        if modo_juego == "Jugador vs bots":
            st.write("Error: Esta opcion aun no hay sido desarrrollada")
        else:
            st.write("El juego ha sido configurado con exito, por favor avance a la interfaz de lobby")


def pagina_lobby():
    st.title("Interfaz de lobby")
    st.write("Aqui puedes iniciar sesion, registrar jugadores, organizar apuestas y ver tokens disponibles")
    st.selectbox("Que deseas hacer?",["Registrar jugadores","Iniciar sesion","Organizar apuestas"])


def pagina_juego():
    st.title("Página de Visualización")
    st.write("Mira tus datos aquí.")

# Crear un menú de navegación en la barra lateral
pagina_actual = st.sidebar.selectbox("Selecciona una Interfaz", ["Inicio", "Lobby", "Juego"])

# Mostrar la página correspondiente según la selección
if pagina_actual == "Inicio":
    pagina_inicio()
elif pagina_actual == "Lobby":
    pagina_lobby()
elif pagina_actual == "Juego":
    pagina_juego()
