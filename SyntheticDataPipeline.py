# as pre-requisits, pip install pandas, numpy, faker and datetime

import pandas as pd
from faker import Faker
import numpy as np
from datetime import datetime

faker = Faker()
def generate_data(num_records):
    data = {'Name': [], 'Age': [], 'Email': [], 'Height': [], 'Weight': []}
    for i in range(num_records):
        data['Name'].append(faker.name())
        data['Email'].append(faker.email())
        data['Age'].append(np.random.randint(18, 70))
        data['Height'].append(np.random.randint(150, 200))
        data['Weight'].append(np.random.randint(50, 100))
    return pd.DataFrame(data)


df = generate_data(2000)
processed_df = df[(df['Age'] > 20) & (df['Age'] < 50)]
unique_timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
processed_df.to_csv(f'unique_timestamp_{unique_timestamp}.csv', index=False)
