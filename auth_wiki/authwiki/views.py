from django.shortcuts import render
from .models import *
from django.http import JsonResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

from .serializers import * 

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework_simplejwt.serializers import TokenObtainSerializer


# Create your views here.
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return Response({
                "Message": "Your account has been successful created",
                "User": serializer.data}, status=status.HTTP_201_CREATED
            )
 
        return Response({"error": serializer._errors}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST',])
def AuthlibView(request):
    if request.method == 'GET':
        authlib = Auth_library.objects.all()
        authlib_serializer = Auth_librarySerializer(authlib, many=True)
        return Response(authlib_serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        authlib_serializer = Auth_librarySerializer(data=request.data)
        if authlib_serializer.is_valid():
            authlib_serializer.save()
            return Response(authlib_serializer.data, status=status.HTTP_201_CREATED)
        return Response(authlib_serializer.error, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def auth_lib_id(request, id):
    try:
        auth_lib = Auth_library.objects.get(id=id)
    except Auth_library.DoesNotExist:
        return Response({"message":"Request not found"}, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'GET':
        authlib_serializer = Auth_librarySerializer(auth_lib)
        return Response(authlib_serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'PUT':
        #data = JSONParser().parse(request)
        authlib_serializer = Auth_librarySerializer(data=request.data)
        if authlib_serializer.is_valid():
            authlib_serializer.save()
            return Response(authlib_serializer.data, status=status.HTTP_201_CREATED)
        return Response(authlib_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == "DELETE":
        auth_lib.delete()
        return Response({"message":"Request deleted"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'POST'])
def UsersView(request):
    if request.method == 'GET':
        users = Users.objects.all()
        users_serializer = UsersSerializer(users, many=True)
        return Response(users_serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        users_serializer = UsersSerializer(data=request.data)
        if users_serializer.is_valid():
            users_serializer.save()
            return Response(users_serializer.data, status=status.HTTP_201_CREATED)
        return Response(users_serializer.error, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def users_id(request, id):
    try:
        users = Users.objects.get(id=id)
    except Users.DoesNotExist:
        return Response({"message":"User not found"}, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        users_serializer = UsersSerializer(users)
        return Response(users_serializer.data, status=status.HTTP_200_OK)
    if request.method == 'PUT':
        #data = JSONParser().parse(request)
        users_serializer = UsersSerializer(data=request.data)
        if users_serializer.is_valid():
            users_serializer.save()
            return Response(users_serializer.data, status=status.HTTP_201_CREATED)
        return Response(users_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == "DELETE":
        users.delete()
        return Response({"message":"User deleted"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET', 'POST'])
def CategoriesView(request):
    try:
        users = Users.objects.get(id=id)
    except Users.DoesNotExist:
        return Response({"message":"User not found"}, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        categories = Categories.objects.all()
        categories_serializer = CategoriesSerializer(categories, many=True)
        return Response(categories_serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        categories_serializer = CategoriesSerializer(data=request.data)
        if categories_serializer.is_valid():
            categories_serializer.save()
            return Response(categories_serializer.data, status=status.HTTP_201_CREATED)
        return Response(categories_serializer.error, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def Categories_id(request, id):
    try:
        users = Users.objects.get(id=id)
    except Users.DoesNotExist:
        return Response({"message":"User not found"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        categories = Categories.objects.get(id=id)
    except Categories.DoesNotExist:
        return Response({"message":"Category not found"}, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        categories_serializer = CategoriesSerializer(categories)
        return Response(categories_serializer.data, status=status.HTTP_200_OK)
    if request.method == 'PUT':
        #data = JSONParser().parse(request)
        categories_serializer = CategoriesSerializer(data=request.data)
        if categories_serializer.is_valid():
            categories_serializer.save()
            return Response(categories_serializer.data, status=status.HTTP_201_CREATED)
        return Response(categories_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == "DELETE":
        categories.delete()
        return Response({"message":"Category deleted"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'POST'])
def CodeView(request):
    try:
        users = Users.objects.get(id=id)
    except Users.DoesNotExist:
        return Response({"message":"User not found"}, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        code = Code.objects.all()
        code_serializer = CodeSerializer(code, many=True)
        return Response(code_serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        code_serializer = CodeSerializer(data=request.data)
        if code_serializer.is_valid():
            code_serializer.save()
            return Response(code_serializer.data, status=status.HTTP_201_CREATED)
        return Response(code_serializer.error, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def Code_id(request, id):
    try:
        code = Categories.objects.get(id=id)
    except Code.DoesNotExist:
        return Response({"message":"Code not found"}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        users = Users.objects.get(id=id)
    except Users.DoesNotExist:
        return Response({"message":"User not found"}, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        code_serializer = CodeSerializer(code)
        return Response(code_serializer.data, status=status.HTTP_200_OK)
    if request.method == 'PUT':
        code_serializer = CodeSerializer(data=request.data)
        if code_serializer.is_valid():
            code_serializer.save()
            return Response(code_serializer.data, status=status.HTTP_201_CREATED)
        return Response(code_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == "DELETE":
        code.delete()
        return Response({"message":"Code deleted"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET', 'POST'])
def CommentsView(request):
    if request.method == 'GET':
        comments = Comments.objects.all()
        comment_serializer = CommentsSerializer(comments, many=True)
        return Response(comment_serializer.data, status=status.HTTP_200_OK)
    try:
        users = Users.objects.get(id=id)
    except Users.DoesNotExist:
        return Response({"message":"User not found"}, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'POST':
        comment_serializer = CommentsSerializer(data=request.data)
        if comment_serializer.is_valid():
            comment_serializer.save()
            return Response(comment_serializer.data, status=status.HTTP_201_CREATED)
        return Response(comment_serializer.error, status=status.HTTP_400_BAD_REQUEST)
 
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def Comments_id(request, id):
    try:
        users = Users.objects.get(id=id)
    except Users.DoesNotExist:
        return Response({"message":"User not found"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        comments = Comments.objects.get(id=id)
    except Code.DoesNotExist:
        return Response({"message":"Comment not found"}, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        comments_serializer = CommentsSerializer(comments)
        return Response(comments_serializer.data, status=status.HTTP_200_OK)
    if request.method == 'PUT':
        comments_serializer = CommentsSerializer(data=request.data)
        if comments_serializer.is_valid():
            comments_serializer.save()
            return Response(comments_serializer.data, status=status.HTTP_201_CREATED)
        return Response(comments_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == "DELETE":
        comments.delete()
        return Response({"message":"Comment deleted"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET', 'POST'])
def ReactionsView(request, pk):
    if request.method == 'GET':
        reactions = Reactions.objects.all()
        reactions_serializer = ReactionsSerializer(reactions, many=True)
    react = Comments.object_or_status.HTTP_404_NOT_FOUND(Comments, id=request.Post.get('comments_id'))
    liked = False
    if react.Reactions.filter(id.request.user.id).exist():
        react.Reactions.remove(request.user)
        liked = False
    else:
        react.Reactions.add(request.user)
        liked = True
    return HttpResponseRedirect(reversed(Comments, args=[str(pk)]))


@api_view(['GET', 'POST'])
def CommunityView(request):
    if request.method == 'GET':
        community = Community.objects.all()
        community_serializer = CommunitySerializer(community, many=True)
        return Response(community_serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        community_serializer = CommunitySerializer(data=request.data)
        if community_serializer.is_valid():
            community_serializer.save()
            return Response(community_serializer.data, status=status.HTTP_201_CREATED)
        return Response(community_serializer.error, status=status.HTTP_400_BAD_REQUEST)


        

