# -*- coding: utf-8 -*-
#pip install streamlit

import streamlit as st

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def main():
    st.title("🎸 Calculadora Simple V0 🚀")

    operacion = st.selectbox("Selecciona una operación:", ["Adición", "Sustración"])

    #num1 = st.number_input("Ingresa el primer número:")
    #num2 = st.number_input("Ingresa el segundo número:")    
    num1 = st.number_input("Ingresa el 1️⃣ número:", value=0, step=1, format="%d")
    num2 = st.number_input("Ingresa el 2️⃣ número:", value=0, step=1, format="%d")

    num1 = int(num1)
    num2 = int(num2)
    
    resultado = 0
    
    if operacion == "Adición":
        resultado = sumar(num1, num2)
    elif operacion == "Sustracción":
        resultado = restar(num1, num2)

    #st.write("Resultado:", resultado)
    st.write("### **Resultado:**", f"**{resultado}** :sunglasses:", unsafe_allow_html=True)


    genre = st.radio(
    "What\'s your favorite movie genre",
    ('Comedy', 'Drama', 'Documentary'))

    if genre == 'Comedy':
        st.write('You selected comedy.')
    else:
        st.write("You didn\'t select comedy.")

if __name__ == "__main__":
    main()
