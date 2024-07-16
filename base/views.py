from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Car

@api_view(['GET'])
def index(req):
    return Response('hello')

@api_view(['GET'])
def test(req):
    return Response('test')

@api_view(['GET', 'POST', 'DELETE', 'PUT'])
def cars(request, id=-1):
    if request.method == 'GET':
        if int(id) > -1:
            try:
                car = Car.objects.get(id=id)
                return Response({
                    "brand": car.brand,
                    "model": car.model,
                    "price": car.price,
                    "desc": car.desc
                })
            except Car.DoesNotExist:
                return Response({"error": "Car not found"}, status=404)
        else:
            res = []
            for carObj in Car.objects.all():
                res.append({
                    "brand": carObj.brand,
                    "model": carObj.model,
                    "price": carObj.price,
                    "id": carObj.id,
                    "desc": carObj.desc
                })
            return Response(res)

    elif request.method == 'POST':
        brand = request.data.get('brand')
        model = request.data.get('model')
        price = request.data.get('price')
        desc = request.data.get('desc')
        
        if not brand or not model or not price:
            return Response({"error": "Brand, model, and price are required."}, status=400)
        
        car = Car.objects.create(brand=brand, model=model, price=price, desc=desc)
        return Response({'message': "Car created successfully", "car": {
            "id": car.id,
            "brand": car.brand,
            "model": car.model,
            "price": car.price,
            "desc": car.desc
        }}, status=201)

    elif request.method == 'DELETE':
        try:
            temp = Car.objects.get(id=id)
            temp.delete()
            return Response({'DELETE': id}, status=204)
        except Car.DoesNotExist:
            return Response({"error": "Car not found"}, status=404)

    elif request.method == 'PUT':
        try:
            temp = Car.objects.get(id=id)
            temp.price = request.data.get('price')
            temp.model = request.data.get('model')
            temp.brand = request.data.get('brand')
            temp.desc = request.data.get('desc')
            temp.save()
            return Response({'PUT': id}, status=200)
        except Car.DoesNotExist:
            return Response({"error": "Car not found"}, status=404)

    return Response({'error': 'Method not allowed'}, status=405)

