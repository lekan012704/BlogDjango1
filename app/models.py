from email.mime import image
from turtle import title
from unicodedata import category
from django.db import models

# Create your models here.
class Blog(models.Model):
  title = models.CharField(max_length=100)
  content = models.TextField()
  image = models.ImageField(upload_to='images/')
  author = models.CharField(max_length=100)
  category = models.ForeignKey(category, on_delete=models.CASCADE)
  slug = models.SlugField(max_length=100, unique=True)
  created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Blog")
        verbose_name_plural = _("Blogs")

    def __str__(self):
        return self.name

    def save:
        slug = slugify(self.name)
        self.slug = slugify(slug,allow_unicode=True
        )
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("blog:detail", kwargs={"slug": self.slug})

    def get_absolute_url(self):
        return reverse("Blog_detail", kwargs={"pk": self.pk})
