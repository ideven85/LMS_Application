import pytest
# Create your tests here.
from core.post.models import Post

@pytest.mark.django_db
def test_create_post(user):
    post = Post.objects.create(author=user,body="Test Body",title="Test")
    assert post.author == user
    assert post.body == "Test Body"