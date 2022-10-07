import allure
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s

browser.config.hold_browser_open = False
browser.config.window_width = 1920
browser.config.window_height = 1080


def test_git_hub():
    browser.open('https://github.com')

    s('.header-search-input').click()
    s('.header-search-input').send_keys('eroshenkoam/allure-example')
    s('.header-search-input').submit()

    s(by.link_text('eroshenkoam/allure-example')).click()

    s('#issues-tab').click()

    s(by.partial_text('#76')).should(be.visible)
