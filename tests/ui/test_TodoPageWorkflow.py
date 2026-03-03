from pages.page_TodoWorkflow import TodoPage
import pytest

def test_workflow(page):
    home_page=TodoPage(page)
    home_page.Maps()
    home_page.add_task('Buy milk')
    home_page.add_task('Walk dog')
    home_page.add_task('Learn POM')
    home_page.mark_test_completed('Walk dog')
    items_remaining = home_page.get_items_left()
    assert '2' in items_remaining