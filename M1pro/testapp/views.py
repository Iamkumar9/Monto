from django.shortcuts import render
from django.template.defaultfilters import title
from django.views import View
from testapp.models import Product
from django.db.models import Count
from django.shortcuts import get_object_or_404
from django.db import models  # This will import the models module
from  testapp.forms import CustomerRegistrationForm
from django.contrib import messages
from django.db.models import Q

def home(request):
    return render(request, 'myapp/home.html')

CATEGORY_MAPPING = {
    'casuals': 'CW',
    'formals': 'FW',
    'sports': 'SW',
    'outwear': 'OW',
    'new-arrivals': 'NA'
}
class CategoryView(View):
    def get(self, request, gender, category):
        gender = gender.upper()
        category = CATEGORY_MAPPING.get(category.lower(), None)  # Default to None if not found
        products = Product.objects.filter(gender=gender, category=category)
        print(f"Filtered Products for Gender: {gender} and Category: {category}: {products}")
        titles = products.values('title').annotate(count=models.Count('title'))
        print(f"Titles and counts: {titles}")


        return render(request, 'myapp/category.html', {
            'products': products,
            'gender': gender,
            'category': category,
            'title': titles  # Pass the titles with their count
        })

class Productdetail(View):
    def get(self, request, pk):
        product = get_object_or_404(Product, id=pk)
        wishlist = False  # Add your wishlist logic here

        # Fetch similar products (e.g., same category or random)
        similar_products = Product.objects.filter(category=product.category).exclude(id=product.id)[:]

        return render(request, 'myapp/productdetail.html', {
            'product': product,
            'wishlist': wishlist,
            'similar_products': similar_products,
        })
class CategoryTitle(View):
    def get(self, request, val):
        product = Product.objects.filter(title=val)
        if not product.exists():
            return render(request, "myapp/category.html", {
                'products': [],
                'titles': [],
                'error': f"No products found with the title '{val}'."
            })

        category = product.first().category
        titles = Product.objects.filter(category=category).values('title').distinct()
        return render(request, "myapp/category.html", {
            'products': product,
            'titles': titles
        })
class CustomerRegistrationView(View):
    def get(self,request):
        form = CustomerRegistrationForm()
        return render(request, 'myapp/customerregistration.html',locals())
    def post(self,request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Congratulations! User Register Successfully")
        else:
            messages.warning(request,"Invalid Input Data")
        return render(request, 'myapp/customerregistration.html',locals())


