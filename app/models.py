from django.db import models
from django.core import validators


class Item(models.Model):

    SEX_CHOICES = (
        (1, 'Man'),
        (2, 'Woman'),
    )

    name = models.CharField(
        verbose_name='Name',
        max_length=200,
    )
    age = models.IntegerField(
        verbose_name='Age',
        validators=[validators.MinValueValidator(1)],
        blank=True,
        null=True,
    )
    sex = models.IntegerField(
        verbose_name='Gender',
        choices=SEX_CHOICES,
        default=1
    )
    memo = models.TextField(
        verbose_name='Comment',
        max_length=300,
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(
        verbose_name='Registered Date',
        auto_now_add=True
    )

    # 管理サイト上の表示設定
    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Item'