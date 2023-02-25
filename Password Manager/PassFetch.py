import pandas as pd
def save_pass(Password_data):
    old_pass = pd.read_csv('password.csv')
    if Password_data['Website'] not in old_pass['Website'].unique():
        new_pass = pd.DataFrame(Password_data)
        new_data = pd.concat([old_pass, new_pass], ignore_index=True)
        new_data.to_csv('password.csv', mode='w', index=False)
    else:
        site = Password_data['Website'][0]
        old_pass.loc[old_pass[old_pass['Website'] == site].index] = [Password_data['Website'][0], Password_data['Username'][0], Password_data['Password'][0]]
        old_pass.to_csv('password.csv', mode='w', index=False)

def fetch_pass(website):
    data = pd.read_csv('password.csv', index_col='Website')
    info = data.loc[website]
    return info