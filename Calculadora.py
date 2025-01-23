#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("************************Calculadora em Python************************")


# In[7]:


def add(x,y):
    return x + y


# In[8]:


def subtract(x,y):
    return x - y


# In[9]:


def multiply(x,y):
    return x * y


# In[10]:


def divide(x,y):
    return x / y


# In[11]:


print("\nSelecione a operação desejada:")
print("\n 1 - Soma \n 2 - Subtração \n 3 - Multiplicação \n 4 - Divisão")


# In[12]:


while True:
    try:
        opcao = int(input("\nDigite sua opção (1/2/3/4): "))
        break     
    except ValueError:
        print("\nVocê deve digitar apenas números!")


# In[13]:


while True:
    try:
        num1 = float(input("\nInforme o primeiro número: "))
        break
    except ValueError:
        print("\nVocê deve digitar apenas números!")


# In[14]:


while True:
    try:
        num2 = float(input("\nInforme o segundo número: "))
        break
    except ValueError:
        print("\nVocê deve digitar apenas números!")


# In[15]:


# Soma
if opcao == 1:
    print("\n")
    print(num1, "+", num2, "=", add(num1,num2))
    print("\n")
    
#Subtração   
elif opcao == 2:
    print("\n")
    print(num1, "-", num2, "=", subtract(num1,num2))
    print("\n")

#Multiplicação
elif opcao == 3: 
    print("\n")
    print(num1, "x", num2, "=", multiply(num1,num2))
    print("\n")
    
#Divisão
elif opcao == 4:
    print("\n")
    print(num1, "/", num2, "=", divide(num1,num2))
    print("\n")
else:
    print("\nOpção inválida!")


# In[ ]:




