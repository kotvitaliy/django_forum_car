# Generated by Django 2.2.5 on 2019-09-09 13:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forum', '0006_remove_product_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg', models.TextField(max_length=1000, verbose_name='Текст комментария')),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_birth', models.DateField(blank=True, null=True)),
                ('bio', models.TextField(blank=True, max_length=5000, null=True, verbose_name='Bio')),
                ('type_view', models.CharField(blank=True, choices=[('fio', 'ФИО'), ('pseudo_name', 'Псевдоним')], max_length=255, null=True, verbose_name='Тип представления')),
                ('pseudoname', models.CharField(blank=True, max_length=255, null=True, verbose_name='Псевдоним')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_created=True, auto_now_add=True)),
                ('title', models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='Title')),
                ('content', models.TextField()),
                ('status', models.CharField(choices=[('publish', 'Да'), ('unpublish', 'Нет')], max_length=55, verbose_name='Publish?')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.Author')),
                ('comments', models.ManyToManyField(to='forum.Comment')),
            ],
        ),
    ]