# Generated by Django 4.0.5 on 2022-08-11 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='نام مقاله')),
                ('article_text', models.TextField(verbose_name='متن مقاله')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال/غیر فعال')),
                ('status', models.CharField(choices=[('draft', 'draft'), ('publish', 'publish')], max_length=50, verbose_name='وضعیت')),
            ],
        ),
    ]
