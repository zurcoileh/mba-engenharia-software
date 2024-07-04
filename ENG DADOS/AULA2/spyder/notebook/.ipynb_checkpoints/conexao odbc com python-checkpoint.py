# -*- coding: utf-8 -*-
"""
Aula 2

Sequências de passos para conexão com Database Local MySql.
"""

# =============================================================================
# 1 - Pacotes
# =============================================================================
# 1.1 - Instala
# !pip install mysql-connector-python
# !pip install pandas

# 1.2 - Importa
import mysql.connector
import pandas as pd


# =============================================================================
# 2 - Realiza conexão
# =============================================================================
config = {
    'user': 'root',
    'password': 'admin',
    'host': 'localhost',
    'database': 'sakila',
    'raise_on_warnings': True
}

try:
    conn = mysql.connector.connect(**config)
    if conn.is_connected():
        print('Conectado ao MySQL com sucesso!')
except mysql.connector.Error as err:
    print(f"Erro: {err}")
    
    
# =============================================================================
# 3 - Query em Dataframe
# =============================================================================
# Criação do cursor
cursor = conn.cursor()

# Escrevendo a query
query = "SELECT * FROM sakila.actor;"

# Executando a query
cursor.execute(query)

# Obtendo os resultados
resultados = cursor.fetchall()

 # Obtendo os nomes das colunas
colunas = cursor.column_names

# Transformando os resultados em um DataFrame do Pandas
df = pd.DataFrame(resultados, columns=colunas)

# =============================================================================
# =============================================================================
