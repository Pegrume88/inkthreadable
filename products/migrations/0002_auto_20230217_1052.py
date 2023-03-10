# Generated by Django 3.2 on 2023-02-17 10:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='created',
            new_name='created_at',
        ),
        migrations.RemoveField(
            model_name='review',
            name='review_star',
        ),
        migrations.AddField(
            model_name='review',
            name='review_rating',
            field=models.IntegerField(default=3),
        ),
        migrations.AlterField(
            model_name='review',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='products.product'),
        ),
    ]
