import streamlit as st

st.markdown('''<style>
#10-trucos-geniales-de-python-para-principiantes-que-te-facilitar-n-la-vida {
  display: inline-block;
  outline: none;
  cursor: pointer;
  font-size: 16px;
  line-height: 20px;
  font-weight: 600;
  border-radius: 8px;
  padding: 14px 24px;
  border: none;
  transition: box-shadow 0.2s ease 0s, -ms-transform 0.1s ease 0s, -webkit-transform 0.1s ease 0s, transform 0.1s ease 0s;
  background: linear-gradient(to right, rgb(230, 30, 77) 0%, rgb(227, 28, 95) 50%, rgb(215, 4, 102) 100%);
  color: #fff;
}
</style>''', unsafe_allow_html=True)

st.title("10 trucos geniales de Python para principiantes que te facilitarán la vida")

st.markdown('''
> Traducido por Abraham Lipa Calabilla ([@abrlipac](https://github.com/abrlipac)) para el **Mojix Bootcamp v2**

> Artículo original: [10 Cool Beginner Python Tricks That Will Make Your Life Easier](https://levelup.gitconnected.com/10-cool-beginner-python-tricks-that-will-make-your-life-easier-6c68c909edf6)''')

st.header("Indice")

st.markdown('''
1. [Operador Walrus](#1-operador-walrus)
2. [Dividir una cadena](#2-dividir-una-cadena)
3. [Revertir una cadena](#3-revertir-una-cadena)
4. [Fusionando dos diccionarios](#4-fusionando-dos-diccionarios)
5. [La función zip()](#5-la-funci-n-zip)
6. [Asignación de múltiples valores de lista a una variable](#6-asignaci-n-de-m-ltiples-valores-de-lista-a-una-variable)
7. [Eliminar elementos de la lista duplicada](#7-eliminar-elementos-de-la-lista-duplicada)
8. [Función lambda](#8-funci-n-lambda)
9. [Intercambio de valor de variable](#9-intercambio-de-valor-de-variable)
10. [Use una contraseña en su código](#10-use-una-contrase-a-en-su-c-digo)''')

st.header("1. Operador Walrus")

st.markdown("El operador `Walrus` o `:=` es una de las últimas incorporaciones a Python 3.8. Es un operador de asignación que le permite asignar valor a una variable dentro de una expresión como declaraciones condicionales, bucles, etc.")

st.subheader("Ejemplo")

st.markdown("Si queremos verificar e imprimir la longitud de una lista:")

st.code('''
Mylist = [1,2,3]
if(l := len(mylist) > 2)
  print(l)''')

st.subheader("Salida")

st.code('3')

st.markdown("[Subir 🔝](#10-trucos-geniales-de-python-para-principiantes-que-te-facilitar-n-la-vida)")

st.header("2. Dividir una cadena")

st.markdown("Si desea dividir los componentes de una cadena en una lista, puede hacerlo fácilmente utilizando la función `split()` en Python. ¡Esto facilitará las operaciones de cadenas!")

st.subheader("Ejemplo")

st.code('''
string = "hello world"
string.split()''')

st.subheader("Salida")

st.code("['hello', 'world']")

st.header("3. Revertir una cadena")

st.markdown("Si desea revertir una cadena dada, puede hacerlo con solo una línea de código utilizando la indexación negativa de la cadena.")

st.subheader("Ejemplo")

st.code('''
str="hello world!"
a=str[::-1]
print(a)''')

st.subheader("Salida")

st.code("!dlrow olleh")

st.header("4. Fusionando dos diccionarios")

st.markdown("Este increíble truco te ayudará a fusionar dos diccionarios con solo 1 línea de código. Solo necesitamos usar `**` frente al nombre de los dos diccionarios para fusionarlos en un solo diccionario:")

st.subheader("Ejemplo")

st.code('''
d1 = {"a": 10, "b":20}
d2 = {"c": 30, "d":40}
d3 = {**d1, **d2}
print(d3)''')

st.subheader("Salida")

st.code("{'a': 10, 'b': 20, 'c': 30, 'd': 40}")

