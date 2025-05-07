from django.db import models


class Blog(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name="Заголовок",
    )

    content = models.TextField(
        verbose_name="Содержимое",
    )

    preview = models.ImageField(
        upload_to="blog/preview",
        verbose_name="Изображение",
    )

    created_at = models.DateTimeField(auto_now_add=True)

    is_published = models.BooleanField(
        default=True,
        verbose_name="Опубликовано",
    )

    views_count = models.PositiveIntegerField(
        default=0,
        verbose_name="Количество просмотров",
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"
        ordering = ["-created_at"]
