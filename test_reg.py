from selenium.webdriver.common.by import By
from config import *
import time


def test_reg_positive(web_browser):
    # 11 + регистрация по емейлу
    web_browser.implicitly_wait(3)
    web_browser.get(url_auth)
    # переход на страницу регистрации
    btn_reg = web_browser.find_element(By.XPATH, '//*[@id="kc-register"]')
    btn_reg.click()
    # ввод имени
    time.sleep(1)
    field_name = web_browser.find_element(By.NAME, 'firstName')
    field_name.send_keys(valid_name)
    # ввод фамилии
    time.sleep(1)
    field_lastname = web_browser.find_element(By.NAME, "lastName")
    field_lastname.send_keys(valid_lastname)
    # ввод почты
    time.sleep(1)
    field_lastname = web_browser.find_element(By.ID, "address")
    field_lastname.send_keys(valid_reg_mail)
    # ввод пароля
    time.sleep(1)
    field_pass = web_browser.find_element(By.ID, "password")
    field_pass.send_keys(valid_pass)
    # подтверждение пароля
    time.sleep(1)
    field_pass_confirm = web_browser.find_element(By.ID, "password-confirm")
    field_pass_confirm.send_keys(valid_pass)
    # клик на кнопку "зарегистрироваться"
    time.sleep(1)
    btn_reg = web_browser.find_element(By.NAME, 'register')
    btn_reg.click()
    time.sleep(2)
    # проверка входа в личный кабинет
    assert web_browser.find_element(By.XPATH, '// *[ @ id = "page-right"] / div[1] / div[1] / h1[1]').text == \
           'Подтверждение email'


def test_reg_short_name(web_browser):
    # 12 - регистрация - короткое имя
    web_browser.implicitly_wait(3)
    web_browser.get(url_auth)
    # переход на страницу регистрации
    btn_reg = web_browser.find_element(By.XPATH, '//*[@id="kc-register"]')
    btn_reg.click()
    # ввод короткого имени
    field_name = web_browser.find_element(By.NAME, 'firstName')
    field_name.send_keys(short_name)
    # ввод фамилии
    field_lastname = web_browser.find_element(By.NAME, "lastName")
    field_lastname.send_keys(valid_lastname)
    # ввод почты
    field_lastname = web_browser.find_element(By.ID, "address")
    field_lastname.send_keys(valid_reg_mail)
    # ввод пароля
    field_pass = web_browser.find_element(By.ID, "password")
    field_pass.send_keys(valid_pass)
    # подтверждение пароля
    field_pass_confirm = web_browser.find_element(By.ID, "password-confirm")
    field_pass_confirm.send_keys(valid_pass)
    # клик на кнопку "зарегистрироваться"
    btn_reg = web_browser.find_element(By.NAME, 'register')
    btn_reg.click()
    time.sleep(2)
    # сообщение о требуемом формате данных
    assert web_browser.find_element(By.XPATH,
                                    '/html/body/div[1]/main/section[2]/div/div/div/form/div[1]/div[1]/span').text == \
           'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'


def test_reg_long_name(web_browser):
    # 13 - регистрация - длинное имя
    web_browser.implicitly_wait(3)
    web_browser.get(url_auth)
    # переход на страницу регистрации
    btn_reg = web_browser.find_element(By.XPATH, '//*[@id="kc-register"]')
    btn_reg.click()
    # ввод короткого имени
    field_name = web_browser.find_element(By.NAME, 'firstName')
    field_name.send_keys(long_name)
    # ввод фамилии
    field_lastname = web_browser.find_element(By.NAME, "lastName")
    field_lastname.send_keys(valid_lastname)
    # ввод почты
    field_lastname = web_browser.find_element(By.ID, "address")
    field_lastname.send_keys(valid_reg_mail)
    # ввод пароля
    field_pass = web_browser.find_element(By.ID, "password")
    field_pass.send_keys(valid_pass)
    # подтверждение пароля
    field_pass_confirm = web_browser.find_element(By.ID, "password-confirm")
    field_pass_confirm.send_keys(valid_pass)
    # клик на кнопку "зарегистрироваться"
    btn_reg = web_browser.find_element(By.NAME, 'register')
    btn_reg.click()
    time.sleep(2)
    # сообщение о требуемом формате данных
    assert web_browser.find_element(By.XPATH,
                                    '/html/body/div[1]/main/section[2]/div/div/div/form/div[1]/div[1]/span').text == \
           'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'


