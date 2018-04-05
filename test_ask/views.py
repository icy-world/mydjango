from django.shortcuts import render
from django.shortcuts import render_to_response

# Create your views here.
from test_ask.models import BasTextbook


def textbook_list(request):
    books = BasTextbook.objects.values('textbook_id','subject_id','grade_name','publishing','textbooks_version','used')
    result = render_to_response('../templates/index.html', {'data': books, 'admin': 'zhangsan'})
    return result
