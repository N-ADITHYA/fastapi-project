from typing import List
import schemas

def test_get_all_posts(authorized_client, test_posts):
    res = authorized_client.get('/posts/')

    def validate(post):
        return schemas.PostVote(**post)
    posts_map = map(validate, res.json())
    posts_list = list(posts_map)
    assert len(res.json()) == len(test_posts)
    assert res.status_code == 200

def test_unauthorized_user_get_all_posts(client, test_posts):
    res = client.get('/posts/')
    print(res.json())
    assert res.status_code == 401


def test_unauthorized_user_get_one_posts(client, test_posts):
    res = client.get(f'/posts/{test_posts[0].id}')
    assert res.status_code == 401

def test_get_one_post_not_exist(client, test_posts):
    res = authorized_client.get(f'/posts/8888')
    assert res.status_code == 404

def test_unauthorized_user_get_one_posts(client, test_posts):
    res = authorized_client.get(f'/posts/{test_posts[0].id}')
    assert res.status_code == 401