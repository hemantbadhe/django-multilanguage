# Generated by Django 2.2.4 on 2019-08-08 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('title_en', models.CharField(max_length=255, null=True)),
                ('title_ur', models.CharField(max_length=255, null=True)),
                ('title_mr', models.CharField(max_length=255, null=True)),
                ('text', models.TextField()),
                ('text_en', models.TextField(null=True)),
                ('text_ur', models.TextField(null=True)),
                ('text_mr', models.TextField(null=True)),
            ],
        ),
    ]