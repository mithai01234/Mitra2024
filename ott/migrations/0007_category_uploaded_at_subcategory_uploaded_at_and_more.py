# Generated by Django 4.2.5 on 2023-12-18 05:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ott', '0006_category_subcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='uploaded_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subcategory',
            name='uploaded_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
