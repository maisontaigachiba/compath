from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, TemplateView

from keras.models import Sequential
from keras.layers import Activation, Dense
from keras.utils.np_utils import to_categorical
import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import RMSprop
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import h5py
from keras.models import model_from_json
from django.core.validators import int_list_validator
from django.shortcuts import render
from os import chdir
import random


class CompathListView(TemplateView):
#      def get(self, request, *args, **kwargs):
#          return HttpResponse('Hello, World!')
    template_name = 'compath.html'

    global count
    count = 0

def TestListView(request):
###    template_name = 'test.html'

    mes = request.POST.get("prm")
    mes2 = request.POST.get("prm2")
    mes3 = request.POST.get("prm3")
    mes4 = request.POST.get("prm4")
    mes5 = request.POST.get("prm5")
    mes6 = request.POST.get("prm6")
    mes7 = request.POST.get("prm7")
    mes8 = request.POST.get("prm8")
    mes9 = request.POST.get("prm9")
    mes10 = request.POST.get("prm10")
    mes11 = request.POST.get("prm11")
    mes12 = request.POST.get("prm12")
    mes13 = request.POST.get("prm13")
    mes14 = request.POST.get("prm14")
    mes15 = request.POST.get("prm15")
    mes16 = request.POST.get("prm16")
    mes17 = request.POST.get("prm17")
    mes18 = request.POST.get("prm18")
    mes19 = request.POST.get("prm19")
    mes20 = request.POST.get("prm20")
    mes21 = request.POST.get("prm21")
    mes22 = request.POST.get("prm22")
    mes23 = request.POST.get("prm23")

#    lis = [mes,mes2,mes3]

#    print(lis)

#    dic = {"msg":message,"msg2":message2,"msg3":message3}

#    print(mes)
#    print(mes2)


#    return HttpResponse("Hello, world. You're at the polls index.")

    global count
    if count == 0:
       chdir("compath")


##    model_list = [mes,mes2,mes3,mes4,mes5,mes6,mes7,mes8,mes9,mes10,mes11,mes12,mes13,mes14,mes15,mes16,mes17,mes18,mes19,mes20,mes21]
##    print(model_list)
#    model_list = pd.Series(model_list)
#    print(model_list[0][0][0])
##    model_list = model_list.T
##    model_list = model_list.values.tolist()
##    model_list = np.array([model_list])
#    model_list = model_list/10

##    model = model_from_json(open('data_model.json').read())

##    model.load_weights('data_predict.hdf5')

##    model.summary()

##    results = model.predict(model_list)

##    print(results)
##    max1_index = np.argmax(results)
##    print(max1_index)

##    results[0][max1_index] = 0

##    max2_index = np.argmax(results)
##    print(max2_index)


#    max2_value = max(results)
#    max2_index = results.index(max2_value)

##    global num1,num2

##    num1 = max1_index
##    num2 = max2_index

    count=+1

#    print("Predict:\n", results)
#    global num
#    num=results

    return render(request, 'test.html')

#print(model_list)


def TestListView2(request):

#    global num1,num2

#    print(num1)
#    print(num2)

    dict = {0:"肉体系",1:"物語系クリエイティブ",2:"未来系クリエイティブ",3:"哲学系",4:"教養",5:"技術系",6:"ラディカル",7:"アート",8:"ファイト系",9:"体育会系",10:"IT系",11:"ハイパー",12:"マックス",13:"コミュニケーション",14:"機械派",15:"のめり込み",16:"マネジメント",17:"リスクテイキング"}

    dict2 = {0:"起業家",1:"ビジネスマン",2:"職人",3:"アーティスト",4:"公務員",5:"研究者",6:"芸能人",7:"ストーリーテラー"}

#    print(dict[num1])
#    print(dict[num2])

    num1 = random.randint(0,17)
    num2 = random.randint(0,17)
    if num2 == num1:
       num2 = random.randint(0,17)
    num3 = random.randint(0,7)

    dic = {"msg":dict[num1],"msg2":dict[num2], "msg3":dict2[num3]}

    
    return render(request, 'test2.html',dic)

#    return HttpResponse()