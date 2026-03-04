from pages.page_LoginSauceDemo import LoginPage
from pages.page_inventoryPage_saucedemo import InventoryPage
from playwright.sync_api import expect
import pytest

def test_loginSaucedemo(page):
    login_page=LoginPage(page)
    login_page.Maps()
    loginPage_text = login_page.password_text.inner_text()
    assert "secret_sauce" in loginPage_text
    login_page.user_login('standard_user', 'secret_sauce')
    home_page=InventoryPage(page)
    actual_text = home_page.get_title_text()
    assert "Products" in actual_text

def test_userflow(page):
    login_page=LoginPage(page)
    login_page.Maps()
    login_page.user_login('standard_user','secret_sauce')
    products_page=InventoryPage(page)
    products_page.add_item_to_cart('Sauce Labs Bike Light')
    products_page.add_item_to_cart('Sauce Labs Fleece Jacket')
    expect(products_page.cart_bdg).to_contain_text('2')
