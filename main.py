import json

import pandas as pd

from src.id3 import build_decision_tree


def dict_to_json_file(file_path, d):
    with open(file_path, "w") as outfile:
        outfile.write(json.dumps(d, indent=4))


if __name__ == '__main__':
    df = pd.read_csv('data/drug200.csv')
    df = df.loc[:, ~df.columns.isin(['Na_to_K'])]
    tree = build_decision_tree(df, 'Drug')
    dict_to_json_file('out/id3-tree.json', tree)
    print(tree)
