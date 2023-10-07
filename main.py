import pandas as pd
import argparse
from typing import List, Dict

def open_file(path:str) -> list[list[object]]:
    df = pd.read_csv(path)
    return df.values.tolist()

def get_y_stats(table: list[list[object]]) -> dict:
    """returns
    {
        '2010': 123,
        '2011': 150,
        .....
        '2022': 300,
    }
    """
    result = {}
    b = 2010
    for i in table:
        if i[1] not in result:
            result[i[1]] = 1
        else:
            result[i[1]] += 1
    return result

def get_most_mentioned_artist(table: List[List[object]]) -> str:
    
    return


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="our cute spotify experience")

    parser.add_argument("file_path", type=str, help="input path here")

    args = parser.parse_args()

    table = open_file(args.file_path)

    print(get_y_stats(table=table))