def test_reg_latin_lastname(web_browser):
    # 14 - регистрация фамилия - английский алфавит
    web_browser.implicitly_wait(3)
    web_browser.get(url_auth)
    # переход на страницу регистрации
    btn_reg = web_browser.find_element(By.XPATH, '//*[@id="kc-register"]')
    btn_reg.click()
    # ввод имени
    time.sleep(1)
    field_name = web_browser.find_element(By.NAME, 'firstName')
    field_name.send_keys(valid_name)
    # ввод фамилии на английском
    time.sleep(1)
    field_lastname = web_browser.find_element(By.NAME, "lastName")
    field_lastname.send_keys(latin_lastname)
    # ввод почты
    time.sleep(1)
    field_lastname = web_browser.find_element(By.ID, "address")
    field_lastname.send_keys(valid_reg_mail)
    # ввод пароля
    time.sleep(1)
    field_pass = web_browser.find_element(By.ID, "password")
    field_pass.send_keys(valid_pass)
    # подтверждение пароля
    time.sleep(1)
    field_pass_confirm = web_browser.find_element(By.ID, "password-confirm")
    field_pass_confirm.send_keys(valid_pass)
    # клик на кнопку "зарегистрироваться"
    time.sleep(1)
    btn_reg = web_browser.find_element(By.NAME, 'register')
    btn_reg.click()
    time.sleep(1)
    # сообщение о требуемом формате данных
    assert web_browser.find_element(By.XPATH,
                                    '/html/body/div[1]/main/section[2]/div/div/div/form/div[1]/div[2]/span').text == \
           'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'


def test_reg_short_pass(web_browser):
    # 15 - регистрация короткий пароль
    web_browser.implicitly_wait(3)
    web_browser.get(url_auth)
    # переход на страницу регистрации
    btn_reg = web_browser.find_element(By.XPATH, '//*[@id="kc-register"]')
    btn_reg.click()
    # ввод имени
    field_name = web_browser.find_element(By.NAME, 'firstName')
    field_name.send_keys(valid_name)
    # ввод фамилии
    field_lastname = web_browser.find_element(By.NAME, "lastName")
    field_lastname.send_keys(valid_lastname)
    # ввод почты
    field_lastname = web_browser.find_element(By.ID, "address")
    field_lastname.send_keys(valid_reg_mail)
    # ввод пароля
    field_pass = web_browser.find_element(By.ID, "password")
    field_pass.send_keys(short_pass)
    # подтверждение пароля
    field_pass_confirm = web_browser.find_element(By.ID, "password-confirm")
    field_pass_confirm.send_keys(short_pass)
    # сообщение о требуемом формате пароля
    assert web_browser.find_element(By.XPATH,
                                    '/html/body/div[1]/main/section[2]/div/div/div/form/div[4]/div[1]/span').text == \
           'Длина пароля должна быть не менее 8 символов'


def test_reg_lower_case_pass(web_browser):
    # 16 - пароль без заглавных букв
    web_browser.implicitly_wait(3)
    web_browser.get(url_auth)
    # переход на страницу регистрации
    btn_reg = web_browser.find_element(By.XPATH, '//*[@id="kc-register"]')
    btn_reg.click()
    # ввод имени
    field_name = web_browser.find_element(By.NAME, 'firstName')
    field_name.send_keys(valid_name)
    # ввод фамилии
    field_lastname = web_browser.find_element(By.NAME, "lastName")
    field_lastname.send_keys(valid_lastname)
    # ввод почты
    field_lastname = web_browser.find_element(By.ID, "address")
    field_lastname.send_keys(valid_reg_mail)
    # ввод пароля
    field_pass = web_browser.find_element(By.ID, "password")
    field_pass.send_keys(lower_case_pass)
    # подтверждение пароля
    field_pass_confirm = web_browser.find_element(By.ID, "password-confirm")
    field_pass_confirm.send_keys(lower_case_pass)
    # сообщение о требуемом формате пароля
    assert web_browser.find_element(By.XPATH,
                                    '/html/body/div[1]/main/section[2]/div/div/div/form/div[4]/div[1]/span').text == \
           'Пароль должен содержать хотя бы одну заглавную букву'


def test_reg_diff_pass(web_browser):
    # 17 - несовпадение паролей
    web_browser.implicitly_wait(3)
    web_browser.get(url_auth)
    # переход на страницу регистрации
    btn_reg = web_browser.find_element(By.XPATH, '//*[@id="kc-register"]')
    btn_reg.click()
    # ввод имени
    field_name = web_browser.find_element(By.NAME, 'firstName')
    field_name.send_keys(valid_name)
    # ввод фамилии
    field_lastname = web_browser.find_element(By.NAME, "lastName")
    field_lastname.send_keys(valid_lastname)
    # ввод почты
    field_lastname = web_browser.find_element(By.ID, "address")
    field_lastname.send_keys(valid_reg_mail)
    # ввод пароля
    field_pass = web_browser.find_element(By.ID, "password")
    field_pass.send_keys(valid_pass)
    # подтверждение пароля
    field_pass_confirm = web_browser.find_element(By.ID, "password-confirm")
    field_pass_confirm.send_keys(valid_reg_pass)
    # клик на кнопку "зарегистрироваться"
    btn_reg = web_browser.find_element(By.NAME, 'register')
    btn_reg.click()
    # сообщение о разных паролях
    assert web_browser.find_element(By.XPATH,
                                    '/html/body/div[1]/main/section[2]/div/div/div/form/div[4]/div[2]/span').text == \
           'Пароли не совпадают'


