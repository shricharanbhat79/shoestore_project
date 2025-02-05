from django.db import models
from django.urls import reverse

#Category Model
class Category(models.Model):
	name = models.CharField(max_length=250, unique=True)
	slug = models.SlugField(max_length=250, unique=True)
	description = models.TextField(blank=True)
	image = models.ImageField(upload_to='category', blank=True)

	class Meta:
		ordering = ('name',)
		verbose_name = 'category'
		verbose_name_plural = 'categories'

	def get_url(self):
		return reverse('shop:products_by_category', args=[self.slug])

	def __str__(self):
		return '{}'.format(self.name)

#Product Model
class Product(models.Model):
	name = models.CharField(max_length=250, unique=True)
	slug = models.SlugField(max_length=250, unique=True)
	description = models.TextField(blank=True)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	image = models.ImageField(upload_to='product', blank=True)
	stock = models.IntegerField()
	available = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ('name',)
		verbose_name = 'product'
		verbose_name_plural = 'products'

	def get_url(self):
		return reverse('shop:ProdCatDetail', args=[self.category.slug, self.slug])

	def __str__(self):
		return '{}'.format(self.name)

#Shoe Size Variation Model
class VariationManager(models.Manager):
	def sizes(self):
		return super(VariationManager, self).filter(variation_category='size', is_active=True)

variation_category_choice = (
    ('size', 'size'),
)

class Variation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variation_category = models.CharField(max_length=100, choices=variation_category_choice)
    variation_value     = models.CharField(max_length=100)
    is_active           = models.BooleanField(default=True)
    created_date        = models.DateTimeField(auto_now=True)

    objects = VariationManager()

    def __str__(self):
        return self.variation_value