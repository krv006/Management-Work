from django.db.models import DateTimeField, CharField, Model, BooleanField
from django.utils.text import slugify


class DeleteBasedModel(Model):
    is_deleted = BooleanField(default=False)

    class Meta:
        abstract = True


class TimeBasedModel(Model):
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class SlugBasedModel(Model):
    title = CharField(max_length=255)
    slug = CharField(max_length=255, unique=True, editable=False)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while self.__class__.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug

        super().save(*args, **kwargs)

    class Meta:
        abstract = True


class SlugTimeBasedModel(SlugBasedModel, TimeBasedModel):
    class Meta:
        abstract = True
