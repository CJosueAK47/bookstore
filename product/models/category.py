<<<<<<< HEAD

=======
>>>>>>> f6ac5dfbe4ee90a476827f702ef4cb128c0e3ee7
from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    active = models.BooleanField(default=True)

    def __unicode__(self):
<<<<<<< HEAD
        return self.title
=======
        return self.title
    

>>>>>>> f6ac5dfbe4ee90a476827f702ef4cb128c0e3ee7
