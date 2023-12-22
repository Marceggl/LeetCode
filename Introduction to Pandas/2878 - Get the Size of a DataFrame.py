import pandas as pd
import numpy as np
from typing import List


# Válida o DataFrame.shape
def getDataframeSize(players: pd.DataFrame) -> List[int]:
    return list(players.shape)  ### Converte o valor de tuple para Lista


def main():
    # Criar um DataFrame com valores aleatórios
    data = np.random.rand(10, 5)

    # Definir nomes de colunas
    colunas = ["Coluna1", "Coluna2", "Coluna3", "Coluna4", "Coluna5"]

    # Criar o DataFrame
    df = pd.DataFrame(data, columns=colunas)

    # Exibir o DataFrame
    print(getDataframeSize(df))


if __name__ == "__main__":
    main()
