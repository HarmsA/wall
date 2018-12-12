from django.db import models
from apps.users.models import User
from apps.posts.models import Post

# Create your models here.

class CommentManager(models.Manager):
    def verify_comment(self, form):
        errors = []
        if len(form['content'])<1:
            errors.append('Must have text in the comment to post.')
            return errors
        else:
            return False

    def create_comment(self, form, id):
        post = Post.objects.get(id=form['post_id'])
        print('id = ',id)
        comment = self.create(
            comment=form['content'],
            user_id=id,
            post_id=post,
        )
        return comment



class Comment(models.Model):
    comment = models.TextField()
    user_id = models.ForeignKey(User, related_name='user_comments')
    post_id = models.ForeignKey(Post, related_name='post_comments')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CommentManager()

