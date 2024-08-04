from django.db import models

class ArticleCategory(models.Model):
    name = models.CharField(max_length=200)
        
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Makala kategoriýa"
        verbose_name_plural = "Makala kategoriýalary"
        ordering = ['name']
        db_table = 'article_categories'


class Arcticle(models.Model):
    title = models.TextField()
    file = models.FileField(upload_to='documents/')
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(ArticleCategory, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    user_name = models.CharField(max_length=200,default='Admin',blank=True, null=True)
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Makala"
        verbose_name_plural = "Makalalar"
        ordering = ['title']
        db_table = 'articles'

