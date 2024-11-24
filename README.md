33.1. Итоговый проект по автоматизации тестирования (PJ-04)

Функциональное тестирование сайта http://rt.ru/
Тестирование страницы: Авторизация через пароль.

Тесты выполнены на VSCode.
Для работы требуется запуск venv

В папке src хранятся данные для тестов и фикстуры.
Для работы требуется ввести валидные данные пользователя в ./srs/settings.py

Тесты разбиты на блоки для каждого типа входа и имеется один общий. Нет разделения на негативные и позитивные.

!!!Некоторые тесты ожидаемо упадут. Такие тесты подписаны как известная ошибка!!!

test_all_auth.py    Сценарий полного тестирования аторизации с паролем.
                    
                    ДДля запуска ввести:    pytest ./test/test_all_auth.py

test_auth.py        Тестирование доступа к странице авторизации с главной RK и по прямой ссылке.
                    
                    Для запуска ввести:     pytest ./test/test_auth.py

test_email_auth.py  Тестирование типа аторизации почта + проль, автоматическая сменна типа авторизации с почта на другие типы.
                    Тестирование поля ввода на предупреждение о неверном формате Электронной почты.
                    
                    Для запуска ввести:     pytest ./test/test_email_auth.py

test_login_auth.py  Тестирование типа аторизации логин + проль, автоматическая сменна типа авторизации с логин на другие типы.
                    
                    Для запуска ввести:     pytest ./test/test_login_auth.py

test_ls_auth.py     Тестирование типа аторизации лс + проль, автоматическая сменна типа авторизации с лс на другие типы.
                    Тестирование поля ввода на предупреждения о неверном формате ЛС
                    
                    Для запуска ввести:     pytest ./test/test_ls_auth.py

test_phone_auth.py  Тестирование типа аторизации лс + проль, автоматическая сменна типа авторизации с телефон на другие типы.
                    Тестирование поля ввода на предупреждения о неверном формате Номера
                    
                    Для запуска ввести:     pytest ./test/test_phone_auth.py