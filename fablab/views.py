from django.http import HttpResponse
from django.shortcuts import render
from datetime import date

servicesData = {
    'conducted_work': [
        {
            'id': 0,
            'title': 'Проектирование плат',
            'description': 'Предоставление услуг по проектированию и изготовлению микроэлектронных плат для прототипирования новых устройств и схем.',
            'image': '../static/images/proect.png',
            'price': '1000'
        },
        {
            'id': 1,
            'title': '3D-печать',
            'description': 'Создание макетов и корпусов для электронных устройств, а также специальных креплений.',
            'image': '../static/images/proisv_fablab.png',
            'price': '1000'
        },
        {
            'id': 2,
            'title': 'Тестирование и анализ микросхем',
            'description': 'Тестирование и анализ произведенных микросхем для обеспечения их работоспособности и качества.',
            'image': '../static/images/sborka.png',
            'price': '1000'
        },
        {
            'id': 3,
            'title': 'Обслуживание микроэлектроники',
            'description': 'Обслуживание и ремонт оборудования для микроэлектроники.',
            'image': '../static/images/Obslug.png',
            'price': '1000'
        },
        {
            'id': 4,
            'title': 'Мастер-классы',
            'description': 'Проведение мероприятий, на которых пользователи могут изучать новые технологии и навыки в области микроэлектроники.',
            'image': '../static/images/master-class.png',
            'price': '1000'
        },
        {
            'id': 5,
            'title': 'Изготовление печатных плат на заказ',
            'description': 'Пользователи могут заказывать индивидуальные печатные платы с необходимой конфигурацией и размерами.',
            'image': '../static/images/izgotov.png',
            'price': '---'
        },

    ]
}

# def GetOrders(request):
#     return render(request, 'index.html', {'data' : {
#         'orders': orders
#     }})
    
def services(request):
    query = request.GET.get('q')

    if query:
        # Фильтруем данные, учитывая как поле "type", так и поле "price"
        filtered_data = [it for it in servicesData['conducted_work'] if
                         query.lower() in it['title'].lower() or query.lower() in it['price'].lower()]
    else:
        filtered_data = servicesData['conducted_work']
        query = ""

    return render(request, "all_service.html", {'filtered_data': filtered_data, 'search_value': query})

# def GetOrder(request, id):
#     return render(request, 'order.html', {'data' : {
#         'current_date': date.today(),
#         'id': id,
#         'title': orders[id]["title"],
#         'link': orders[id]["link"]
#     }})

def study_for_offer(request, offer_id):
    data_by_id = servicesData.get('conducted_work')[offer_id]
    return render(request, "study_offer.html", {
        'conducted_work': data_by_id
    })