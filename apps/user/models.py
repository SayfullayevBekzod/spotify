from django.contrib.auth.models import AbstractUser
from django.db.models import (
    ImageField,
    OneToOneField,
    EmailField,
    DateField,
    TextChoices,
    CharField,
    ForeignKey,
    ManyToManyField,
    CASCADE,
)
from django.dispatch import receiver

from apps.shared.models import AbstractModel
from apps.user.managers import UserManager
# from django_rest_passwordreset.signals import reset_password_token_created


class UserGender(TextChoices):
    MALE = "M", "male"
    FEMALE = "F", "female"


class User(AbstractUser):
    avatar = ImageField(upload_to="user/%Y/%m/%d")
    email = None
    followings = ManyToManyField("self", symmetrical=False, related_name="followers")
    artist_following = ManyToManyField(
        "music.Artist",
        "users",
    )

    EMAIL_FIELD = None
    REQUIRED_FIELDS = []
    manager = UserManager()

    def __str__(self):
        return self.username


class UserProfile(AbstractModel):
    user = OneToOneField("User", CASCADE)
    email = EmailField(unique=True, null=True, blank=True)
    birthdate = DateField(null=True, blank=True)
    gender = CharField(max_length=6, choices=UserGender.choices, null=True)
    country = CharField(max_length=32, blank=True)

    def follow(self, user):
        self.user.followings.add(user)

    def unfollow(self, user):
        self.user.followings.remove(user)

    def follow_artist(self, artist_id):
        self.user.artist_following.add(artist_id)

    def unfollow_artist(self, artist_id):
        self.user.artist_following.remove(artist_id)

    def __str__(self):
        return f"{self.user.username} {self.gender}"


class Playlist(AbstractModel):
    owner = ForeignKey("user.User", CASCADE)
    title = CharField(max_length=128)
    musics = ManyToManyField("music.Song")

# @receiver(reset_password_token_created)
# def password_reset_token_created(
#     sender, instance, reset_password_token, *args, **kwargs
# ):
#     email_plaintext_message = "{}?token={}".format(
#         reverse("password_reset:reset-password-request"), reset_password_token.key
#     )
#
#     send_mail(
#         # title:
#         "Password Reset for {title}".format(title="Some website title"),
#         # message:
#         email_plaintext_message,
#         # from:
#         "noreply@somehost.local",
#         # to:
#         [reset_password_token.user.email],
#     )
