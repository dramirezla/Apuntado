import streamlit as st
from PIL import Image
import io
import pandas as pd
import random

cartas_clasicas=Image.open("az clasico.png")

imagen_capi = "OIG (2).jpg"
imagen3 = Image.open(imagen_capi)

interfaz_usuario = Image.open("capibara.png")


###################################

corazon_1 = Image.open("Cartas/corazon/1.png")
corazon_5 = Image.open("Cartas/corazon/5.png")
corazon_7 = Image.open("Cartas/corazon/7.png")
corazon_9 = Image.open("Cartas/corazon/9.png")
corazon_J = Image.open("Cartas/corazon/J.png")
corazon_K = Image.open("Cartas/corazon/K.png")
corazon_Q = Image.open("Cartas/corazon/Q.png")

diamante_1 = Image.open("Cartas/diamante/1.png")
diamante_2 = Image.open("Cartas/diamante/2.png")
diamante_3 = Image.open("Cartas/diamante/3.png")
diamante_4 = Image.open("Cartas/diamante/4.png")
diamante_5 = Image.open("Cartas/diamante/5.png")
diamante_6 = Image.open("Cartas/diamante/6.png")
diamante_A = Image.open("Cartas/diamante/A.png")

picas_7 = Image.open("Cartas/picas/7.png")
picas_8 = Image.open("Cartas/picas/8.png")
picas_9 = Image.open("Cartas/picas/9.png")
picas_10 = Image.open("Cartas/picas/10.png")
picas_J = Image.open("Cartas/picas/J.png")
picas_K = Image.open("Cartas/picas/K.png")
picas_Q = Image.open("Cartas/picas/Q.png")

trebol_2 = Image.open("Cartas/trebol/2.png")
trebol_4 = Image.open("Cartas/trebol/4.png")
trebol_6 = Image.open("Cartas/trebol/6.png")
trebol_8 = Image.open("Cartas/trebol/8.png")
trebol_A = Image.open("Cartas/trebol/A.png")
trebol_Q = Image.open("Cartas/trebol/Q.png")


def pagina_inicio():   
    st.title("🃏 ¡Bienvenido a Apuntado! 🎲")
    st.write("¡Prepárate para una emocionante experiencia de juego de cartas! Elige tu modo de juego y diseño de cartas.")
    modo_juego = st.selectbox("Selecciona el modo de juego",["Jugador vs jugador","Jugador vs bots"])
    if modo_juego == "Jugador vs jugador":
        num_jugadores = st.selectbox("¿Cuántos jugadores participarán?",[2,3,4,5])
    diseño_cartas = st.selectbox("🎨 Elige el diseño de las cartas",["Clasicas","Capibara"])

    colum1, colum2=st.columns(2)
    with colum1.expander("**🎲 Reglas del Juego**"):
        st.markdown("👉 ¡Descubre las reglas del juego [aquí](https://es.wikipedia.org/wiki/51_(juego_de_naipes))!")

    boton_inicio = colum2.button("**¡Comencemos el Juego!**")

    
    if boton_inicio:
        if modo_juego == "Jugador vs bots":
            st.write("🚨 **Error**: El modo de juego Jugador vs bots aún está en desarrollo.")
        else:
            st.write("🎉 ¡Configuración exitosa! Dirígete al lobby.")

    
    colum1.image(imagen3, caption="Capibara 🛸", use_column_width=False)
    colum2.image(cartas_clasicas, caption="Clasicas",use_column_width=False)


