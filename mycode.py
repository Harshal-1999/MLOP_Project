import pandas as pd
import os 

data = {'Name': ['Alice', 'Bob', 'sam'],
    'Age': [25, 30, 35],
    'city': ['pune', 'mumbai', 'nashik']
    }

df = pd.DataFrame(data)

data_dir = "data"
os.makedirs(data_dir, exist_ok=True)

file_path = os.path.join(data_dir, 'sample_data.csv')

df.to_csv(file_path, index=False)

print(f"CSV file save to {file_path}")