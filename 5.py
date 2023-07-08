import requests

# Функция для создания пользователя
def create_user():
    endpoint = "https://gorest.co.in/public-api/users"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer YOUR_ACCESS_TOKEN"  # Замените YOUR_ACCESS_TOKEN на ваш токен авторизации
    }
    data = {
        "name": "Test User",
        "email": "testuser@example.com",
        "gender": "male",
        "status": "active"
    }

    response = requests.post(endpoint, headers=headers, json=data)
    user_data = response.json()
    user_id = user_data["data"]["id"]
    return user_id

# Функция для создания поста
def create_post(user_id, title, body):
    endpoint = "https://gorest.co.in/public-api/posts"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer YOUR_ACCESS_TOKEN"  # Замените YOUR_ACCESS_TOKEN на ваш токен авторизации
    }
    data = {
        "user_id": user_id,
        "title": title,
        "body": body
    }

    response = requests.post(endpoint, headers=headers, json=data)
    post_data = response.json()
    post_id = post_data["data"]["id"]
    return post_id

# Функция для удаления пользователя
def delete_user(user_id):
    endpoint = f"https://gorest.co.in/public-api/users/{user_id}"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer YOUR_ACCESS_TOKEN"  # Замените YOUR_ACCESS_TOKEN на ваш токен авторизации
    }

    response = requests.delete(endpoint, headers=headers)
    return response.status_code

# Тест для проверки создания поста
def test_create_post():
    # Создаем пользователя
    user_id = create_user()

    # Создаем пост
    title = "Test Post"
    body = "This is a test post."
    post_id = create_post(user_id, title, body)

    # Проверяем успешное создание поста
    assert post_id is not None, "Failed to create post"

    # Удаляем пользователя после теста
    status_code = delete_user(user_id)

    # Проверяем успешное удаление пользователя
    assert status_code == 204, "Failed to delete user"

# Запуск теста
test_create_post()