def pagina_lobby():
    try:
        df_cuentas = pd.read_csv("cuentas.csv")
    except (FileNotFoundError,pd.errors.EmptyDataError):
        df_cuentas = pd.DataFrame(
    columns=["Correo", "Primer Nombre", "Primer Apellido", "Contraseña", "Tokens"]
    )
        
    st.title("🎰 Lobby")
    st.write("🃏 Registra, inicia sesión, organiza apuestas y verifica los tokens de los jugadores. ¡Suerte en la mesa de juego!")
    st.write("Recuerda que para organizar apuestas deben haber por lo menos 2 cuentas inicializadas")
    opcion = st.selectbox("¿Qué acción deseas realizar?",["Registrar Jugador","Iniciar Sesión","Organizar Apuestas"])
    if opcion == "Registrar Jugador":
        st.markdown("<h1 📝>Registro de Jugador</h1>", unsafe_allow_html=True)
        formulario_registro = st.form
        with formulario_registro("Formulario de Registro 🎰"):
            st.subheader("¡Completa todos los campos para unirte a la mesa de juego!")

            cl1, cl2 = st.columns(2)
            numero_aleatorio = random.randint(0, 100000)
            p_nombre = cl1.text_input("Primer nombre")
            p_apellido = cl2.text_input("Primer apellido")
            correo = st.text_input("Correo electrónico")
            contra = cl1.text_input("Contraseña", type="password")
            confcontra = cl2.text_input("Confirmar Contraseña", type="password")
            acepta_politicas = st.checkbox(
        "Acepto las políticas de tratamiento de datos personales"
            )

            boton_registro = st.form_submit_button("¡Unirse al lobby!")
            politica_text = """
# Política de Tratamiento de Datos Personales

## 1. Introducción

Esta Política de Tratamiento de Datos Personales describe cómo Apuntado, en su calidad de proveedor de servicios de juego de azar, recopila, utiliza, almacena y protege la información personal que proporcionas a través de nuestra aplicación de juego. Esta Política se aplica a todos los usuarios de la Aplicación.

## 2. Información Personal que Recopilamos

Recopilamos información personal que tú proporcionas voluntariamente cuando utilizas la Aplicación de Apuntado. Esta información puede incluir, entre otros:

- Nombre y apellidos.
- Dirección de correo electrónico.
- Información de la cuenta, como nombre de usuario y contraseña.
- Número de cuenta.
- Tokens.

## 3. Uso de la Información Personal

Utilizamos la información personal que recopilamos para los siguientes propósitos:

- Facilitar la participación en juegos de azar y competiciones.
- Mejorar la experiencia del usuario en la Aplicación de Apuntado.
- Proteger la integridad y la seguridad de la Aplicación y de nuestros usuarios.
- Cumplir con las leyes y regulaciones aplicables en el ámbito de los juegos de azar.

## 4. Consentimiento

Al utilizar la Aplicación de Apuntado, aceptas y consientes el tratamiento de tu información personal de acuerdo con esta Política de Tratamiento de Datos Personales.

## 5. Compartir Información Personal

No compartimos tu información personal con terceros sin tu consentimiento, excepto en los siguientes casos:

- Proveedores de servicios: Podemos compartir tu información con terceros que nos brindan servicios esenciales para la operación de juegos de azar, como el procesamiento de pagos y la verificación de identidad.
- Cumplimiento legal: Podemos divulgar tu información personal si estamos obligados por ley o si creemos de buena fe que dicha divulgación es necesaria para cumplir con una obligación legal, proteger nuestros derechos, resolver disputas o garantizar la seguridad de nuestros usuarios.

## 6. Seguridad de Datos

Tomamos medidas razonables para proteger tu información personal contra pérdida, acceso no autorizado, divulgación, alteración o destrucción. Sin embargo, ten en cuenta que ninguna transmisión de datos en Internet o sistema de almacenamiento es completamente seguro.

## 7. Derechos del Titular de los Datos

Tienes derechos sobre tus datos personales, que incluyen:

- Acceder a tus datos personales.
- Corregir tus datos personales.

## 8. Cambios en la Política

Nos reservamos el derecho de actualizar o modificar esta Política en cualquier momento. Te notificaremos sobre los cambios a través de la Aplicación de Apuntado o por otros medios. El uso continuado de la Aplicación después de dichas modificaciones constituye tu aceptación de la Política revisada.

## 9. Contacto

Si tienes preguntas, inquietudes o solicitudes relacionadas con esta Política de Tratamiento de Datos Personales, contáctanos a través de dramirezla@unal.edu.co.

Fecha de entrada en vigor: Octubre 28 del 2023

"""

