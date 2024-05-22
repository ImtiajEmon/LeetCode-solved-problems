import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    return customers.drop_duplicates('email', keep = 'first')
    # OR
    # customers.drop_duplicates('email', keep = 'first', inplace = True)
    # return customers
