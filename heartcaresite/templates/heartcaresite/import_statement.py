import pandas as pd

# Load the XLS file
xls_file = 'your_statement.xls'
df = pd.read_excel(xls_file, header=None)  # No headers as it seems unstructured

# Extract transaction section based on known patterns
# Assuming the transactions start at a known row index (e.g., after 'lançamentos nacionais')
start_row = df[df[0].str.contains('lançamentos nacionais', na=False)].index[0] + 3
transaction_data = df.iloc[start_row:, [0, 1, 3]].dropna(how='all')

# Rename columns for easier processing
transaction_data.columns = ['Date', 'Description', 'Amount']

# Convert the amount to numeric (handling R$ symbols and formatting issues)
transaction_data['Amount'] = transaction_data['Amount'].replace({'R\$ ': '', ',': ''}, regex=True).astype(float)

# Parse the date into a proper datetime format
transaction_data['Date'] = pd.to_datetime(transaction_data['Date'], errors='coerce')

# Show the cleaned transaction data
print(transaction_data.head())
