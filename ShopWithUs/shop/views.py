from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Contact, Order, OrderUpdate
from math import ceil
import json


def index(request):
    # Fetching products from models
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds': allProds}
    return render(request, 'shop/index.html', params)


def matchProd(query, item):
    if query in item.description.lower() or query in item.product_name.lower() or query in item.category.lower():
        return True
    else:
        return False


def search(request):
    query = request.GET.get('search')
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prodTemp = Product.objects.filter(category=cat)
        prod = [item for item in prodTemp if matchProd(query, item)]
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        if len(prod) != 0:
            allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds': allProds}
    return render(request, 'shop/search.html', params)


def about(request):
    return render(request, "shop/about.html")


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        phone = request.POST.get("phone", "")
        desc = request.POST.get("desc", "")
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()

    return render(request, "shop/contact.html")


def tracker(request):
    if request.method == "POST":
        order_id = request.POST.get("order_id", "")
        email = request.POST.get("email", "")

        try:
            order = Order.objects.filter(order_id=order_id, email=email)
            if len(order) > 0:
                # Matching Given order_id to order_id in model
                update = OrderUpdate.objects.filter(order_id=order_id)
                updates = []
                for item in update:
                    updates.append(
                        {"text": item.update_desc, "time": item.timestamp})
                    # Getting update details from 'OrderUPdate; model and Order Details from 'Order' model
                    response = json.dumps(
                        {"status":"success", "updates":updates, "itemjson": order[0].item_json}, default=str)
                return HttpResponse(response)

            else:
                return HttpResponse('{"status":"No Item with this Order Id"}')

        except Exception as e:
            return HttpResponse('{"status":"error"}')

    return render(request, "shop/tracker.html")


def product(request, myid):
    # Fetch the product using product_id
    product = Product.objects.filter(id=myid)

    return render(request, "shop/prodView.html", {'product': product[0]})


def checkout(request):
    if request.method == "POST":
        item_json = request.POST.get("itemJson", "")
        amount = request.POST.get("amount", "")
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        phone = request.POST.get("phone", "")
        address = request.POST.get("address1", "") + \
            request.POST.get("address2", "")
        state = request.POST.get("state", "")
        city = request.POST.get("city", "")
        zip_code = request.POST.get("zip_code", "")

        order = Order(item_json=item_json, amount=amount, name=name, email=email, phone=phone,
                      address=address, state=state, city=city, zip_code=zip_code)
        order.save()
        update = OrderUpdate(order_id=order.order_id,
                             update_desc="The Order has been placed.")

        thank = True
        id = order.order_id

        return render(request, "shop/checkout.html", {'thank': thank, 'id': id})
    return render(request, "shop/checkout.html")
