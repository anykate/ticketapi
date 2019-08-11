from django.db import models
import uuid
from django.contrib.auth.models import User
from django.utils.text import slugify


# Create your models here.
def generate_ticket_id():
    return str(uuid.uuid4()).split("-")[-1]  # generate unique ticket id


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(
        editable=False,
        unique=True,
        max_length=255
    )
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def _get_unique_slug(self):
        slug = slugify(self.name)
        unique_slug = slug
        num = 1
        while Category.objects.filter(slug=unique_slug).exists():
            unique_slug = f'{slug}-{num}'
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'categories'
        ordering = ["-created"]


class Ticket(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    ticket_id = models.CharField(max_length=255, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.ticket_id}"

    def save(self, *args, **kwargs):
        if len(self.ticket_id.strip(" ")) == 0:
            self.ticket_id = generate_ticket_id()

        # Call the real save() method
        super(Ticket, self).save(*args, **kwargs)

    class Meta:
        ordering = ["-created"]
