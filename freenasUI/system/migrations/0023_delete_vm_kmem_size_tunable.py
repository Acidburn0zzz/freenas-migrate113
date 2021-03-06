from django.db import migrations


def delete_vm_kmem_size(apps, schemaeditor):
    tunables = apps.get_model('system', 'tunable')
    kmem_size_tunable = tunables.objects.filter(tun_var='vm.kmem_size',
                                                tun_comment='Generated by autotune')
    kmem_size_tunable.delete()


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0022_cert_serial'),
    ]

    operations = [
        migrations.RunPython(
            delete_vm_kmem_size
        ),
    ]
