# Generated by Django 4.1.13 on 2024-05-06 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ott', '0009_ott_category_ott_subcategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategory',
            name='name',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]