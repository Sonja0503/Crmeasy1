from django.views.generic import ListView
from .models import Blog
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from .forms import BlogForm
from django.views.generic.edit import DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class BlogList(ListView):

    model = Blog
    template_name = 'blog/blog_list.html'
    context_object_name = 'blog'


def user_list_blog(request, id):
    blog_post = Blog.objects.filter(blogger_id=id)
    return render(request, 'blog/user_list_blog.html', {'blog': blog_post})


def blog_new(request):

    if request.POST:
        blog = Blog(blogger=request.user)
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            redirect_url = reverse('blog_list')
            return HttpResponseRedirect(redirect_url)

    else:
        form = BlogForm()

    variables = {'form': form, }
    template = 'blog/blog_item_form.html'
    return render(request, template, variables)


def blog_cru(request, id=None):
    if id:
        blog = Blog.objects.get(id=id)

        if blog.blogger != request.user:
            raise Http404

    if request.POST:
        form = BlogForm(request.POST, instance=blog)

        if form.is_valid():
            form.save()
            redirect_url = reverse('blog_list')
            return HttpResponseRedirect(redirect_url)
    else:
        form = BlogForm(instance=blog)

    variables = {'form': form, }
    template = 'blog/blog_item_form.html'
    return render(request, template, variables)


class BlogDelete(DeleteView):
    model = Blog
    template_name = 'object_confirm_delete.html'

    def get_context_data(self, **kwargs):
        kwargs.update({'object_name': 'Blog'})
        return kwargs


    def get_object(self, queryset=None):
        obj = super(BlogDelete, self).get_object()
        if obj.blogger != self.request.user:
            raise Http404
        return obj


    def get_success_url(self):
        return reverse('blog_list')


    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(BlogDelete, self).dispatch(*args, **kwargs)




