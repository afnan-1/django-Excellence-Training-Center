# from django.views import ListView
from django.http import Http404
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Product

#Featured section

class ProductFeaturedListView(ListView):
	template_name = "products/list.html"

	def get_queryset(self, *args, **kwargs):
		request = self.request
		return Product.objects.featured()


class ProductFeaturedDetailView(DetailView):
	template_name = "products/featured-detail.html"

	def get_queryset(self, *args, **kwargs):
		request = self.request
		return Product.objects.featured()



# list section

class ProductListView(ListView):
	queryset = Product.objects.all()
	template_name = "products/list.html"

	def get_context_data(self, *args, **kwargs):
		context = super(ProductListView, self).get_context_data(*args,**kwargs)
		print(context)
		return context


def product_list_view(request):
	queryset = Product.objects.all()
	context = {
		'object_list': queryset
	}

	return render(request,"products/list.html", context)




#detailed View section


class ProductDetailSlugView(DetailView):
	queryset = Product.objects.all()
	template_name = "products/detail.html"

	# def get_object(self, *args, **kwargs):
	# 	request = self.request
	# 	slug = self.kwargs.get('slug')
	# 	# instance = Product.objects.get_by_id(pk)
	# 	try:
	# 		instance = Product.objects.get(slug=slug, active=True)
	# 	except Product.DoesNotExist:
	# 		raise Http404("sorry product is not there")
	# 	except Product.MultipleObjectsReturned:
	# 		qs = Product.objects.filter(slug=slug, active=True)
	# 		instance = qs.first()
	# 	except:
	# 		raise Http404("u sure ??")
	# 	return instance

class ProductDetailView(DetailView):
	# queryset = Product.objects.all()
	template_name = "products/detail.html"

	def get_context_data(self, *args, **kwargs):
		context = super(ProductDetailView, self).get_context_data(*args,**kwargs)
		print(context)
		return context

	def get_object(self, *args, **kwargs):
		request = self.request
		pk = self.kwargs.get('pk')
		instance = Product.objects.get_by_id(pk)
		if instance is None:
			raise Http404("Product is non existing please check your spelling")
		return instance

	# def get_queryset(self, *args, **kwargs):
	# 	request = self.request
	# 	pk= self.kwargs.get('pk')
	# 	return Product.objects.filter(pk=pk)


def product_detail_view(request, pk=None, *args, **kwargs):
	# instance = get_object_or_404(Product, pk=pk) #ID

	instance = Product.objects.get_by_id(pk)
	if instance is None:
		raise Http404("Product is non existing please check your spelling")
	# qs = Product.objects.filter(id=pk)
	
	# if qs.exists() and qs.count() == 1: #len(qs)
	# 	instance = qs.first()

	# else:
	# 	raise Http404("Please go back and search for new product")

	context = {
		'object': instance
	}

	return render(request,"products/detail.html", context)