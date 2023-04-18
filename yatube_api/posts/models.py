from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class Group(models.Model):
    """Модель для групп."""

    title = models.CharField(_("Название группы"), max_length=200)
    description = models.TextField(_("Описание группы"))
    slug = models.SlugField(
        max_length=255,
        unique=True,
        verbose_name=_("Адрес для страницы с группой"),
        help_text=(
            _(
                "Укажите адрес для страницы группы. Используйте только "
                "латиницу, цифры, дефисы и знаки подчёркивания"
            )
        ),
    )

    class Meta:
        verbose_name = _("Группа")
        verbose_name_plural = _("Группы")

    def __str__(self):
        return self.title


class Post(models.Model):
    """Модель для постов."""

    text = models.TextField(
        _("Текст поста"), help_text=_("Введите текст поста")
    )
    pub_date = models.DateTimeField(
        _("Дата публикации"), auto_now_add=True, db_index=True
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="posts",
        verbose_name=_("Автор"),
    )
    group = models.ForeignKey(
        Group,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="posts",
        verbose_name=_("Группа"),
        help_text=_("Группа, к которой будет относиться пост"),
    )
    image = models.ImageField(
        _("Картинка"), upload_to="posts/", null=True, blank=True
    )

    class Meta:
        verbose_name = _("Пост")
        verbose_name_plural = _("Посты")

    def __str__(self):
        return self.text[:15]


class Comment(models.Model):
    """Модель для комментариев."""

    text = models.TextField(_("Текст комментария"))
    created = models.DateTimeField(
        _("Дата добавления"), auto_now_add=True, db_index=True
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name=_("Пост"),
        help_text=_("Пост, к которому оставлен комментарий"),
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name=_("Автор комментария"),
    )

    class Meta:
        verbose_name = _("Комментарий")
        verbose_name_plural = _("Комментарии")
        ordering = ("-created", "-id")

    def __str__(self):
        return self.text[:15]


class Follow(models.Model):
    """Модель для подписки на авторов."""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="follower",
        verbose_name=_("Подписчик"),
    )
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="following",
        verbose_name=_("Подписка на автора"),
    )

    class Meta:
        verbose_name = _("Подписка")
        verbose_name_plural = _("Подписки")
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'following'],
                name='unique_user_following'
            )
        ]

    def __str__(self):
        return f"Автор - {self.following}, подписчики: {self.user}"
