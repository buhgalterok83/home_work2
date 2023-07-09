import requests
import json
import unittest


class PostCreationTest(unittest.TestCase):
    base_url = 'https://gorest.co.in/public-api'
    token = '<YOUR_ACCESS_TOKEN>'

    @classmethod
    def setUpClass(cls):
        # Создание пользователя для тестов
        cls.user_id = cls.create_user()

    @classmethod
    def tearDownClass(cls):
        # Удаление пользователя после тестов
        cls.delete_user(cls.user_id)

    @classmethod
    def create_user(cls):
        headers = {
            'Authorization': f'Bearer {cls.token}',
            'Content-Type': 'application/json',
        }
        data = {
            'name': 'Test User',
            'gender': 'Male',
            'email': 'testuser@example.com',
            'status': 'Active'
        }
        response = requests.post(f'{cls.base_url}/users', headers=headers, json=data)
        user_id = response.json().get('data', {}).get('id')
        return user_id

    @classmethod
    def delete_user(cls, user_id):
        headers = {
            'Authorization': f'Bearer {cls.token}'
        }
        response = requests.delete(f'{cls.base_url}/users/{user_id}', headers=headers)
        status_code = response.status_code
        assert status_code == 204, "Failed to delete user"

    def create_post(self, post_data):
        headers = {
            'Authorization': f'Bearer {self.token}',
            'Content-Type': 'application/json',
        }
        response = requests.post(f'{self.base_url}/posts', headers=headers, json=post_data)
        return response

    def test_post_creation(self):
        # Параметры поста для теста
        post_data = {
            'title': 'Test Post',
            'body': 'This is a test post'
        }

        response = self.create_post(post_data)
        self.assertEqual(response.status_code, 201)
        post_id = response.json().get('data', {}).get('id')
        assert post_id is not None, "Failed to create post"

        # Проверяем, что созданный пост соответствует ожиданиям
        self.assertEqual(response.json().get('data', {}).get('title'), post_data['title'])
        self.assertEqual(response.json().get('data', {}).get('body'), post_data['body'])


if __name__ == '__main__':
    unittest.main()
