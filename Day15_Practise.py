# Task: Data Cleaning and Transformation
# Read the file messy_data (source: AlextheAnalyst)
# List the issues you notice in the dataset
# Hint: Look for missing data, inconsistent formats, special characters, or incorrect data types.
"""Cột CustomerID chuyển từ int => str
Cột Last_Name chứa giá trị  NaN => thay thế bằng giá trị Unknow
Cột Phone_Number chứa giá trị lộn xộn, N/a (thiếu từ đầu) => chỉnh lại chính tả và typos
Cột Address chứa giá trị N/a (thiếu từ đầu) => không cần sửa
Cột Paying Customer chứa giá trị lộn xộn, N/a, NaN  => chỉnh lại chính tả và xử lý row NaN
Cột Do_Not_Contact chứa giá trị lộn xộn  => chỉnh lại chính tả """

# Remove non-alphabetic characters from First_Name and Last_Name
# Example: If the name is /Alex.1, it should be converted to Alex.
# Hint: Use string methods like .str.replace() or regular expressions (regex) to remove unwanted characters.
df_messy['First_Name'] = df_messy['First_Name'].str.replace(r'[^a-zA-Z]', '', regex=True)
df_messy['Last_Name'] = df_messy['Last_Name'].str.replace(r'[^a-zA-Z]', '', regex=True)
df_messy['Last_Name'] = df_messy['Last_Name'].fillna('Unknow')

# Format phone numbers to the format nnn-nnn-nnnn
# Hint:
# For rows containing any non-numeric characters (such as letters), replace them with an empty string.
df_messy['Phone_Number'] = df_messy['Phone_Number'].str.replace(r'\D', '', regex=True)
df_messy['Phone_Number'] = df_messy['Phone_Number'].str.replace(r'(\d{3})(\d{3})(\d{4})', r'\1-\2-\3', regex=True)

# After cleaning the phone numbers, format them in the style nnn-nnn-nnnn (e.g., 123-178-3720)
# Create new columns Street_Address, State, and Zip_Code from the existing Street_Address column
# Example: 980 Paper Avenue, Pennsylvania, 18503 should be split as:
# Street_Address = '980 Paper Avenue'
# Zip_Code = 18503
# State = 'Pennsylvania'.  If any part is missing, assign None.
# Hint: Use .str.extract() with regex or .str.split() to separate the address into components.

# Standardize the Do_Not_Contact column to only have two values: Y or N
# Hint: You can use .map() or .replace() to convert any variations (e.g., yes, no, y, n) to a consistent format.

# Replace all (NaN,N/A, N/a,nan)values with Unknown
# Drop duplicate rows:
# Remove rows where all column values are identical, leaving only unique rows.
# Hint: Use .drop_duplicates() to perform this operation.