# Mostrar la política de tratamiento de datos personales en Markdown
            with st.expander("Ver Política de Tratamiento de Datos Personales"):
                st.markdown(politica_text)

        if boton_registro:
            if confcontra != contra:
                st.write(
            "<span style='color:red; font-weight:bold;'>¡Cuidado! Las contraseñas no coinciden.</span>",
            unsafe_allow_html=True,
        )
            
            elif correo == "" or p_nombre == "" or p_apellido == "" or contra == "":
                st.write(
            "<span style='color:red; font-weight:bold;'>¡Atención! Completa todos los campos.</span>",
            unsafe_allow_html=True,
        )
            elif correo.find("@") == -1:
                st.write(
            "<span style='color:red; font-weight:bold;'>¡Alerta! Ingresa una dirección de correo válida</span>",
            unsafe_allow_html=True,
        )
            elif not acepta_politicas:
                st.write(
            "<span style='color:red; font-weight:bold;'>¡Precaución! Acepta las políticas de tratamiento de datos.</span>",
            unsafe_allow_html=True,
        )
            elif len(contra) < 8:
                st.write(
            "<span style='color:red; font-weight:bold;'>¡Peligro! La contraseña debe tener al menos 8 caracteres.</span>",
            unsafe_allow_html=True,
        )
        
            elif correo in df_cuentas["Correo"].values:
                st.write(
            "<span style='color:red; font-weight:bold;'>¡Advertencia! El correo ya está registrado. Elige otro.</span>",
            unsafe_allow_html=True,
        )
            else:
            
                nueva_cuenta = pd.DataFrame(
            {
                "Correo": [correo],
                "Primer Nombre": [p_nombre],
                "Primer Apellido": [p_apellido],
                "Contraseña": [contra],
                "Tokens": [numero_aleatorio],
            }
        )
                df_cuentas = pd.concat([df_cuentas, nueva_cuenta], ignore_index=True)

                df_cuentas.to_csv("cuentas.csv", index=False)

                st.write("🎉 Jugador registrado exitosamente!")

    if opcion == "Iniciar Sesión":
        try:
            df_cuentas = pd.read_csv("cuentas.csv")
        except FileNotFoundError:
            df_cuentas = pd.DataFrame(columns=["Correo", "Contraseña","Tokens"])
        try:
            df_cuentas_iniciadas = pd.read_csv("cuentas_iniciadas.csv")
        except (FileNotFoundError,pd.errors.EmptyDataError):
            df_cuentas_iniciadas = pd.DataFrame(columns=["Primer Nombre","Tokens"])

        formulario_inicio_sesion = st.form
        with formulario_inicio_sesion("Formulario de Inicio de Sesión"):
            st.subheader("¡Ingresa a la lobby con tus credenciales!")

            correo = st.text_input("Correo electrónico")
            contra = st.text_input("Contraseña", type="password")

            boton_logearse = st.form_submit_button("Iniciar sesion")

            if correo == "" or contra == "":
                st.write(
            "<span style='color:red; font-weight:bold;'>¡Atención! Completa todos los campos.</span>",
            unsafe_allow_html=True,
        )
            elif (
                correo not in df_cuentas["Correo"].values
                or contra
                != df_cuentas.loc[df_cuentas["Correo"] == correo, "Contraseña"].values[0]
    ):
                st.write(
            "<span style='color:red; font-weight:bold;'>¡Error! Credenciales incorrectas. Verifica tu correo y contraseña.</span>",
            unsafe_allow_html=True,
        )
            else:
                st.write("🎉 Inicio de sesión exitoso!")
                nombre_usuario = df_cuentas.loc[
                    df_cuentas["Correo"] == correo, "Primer Nombre"
                    ].values[0]

                Tokens_usuario = df_cuentas.loc[
                    df_cuentas["Correo"] == correo, "Tokens"
                    ].values[0]
                cuenta_iniciada = pd.DataFrame(
            {
                "Primer Nombre": [nombre_usuario],
                "Tokens": [Tokens_usuario],
            }
        )
                df_cuentas_iniciadas = pd.concat([df_cuentas_iniciadas, cuenta_iniciada], ignore_index=True)

                df_cuentas_iniciadas.to_csv("cuentas_iniciadas.csv", index=False)

            if len(df_cuentas_iniciadas) >= 5:
                df_vacio = pd.DataFrame(columns=["Primer Nombre","Tokens"])
                df_vacio.to_csv("cuentas_iniciadas.csv", index=False)
            with st.sidebar:
                st.write(df_cuentas_iniciadas)

    if opcion == "Organizar Apuestas":
        try:
            df_cuentas_iniciadas = pd.read_csv("cuentas_iniciadas.csv")
        except (FileNotFoundError,pd.errors.EmptyDataError):
            df_cuentas_iniciadas = pd.DataFrame(columns=["Primer Nombre","Tokens"])
        with st.sidebar:
            st.write(df_cuentas_iniciadas)
        
        todos_apuestan = st.text_input("Indica la cantidad de tokens que apostarán todos los jugadores")
        boton_organizar = st.button("¡Verificar Apuestas!")
        if boton_organizar:
            if int(todos_apuestan) > min(df_cuentas_iniciadas["Tokens"]):
                st.write("🚨 ¡Alerta! No todos los jugadores tienen esa cantidad de tokens. Imposible organizar las apuestas así.")
            else:
                st.write("🎉 Apuestas verificadas con éxito. ¡Que empiece el juego!, continua a la interfaz de Juego")

def pagina_juego():
    st.title("🃏 Sala de Juego")
    st.image(interfaz_usuario, caption="Interfaz de juego", use_column_width=True)
    col1,col2,col3,col4,col5,col6,col7 = st.columns(7) 


    col1.image(corazon_1)
    col2.image(corazon_5)
    col3.image(corazon_7)
    col4.image(corazon_9)
    col5.image(corazon_J)
    col6.image(corazon_K)
    col7.image(corazon_Q)

    col1.image(diamante_1)
    col2.image(diamante_2)
    col3.image(diamante_3)
    col4.image(diamante_4)
    col5.image(diamante_5)
    col6.image(diamante_6)
    col7.image(diamante_A)

    col1.image(picas_7)
    col2.image(picas_8)
    col3.image(picas_9)
    col4.image(picas_10)
    col5.image(picas_J)
    col6.image(picas_K)
    col7.image(picas_Q)

    col1.image(trebol_2)
    col2.image(trebol_4)
    col3.image(trebol_6)
    col4.image(trebol_8)
    col5.image(trebol_A)
    col6.image(trebol_Q)

# Menú de navegación en la barra lateral
pagina_actual = st.sidebar.selectbox("Selecciona una Interfaz", ["Inicio", "Lobby", "Juego"])

# Mostrar la página correspondiente según la selección
if pagina_actual == "Inicio":
    pagina_inicio()
elif pagina_actual == "Lobby":
    pagina_lobby()
elif pagina_actual == "Juego":
    pagina_juego()
