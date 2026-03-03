import pytest

def test_api_crud_lifecycle(page):
    # --- 1. CREATE (POST) ---
    new_data = {'title':'Automation Engine', 'body':'Playwright'}
    response = page.request.post('https://jsonplaceholder.typicode.com/posts', data=new_data)
    assert response.status == 201
    
    # Extract the ID (JSONPlaceholder always returns 101 for new items)
    new_id = response.json()['id']
    print(f"\nCreated new post with ID: {new_id}")

    # --- 2. READ (GET) ---

    response_get = page.request.get('https://jsonplaceholder.typicode.com/posts/1')
    assert response_get.status == 200

    # --- 3. UPDATE (PUT) ---
    add_data = {'title':'Updated Engine', 'body':'Playwright API'}
    put_response = page.request.put('https://jsonplaceholder.typicode.com/posts/1', data=add_data)
    assert put_response.status == 200

    # --- 4. DELETE (DELETE) ---
    remove_data_response = page.request.delete('https://jsonplaceholder.typicode.com/posts/1')
    assert remove_data_response.status == 200