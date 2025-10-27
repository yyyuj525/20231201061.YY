from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.urls import reverse
from .models import Entry, Category
from .forms import EntryForm

def entry_list(request):
    """词条列表页面"""
    entries = Entry.objects.filter(is_published=True).order_by('-created_at')
    categories = Category.objects.all()
    
    # 按分类筛选
    category_id = request.GET.get('category')
    if category_id:
        entries = entries.filter(category_id=category_id)
    
    # 搜索功能
    search_query = request.GET.get('search', '')
    if search_query:
        entries = entries.filter(title__icontains=search_query)
    
    context = {
        'entries': entries,
        'categories': categories,
        'search_query': search_query,
        'selected_category': category_id,
    }
    return render(request, 'wiki/entry_list.html', context)

def entry_detail(request, entry_id):
    """词条详情页面"""
    entry = get_object_or_404(Entry, id=entry_id, is_published=True)
    return render(request, 'wiki/entry_detail.html', {'entry': entry})

def entry_create(request):
    """创建新词条"""
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            entry = form.save()
            messages.success(request, f'词条"{entry.title}"创建成功！')
            return redirect('wiki:entry_detail', entry_id=entry.id)
    else:
        form = EntryForm()
    
    return render(request, 'wiki/entry_form.html', {'form': form, 'title': '创建新词条'})

def entry_edit(request, entry_id):
    """编辑词条"""
    entry = get_object_or_404(Entry, id=entry_id)
    
    if request.method == 'POST':
        form = EntryForm(request.POST, instance=entry)
        if form.is_valid():
            entry = form.save()
            messages.success(request, f'词条"{entry.title}"更新成功！')
            return redirect('wiki:entry_detail', entry_id=entry.id)
    else:
        form = EntryForm(instance=entry)
    
    return render(request, 'wiki/entry_form.html', {'form': form, 'title': '编辑词条'})

def entry_delete(request, entry_id):
    """删除词条"""
    entry = get_object_or_404(Entry, id=entry_id)
    
    if request.method == 'POST':
        entry_title = entry.title
        entry.delete()
        messages.success(request, f'词条"{entry_title}"已删除！')
        return redirect('wiki:entry_list')
    
    return render(request, 'wiki/entry_confirm_delete.html', {'entry': entry})

def category_list(request):
    """分类列表页面"""
    categories = Category.objects.all()
    return render(request, 'wiki/category_list.html', {'categories': categories})

def category_entries(request, category_id):
    """特定分类下的词条列表"""
    category = get_object_or_404(Category, id=category_id)
    entries = Entry.objects.filter(category=category, is_published=True).order_by('-created_at')
    return render(request, 'wiki/category_entries.html', {'category': category, 'entries': entries})
