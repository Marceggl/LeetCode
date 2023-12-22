import pandas as pd
import numpy as np


# Função Leetcode
def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.head(3)


def main():
    # Criar um lista com valores aleatorios
    data = np.random.rand(6, 4)

    # Cabeçalho das colunas
    colunas = ["Col1", "Col2", "Col3", "Col4"]

    data_df = pd.DataFrame(data, columns=colunas)

    print(selectFirstRows(data_df))


if __name__ == "__main__":
    main()
