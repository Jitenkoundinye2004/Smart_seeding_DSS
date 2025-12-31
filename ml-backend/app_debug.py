import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
try:
    csv_path = os.path.join(BASE_DIR, 'dataset', 'village_crop_yield_2000.csv')
    df = pd.read_csv(csv_path)
    with open('cols.txt', 'w') as f:
        for col in df.columns:
            f.write(col + '\n')
    print("Done")
except Exception as e:
    print(e)
