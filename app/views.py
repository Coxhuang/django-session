from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response





class get_session(APIView):


    def get(self,request):

        print("get:")
        print(request.session.get("email",None))
        print(request.session.exists("email"))
        return Response("获取session")


class set_session(APIView):

    def post(self, request):

        print("set")
        request.session['username'] = 'cox'
        request.session['email'] = 'cox@cox.com'

        return Response("设置session")