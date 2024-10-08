# Generated by Django 5.0.4 on 2024-06-05 05:19

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cursussen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naam', models.CharField(max_length=64)),
                ('beschrijving', models.CharField(blank=True, max_length=640)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_teacher', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, related_name='user_groups', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, related_name='user_user_permissions', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='IngschrCursus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voortgang', models.IntegerField(default=0)),
                ('cursus', models.ForeignKey(db_column='cursussen_id', on_delete=django.db.models.deletion.DO_NOTHING, to='game.cursussen')),
                ('student', models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='ingschr_cursus',
            field=models.ManyToManyField(blank=True, through='game.IngschrCursus', to='game.cursussen'),
        ),
        migrations.CreateModel(
            name='Modules',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('naam', models.CharField(max_length=64)),
                ('beschrijving', models.CharField(blank=True, max_length=640)),
                ('cursus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.cursussen')),
            ],
        ),
        migrations.CreateModel(
            name='HoofdOpdrachten',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naam', models.CharField(max_length=64)),
                ('beschrijving', models.CharField(blank=True, max_length=640)),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.modules')),
            ],
        ),
        migrations.CreateModel(
            name='ConceptOpdracht',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naam', models.CharField(max_length=64)),
                ('beschrijving', models.CharField(blank=True, max_length=640)),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.modules')),
            ],
            options={
                'db_table': 'game_conceptopdracht',
            },
        ),
        migrations.CreateModel(
            name='Activiteiten',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naam', models.CharField(max_length=64)),
                ('beschrijving', models.CharField(blank=True, max_length=640)),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.modules')),
            ],
        ),
        migrations.CreateModel(
            name='Niveaus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beschrijving', models.CharField(blank=True, max_length=640)),
                ('activiteit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.activiteiten')),
            ],
        ),
        migrations.CreateModel(
            name='PuntenUitdagingen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('benodige_punten', models.IntegerField()),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.modules')),
            ],
        ),
        migrations.CreateModel(
            name='VoortgangActiviteitenNiveaus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voortgang', models.IntegerField(default=0)),
                ('niveau', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='game.niveaus')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='voortgang_activiteit_niveaus',
            field=models.ManyToManyField(blank=True, through='game.VoortgangActiviteitenNiveaus', to='game.niveaus'),
        ),
        migrations.CreateModel(
            name='VoortgangConceptOpdrachten',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voortgang', models.BooleanField(default=False)),
                ('concept_opdracht', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='game.conceptopdracht')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='voortgang_concept_opdracht',
            field=models.ManyToManyField(blank=True, through='game.VoortgangConceptOpdrachten', to='game.conceptopdracht'),
        ),
        migrations.CreateModel(
            name='VoortgangHoofdOpdrachten',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voortgang', models.BooleanField(default=False)),
                ('hoofd_opdracht', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='game.hoofdopdrachten')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='voortgang_hoofd_opdracht',
            field=models.ManyToManyField(blank=True, through='game.VoortgangHoofdOpdrachten', to='game.hoofdopdrachten'),
        ),
        migrations.CreateModel(
            name='VoortgangPuntenUitdaging',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voortgang', models.BooleanField(default=False)),
                ('punten_uitdaging', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='game.puntenuitdagingen')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='voortgang_punten_uitdaging',
            field=models.ManyToManyField(blank=True, through='game.VoortgangPuntenUitdaging', to='game.puntenuitdagingen'),
        ),
    ]
