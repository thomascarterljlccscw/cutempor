import numpy as np

# Sample data
data = {
    'UserID': ['user1', 'user2', 'user3', 'user4'],
    'Status': ['active', 'inactive', 'active', 'inactive']
}

df = pd.DataFrame(data)

# Key-value pairs for the condition
key_value_pairs = {'user1': 'active', 'user3': 'active'}

# Function to check condition
def check_condition(row):
    return row['UserID'] in key_value_pairs and row['Status'] == key_value_pairs[row['UserID']]

# Create new column based on condition using np.where
df['NewColumn'] = np.where(df.apply(check_condition, axis=1), '@' + df['UserID'], None)

print(df)
