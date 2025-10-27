from django import forms
from .models import Entry, Category

class EntryForm(forms.ModelForm):
    """词条表单"""
    class Meta:
        model = Entry
        fields = ['title', 'content', 'category', 'is_published']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '请输入词条标题'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': '请输入词条内容',
                'rows': 10
            }),
            'category': forms.Select(attrs={
                'class': 'form-control'
            }),
            'is_published': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            })
        }
        labels = {
            'title': '词条标题',
            'content': '词条内容',
            'category': '分类',
            'is_published': '是否发布'
        }
    
    def clean_title(self):
        """验证标题唯一性"""
        title = self.cleaned_data.get('title')
        category = self.cleaned_data.get('category')
        
        if self.instance and self.instance.pk:
            # 编辑现有词条时，排除自身
            if Entry.objects.filter(title=title, category=category).exclude(pk=self.instance.pk).exists():
                raise forms.ValidationError('该分类下已存在相同标题的词条')
        else:
            # 创建新词条时
            if Entry.objects.filter(title=title, category=category).exists():
                raise forms.ValidationError('该分类下已存在相同标题的词条')
        
        return title

class CategoryForm(forms.ModelForm):
    """分类表单"""
    class Meta:
        model = Category
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '请输入分类名称'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': '请输入分类描述',
                'rows': 3
            })
        }
        labels = {
            'name': '分类名称',
            'description': '分类描述'
        }