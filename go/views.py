from django.shortcuts import render
from django.shortcuts import render_to_response

# Create your views here.

def user_list(request):
    users = []
    for i in range(10):
        dic = {'username': 'zhang' + str(i), 'age': i, 'nickname': str(i) + 'xiaodan'}
        users.append(dic)
    result = render_to_response('../templates/index.html', {'data': users, 'admin': 'zhangsan'})
    return result
