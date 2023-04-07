import json
def save_pass(Password_data_list):
    try:
        with open('password.json') as passworddata:
            old_pass = json.load(passworddata)
    except:
        with open('password.json', 'w') as new_file:
            data_entries = {
                Password_data_list['Website'] : {
                'Username' : Password_data_list['Username'],
                'Password' : Password_data_list['Password'],
                },
            }
            json.dump(data_entries, new_file, indent=4)
    else:
        old_pass[Password_data_list['Website']] = {
            'Username' : Password_data_list['Username'],
            'Password' : Password_data_list['Password'],
        }
        with open('password.json', mode='w') as append_data:
            json.dump(old_pass, append_data, indent=4)

def fetch_pass(website):
    with open ('password.json') as master_data:
        all_data = json.load(master_data)
        if website in all_data.keys():
            info = all_data[website]
            return info
        else:
            raise FileNotFoundError()