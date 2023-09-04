<h1 align="center">Hi there, I'm <a href="Alex M" target="_blank">Alex</a> 
<img src="https://github.com/blackcater/blackcater/raw/main/images/Hi.gif" height="32"/></h1>
# Функции
В этом приложении реализованы функции для телефонной книги, приложение позволяет выполнять следующие запросы:
1.	/contacts с методом GET позволяет получить список всех контактов, 
2.	/contacts/{contact_id} с методом GET позволяет получить контакт по идентификатору
3.	/contacts с методом POST позволяет добавить новый контакт, 
4.	/contacts/{contact_id} с методом PUT позволяет обновить контакт по идентификатору 
5.	/contacts/{contact_id} с методом DELETE позволяет удалить контакт по идентификатору.
6.	/contacts_search с методом GET позволяет найти контакты по части названия
Написаны готовые запросы к каждому маршруту, все изменяемые переменные ограничены записями
SET YOUR VALUES
END SET YOUR VALUES
Например, чтобы воспользоваться поиском контактов, поменяйте QUERY на искомую часть имени в contacts_search.py и запустите скрипт
SET YOUR VALUES
QUERY = "SET_YOUR_NAME"
END SET YOUR VALUES
# Подробное описание
Полное описание оформленных запросов и переменных, доступных к изменению:
1.	Получить список всех контактов: get_all_contacts.py. Доступных изменяемых параметров нет.
На выходе будет выведен список всех контактов
2.	Добавить новый контакт и Получить контакт по идентификатору объединены в add_contact_and_get_one_contact.py 
Внесите свои данные в переменные 
NAMES = "Иванов Иван" – имя, фамилия;
PHONE = "+123456789" – номер телефона;
EMAIL = "ivanov@example.com" – электронная почта;
На выходе будет выведен id текущего контакта, а после этого отобразится информация о добавленном контакте по его id
3.	Смотри п.2
4.	Обновить контакт по идентификатору : update_contact.py
contact_id = 498576451 – id изменяемого контакта
NAMES = "Новое имя" – имя, фамилия
PHONE = "Новый телефон" – номер телефона
EMAIL = "Новый email" – электронная почта
На выходе будет выведена информация о полях обновленного контакта
5.	Удаление контакт по идентификатору: delete_contact.py 
contact_id = 498576451 – id удаляемого контакта
На выходе будет выведена информация об успешном удалении контакта
6.	Поиск контактов: contacts_search.py, поменяйте QUERY на искомую часть имени в contacts_search.py и запустите скрипт
QUERY = "SET_YOUR_NAME" – часть искомого имени
На выходе будет выведен список всех контактов, которые содержат часть указанного имени.

Запуск контейнера на другом компьютере
1.	Перенесите файлы проекта (main.py, database, Dockerfile,docker-compose.yml) на компьютер, на котором вы хотите развернуть контейнер.
2.	Убедитесь, что у вас установлен Docker и Docker Compose
3.	Откройте терминал или командную строку на этом компьютере и перейдите в директорию проекта.
4.	Выполните следующую команду для запуска контейнера с использованием Docker Compose:
docker-compose up -d --build

