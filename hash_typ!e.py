import hashlib
import pandas as pd
import openpyxl.utils

logo='''
╦ ╦┌─┐┌─┐┬ ┬╔╦╗┬ ┬┌─┐┬┌─┐
╠═╣├─┤└─┐├─┤ ║ └┬┘├─┘│├┤ 
╩ ╩┴ ┴└─┘┴ ┴ ╩  ┴ ┴  o└─┘
'''
print(logo)

def find_hash_type(hash_value):
    expected_lengths = {
        32: 'MD5',
        40: 'SHA1',
        64: 'SHA256',
        # Add more hash types and lengths as needed
    }

    hash_length = len(hash_value)
    if hash_length in expected_lengths:
        return expected_lengths[hash_length]
    else:
        return 'Unknown'

# Prompt the user to specify the path to the Excel file
excel_file_path = input("Enter the path to the Excel file: ")

# Read the Excel file into a pandas DataFrame
df = pd.read_excel(excel_file_path)
hashlib.algorithms_guaranteed
# Prompt the user to specify the column containing the hash values
hash_value_column = input("Enter the column letter containing the hash values: ")

# Convert column letter to column index
column_index = openpyxl.utils.column_index_from_string(hash_value_column) - 1

# Calculate and append the hash type column
hash_types = []
for index, row in df.iterrows():
    hash_value = row[column_index]
    hash_type = find_hash_type(hash_value)
    hash_types.append(hash_type)

df['Hash Type'] = hash_types

# Save the modified DataFrame back to the Excel file
df.to_excel(excel_file_path, index=False)