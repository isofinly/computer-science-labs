import pandas as pd

with open('input.json', encoding='utf-8-sig') as f_input:
    df = pd.read_json(f_input)

df.to_csv('output4.csv', encoding='utf-16', sep='\t', index=False)