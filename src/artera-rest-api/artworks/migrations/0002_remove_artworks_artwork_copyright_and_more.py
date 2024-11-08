# Generated by Django 4.2.13 on 2024-10-29 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artworks', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artworks',
            name='artwork_copyright',
        ),
        migrations.RemoveField(
            model_name='artworks',
            name='artwork_creator_list',
        ),
        migrations.RemoveField(
            model_name='artworks',
            name='artwork_dimensions',
        ),
        migrations.RemoveField(
            model_name='artworks',
            name='artwork_superuser_list',
        ),
        migrations.RemoveField(
            model_name='artworks',
            name='artwork_verification',
        ),
        migrations.AlterField(
            model_name='artworks',
            name='artwork_collections_counter',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='artworks',
            name='artwork_comments_counter',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='artworks',
            name='artwork_likes_counter',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='artworks',
            name='artwork_main_image_height',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='artworks',
            name='artwork_main_image_width',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='artworks',
            name='artwork_shares_counter',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='artworks',
            name='artwork_views_counter',
            field=models.IntegerField(default=0),
        ),
    ]
