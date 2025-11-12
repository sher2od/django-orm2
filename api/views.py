import json

from django.http import HttpRequest,JsonResponse

from .models import Product

def to_json(product: Product) -> dict:
    return {
        "id": product.id,
        "name": product.name,
        "category": product.category,
        "price": product.price,
        "quantity": product.quantity,
        "rating": product.rating,
        "active": product.active,
        "created_at": product.created_at.strftime('%d/%m/%Y, %H:%M:%S'),
        "updated_at": product.updated_at.strftime('%d/%m/%Y, %H:%M:%S'),

        }


def products_view(request: HttpRequest) -> JsonResponse:
    # POST ->> Yangi productlar qo'shish
    if request.method == "POST":
        result = []
        for data in json.loads(request.body.decode()):
        
            new_product = Product(
                name = data['name'],
                category = data['category'],
                price = data['price'],
                quantity = data['quantity'],
                active = data['active'],
                rating = data['rating']
            )
            new_product.save()
            result.append(to_json(new_product))

        return JsonResponse(data={'result':result,'count':len(result)},status=201)
    
    # GET ->> productlarni olish (filter bilan)
    if request.method == "GET":
        params = request.GET
        products = Product.objects.all()

        #  TODO Kategorya bo'yicha filter
        category = params.get('category')
        if category:
            products = products.filter(category=category)

        # TODO Narix boyicha Filter
        min_price = params.get('min_price')
        max_price = params.get('max_price')
        if min_price and max_price:
            products = products.filter(price__gte=min_price,price__lte=max_price)

        result = []
        for product in products:
            result.append(to_json(product))

        return JsonResponse(data = {'count': len(result),'result': result})
    return JsonResponse(data={})



    