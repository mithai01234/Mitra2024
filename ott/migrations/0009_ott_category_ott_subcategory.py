# Generated by Django 4.2.5 on 2023-12-18 06:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ott', '0008_category_status_subcategory_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='ott',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ott.category'),
        ),
        migrations.AddField(
            model_name='ott',
            name='subcategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ott.subcategory'),
        ),
    ]
