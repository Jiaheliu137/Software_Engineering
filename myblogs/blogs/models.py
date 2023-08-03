from django.db import models

from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver

from django.utils import timezone

import bleach
from django.conf import settings





# from django.contrib.auth.models import User
class Author(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='author')

    def __str__(self):
        return self.user.username
    
# from django.db.models.signals import post_save
@receiver(post_save, sender=User)
def create_user_author(sender, instance, created, **kwargs):
    if created:
        Author.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_author(sender, instance, **kwargs):
    instance.author.save()



# from django.db import models
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    # date_created = models.DateTimeField(default=timezone.now) # This code can let you change time
    date_created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.title
    
    

    def save(self, *args, **kwargs):
        additional_tags = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'br', 'p', 'pre', 'span', 'div', 'img', 'table', 'thead', 'tbody', 'tr', 'th', 'td']
        additional_attributes = {
            'a': ['href', 'rel', 'target'],
            'img': ['src', 'alt'],
        }
        ALLOWED_TAGS = bleach.sanitizer.ALLOWED_TAGS.union(additional_tags)
        ALLOWED_ATTRIBUTES = {**bleach.sanitizer.ALLOWED_ATTRIBUTES, **additional_attributes}
        

        self.content = bleach.clean(
            self.content,
            tags=ALLOWED_TAGS,
            attributes=ALLOWED_ATTRIBUTES,
            strip=False,
        )
        super().save(*args, **kwargs)


    # Create your models here.
