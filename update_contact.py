import requests

# SET YOUR VALUES
contact_id = 498576451
NAMES = "Новое имя"
PHONE = "Новый телефон"
EMAIL = "Новый email"
# END SET YOUR VALUES

username = "user"
password = "user"
credentials = (username, password)
base_url = "http://localhost:8000"
new_contact_data = {
    "names": str(NAMES),
    "phone": str(PHONE),
    "email": str(EMAIL)
}
update_contact_url = f"{base_url}/contacts/{contact_id}"
response = requests.put(update_contact_url, json=new_contact_data, auth=credentials)

if response.status_code == 200:
    updated_contact = response.json()
    print("Контакт успешно обновлен:")
    print("ID:", updated_contact["id"])
    print("Имя:", updated_contact["names"])
    print("Телефон:", updated_contact["phone"])
    print("Email:", updated_contact["email"])
else:
    print("Ошибка при обновлении контакта:", response.text)
