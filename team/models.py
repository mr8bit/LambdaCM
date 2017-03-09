from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, Group
from django.utils.translation import gettext_lazy as _
from filebrowser.fields import FileBrowseField

social_network = (
    ('mdi-github-circle', 'GitHub'),
    ('mdi-twitter', 'Twitter'),
    ('mdi-gmail', 'Mail'),
    ('mdi-vk', 'Vk'),  # mdi-vk - ставиться как иконка соц сети, а vk - видет пользователь
    ('mdi-facebook', 'Facebook'),
)


class SocialNetwork(models.Model):
    name = models.CharField(max_length=300, verbose_name="Название социальной сети", choices=social_network)
    link = models.CharField(max_length=300, verbose_name="Ссылка на профиль")
    user = models.ForeignKey('Member')

    def __str__(self):
        return self.get_full_name

    class Meta:
        verbose_name = "Социальные сети"
        verbose_name_plural = "Социальные сети"


class TeamManager(BaseUserManager):
    def create_user(self,  email,  password=None):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=self.normalize_email(email),

        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,   password):
        user = self.create_user(
            email,
            password=password,  )
        user.is_admin = True
        user.save(using=self._db)
        return user


class Member(AbstractBaseUser):
    email = models.EmailField(unique=True)
    git_username = models.CharField(max_length=300, verbose_name="Git username")
    groups = models.ManyToManyField(
        Group,
        verbose_name='Группа',
        blank=True,
        help_text=_(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name="user_set",
        related_query_name="user",
    )
    first_name = models.CharField(max_length=300, null=True, blank=True, verbose_name="Имя")
    last_name = models.CharField(max_length=300, null=True, blank=True, verbose_name="Фамилия")
    date_of_birth = models.DateField(null=True, blank=True, verbose_name="Дата рождения")
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    profile_image = FileBrowseField("Изображения профиля", max_length=200, directory="состав_клуба/", blank=True,
                                    null=True)

    objects = TeamManager()

    USERNAME_FIELD = 'email'

    class Meta:
        verbose_name = "Участника"
        verbose_name_plural = "Участники"

    def get_full_name(self):
        if self.first_name and self.last_name :
            return self.first_name + ' ' + self.last_name
        else:
            return self.email

    def __str__(self):
        if self.first_name and self.last_name :
            return self.first_name + ' ' + self.last_name
        else:
            return self.email

    def get_short_name(self):
        return self.first_name

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
