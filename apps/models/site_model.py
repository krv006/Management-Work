from django.db.models import CharField, DateTimeField, Model, ForeignKey, TextField, CASCADE

from apps.models import TimeBasedModel


class Question(Model):
    text = CharField(max_length=255, verbose_name="Savol matni")
    created_at = DateTimeField(auto_now_add=True, verbose_name="Yaratilgan vaqt")

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Savol"
        verbose_name_plural = "Savollar"


class Answer(Model):
    question = ForeignKey('apps.Question', CASCADE, related_name="answers", verbose_name="Savol")
    text = TextField(verbose_name="Javob matni")
    created_at = DateTimeField(auto_now_add=True, verbose_name="Yaratilgan vaqt")

    def __str__(self):
        return f"Javob: {self.text[:50]}..."

    class Meta:
        verbose_name = "Javob"
        verbose_name_plural = "Javoblar"


class SiteSettings(TimeBasedModel):
    region_to_region = CharField(max_length=255, help_text='Samarqand, Jizzax, Buxoro ...')
