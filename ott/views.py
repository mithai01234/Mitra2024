# yourapp/views.py
from rest_framework import viewsets
from .models import Ott,Category,Subcategory
from .serializers import UploadedContentSerializer
from django.shortcuts import render
# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from registration.models import CustomUser
from rest_framework import generics
from registration.serializers import CustomUserSerializer
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='backend/login')
def Ottlist(request):
    registerapp=Ott.objects.all()
    context={
        'regform': registerapp



    }
    return render(request,'backend/ottlist.html',context)
# views.py
from django.http import JsonResponse

def get_subcategories(request):
    category_id = request.GET.get('category_id')
    subcategories = Subcategory.objects.filter(category_id=category_id).values('id', 'name')
    return JsonResponse(list(subcategories), safe=False)

@login_required(login_url='backend/login')
def add_account(request):
    categories = Category.objects.all()
    subcategories = Subcategory.objects.all()

    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        video_file = request.FILES.get('video')
        thumbnail_file = request.FILES.get('thumbnail')
        category_id = request.POST.get('category')
        subcategory_id = request.POST.get('subcategory')

        # Check if the selected category and subcategory exist
        try:
            category = Category.objects.get(pk=category_id)
        except Category.DoesNotExist:
            # Handle the case where the selected category doesn't exist
            # You might want to add an error message or redirect to an error page
            return render(request, 'backend/uploadott.html', {'categories': categories, 'subcategories': subcategories})

        try:
            subcategory = Subcategory.objects.get(pk=subcategory_id)
        except Subcategory.DoesNotExist:
            # Handle the case where the selected subcategory doesn't exist
            # You might want to add an error message or redirect to an error page
            return render(request, 'backend/uploadott.html', {'categories': categories, 'subcategories': subcategories})

        ott_instance = Ott(
            title=title,
            description=description,
            file=video_file,
            thumbnail=thumbnail_file,
            category=category,
            subcategory=subcategory
        )

        ott_instance.save()

        return redirect('ottlist')  # Redirect to a view that displays a list of Ott items

    return render(request, 'backend/uploadott.html', {'categories': categories, 'subcategories': subcategories})
@login_required(login_url='backend/login')
def add_category(request):
    if request.method == "POST":
        contact = Category()
        description = request.POST.get('description')
        name = request.POST.get('name')


        contact.name = name
        contact.description =description

        contact.save()

        return redirect('category_list')
    return render(request, 'backend/addcategory.html')

@login_required(login_url='backend/login')
def add_subcategory(request):
    categories = Category.objects.all()

    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        category_id = request.POST.get('category')

        # Check if the selected category exists
        try:
            category = Category.objects.get(pk=category_id)
        except Category.DoesNotExist:
            # Handle the case where the selected category doesn't exist
            # You might want to add an error message or redirect to an error page
            return render(request, 'backend/addsubcategory.html', {'categories': categories})

        subcategory = Subcategory(name=name, description=description, category=category)
        subcategory.save()

        # Optionally, add a success message
        return redirect('subcategory_list')  # Redirect to a view that displays a list of subcategories

    return render(request, 'backend/addsubcategory.html', {'categories': categories})
@login_required(login_url='backend/login')
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'backend/categorylist.html', {'categories': categories})
@login_required(login_url='backend/login')
def subcategory_list(request):
    subcategories = Subcategory.objects.all()
    return render(request, 'backend/subcategorylist.html', {'subcategories': subcategories})
@login_required(login_url='backend/login')
def activate_product(request, id):
    banner = get_object_or_404(Ott, id=id)
    banner.status = True
    banner.save()
    return redirect('ottlist')  # Redirect to your banner list view
@login_required(login_url='backend/login')
def deactivate_product(request, id):
    banner = get_object_or_404(Ott, id=id)
    banner.status = False
    banner.save()
    return redirect('ottlist')  # Redirect to your banner list view
@login_required(login_url='backend/login')
def delete_item(request, myid):
    productapp = Ott.objects.get(id=myid)
    productapp.delete()
    return redirect('ottlist')
@login_required(login_url='backend/login')
def edit_account(request, ott_id):
    ott_instance = get_object_or_404(Ott, id=ott_id)

    if request.method == "POST":
        # Update Ott instance with form data
        ott_instance.title = request.POST.get('title')
        ott_instance.description = request.POST.get('description')

        # Handle video file
        video_file = request.FILES.get('video')
        if video_file:
            ott_instance.file = video_file

        # Handle thumbnail file
        thumbnail_file = request.FILES.get('thumbnail')
        if thumbnail_file:
            ott_instance.thumbnail = thumbnail_file

        # Save Ott instance
        ott_instance.save()

        # Redirect to a page displaying Ott details or Ott list
        return redirect('ottlist')  # Change 'ott_detail' to your detail view name

    context = {
        'ott_instance': ott_instance,
        'uploaded_video_location': ott_instance.file.url if ott_instance.file else None,
        'uploaded_thumbnail_location': ott_instance.thumbnail.url if ott_instance.thumbnail else None,
    }

    return render(request, 'backend/edit_ott.html', context)

# yourapp/views.py
from rest_framework import viewsets
from .models import Category
from .serializers import CategorySerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# yourapp/views.py
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Category, Subcategory
from .serializers import SubcategorySerializer

class SubcategoryViewSet(viewsets.ModelViewSet):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer

    def list(self, request, *args, **kwargs):
        category_id = self.request.query_params.get('lang_id', None)

        if category_id is not None:
            subcategories = Subcategory.objects.filter(category__id=category_id)
            serializer = SubcategorySerializer(subcategories, many=True)
            return Response(serializer.data)
        else:
            return Response({"error": "Please provide a 'lang_id' parameter in the query."}, status=400)
from .serializers import OttSerializer


class OttByCategoryAndSubcategoryViewSet(viewsets.ModelViewSet):
    queryset = Ott.objects.all()
    serializer_class = OttSerializer

    def list(self, request, *args, **kwargs):
        category_id = self.request.query_params.get('lang_id', None)
        subcategory_id = self.request.query_params.get('genre_id', None)

        if category_id is not None and subcategory_id is not None:
            otts = Ott.objects.filter(category__id=category_id, subcategory__id=subcategory_id)
            serializer = OttSerializer(otts, many=True)
            return Response(serializer.data)
        else:
            return Response({"error": "Please provide 'category_id' and 'subcategory_id' parameters in the query."}, status=400)
class UploadedContentViewSet(viewsets.ModelViewSet):
    queryset = Ott.objects.filter(status=True)
    serializer_class = OttSerializer


    def get_all_uploads(self, request):
        """
        Retrieve a list of all uploaded content with status=True.
        """
        uploads = Ott.objects.filter(status=True)
        serializer = self.get_serializer(uploads, many=True)
        return Response(serializer.data)

    def get_video_by_id(self, request, ):
        video_id = request.query_params.get('film_id')
        """
        Retrieve a specific video by ID.
        """
        try:
            video = Ott.objects.get(id=video_id, status=True)
            serializer = self.get_serializer(video)
            return Response(serializer.data)
        except Ott.DoesNotExist:
            return Response({"message": "Video not found"}, status=404)