from playwright.sync_api import sync_playwright, expect
import pytest

class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username = page.get_by_placeholder('Username')
        self.password = page.get_by_placeholder('Password')
        self.loginbutton = page.get_by_role('button', name='Login')
        self.loginpage_header = page.locator('.login_logo')
        self.password_text = page.locator('[data-test="login-password"]')
    def Maps(self):
        self.page.goto('https://www.saucedemo.com/')
    def user_login(self, username, password):
        self.username.fill(username)
        self.password.fill(password)
        self.loginbutton.click()