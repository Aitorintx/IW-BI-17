# Generated by Django 4.2.7 on 2023-11-09 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appPromoConcert', '0003_alter_festival_idpromotor'),
    ]

    operations = [
        migrations.AddField(
            model_name='interprete',
            name='festivales',
            field=models.ManyToManyField(to='appPromoConcert.festival'),
        ),
        migrations.DeleteModel(
            name='Actuacion',
        ),
    ]