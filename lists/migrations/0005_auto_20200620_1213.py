# Generated by Django 3.0.7 on 2020-06-20 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0004_item_list'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ('id',)},
        ),
        migrations.AddConstraint(
            model_name='item',
            constraint=models.UniqueConstraint(fields=('list', 'text'), name='unique_item'),
        ),
    ]