def test_reg_unique_mail(web_browser):
    # 18 - регистрация с неуникальным email
    web_browser.implicitly_wait(3)
    web_browser.get(url_auth)
    # переход на страницу регистрации
    btn_reg = web_browser.find_element(By.XPATH, '//*[@id="kc-register"]')
    btn_reg.click()
    # ввод имени
    field_name = web_browser.find_element(By.NAME, 'firstName')
    field_name.send_keys(valid_name)
    # ввод фамилии
    field_lastname = web_browser.find_element(By.NAME, "lastName")
    field_lastname.send_keys(valid_lastname)
    # ввод неуникальной почты
    field_lastname = web_browser.find_element(By.ID, "address")
    field_lastname.send_keys(valid_mail)
    # ввод пароля
    field_pass = web_browser.find_element(By.ID, "password")
    field_pass.send_keys(valid_reg_pass)
    # подтверждение пароля
    field_pass_confirm = web_browser.find_element(By.ID, "password-confirm")
    field_pass_confirm.send_keys(valid_reg_pass)
    # клик на кнопку "зарегистрироваться"
    btn_reg = web_browser.find_element(By.NAME, 'register')
    btn_reg.click()
    # сообщение о существовании учетной записи
    assert web_browser.find_element(By.XPATH,
                                    '/html/body/div[1]/main/section[2]/div/div/div/form/div[1]/div/div/h2').text == \
           'Учётная запись уже существует'


def test_reg_long_phone(web_browser):
    # 19 - регистрация - длинный номер телефона
    web_browser.implicitly_wait(3)
    web_browser.get(url_auth)
    # переход на страницу регистрации
    btn_reg = web_browser.find_element(By.XPATH, '//*[@id="kc-register"]')
    btn_reg.click()
    # ввод имени
    field_name = web_browser.find_element(By.NAME, 'firstName')
    field_name.send_keys(valid_name)
    # ввод фамилии
    field_lastname = web_browser.find_element(By.NAME, "lastName")
    field_lastname.send_keys(valid_lastname)
    # ввод номера телефона
    field_lastname = web_browser.find_element(By.ID, "address")
    field_lastname.send_keys(long_number)
    # ввод пароля
    field_pass = web_browser.find_element(By.ID, "password")
    field_pass.send_keys(valid_pass)
    # подтверждение пароля
    field_pass_confirm = web_browser.find_element(By.ID, "password-confirm")
    field_pass_confirm.send_keys(valid_pass)
    # клик на кнопку "зарегистрироваться"
    btn_reg = web_browser.find_element(By.NAME, 'register')
    btn_reg.click()
    time.sleep(2)
    # сообщение о требуемом формате данных
    assert web_browser.find_element(By.XPATH,
                                    '/html/body/div[1]/main/section[2]/div/div/div/form/div[3]/span').text == \
           'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru'


def test_reg_rus_pass(web_browser):
    # 20 - пароль на русском
    web_browser.implicitly_wait(3)
    web_browser.get(url_auth)
    # переход на страницу регистрации
    btn_reg = web_browser.find_element(By.XPATH, '//*[@id="kc-register"]')
    btn_reg.click()
    # ввод имени
    field_name = web_browser.find_element(By.NAME, 'firstName')
    field_name.send_keys(valid_name)
    # ввод фамилии
    field_lastname = web_browser.find_element(By.NAME, "lastName")
    field_lastname.send_keys(valid_lastname)
    # ввод почты
    field_lastname = web_browser.find_element(By.ID, "address")
    field_lastname.send_keys(valid_reg_mail)
    # ввод пароля
    field_pass = web_browser.find_element(By.ID, "password")
    field_pass.send_keys(russian_pass)
    # подтверждение пароля
    field_pass_confirm = web_browser.find_element(By.ID, "password-confirm")
    field_pass_confirm.send_keys(russian_pass)
    # клик на кнопку "зарегистрироваться"
    btn_reg = web_browser.find_element(By.NAME, 'register')
    btn_reg.click()
    # сообщение о разных паролях
    assert web_browser.find_element(By.XPATH,
                                    '/html/body/div[1]/main/section[2]/div/div/div/form/div[4]/div[1]/span').text == \
           'Пароль должен содержать только латинские буквы'
