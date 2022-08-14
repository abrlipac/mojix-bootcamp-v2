import streamlit as st

st.title("10 trucos geniales de Python para principiantes que te facilitarán la vida")

st.markdown('''
> Traducido por [@abrlipac](https://github.com/abrlipac)
> Artículo original: [10 Cool Beginner Python Tricks That Will Make Your Life Easier](https://levelup.gitconnected.com/10-cool-beginner-python-tricks-that-will-make-your-life-easier-6c68c909edf6)''')

st.header("1. Walrus operator")

st.markdown("El operador `Walrus` o `:=` es una de las últimas incorporaciones a Python 3.8. Es un operador de asignación que le permite asignar valor a una variable dentro de una expresión como declaraciones condicionales, bucles, etc.")

st.subheader("Ejemplo")

st.markdown("Si queremos verificar e imprimir la longitud de una lista:")

st.code('''
Mylist = [1,2,3]
if(l := len(mylist) > 2)
print(l)''')

st.subheader("Salida")

st.code('3')
