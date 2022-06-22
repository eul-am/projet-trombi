from django.db import models


# (I) on créé la table
class User(models.Model):
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=30)

    def __str__(self):
        """  """
        return self.last_name
