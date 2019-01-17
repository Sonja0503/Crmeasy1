from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class Blog(models.Model):
    blogger = models.ForeignKey(User)
    title = models.CharField(max_length=20)
    text_area = models.TextField()
    created_on = models.DateField(auto_now_add=True)
    like = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'blog'
        ordering = ('-created_on', )

    def __unicode__(self):
        return u"{}".format(self.title)

    def get_absolute_url(self):
        return reverse('user_list_blog', args=(self.blogger.id, ))

    def get_update_url(self):
        return reverse('blog_cru', args=(self.id, ))

    def get_delete_url(self):
        return reverse('blog_delete', args=(self.id, ))
