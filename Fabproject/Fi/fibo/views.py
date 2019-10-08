import timeit
import time
from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect

from fibo.models import FibonacciResults


def fibonacci_calculation(num):
    #start_time = time.time()
    if num < 2:
        #end_time = time.time() - start_time
        return 1
    else:
        a = 1
        b = 1
        for i in range(2, num):
            c = a+b
            a = b
            b = c
        #end_time = time.time() - start_time
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
        end_time=(timeit.timeit() +start_time)*60
        #print(end_time)
        #time_taken=(timeit.timeit("fibonacci_calculation(num)"))

        #end_time =timeit.timeit("fibanocci_calculaton()", setup="from __main__ import fibonocci_calculation")
        #end_time=abs(start_time-timeit.timeit())
        time_taken = round(end_time)

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
