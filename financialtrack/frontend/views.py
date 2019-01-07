import calendar
from django.shortcuts import render
from django.views.generic import View
from django.utils.translation import gettext as _
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from frontend.models import NavMenu
from transactions.models import Transactions
from frontend.serializers import NavMenuSerializer
from financialTrack.settings.base import LANGUAGE_CODE


class AppView(View):

    def get(self, request):
        return render(request,'frontend/index.html',{})


class NavMenuView(ListCreateAPIView):
    queryset = NavMenu.objects.all()
    serializer_class = NavMenuSerializer

class MainMenuAPIView(APIView):
    permissions_classes = [IsAuthenticated]

    def get(self, request):
        main_menu = {}

        years = list(set(
            [year.dt_transaction.year for year in
                Transactions.objects.filter(created_by=request.user)])
            )

        for year in years:
            main_menu[year]= list(set(
                [months.dt_transaction.month
                 for months in Transactions.objects.filter(
                     dt_transaction__year=year, created_by=request.user)
                 ])
            )

        for k, v in main_menu.items():
            v.sort()
            for i, month in enumerate(v):
                main_menu[k][i] = _(calendar.month_name[month])

        return Response(main_menu)

"""
TODO:
    Keep using internationalization for month names at backend or
        transfer this to moment in frontend
"""
