# Generated by Django 2.0 on 2018-07-01 21:48

from django.db import migrations, models
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0035_add_event_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='about_page',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='logo',
            field=imagekit.models.fields.ProcessedImageField(blank=True, help_text='Will be scaled and cropped to max 250x200 px.', upload_to='sponsors', verbose_name='Logo'),
        ),
        migrations.AlterField(
            model_name='team',
            name='slug',
            field=models.CharField(max_length=256, unique=True),
        ),
    ]
