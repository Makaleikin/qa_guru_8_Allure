import allure
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s

browser.config.hold_browser_open = False
browser.config.window_width = 1920
browser.config.window_height = 1080


def test_dynamic_step():
    with allure.step('Открываем главную страницу'):
        browser.open('https://github.com')
    with allure.step('Ищем репозиторий'):
        s('.header-search-input').click()
        s('.header-search-input').send_keys('eroshenkoam/allure-example')
        s('.header-search-input').submit()
    with allure.step('Переходим по ссылке репозитория'):
        s(by.link_text('eroshenkoam/allure-example')).click()
    with allure.step('Открываем таб Issues'):
        s('#issues-tab').click()
    with allure.step('Проверяем наличие issue с номером 76'):
        s(by.partial_text('#76')).should(be.visible)