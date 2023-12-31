# Generated by Django 4.2.3 on 2023-07-25 14:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('noticias', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_publicacion', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('fecha_modificacion', models.DateTimeField(auto_now=True, verbose_name='modified at')),
                ('texto', models.TextField(max_length=1000)),
                ('autor', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('noticia', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='noticias.noticia')),
            ],
        ),
    ]
