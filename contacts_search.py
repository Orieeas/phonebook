import requests

# SET YOUR VALUES
QUERY = "SET_YOUR_NAME"
# END SET YOUR VALUES

def get_all_contacts():
    username = "user"
    password = "user"
    credentials = (username, password)
    url = "http://localhost:8000/contacts_search"
    response = requests.get(url, params={"query": QUERY}, auth=credentials)
    if response.status_code == 200:
        contacts = response.json()
        print(contacts)
        for contact in contacts:
            print(f"ID: {contact['id']}")
            print(f"Names: {contact['names']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print("---")
    else:
        print(response.json())


get_all_contacts()