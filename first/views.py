from django.shortcuts import render
from django.db.models import Max,Sum
from .models import Foods

# Create your views here.
def dashboard(request):

    data1996 = Foods.objects.filter(cook_year="1996")
    data1999 = Foods.objects.filter(cook_year="1999")
    data2005 = Foods.objects.filter(cook_year="2005")
    data2010 = Foods.objects.filter(cook_year="2010")
    data2015 = Foods.objects.filter(cook_year="2015")
    data2020 = Foods.objects.filter(cook_year="2020")
    data2022 = Foods.objects.filter(cook_year="2022")
    
    data1996Top5 = data1996.order_by("-unit_price")[:5]
    data1999Top5 = data1999.order_by("-unit_price")[:5]
    data2005Top5 = data2005.order_by("-unit_price")[:5]
    data2010Top5 = data2010.order_by("-unit_price")[:5]
    data2015Top5 = data2015.order_by("-unit_price")[:5]
    data2020Top5 = data2020.order_by("-unit_price")[:5]
    data2022Top5 = data2022.order_by("-unit_price")[:5]

    gdata2022 = data2022.order_by("-unit_price")
    
    data1996 = list(data1996.values())
    data1999 = list(data1999.values())
    data2005 = list(data2005.values())
    data2010 = list(data2010.values())
    data2015 = list(data2015.values())
    data2020 = list(data2020.values())
    data2022 = list(data2022.values())

    # data1996Top5 = Foods.objects.filter(cook_year="1996").order_by("-unit_price")[:5]
    # data1999Top5 = Foods.objects.filter(cook_year="1999").order_by("-unit_price")[:5]
    # data2005Top5 = Foods.objects.filter(cook_year="2005").order_by("-unit_price")[:5]
    # data2010Top5 = Foods.objects.filter(cook_year="2010").order_by("-unit_price")[:5]
    # data2015Top5 = Foods.objects.filter(cook_year="2015").order_by("-unit_price")[:5]
    # data2020Top5 = Foods.objects.filter(cook_year="2020").order_by("-unit_price")[:5]
    # data2022Top5 = Foods.objects.filter(cook_year="2022").order_by("-unit_price")[:5]
    
    
    
    # print(data1996Top5)
    # data1996Top5 = sorted(data1996,reverse=True)[:5]




    # pdata1996 = []
    # for i in data1996:
    #     pdata1996.append(i["unit_price"])
    
    # data1996Top5 = sorted(pdata1996,reverse=True)[:5]
    # print(pdata1996)
    # data1996Top5 = pdata1996[0]
    # for i in pdata1996:
    #     if i > data1996Top5:
    #         data1996Top5 = i
            
        
    context = {
        "data1996": data1996,
        "data1999": data1999,
        "data2005": data2005,
        "data2010": data2010,
        "data2015": data2015,
        "data2020": data2020,
        "data2022": data2022,
        "data1996Top5":data1996Top5,
        "data1999Top5":data1999Top5,
        "data2005Top5":data2005Top5,
        "data2010Top5":data2010Top5,
        "data2015Top5":data2015Top5,
        "data2020Top5":data2020Top5,
        "data2022Top5":data2022Top5,
        "gdata2022":gdata2022,




    }


    
    return render(request, "first/1cha.html", context)