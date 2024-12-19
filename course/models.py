from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=100)
    keywords = models.CharField(max_length=255) # max of char: 256 -1
    description = models.TextField(max_length=500)
    image = models.ImageField(null=False, upload_to="images/")
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.title

class Subject(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    subject_tutor = models.CharField(max_length=255)
    description = models.TextField(max_length=500)
    image = models.ImageField(null=False, upload_to="images/")
    price = models.CharField(max_length=50)
    detail = models.CharField(max_length=255)
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.title

class Setting(models.Model):
    title = models.CharField(max_length=100)
    keywords = models.CharField(max_length=255)
    description = models.TextField()
    phone = models.CharField(max_length=16)
    email = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    smpt_server = models.CharField(max_length=255)
    smpt_email = models.CharField(max_length=255)
    smpt_password = models.CharField(max_length=32)
    smpt_port = models.CharField(max_length=255)
    # youtube = models.SlugField(null=False, unique=True)
    # instagram = models.SlugField(null=False, unique=True)
    # facebook = models.SlugField(null=False, unique=True)
    youtube = models.CharField(max_length=255)
    instagram = models.CharField(max_length=255)
    facebook = models.CharField(max_length=255)
    icon = models.ImageField(null=False, upload_to="images/")
    aboutus = models.TextField(max_length=255)
    contact = models.TextField(max_length=255)
    # slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.title