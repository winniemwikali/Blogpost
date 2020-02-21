import unittest
from app.models import Comment, User
from app import db

class TestComment(unittest.TestCase):
    def setUp(self):
        self.user_Winnie = User(username='Winnie', password='2001mwiks', email='winnishgabriella@gmail.com')
        self.new_comment = Comment(comment_id=112233, text='Flask not a friend', user=self.user_Winnie)

    def tearDown(self):
        Comment.query.delete()
        User.query.delete()
    def test_instance(self):
        self.assertTrue(isinstance(self.new_comment, Comment))

    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.comment_id, 112233)
        self.assertEquals(self.new_comment.pitch_comment,'Flask is tiresome')
        self.assertEquals(self.new_comment.user, self.user_Winnie)

    def test_save_comment(self):
        self.new_comment.save_comment()
        self.assertTrue(len(Comment.query.all()) > 0)

    def test_get_comment_by_id(self):
        self.new_comment.save_comment()
        got_comments = Comment.get_comments(112233)
        self.assertTrue(len(got_comments) == 1)
      