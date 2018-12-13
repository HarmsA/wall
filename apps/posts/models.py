from django.db import models
from apps.users.models import User

# Create your models here.
class PostManager(models.Manager):
    def process_post(self, form, id):
        user = User.objects.get(id=id)
        errors = []
        # print('User = ', user.id)
        # print('*'*80)
        if len(form['title'])<1:
            errors.append('Must have a Title.')
        if len(form['message'])<1:
            errors.append('Post must have content.')
        # print(form)
        if errors:
            return errors
        else:
            user = User.objects.get(id=id)
            new_post = self.create(
                title=form['title'],
                message=form['message'],
                user=user
            )
        return new_post



class Post(models.Model):
    title = models.CharField(max_length=255)
    message = models.TextField()
    user = models.ForeignKey(User, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = PostManager()