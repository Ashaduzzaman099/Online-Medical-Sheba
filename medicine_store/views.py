from django.db.models import Count
from .models import Medicine, Category
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

def store_view(request):
    # Retrieve all medicines
    medicines = Medicine.objects.all()

    # Retrieve all categories and annotate them with the count of medicines in each category
    categories = Category.objects.annotate(medicine_count=Count('medicines'))

    # Render the template with medicines and categories
    return render(request, 'store/medicine_store.html', {
        'medicines': medicines,
        'categories': categories
    })


def product_detail(request, id, slug):
    # Fetch the product by ID and slug
    product = get_object_or_404(Medicine, id=id, slug=slug)
    return render(request, 'store/single-product-page.html', {'product': product})

def filter_medicines(request):
    min_price = request.GET.get('min_price', 0)
    max_price = request.GET.get('max_price', 500)
    
    # Filter medicines based on price range
    medicines = Medicine.objects.filter(price__gte=min_price, price__lte=max_price)

    # Serialize medicines into JSON format
    medicines_data = [
        {
            "id": medicine.id,
            "name": medicine.name,
            "slug": medicine.slug,
            "price": medicine.price,
            "power": medicine.power,
            "thumbnail_url": medicine.thumbnail.url if medicine.thumbnail else "",
        }
        for medicine in medicines
    ]

    return JsonResponse({"medicines": medicines_data})


from django.shortcuts import render
from .models import Medicine



