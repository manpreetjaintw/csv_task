from django.shortcuts import render
from rest_framework.decorators import APIView
from rest_framework.response import Response
from pharma_app.models import Pharma, Drug
from pharma_app.serializer import DrugSerializer, PharmaSerializer


class PharmaReview(APIView):

    def post(self, request, *args):
        year = request.data.get('year', None)
        drug = request.data.get('drug', None)
        drug_classification = request.data.get('drug_classification', None)

        final_output = []

        # pharma_serializer = PharmaSerializer(pharma_queryset, many=True)

        if drug_classification == 'm01ab':
            fields = ('m01ab', 'year')
            pharma_queryset = Pharma.objects.filter(year=year).values('m01ab', 'year')
            pharma_serializer = PharmaSerializer(pharma_queryset, many=True, fields=fields)

        elif drug_classification == 'm01ae':
            fields = ('m01ae', 'year')
            pharma_queryset = Pharma.objects.filter(year=year).values('m01ae', 'year')
            pharma_serializer = PharmaSerializer(pharma_queryset, many=True, fields=fields)

        elif drug_classification == 'n02ba':
            fields = ('n02ba', 'year')
            pharma_queryset = Pharma.objects.filter(year=year).values('n02ba', 'year')
            pharma_serializer = PharmaSerializer(pharma_queryset, many=True, fields=fields)

        elif drug_classification == 'n02be':
            fields = ('n02be', 'year')
            pharma_queryset = Pharma.objects.filter(year=year).values('n02be', 'year')
            pharma_serializer = PharmaSerializer(pharma_queryset, many=True, fields=fields)

        elif drug_classification == 'n05b':
            fields = ('n05b', 'year')
            pharma_queryset = Pharma.objects.filter(year=year).values('n05b', 'year')
            pharma_serializer = PharmaSerializer(pharma_queryset, many=True, fields=fields)

        elif drug_classification == 'r03':
            fields = ('r03', 'year')
            pharma_queryset = Pharma.objects.filter(year=year).values('r03', 'year')
            pharma_serializer = PharmaSerializer(pharma_queryset, many=True, fields=fields)

        elif drug_classification == 'r06':
            fields = ('r06', 'year')
            pharma_queryset = Pharma.objects.filter(year=year).values('r06', 'year')
            pharma_serializer = PharmaSerializer(pharma_queryset, many=True, fields=fields)

        if drug and year:
            drug_queryset = Drug.objects.filter(drugName=drug, date__year=year)
            drug_serializer = DrugSerializer(drug_queryset, many=True)
        elif drug:
            drug_queryset = Drug.objects.filter(drugName=drug)
            drug_serializer = DrugSerializer(drug_queryset, many=True)
        else:
            drug_queryset = Drug.objects.filter(date__year=year)
            drug_serializer = DrugSerializer(drug_queryset, many=True)

        final_output.append(drug_serializer.data)
        if drug_classification:
            final_output.append(pharma_serializer.data)
        return Response(final_output)
