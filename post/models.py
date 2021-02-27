from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.shortcuts import reverse

# Create your models here.
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=250,verbose_name='Kategori')
    class Meta:
        verbose_name = 'Kategori'
        verbose_name_plural = 'Kategoriler'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')

class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=Category, verbose_name='Kategori')
    title = models.CharField(max_length=150, verbose_name='Başlık')
    description = RichTextField(verbose_name='Açıklama', blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Oluşturma Tarihi')
    is_published = models.BooleanField(verbose_name='Yayında mı ?', default=True)
    image = models.CharField(max_length=200, verbose_name='Fotoğraf Adı')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Yazar Adı')
    snippet = models.TextField(max_length=200)
    slug = models.SlugField(unique=True, editable=False, max_length=160)
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Postlar'
        get_latest_by = 'created_date'

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_image_path(self):
        return '/img/'+ self.image

    def get_absolute_url(self):
        return reverse('post')

    def get_detail_url(self):
        return reverse('details', kwargs={'pk': self.id})

    def save(self, *args, **kwargs):
        self.slug = self._get_unique_slug()
        return super(Post, self).save(*args, **kwargs)

    def _get_unique_slug(self):
        slug = slugify(self.title.replace('ı', 'i'))
        unique_slug = slug
        counter = 1
        while Post.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, counter)
            counter += 1
        return unique_slug



class Comments(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name_lname = models.CharField(max_length=200, verbose_name='Ad-Soyad')
    email = models.EmailField(verbose_name='Email Adresi')
    comment = models.TextField(verbose_name='Yorum')
    comment_date = models.DateTimeField(auto_now_add=True, verbose_name='Yorum Tarihi')

    class Meta:
        verbose_name = 'Yorum'
        verbose_name_plural = 'Yorumlar'

    
    def __str__(self):
        return '%s - %s' % (self.post.title, self.name_lname)