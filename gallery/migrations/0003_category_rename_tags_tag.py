# Generated by Django 4.0.4 on 2022-05-27 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_tags_alter_editor_options_editor_phone_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('F', 'Food'), ('Ent', 'Entertainment')], max_length=3)),
            ],
        ),
        migrations.RenameModel(
            old_name='tags',
            new_name='tag',
        ),
    ]
