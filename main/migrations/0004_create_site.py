from django.db import migrations

def create_site(apps, schema_editor):
    Site = apps.get_model('sites', 'Site')
    Site.objects.update_or_create(
        id=1,
        defaults={
            'domain': 'cliqueseguro.onrender.com',
            'name': 'Clique Seguro',
        }
    )

class Migration(migrations.Migration):
    dependencies = [
        ('main', '0003_passo_html_interativo_alter_passo_interactiveimage'),
        ('sites', '0002_alter_domain_unique'),
    ]

    operations = [
        migrations.RunPython(create_site, migrations.RunPython.noop),
    ]