from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0025_auto_20180325_2338'),
    ]

    operations = [
        migrations.RenameModel ("Compiler", "Language")
    ]
