from playwright.sync_api import expect
import pytest

class TodoPage:
    def __init__ (self, page):
        self.page = page
        self.url = 'https://demo.playwright.dev/todomvc/'
        self.main_textbox = page.get_by_placeholder('What needs to be done?')
        self.heading = page.get_by_role('heading',name='todos')
        self.items_left = page.locator('[data-testid="todo-count"]')
        self.to_do_items= page.locator('.todo-list li')
        self.completed_checkbox = self.to_do_items.get_by_role('checkbox')
    def Maps(self):
        self.page.goto(self.url)
    def add_task(self, task_name):
        self.main_textbox.fill(task_name)
        self.main_textbox.press("Enter")
    def mark_test_completed(self, task_name):
        to_be_completed_item = self.to_do_items.filter(has_text=task_name)
        to_be_completed_item.get_by_role('checkbox').check()
    def get_items_left(self):
        item_left_in_footer = self.items_left.inner_text()
        return item_left_in_footer



