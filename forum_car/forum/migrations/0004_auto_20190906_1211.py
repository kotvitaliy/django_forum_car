# Generated by Django 2.2.5 on 2019-09-06 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0003_auto_20190906_1209'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='petrol',
            field=models.CharField(db_index=True, default='', max_length=200, verbose_name='Вид топлива'),
        ),
        migrations.AlterField(
            model_name='product',
            name='engine',
            field=models.DecimalField(decimal_places=2, default='', max_digits=10, verbose_name='Обьем двигателя'),
        ),
    ]
