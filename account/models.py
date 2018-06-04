from django.db import models


class Address(models.Model):
    add_id = models.AutoField(verbose_name='用户ID', primary_key=True)
    province = models.CharField(verbose_name='省', max_length=100)
    city = models.CharField(verbose_name='市', max_length=32)

    class Meta:
        db_table = 'address'
        verbose_name = u'地址'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.province + self.city
