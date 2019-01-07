from django.db import models


class aws_account(models.Model):

    aws_id = models.CharField(max_length=200)
    number = models.CharField(max_length=200)
    profile = models.CharField(max_length=200)
    alias = models.CharField(max_length=200)
    owner = models.CharField(max_length=200)
    access_key = models.CharField(max_length=200)
    secret_key = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.alias

    class Meta:
        verbose_name = 'AWS Account'
        verbose_name_plural = 'AWS Accounts'