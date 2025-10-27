from django.db import models
from django.utils import timezone

class Category(models.Model):
    """百科分类模型"""
    name = models.CharField(max_length=100, unique=True, verbose_name='分类名称')
    description = models.TextField(blank=True, verbose_name='分类描述')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='创建时间')
    
    class Meta:
        verbose_name = '分类'
        verbose_name_plural = '分类'
        ordering = ['name']
    
    def __str__(self):
        return self.name

class Entry(models.Model):
    """百科词条模型"""
    title = models.CharField(max_length=200, verbose_name='词条标题')
    content = models.TextField(verbose_name='词条内容')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='分类')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    is_published = models.BooleanField(default=True, verbose_name='是否发布')
    
    class Meta:
        verbose_name = '词条'
        verbose_name_plural = '词条'
        ordering = ['-created_at']
        unique_together = ['title', 'category']
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        """保存时自动更新更新时间"""
        if not self.id:
            self.created_at = timezone.now()
        super().save(*args, **kwargs)
