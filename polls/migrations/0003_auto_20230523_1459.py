# Generated by Django 3.2 on 2023-05-23 14:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_poll_approved'),
    ]

    operations = [
        migrations.RenameField(
            model_name='poll',
            old_name='option_one',
            new_name='choice_one',
        ),
        migrations.RenameField(
            model_name='poll',
            old_name='option_one_count',
            new_name='choice_one_count',
        ),
        migrations.RenameField(
            model_name='poll',
            old_name='option_three',
            new_name='choice_three',
        ),
        migrations.RenameField(
            model_name='poll',
            old_name='option_three_count',
            new_name='choice_three_count',
        ),
        migrations.RenameField(
            model_name='poll',
            old_name='option_two',
            new_name='choice_two',
        ),
        migrations.RenameField(
            model_name='poll',
            old_name='option_two_count',
            new_name='choice_two_count',
        ),
    ]
