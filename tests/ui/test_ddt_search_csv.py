import pytest
import csv
from playwright.sync_api import expect
from pages.page_LoginSauceDemo import LoginPage
def get_csv_data():
    test_data=[]
    with open('data/test_users.csv', mode='r') as file:
        reader=csv.reader(file)
        next(reader)
        for row in reader:
            test_data.append(row)
    return test_data

@pytest.mark.parametrize("username,password,expected_error", get_csv_data())
def test_csv_login_matrix(page, username, password, expected_error):
    login_page=LoginPage(page)
    login_page.Maps()
    login_page.user_login(username,password)
    if expected_error == 'None':
        expect(page).to_have_url('https://www.saucedemo.com/inventory.html')
    else:
        expect(login_page.error_locator).to_contain_text(expected_error)