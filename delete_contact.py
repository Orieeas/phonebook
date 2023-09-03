import requests

# SET YOUR VALUES
contact_id = 498576451
# END SET YOUR VALUES

username = "user"
password = "user"

credentials = (username, password)
base_url = "http://localhost:8000"
delete_contact_url = f"{base_url}/contacts/{contact_id}"
response = requests.delete(delete_contact_url, auth=credentials)
if response.status_code == 200:
    print("Контакт успешно удален")
else:
    print("Ошибка при удалении контакта:", response.text)

