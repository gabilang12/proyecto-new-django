from django.shortcuts import render

import tensorflow as tf

def mi_vista(request):
    modelo = tf.lite.Interpreter('app_final\mobilenet_v2_1.0_224_1_default_1.tflite')
    return HttpResponse('Vista de ejemplo')