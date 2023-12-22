import pandas as pd
from typing import List  # No LeetCode funciona sem este import

"""
1 - Esta função recebe uma lista de listas de inteiros como argumento.
2 - Retorna um objeto DataFrame do pandas.
3 - Os rótulos das colunas do DataFrame são definidos como "Coluna 1" e "Coluna 2".
"""


def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    df = pd.DataFrame(student_data, columns=["student_id", "age"])

    return df


""""
Chama a função CreateDataframe enviando os dados diretamente pelo chamado
"""
dados_df = createDataframe(student_data=[[1, 15], [2, 11], [3, 11], [4, 20]])

print(dados_df)
