from django.db import models
from django.shortcuts import reverse , get_object_or_404
# Create your models here.

class Book(models.Model):
    name= models.CharField(max_length=30)
    image = models.ImageField(upload_to='books/images' ,null=True, blank=True)
    auther = models.CharField(max_length=100, null=True, blank=True , default='mohamed nasser')
    info = models.TextField(null=True, blank=True)
    borrowed = models.BooleanField(default=False)
    borrower_name = models.CharField(max_length=100, null=True, blank=True)
    borrowed_date = models.DateField(null=True, blank=True)
    price = models.IntegerField(default=300,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"

    @classmethod
    def get_all_categorys(cls):
        return cls.objects.all()

    def get_image_urls(self):
        return f"/media/{self.image}"

    @classmethod
    def get_specific_category(cls,id):
        return cls.objects.get(id=id)

    def get_show_url(self):
        return reverse('books.show', args=[self.id])

    # def get_borrow_url(self):
    #     return reverse('books.book_unavilable', args=[self.id])


    # @classmethod
    # def delete_object(cls, id):
    #     obj = get_object_or_404(cls, pk=id)
    #     if obj:
    #         obj.delete()
    #         return True


    # def get_delete_url(self):
    #     return reverse('category.delete', args=[self.id])
    #
    def get_borrow_url(self):
        return reverse('books.edit', args=[self.id])





