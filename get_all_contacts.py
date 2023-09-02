import requests

def get_all_contacts():
    username = "user"
    password = "user"
    credentials = (username, password)
    url = "http://localhost:8000/contacts"
    response = requests.get(url, auth=credentials)

    if response.status_code == 200:
        contacts = response.json()
        for contact in contacts:
            print(f"ID: {contact['id']}")
            print(f"Names: {contact['names']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print("---")
    else:
        print("Ошибка при получении контактов")

get_all_contacts()