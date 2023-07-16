import requests

BASE_URL = 'https://gorest.co.in/'
ACCESS_TOKEN = 'd09843bcb0e48c560257f82ec4d7923b698a41caf549b8198f6ef0e6655c869f'

def create_user(user_data):
    # Create a user
    headers = {'Authorization': f'Bearer {ACCESS_TOKEN}'}
    response = requests.post(BASE_URL + 'public/v1/users', headers=headers, data=user_data)
    user_id = response.json().get('data', {}).get('id')
    return user_id

def delete_user(user_id):
    # Delete a user
    headers = {'Authorization': f'Bearer {ACCESS_TOKEN}'}
    response = requests.delete(BASE_URL + f'public/v1/users/{user_id}', headers=headers)
    status_code = response.status_code
    if status_code == 204:
        print(f"User {user_id} deleted successfully.")
    else:
        print(f"Failed to delete user {user_id}. Status code: {status_code}")

def create_post_test():
    # User data for creation
    user_data = {
        'name': 'Test User',
        'gender': 'male',
        'email': 'testuser@example.com',
        'status': 'active'
    }
    user_id = create_user(user_data)
    if user_id:
        # Create a post for the user
        headers = {'Authorization': f'Bearer {ACCESS_TOKEN}'}
        post_data = {
            'title': 'Test Post',
            'body': 'This is a test post.'
        }
        response = requests.post(BASE_URL + f'public/v1/users/{user_id}/posts', headers=headers, data=post_data)
        if response.status_code == 201:
            post_id = response.json().get('data', {}).get('id')
            print(f"Post created successfully. Post ID: {post_id}")
            delete_user(user_id)
        else:
            print("Failed to create post.")
            delete_user(user_id)
    else:
        print("Failed to create test user.")

# Run the post creation test
create_post_test()
