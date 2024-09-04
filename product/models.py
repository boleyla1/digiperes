from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Size(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'سایز'
        verbose_name_plural = 'سایز'

    def __str__(self):
        return self.title


class Color(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'رنگ'
        verbose_name_plural = 'رنگ'

    def __str__(self):
        return self.title


# class Image(models.Model):
#     title = models.CharField(max_length=100, blank=True, null=True, verbose_name="نام عکس")
#     image = models.ImageField(upload_to='products_img/', verbose_name='عکس کالا')
#
#     def __str__(self):
#         return self.image.name


class Category(models.Model):
    name = models.CharField(max_length=100,verbose_name='نام دسته بندی')
    image = models.ImageField(upload_to='category_img/', null=True, blank=True)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=100,verbose_name="نام برند")
    image = models.ImageField(upload_to='brand_img/', blank=True, null=True,verbose_name="عکس برند")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True, blank=True)
    category = models.ManyToManyField(Category)
    title = models.CharField(max_length=100, verbose_name='نام محصول')
    discription = models.TextField("توضیحات")
    price = models.FloatField(verbose_name='قیمت')
    discount = models.SmallIntegerField(verbose_name='تخفیف', default=0)
    size = models.ManyToManyField(Size, blank=True, null=True, verbose_name='سایز', related_name='محصولات')
    color = models.ManyToManyField(Color, blank=True, null=True, related_name='محصولات', verbose_name='رنگ')
    # image = models.ManyToManyField(Image, blank=True)
    pictur = models.ImageField(upload_to='product_img/', blank=True, null=True)
    Star = models.IntegerField(default=0, validators=(MinValueValidator(0), MaxValueValidator(5)))
    Offer = models.BooleanField(default=False)
    OfferPrice = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'محصولات'
        verbose_name_plural = 'محصولات'

    def __str__(self):
        return self.title


class Information(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, related_name='اطلاعات')
    text = models.TextField()

    def __str__(self):
        return self.text[:30]



# Create your models here.
