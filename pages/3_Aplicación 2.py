import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def generar_grafico():
    # Generar datos
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    
    # Crear gráfico
    plt.figure(figsize=(8, 4))
    plt.plot(x, y)
    plt.title('Gráfico de Seno')
    plt.xlabel('X')
    plt.ylabel('Y')
    
    return plt

def main():
    st.title("Aplicación con Gráfico")
    
    # Generar el gráfico
    plt = generar_grafico()
    
    # Visualizar el gráfico en Streamlit
    st.pyplot(plt)

if __name__ == "__main__":
    main()

# Diseño personalizado
st.header("Aplicación 2")