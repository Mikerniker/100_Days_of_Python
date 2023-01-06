import requests

print("Welcome to Mik's Flight Club! \nWe find the best flight deals and email you.")
first_name = input("What is your first name?: ").capitalize()
last_name = input("What is your last name?: ").capitalize()
email1 = input("What is your email? ")
email2 = input("Type your email again. ")
if email1 == email2:
    print(f"Success! Thank you {first_name} {last_name} Your email {email1} has been added, you're in the club!")
else:
    print("Your emails don't match. Please try again.")

SHEETY_ENDPOINT = "https://api.sheety.co/******************"
SHEETY_API = "**********************************"

sheety_table = requests.get(SHEETY_ENDPOINT)

sheety_table.raise_for_status()
sheet_data = sheety_table.json()
print(sheet_data)


user_information = {
    "user": {
        "firstName": first_name,
        "lastName": last_name,
        "email": email1
}
}

headers = {"apikey": SHEETY_API}

# Put customer data in sheety
edit_sheety_row = requests.post(url=SHEETY_ENDPOINT, json=user_information, headers=headers)
print(edit_sheety_row.text)

# Get customer email from sheety

def get_customer_email():
    customer_data = requests.get(SHEETY_ENDPOINT)

    customer_data.raise_for_status()
    customer_information = customer_data.json()['users']

    return customer_information