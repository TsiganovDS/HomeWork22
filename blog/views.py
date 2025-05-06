from audioop import reverse

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import BlogPost

class BlogListView(ListView):
    model = BlogPost
    template_name = 'blog/blog_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return super().get_queryset().filter(is_published=True)

class BlogDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/blog_detail.html'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.views_count += 1
        obj.save()
        return obj

class BlogCreateView(CreateView):
    model = BlogPost
    fields = ['title', 'content', 'preview_image', 'is_published']
    template_name = 'blog/blog_form.html'
    success_url = reverse_lazy('blog:blog_list')

class BlogUpdateView(UpdateView):
    model = BlogPost
    fields = ['title', 'content', 'preview_image', 'is_published']
    template_name = 'blog/blog_form.html'
    success_url = reverse_lazy('blog:blog_list')

    def get_success_url(self):
        return reverse('blog:blog_detail', kwargs={'pk': self.object.pk})

class BlogDeleteView(DeleteView):
    model = BlogPost
    template_name = 'blog/blog_confirm_delete.html'
    success_url = reverse_lazy('blog:blog_list')
