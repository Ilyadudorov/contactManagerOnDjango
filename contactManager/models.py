from django.db import models
from django.core.validators import RegexValidator
# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=20)
    phoneNumberRegex = RegexValidator(regex=r"^\+[1-9]\d{1,16}$")
    phoneNumber = models.CharField(validators= [phoneNumberRegex], max_length=50, unique=True, null=True, blank=True)
    email = models.EmailField(blank=True)
    birthdayRegex = RegexValidator(regex=r"(?:(?:31(\/|-|\.)(?:0?[13578]|1[02]))\1|(?:(?:29|30)(\/|-|\.)(?:0?[13-9]|1[0-2])\2))(?:(?:1[6-9]|[2-9]\d)?\d{2})$|^(?:29(\/|-|\.)0?2\3(?:(?:(?:1[6-9]|[2-9]\d)?(?:0[48]|[2468][048]|[13579][26])|(?:(?:16|[2468][048]|[3579][26])00))))$|^(?:0?[1-9]|1\d|2[0-8])(\/|-|\.)(?:(?:0?[1-9])|(?:1[0-2]))\4(?:(?:1[6-9]|[2-9]\d)?\d{2})")
    birthday = models.CharField(validators= [birthdayRegex], max_length=40, blank=True)
    position = models.CharField(max_length=30, blank=True)
    note = models.TextField(blank=True) #Заметка о контакта blank=True означает что поле может быть пустым
    photo = models.ImageField(upload_to="photo/%ContactID", blank=True)
    timeCreate = models.DateTimeField(auto_now_add=True, blank=True) #Дата создания контакта
    timeUpdate = models.DateTimeField(auto_now=True)
    is_favorite = models.BooleanField(default=False)
    group = models.ForeignKey('Group', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.name

class Group(models.Model):

    name = models.CharField(max_length=20, db_index=True, unique=True)

    def __str__(self):
        return self.name