st.header("5. La función zip()")

st.markdown("La función `zip()` en Python puede hacer que su vida sea mucho más fácil cuando se trabaja con listas y diccionarios. Se utiliza para combinar varias listas de la misma longitud.")

st.subheader("Ejemplo 1")

st.code('''
colour = ["red", "yellow", "green"]
fruits = ['apple', 'banana', 'mango']
for colour, fruits in zip(colour, fruits):
  print(colour, fruits)''')

st.subheader("Salida 1")

st.code('''
red apple
yellow banana
green mango''')

st.markdown("La función `zip()` también se puede usar para combinar dos listas en un diccionario. Este método puede ser realmente útil al agrupar los datos de la lista.")

st.subheader("Ejemplo 2")

st.code('''
students = ["Rajesh", "kumar", "Kriti"]
marks = [87, 90, 88]
dictionary = dict(zip(students, marks))
print(dictionary)''')

st.subheader("Salida 2")

st.code("{'Rajesh': 87, 'kumar': 90, 'Kriti': 88}")

st.header("6. Asignación de múltiples valores de lista a una variable")

st.markdown("Si desea asignar algunos valores específicos de una lista a una variable y todos los valores restantes a otra variable en un formato de lista, puede usar la siguiente técnica:")

st.subheader("Ejemplo")

st.code('''
mylist = [1,2,3,4,5]
a,*b = mylist
print(f"a =",a)
print(f"b =",b)''')

st.subheader("Salida")

st.code('''
a = 1
b = [2, 3, 4, 5]''')

st.markdown("Este proceso también se llama desempaquetado de la lista y puede aplicar este método para más de 2 variables también.")

st.header("7. Eliminar elementos de la lista duplicada")

st.markdown("¿Tiene elementos duplicados en su lista que desea eliminar? Puede hacerlo con solo una línea de código utilizando la función `set()`.")

st.subheader("Ejemplo")

st.code('''
mylist = [1,1,1,2,2,3,3,4,4,5,6,7,7,8,9]
newlist = set(mylist)
print(newlist)''')

st.subheader("Salida")

st.code("{1, 2, 3, 4, 5, 6, 7, 8, 9}")

st.header("8. Función lambda")

st.markdown("Si necesita una función que no sea muy complicada, se puede hacer fácilmente en una línea usando **lambda**. También se llaman funciones anónimas y se utilizan en gran medida en ciencia de datos y desarrollo web.")

st.subheader("Ejemplo")

st.markdown("Supongamos que desea escribir una función para multiplicar dos números.En lugar de escribir una función convencional, puede hacerlo en una línea usando:")

st.code('''
mul = lambda a,b: a*b
mul(5,6)''')

st.subheader("Salida")

st.code("30")

st.header("9. Intercambio de valor de variable")

st.markdown("Uno de los primeros programas que aprendemos mientras aprende sobre variables es intercambiar los valores de dos variables. En Python puedes lograrlo con una línea de código:")

st.subheader("Ejemplo")

st.code('''
a = 100
b = 200
a,b = b,a
print(f'a = ',a)
print(f'b = ',b)''')
  
st.subheader("Salida")

st.code('''
a = 200
b = 100''')

st.header("10. Use una contraseña en su código")

st.markdown("Este truco de Python es sorprendente para asegurar su código con una contraseña. Usaremos la función `getpass()` de la biblioteca `getpass` que codifica su entrada. Esto evitará que cualquiera ejecute el código sin contraseña. ¿No es genial?")

st.subheader("Ejemplo")

st.code('''
from getpass import getpass

password = getpass("password: ")

if password == "abcd":
  print("welcome strnger!")
else:
  print("wrong password")''')

st.subheader("Salida")

st.code('''
password: **** [abcd]
Welcome stranger!
Password: **** [abdc]
Wrong password''')

st.markdown('''
> No olvides ver el artículo original: [10 Cool Beginner Python Tricks That Will Make Your Life Easier](https://levelup.gitconnected.com/10-cool-beginner-python-tricks-that-will-make-your-life-easier-6c68c909edf6)''')