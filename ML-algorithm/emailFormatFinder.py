import pandas as pd
!pip install pandas fuzzywuzzy
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

# Load the CSV dataset into a pandas DataFrame
dataset_path = '/content/drive/MyDrive/csv/sample-2.csv'
df = pd.read_csv(dataset_path)

def predict_name_and_domain(email):
    # Extract the domain from the email using regular expressions
    domain = email.split('@')[-1]

    # Remove the domain part from the email
    email_without_domain = email.replace('@' + domain, '')

    # Fuzzy match email_without_domain with DataFrame's email values
    matches = process.extract(email_without_domain, df['Email'], scorer=fuzz.ratio, limit=1)

    if matches:
        matched_email = matches[0][0]
        matched_row = df[df['Email'] == matched_email]
        first_name = matched_row['FirstName'].iloc[0]
        last_name = matched_row['LastName'].iloc[0]
        return first_name, last_name, domain
    else:
        return None, None, domain

# Example email to predict
# email_to_predict = 'patelkishankumar@forenzy.net'


# ... (previous code)

# Example email to predict
email_to_predict = 'patel2332kishankumar322@gmail.com'

# Predict the first name, last name, and domain
predicted_first_name, predicted_last_name, predicted_domain = predict_name_and_domain(email_to_predict)

if predicted_first_name and predicted_last_name:
    print("Email: ",str(email_to_predict))
    print(f'Predicted First Name: {predicted_first_name}')
    print(f'Predicted Last Name: {predicted_last_name}')
    print(f'Predicted Domain: {predicted_domain}')

    # Determine the position of the predicted first name and last name in the email
    first_name_position = email_to_predict.find(predicted_first_name.lower())
    last_name_position = email_to_predict.find(predicted_last_name.lower())

    if first_name_position < last_name_position:
        email_format = f'Email Format: {predicted_first_name.lower()}{predicted_last_name.lower()}@{predicted_domain}'
        print('{First name}{Last name}@{domain}')
    else:
        email_format = f'Email Format: {predicted_last_name.lower()}{predicted_first_name.lower()}@{predicted_domain}'
        print('{Last name}{First name}@{domain}')
    # print(email_format)
else:
    print(f'Could not predict name for domain: {predicted_domain}')
