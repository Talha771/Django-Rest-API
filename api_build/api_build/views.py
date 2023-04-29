from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from base.models import User, ToDoList
from .serializers import userserializer, ToDoListSerializer


@api_view(["GET"])
def getUserName(request):
    user_id = request.query_params.get('id')
    if not user_id:
        return Response("Please provide a user id", status=400)
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Response("User with id {} does not exist".format(user_id), status=404)
    userser = userserializer(user)
    return Response(userser.data)


@api_view(["GET"])
def ToDoListView(request):
    todo_id = request.query_params.get('id')
    if not todo_id:
        return Response("Please provide a valid todo id", status=400)
    try:
        todo = ToDoList.objects.get(id=todo_id)
    except ToDoList.DoesNotExist:
        return Response("No such ToDoList found", status=404)
    response = ToDoListSerializer(todo)
    return Response(response.data)


@api_view(["POST"])
def addUser(request):
    serializer = userserializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        print("wrong input")
    return Response(serializer.data)


@api_view(["POST"])
def ToDoCreateView(request):
    serializer = ToDoListSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        print("wrong input")


@api_view(["GET"])
def login(request):
    user_email = request.query_params.get('email')
    password = request.query_params.get('password')

    if not user_email or not password:
        return Response("Please provide both email and password", status=400)

    try:
        user = User.objects.get(email=user_email)
    except User.DoesNotExist:
        return Response("User with email {} does not exist".format(user_email), status=404)
    if (user.password != password):
        return Response("Email or password is incorrect")
    # if user.check_password(password):
    #     return Response("Email and password are correct")
    else:
        return Response("Email and password correct", status=200)
