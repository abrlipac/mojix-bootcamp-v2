import streamlit as st

st.markdown('# 10 Cool Beginner Python Tricks')
st.markdown('from **Mojix Bootcamp** v2')

st.markdown('## 1. Walrus operator')

number1 = st.number_input('Enter a number')

list1 = range[1, number1]
l1 := len(list1)

st.markdown('### Code example')

st.markdown(f'''```python
list1 = range{list1}
print(l1 := len(list1))
print(l1)```''')

st.markdown('### Output')

# no se puede imprimir una expresión con este operador
st.markdown(f'''```
{l1}
{l1}```''')
