import requests
import pytest
import random
import string

BASE_URL = 'https://gorest.co.in/'
ACCESS_TOKEN = 'd09843bcb0e48c560257f82ec4d7923b698a41caf549b8198f6ef0e6655c869f'

@pytest.fixture
def user_data():
    # Данные пользователя для создания
    email = ''.join(random.choices(string.ascii_lowercase, k=10)) + "@example.com"
    return {
        'name': 'Test User',
        'gender': 'male',
        'email': email,
        'status': 'active'
    }

@pytest.fixture
def create_user_fixture(user_data):
    # Создание пользователя
    headers = {'Authorization': f'Bearer {ACCESS_TOKEN}'}
    response = requests.post(BASE_URL + 'public/v1/users', headers=headers, data=user_data)
    user_id = response.json().get('data', {}).get('id')
    assert user_id is not None, "Failed to create user"
    yield user_id
    # Удаление пользователя после завершения
    headers = {'Authorization': f'Bearer {ACCESS_TOKEN}'}
    requests.delete(BASE_URL + f'public/v1/users/{user_id}', headers=headers)

def create_post(user_id):
    # Создание поста для пользователя
    headers = {'Authorization': f'Bearer {ACCESS_TOKEN}'}
    post_data = {
        'title': 'Test Post',
        'body': 'This is a test post.'
    }
    response = requests.post(BASE_URL + f'public/v1/users/{user_id}/posts', headers=headers, data=post_data)
    return response

@pytest.mark.parametrize('post_title, post_body', [('Test Post', 'This is a test post.')])
def test_create_post(create_user_fixture, post_title, post_body):
    # Тест создания поста
    user_id = create_user_fixture
    response = create_post(user_id)
    assert response.status_code == 201, "Failed to create post"
    assert response.json().get('data', {}).get('title') == post_title, "Unexpected post title"
    assert response.json().get('data', {}).get('body') == post_body, "Unexpected post body"

# Запуск теста создания поста
pytest.main([__file__, '-v'])
