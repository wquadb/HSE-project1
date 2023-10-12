import os
from typing import List, Dict
import argparse

import pandas as pd


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
    for i in table:
        if i[1] not in result:
            result[i[1]] = 1
        else:
            result[i[1]] += 1
    return result

def sort_y_stats(main: dict, frm, to) -> dict:
    res = {}
    for i in main:
        if i in range(frm,to+1):
            res[i] = main[i]
    return res

def present(main: dict):
    print('{')
    for i in main:
        print(f'   {i}: {main[i]},') 
    print('}')
    return 0

def get_most_mentioned_artist(table: List[List[object]]) -> str:
    result = {}
    for i in table:
        if i[6] not in result:
            result[i[6]] = 1
        else:
            result[i[6]] += 1
    point = max(result.values())
    most_ment = []
    for i in result:
        if result[i] == point:
            most_ment.append(i)

    popular = []
    for i in table:
        if i[6] in most_ment:
            if i[7] not in popular:
                popular.append(i[7])
    return popular


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="our cute spotify experience")

    parser.add_argument("file_path", type=str, help="input path here")

    parser.add_argument("-m", "--most", action="store_true")

    parser.add_argument("-s", "--stats", type=int)

    args = parser.parse_args()

    table = open_file(args.file_path)

    os.system("clear")

    if args.stats:

        yearstart = args.stats
        
        data = sort_y_stats(get_y_stats(table=table), yearstart, 2023)
        
        present(data)

    if args.most:

        print("\nMost mentioned artist(-s):")
        
        print(get_most_mentioned_artist(table=table))

