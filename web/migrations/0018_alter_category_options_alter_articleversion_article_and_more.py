# Generated by Django 4.0.6 on 2022-09-04 15:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0017_update_rimg_syntax_2'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Настройки категории',
                     'verbose_name_plural': 'Настройки категорий'},
        ),
        migrations.AlterField(
            model_name='articleversion',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                    related_name='versions', to='web.article', verbose_name='Статья'),
        ),
        migrations.AddIndex(
            model_name='article',
            index=models.Index(fields=['created_at'],
                               name='web_article_created_5524a8_idx'),
        ),
        migrations.AddIndex(
            model_name='article',
            index=models.Index(fields=['updated_at'],
                               name='web_article_updated_20aa03_idx'),
        ),
        migrations.AddIndex(
            model_name='vote',
            index=models.Index(fields=['article'],
                               name='web_vote_article_a54b49_idx'),
        ),
    ]
