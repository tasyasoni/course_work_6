from django.db import models


NULLABLE = {'null': True, 'blank': True}

class Blog(models.Model):
    header = models.CharField(max_length=100, verbose_name='заголовок')
    blog_content = models.TextField(max_length=500, verbose_name='содержимое')
    picture = models.ImageField(upload_to = 'blog', verbose_name='картинка', **NULLABLE)
    public_sign = models.BooleanField(default=True, verbose_name='признак_публикации')
    number_of_views = models.IntegerField(default=0, verbose_name='количество просмотров')


    def __str__(self):
        return  f'{self.header}'


    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'