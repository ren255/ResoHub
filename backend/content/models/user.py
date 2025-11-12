from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager

from django.utils import timezone
import uuid as uuid_lib
from django.core.mail import send_mail

from rapidfuzz.process import extract, extractOne


class UserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.username = email
        user.set_password(password)
        user.save(using=self._db)
        return user


class UserRole(models.TextChoices):
    """ユーザーロール定義"""

    STUDENT = "student", "生徒"
    TEACHER = "teacher", "教師"
    STAFF = "staff", "管理者"
    SYSTEM = "system", "System"
    OTHER = "other", "その他"


class User(AbstractBaseUser, PermissionsMixin):
    """Custom User"""

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "user"

    uuid = models.UUIDField(default=uuid_lib.uuid4, primary_key=True, editable=False)
    role = models.CharField(
        max_length=20,
        choices=UserRole.choices,
        default=UserRole.OTHER,
        verbose_name="役割",
        db_index=True,
    )
    # ユーザ氏名
    name = models.CharField(max_length=30, unique=False, blank=True)
    username = models.CharField(max_length=30, unique=False, blank=True)
    # メールアドレス = これで認証する
    email = models.EmailField(unique=True, blank=True, null=True)

    is_active = models.BooleanField(default=True)  # アクティブ権限
    is_staff = models.BooleanField(default=False)  # スタッフ権限
    is_superuser = models.BooleanField(default=False)  # 管理者権限
    date_joined = models.DateTimeField(default=timezone.now)  # アカウント作成日時

    objects = UserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"

    def search(query):
        users = list(User.objects.all())  # QuerySetをリストに変換

        choices = [user.name for user in users]
        results = extract(query, choices)
        # (UserInstance, score)の形式で返す
        return [(users[index], score) for text, score, index in results]

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def has_full_access(self):
        """完全アクセス権限を持つか"""
        return self.role in [UserRole.STAFF, UserRole.SYSTEM]

    def __str__(self):
        return self.name
