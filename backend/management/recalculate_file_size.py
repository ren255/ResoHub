from django.core.management.base import BaseCommand
from yourapp.models import TextFileStorage


class Command(BaseCommand):
    help = "TextFileStorageのfile_sizeとmime_typeを再計算する"

    def handle(self, *args, **options):
        objs = TextFileStorage.objects.all()
        self.stdout.write(f"対象件数: {objs.count()}件")

        for obj in objs.iterator():
            obj.save()
            self.stdout.write(f"✓ {obj.key}: {obj.file_size} bytes")

        self.stdout.write("完了!")
