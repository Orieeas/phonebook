import requests

username = "user"
password = "user"

credentials = (username, password)

base_url = "http://localhost:8000"

new_contact_data = {
    "names": "Иванов Иван",
    "phone": "+123456789",
    "email": "ivanov@example.com"
}

create_contact_url = f"{base_url}/contacts/"
response = requests.post(create_contact_url, json=new_contact_data, auth=credentials)
response_data = response.json()
print(response_data)

contact_id = response_data["contact_id"]
get_contact_url = f"{base_url}/contacts/{contact_id}"
response = requests.get(get_contact_url, auth=credentials)
response_data = response.json()
print(response_data)


