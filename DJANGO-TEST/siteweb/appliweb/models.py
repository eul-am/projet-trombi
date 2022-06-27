from django.db import models


class Person(models.Model):
    registration_number = models.CharField(max_length=10, null=True)
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    birth_date = models.DateField()
    email = models.EmailField()
    home_phone_number = models.CharField(max_length=20, null=True)
    cellphone_number = models.CharField(max_length=20, null=True)
    # Dans un cas reel, nous ne devrions pas stocker le mot de passe en clair.
    password = models.CharField(max_length=32)
    friends = models.ManyToManyField('self')
    faculty = models.ForeignKey('Faculty', default=None, null=True, on_delete=models.CASCADE)
    person_type = 'generic'

    def __str__(self):
        return self.first_name + " " + self.last_name


class Message(models.Model):
    author = models.ForeignKey('Person', on_delete=models.CASCADE)
    content = models.TextField()
    publication_date = models.DateField()

    def __str__(self):
        if len(self.content) > 20:
            return self.content[:19] + "..."
        else:
            return self.content


class Faculty(models.Model):
    name = models.CharField(max_length=30)
    color = models.CharField(max_length=6)

    def __str__(self):
        return self.name


class Campus(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Job(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class Cursus(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class Employee(Person):
    office = models.CharField(max_length=30)
    campus = models.ForeignKey('Campus', on_delete=models.CASCADE)
    job = models.ForeignKey('Job', on_delete=models.CASCADE)
    person_type = 'employee'

    def __str__(self):
        return self.office


class Student(Person):
    cursus = models.ForeignKey('Cursus', on_delete=models.CASCADE)
    year = models.IntegerField()
    person_type = 'student'

    def __str__(self):
        return self.year

# Problème de migrations ? voir la commande : python manage.py migrate --run-syncdb
