import unittest
from app.models import Post, User
from app import db

class TestPost(unittest.TestCase):
    def setUp(self):
        self.user_Murathe = User(username='Winnie', password='2001mwiks', email='winnishgabriella@gamil.com')
        self.new_post = Post(post_id=112233, text='Django should be good', user=self.user_Winnie)

    def tearDown(self):
        Post.query.delete()
        User.query.delete()
    def test_instance(self):
        self.assertTrue(isinstance(self.new_post, Post))

    def test_check_instance_variables(self):
        self.assertEquals(self.new_post.post_id, 112233)
        self.assertEquals(self.new_post.text, 'Django I smell a rat')
        self.assertEquals(self.new_post.user, self.user_Winnie)

    def test_save_post(self):
        self.new_post.save_post()
        self.assertTrue(len(Post.query.all()) > 0)

    def test_get_post_by_id(self):
        self.new_post.save_post()
        got_posts = Post.get_posts(112233)
        self.assertTrue(len(got_posts) == 1)