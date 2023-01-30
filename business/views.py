from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests

from business.models import Business
from app.models import App

@api_view(['GET'])
def Index(request):
    data = {
    }

    return Response(data)




@api_view(['POST'])
def Add(request):
    if request.method == 'POST':


        auth_code =request.data["auth_code"]
        name =request.data["name"]
        category =request.data["category"]
        location =request.data["location"]
        bio =request.data["bio"]
        email =request.data["email"]
        phone =request.data["phone"]
        address =request.data["address"]


        try:
            app_user = App.objects.get(auth_code=auth_code)

            business = Business.objects.create(app_user=app_user, name=name, category=category,
            location=location, bio=bio, email=email, phone=phone, address=address)
            business.save()

            data = {"detail": "Business created successfully",
            "status_lean": True, "business_id": business.id}
            return Response(data)

        except:

            data = {"detail": "Error!!", "status_lean": False}
            return Response(data)


@api_view(['POST'])
def Edit(request):
    if request.method == 'POST':

        auth_code =request.data["auth_code"]
        business_id =request.data["business_id"]

        name =request.data["name"]
        category =request.data["category"]
        location =request.data["location"]
        bio =request.data["bio"]
        email =request.data["email"]
        phone =request.data["phone"]
        address =request.data["address"]


        try:
            app_user = App.objects.get(auth_code=auth_code)

            business = Business.objects.get(id=business_id)
            business.name = name
            business.category = category
            business.location = location
            business.bio = bio
            business.email = email
            business.phone = phone
            business.address = address
            business.save()

            data = {"detail": "Business edit successfully",
            "status_lean": True, "business_id": business.id}
            return Response(data)

        except:

            data = {"detail": "Error!!", "status_lean": False}
            return Response(data)





@api_view(['POST'])
def Delete(request):
    if request.method == 'POST':

        auth_code =request.data["auth_code"]
        business_id =request.data["business_id"]

        try:
            app_user = App.objects.get(auth_code=auth_code)

            business = Business.objects.get(id=business_id)
            business.status = False
            business.save()

            data = {"detail": "Business removed successfully",
            "status_lean": True, "business_id": business.id}
            return Response(data)

        except:

            data = {"detail": "Error!!", "status_lean": False}
            return Response(data)


