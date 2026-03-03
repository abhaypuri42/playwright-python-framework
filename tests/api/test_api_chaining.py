import pytest

def test_employee_post_chaining(page):
    response = page.request.get('https://jsonplaceholder.typicode.com/users/3')
    data = response.json()
    employee_name = data['name']
    response_post = page.request.get('https://jsonplaceholder.typicode.com/posts', params={'userId': 3})
    post_data = response_post.json()
    assert len(post_data) == 10
def test_dynamic_data_handoff(page):
    response_all_users = page.request.get('https://jsonplaceholder.typicode.com/users')
    all_users_data = response_all_users.json()
    target_user_id = all_users_data[0]['id']
    target_user_response = page.request.get('https://jsonplaceholder.typicode.com/posts', params={'userId': target_user_id})
    target_data = target_user_response.json()
    first_post_userId = target_data[0]['userId']
    assert first_post_userId == target_user_id

