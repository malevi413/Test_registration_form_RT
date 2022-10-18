from selenium.webdriver.common.by import By
from config import *


def test_auth_phone_positive(web_browser):
    # 1 + успешная авторизация
    web_browser.implicitly_wait(3)
    web_browser.get(url_auth)
    # клик на кнопку 'телефон'
    btn_phone = web_browser.find_element(By.ID, 't-btn-tab-phone')
    btn_phone.click()
    # ввод логина(номер)
    field_phone = web_browser.find_element(By.ID, "username")
    field_phone.send_keys(valid_phone)
    # ввод пароля
    field_pass = web_browser.find_element(By.ID, "password")
    field_pass.send_keys(valid_pass)
    # клик на кнопку "войти"
    btn_auth = web_browser.find_element(By.ID, 'kc-login')
    btn_auth.click()
    # клик на кнопку "личный кабинет"
    btn_lk = web_browser.find_element(By.ID, 'lk-btn')
    btn_lk.click()
    # проверка входа в личный кабинет
    assert web_browser.current_url == 'https://start.rt.ru/?tab=main' or 'https://lk.rt.ru/'


def test_auth_phone_negative(web_browser):
    web_browser.implicitly_wait(3)
    # 2 - авторизация с пустым номером
    web_browser.get(url_auth)
    # клик на кнопку 'телефон'
    btn_phone = web_browser.find_element(By.ID, 't-btn-tab-phone')
    btn_phone.click()
    # ввод логина(пустой номер)
    field_phone = web_browser.find_element(By.ID, "username")
    field_phone.send_keys(empty_login)
    # ввод пароля
    field_pass = web_browser.find_element(By.ID, "password")
    field_pass.send_keys(valid_pass)
    # клик на кнопку "войти"
    btn_auth = web_browser.find_element(By.ID, 'kc-login')
    btn_auth.click()
    # проверка вывода сообщения 'Введите номер телефона'
    assert web_browser.find_element(By.CSS_SELECTOR,
                                    'section#page-right > div > div > div > form > div > div:nth-of-type(2) > span'). \
               text == 'Введите номер телефона'


def test_auth_phone_short_number(web_browser):
    web_browser.implicitly_wait(3)
    # 3 - авторизация с коротким номером
    web_browser.get(url_auth)
    # клик на кнопку 'телефон'
    btn_phone = web_browser.find_element(By.ID, 't-btn-tab-phone')
    btn_phone.click()
    # ввод логина
    field_phone = web_browser.find_element(By.ID, "username")
    field_phone.send_keys(short_number)
    # ввод пароля
    field_pass = web_browser.find_element(By.ID, "password")
    field_pass.send_keys(valid_pass)
    # клик на кнопку "войти"
    btn_auth = web_browser.find_element(By.ID, 'kc-login')
    btn_auth.click()
    # проверка вывода сообщения 'Введите номер телефона'
    assert web_browser.find_element(By.XPATH,
                                    '/html/body/div[1]/main/section[2]/div/div/div/form/div[1]/div[2]/span'). \
               text == 'Неверный формат телефона'


def test_auth_mail(web_browser):
    web_browser.implicitly_wait(3)
    # 4 + авторизация по mail
    web_browser.get(url_auth)
    # клик на кнопку 'email'
    btn_mail = web_browser.find_element(By.ID, 't-btn-tab-mail')
    btn_mail.click()
    # ввод логина(email)
    field_mail = web_browser.find_element(By.ID, "username")
    field_mail.send_keys(valid_mail)
    # ввод пароля
    field_pass = web_browser.find_element(By.ID, "password")
    field_pass.send_keys(valid_pass)
    # клик на кнопку "войти"
    btn_auth = web_browser.find_element(By.ID, 'kc-login')
    btn_auth.click()
    # клик на кнопку "личный кабинет"
    btn_lk = web_browser.find_element(By.ID, 'lk-btn')
    btn_lk.click()
    # проверка входа в личный кабинет
    assert web_browser.current_url == 'https://start.rt.ru/?tab=main' or 'https://lk.rt.ru/'


def test_auth_mail_negative(web_browser):
    web_browser.implicitly_wait(2)
    # 5 - авторизация c пустым mail
    web_browser.get(url_auth)
    # клик на кнопку 'email'
    btn_mail = web_browser.find_element(By.ID, 't-btn-tab-mail')
    btn_mail.click()
    # ввод логина(email)
    field_mail = web_browser.find_element(By.ID, "username")
    field_mail.send_keys(empty_login)
    # ввод пароля
    field_pass = web_browser.find_element(By.ID, "password")
    field_pass.send_keys(valid_pass)
    # клик на кнопку "войти"
    btn_auth = web_browser.find_element(By.ID, 'kc-login')
    btn_auth.click()
    # проверка вывода сообщения 'Введите адрес, указанный при регистрации'
    assert web_browser.find_element(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div >'
                                                     ' div:nth-of-type(2) > span').text == 'Введите адрес, указанный ' \
                                                                                           'при регистрации'


