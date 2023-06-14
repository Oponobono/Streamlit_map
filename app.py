import pandas as pd
import streamlit as st

# Título de la página
st.title("¡Bienvenido a mi página de presentación!")

# Información personal
st.write("¡Hola! Me llamo Cristian Marin, soy estudiante de Desarrollo de Software en último semestre y vivo en Bello.")

# Imagen personal
st.image("profile_pic.jpg", width=300)

# Sección de intereses
st.write("Me apasiona la tecnología y el desarrollo de software. Me gusta aprender nuevas habilidades y desafiar mi conocimiento existente.")

# Video de presentación
st.video("https://www.youtube.com/watch?v=JUxITamPWrY")

# Sección de contacto
st.write("¡No dudes en contactarme si quieres saber más sobre mí o tienes alguna oportunidad de trabajo interesante!")
st.write("Email: cristian.marinc@example.com")
st.write("LinkedIn: https://www.linkedin.com/in/cristianmarin/")

# Fondo de pantalla
st.markdown(
    """
    <style>
    .stApp {
        background-image: url('https://img.freepik.com/foto-gratis/fondo-cuadricula-digital-abstracto-negro_53876-97647.jpg?t=st=1682794040~exp=1682794640~hmac=870f06ff2e3d497aef71e9793f98dc3a76be27bd28d0a214745a3f98821b7519');
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True
)
