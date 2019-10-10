import timeit
import time
from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect

from fibo.models import FibonacciResults


def fibonacci_calculation(num):
       if num < 2:
   
        return 1
    else:
        a = 1
        b = 1
        for i in range(2, num):
            c = a+b
            a = b
            b = c
   
        return b
   
def fib(request):

    num = 0
    result = 0
    time_taken = 0

    if request.GET.get('num1'):
        start_time = timeit.timeit()
        #print(start_time)
        number = request.GET.get('num1')
        num = int(number)
        result=fibonacci_calculation(num)
        end_time=timeit.timeit()
        t=abs(end_time-start_time)
        time_taken = t

        obj = FibonacciResults.objects.create(
            number=num, result=result, time_taken=time_taken)
        obj.save()

    return render(
        request,
        'index.html',
        {
            'number': num,
            'result': result,
            'time_taken': time_taken
        }
    )