def test_auth_login_positive(web_browser):
    web_browser.implicitly_wait(3)
    # 6 + авторизация по логину
    web_browser.get(url_auth)
    # клик на кнопку 'логин'
    btn_login = web_browser.find_element(By.ID, 't-btn-tab-login')
    btn_login.click()
    # ввод логина
    field_login = web_browser.find_element(By.ID, "username")
    field_login.send_keys(valid_login)
    # ввод пароля
    field_pass = web_browser.find_element(By.ID, "password")
    field_pass.send_keys(valid_pass)
    # клик на кнопку "войти"
    btn_auth = web_browser.find_element(By.ID, 'kc-login')
    btn_auth.click()
    # клик на кнопку "личный кабинет"
    btn_lk = web_browser.find_element(By.ID, 'lk-btn')
    btn_lk.click()
    # проверка входа в личный кабинет
    assert web_browser.current_url == 'https://start.rt.ru/?tab=main' or 'https://start.rt.ru/'


def test_auth_login_negative(web_browser):
    web_browser.implicitly_wait(3)
    # 7 - авторизация по логину c пустым паролем
    web_browser.get(url_auth)
    # клик на кнопку 'логин'
    btn_login = web_browser.find_element(By.ID, 't-btn-tab-login')
    btn_login.click()
    # ввод логина
    field_mail = web_browser.find_element(By.ID, "username")
    field_mail.send_keys(valid_login)
    # ввод пустого пароля
    field_pass = web_browser.find_element(By.ID, "password")
    field_pass.send_keys(empty_pass)
    # клик на кнопку "войти"
    btn_auth = web_browser.find_element(By.ID, 'kc-login')
    btn_auth.click()
    # проверка вывода сообщения 'Неверный логин или пароль''
    assert web_browser.find_element(By.CLASS_NAME, 'card-container__error login-form-container__error--bold').text == \
           'Неверный логин или пароль'


def test_auth_login_invalid_pass(web_browser):
    web_browser.implicitly_wait(3)
    # 8 - авторизация по логину c некорректным паролем
    web_browser.get(url_auth)
    # клик на кнопку 'логин'
    btn_login = web_browser.find_element(By.ID, 't-btn-tab-login')
    btn_login.click()
    # ввод логина
    field_mail = web_browser.find_element(By.ID, "username")
    field_mail.send_keys(valid_login)
    # ввод  пароля
    field_pass = web_browser.find_element(By.ID, "password")
    field_pass.send_keys(invalid_pass)
    # клик на кнопку "войти"
    btn_auth = web_browser.find_element(By.ID, 'kc-login')
    btn_auth.click()
    # проверка вывода сообщения 'Неверный логин или пароль''
    assert web_browser.find_element(By.CSS_SELECTOR, 'section#page-right > div > div > p').text == \
           'Неверный логин или пароль'


def test_auth_account_positive(web_browser):
    web_browser.implicitly_wait(3)
    # 9 + авторизация по лицевому счету
    web_browser.get(url_auth)
    # клик на кнопку 'лицевой счет'
    btn_account = web_browser.find_element(By.ID, 't-btn-tab-ls')
    btn_account.click()
    # ввод лицевого счета
    field_lc = web_browser.find_element(By.ID, "username")
    field_lc.send_keys(valid_account)
    # ввод пароля
    field_pass = web_browser.find_element(By.ID, "password")
    field_pass.send_keys(valid_pass)
    # клик на кнопку "войти"
    btn_auth = web_browser.find_element(By.ID, 'kc-login')
    btn_auth.click()
    # клик на кнопку "личный кабинет"
    btn_lk = web_browser.find_element(By.ID, 'lk-btn')
    btn_lk.click()
    # проверка входа в личный кабинет
    assert web_browser.current_url == 'https://start.rt.ru/?tab=main' or 'https://start.rt.ru/'


def test_auth_account_negative(web_browser):
    web_browser.implicitly_wait(3)
    # 10 - авторизация по лицевому счету c некорректным логином
    web_browser.get(url_auth)
    # клик на кнопку 'логин'
    btn_account = web_browser.find_element(By.ID, 't-btn-tab-ls')
    btn_account.click()
    # ввод некорректного лицевого счета
    field_lc = web_browser.find_element(By.ID, "username")
    field_lc.send_keys(invalid_account)
    # ввод пустого пароля
    field_pass = web_browser.find_element(By.ID, "password")
    field_pass.send_keys(valid_pass)
    # клик на кнопку "войти"
    btn_auth = web_browser.find_element(By.ID, 'kc-login')
    btn_auth.click()
    # проверка вывода сообщения 'Неверный логин или пароль'
    assert web_browser.find_element(By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/p[1]').text == \
           'Неверный логин или пароль'
