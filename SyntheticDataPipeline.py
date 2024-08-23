# as pre-requisits, pip install pandas, numpy, faker and datetime
# Import the libraries
import pandas as pd
from faker import Faker
import numpy as np
from datetime import datetime

# instantiate Faker
faker = Faker()
def generate_data(num_records): # This function creates and populates a data frame of a given size with fields 'Name', 'Age', 'Email', 'Height' and 'Weight'
    data = {'Name': [], 'Age': [], 'Email': [], 'Height': [], 'Weight': []}
    for i in range(num_records):
        data['Name'].append(faker.name())
        data['Email'].append(faker.email())
        data['Age'].append(np.random.randint(18, 70))
        data['Height'].append(np.random.randint(150, 200))
        data['Weight'].append(np.random.randint(50, 100))
    return pd.DataFrame(data)


df = generate_data(2000)
processed_df = df[(df['Age'] > 20) & (df['Age'] < 50)] # Filterining the data based on a certain criteria
unique_timestamp = datetime.now().strftime('%Y%m%d%H%M%S')  
processed_df.to_csv(f'unique_timestamp_{unique_timestamp}.csv', index=False) # Creating a .csv file with filtered data
