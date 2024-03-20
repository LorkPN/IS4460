# Generated by Django 5.0.2 on 2024-03-14 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_app', '0007_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='gender',
            field=models.CharField(choices=[('woman', 'Woman'), ('man', 'Man'), ('transgender', 'Transgender (non-male/non-female)'), ('agender', 'Non-binary/Non-conforming'), (None, 'Prefer not to respond')], max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='linkedin',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='logo',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='customer',
            name='notes',
            field=models.TextField(null=True),
        ),
    ]