# Generated by Django 4.0.6 on 2022-07-11 08:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_product_options_alter_product_creator'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='creator',
            new_name='manufacturer',
        ),
    ]