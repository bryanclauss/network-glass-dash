# Generated by Django 2.1 on 2019-03-06 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='site',
            field=models.CharField(blank=True, choices=[('Short_Hills_101', 'Short Hills 101'), ('Short_Hills_103', 'Short Hills 103'), ('Center_Valley', 'Center Valley'), ('Austin', 'Austin'), ('Waltham', 'Waltham'), ('irvine', 'irvine'), ('Santa_Clara', 'Santa Clara'), ('Charlotte', 'Charlotte'), ('Chicago', 'Chicago'), ('Atlanta', 'Atlanta'), ('Naperville', 'Naperville'), ('Orange', 'Orange'), ('Portland', 'Portland'), ('Reston', 'Reston'), ('San_Francisco', 'San Francisco'), ('Dallas', 'Dallas'), ('London', 'London'), ('Dublin', 'Dublin'), ('Marlow', 'Marlow'), ('Cardiff', 'Cardiff'), ('Shelton', 'Shelton'), ('New_York_City', 'New York City'), ('Portland', 'Portland'), ('Independence', 'Independence'), ('Mississauga', 'Mississauga'), ('Calgary', 'Calgary'), ('Mumbai', 'Mumbai'), ('Ashburn', 'Ashburn'), ('Seatle', 'Seatle'), ('Sydney', 'Sydney'), ('Singapore', 'Singapore'), ('London', 'London')], max_length=30),
        ),
    ]
