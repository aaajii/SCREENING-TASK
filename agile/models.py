from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['created_at']


class Content(models.Model):
    order = models.IntegerField()
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 related_name="content")
    item = models.CharField(max_length=100)
    details = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s.) %s" % (self.order, self.item)

    def category_name(self):
        return self.category.name

    class Meta:
        ordering = ['created_at', 'order']
