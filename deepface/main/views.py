import logging
from urllib.request import urlopen

from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from main.forms import DocumentForm

import tensorflow as tf
from PIL import Image
import numpy as np

from main.models import Document

ages = {
    0: '0-3 years old',
    1: '3-18 years old',
    2: '18-45 years old',
    3: '45-64 years old',
    4: '64-116 years old'
}

ethnicity = {
    0: "White",
    1: "Black",
    2: "Asian",
    3: "Indian",
    4: "Hispanic"
}


def index(request):
    coffees = ['Espresso', 'Doppio', 'Macchiato', 'Ristretto', 'Americano', 'Café Latte', 'Cappuccino', 'Flat White', 'Piccolo Latte', 'Mocha', 'Affogato', 'Irish Coffee']
    return render(request, template_name='main/index.html', context={'coffees': coffees})


def recognize(request):
    if request.method == 'POST':
        image = NamedTemporaryFile()
        image.write(urlopen(request.POST['img']).read())
        image.flush()
        image = File(image)
        name = str(image.name).split('\\')[-1]
        name += '.jpg'  # store image in jpeg format
        image.name = name

        im = Image.open(image)
        model_gender = tf.keras.models.load_model('model_gender.h5')
        model_ethnicity = tf.keras.models.load_model('model_ethnicity.h5')
        model_age = tf.keras.models.load_model('model_age.h5')

        im = im.resize((48, 48))
        main = []
        pixels = np.array(im.getdata())
        for i in pixels:
            main.append(np.array(i).mean())
        to_doc = main.copy()
        main = np.array([np.array(main)])
        main = main.reshape(main.shape[0], 48, 48, 1)
        gender = 'Male' if model_gender.predict([main])[0][0] == 1. else 'Female'

        index_ethnicity = \
            np.where(model_ethnicity.predict([main])[0] == np.amax(model_ethnicity.predict([main])[0]))[0][0] + 1

        index_age = np.where(model_age.predict([main])[0] == 1.)[0][0]

        client_id = request.POST['client_id']
        coffee_type = request.POST['coffee_type']

        doc = Document.objects.create(coffee_type=coffee_type, client_id=client_id, file=image, gender=gender, age=ages[index_age],
                                      ethnicity=ethnicity[index_ethnicity],
                                      pixels=to_doc)
        doc.save()
        logging.info(f'gender: {gender}, ethnicity: {str(index_ethnicity)}, age: {ages[index_age]}')
        return JsonResponse({
            "success": True,
            "gender": gender,
            "ethnicity": ethnicity[index_ethnicity],
            "age": ages[index_age],
        })
    else:
        return HttpResponse('Error!')


def upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            im = Image.open(request.FILES['file'])
            model_gender = tf.keras.models.load_model('model_gender.h5')
            model_ethnicity = tf.keras.models.load_model('model_ethnicity.h5')
            model_age = tf.keras.models.load_model('model_age.h5')

            im = im.resize((48, 48))
            main = []
            pixels = np.array(im.getdata())
            for i in pixels:
                main.append(np.array(i).mean())
            to_doc = main.copy()
            main = np.array([np.array(main)])
            main = main.reshape(main.shape[0], 48, 48, 1)
            gender = 'Male' if model_gender.predict([main])[0][0] == 1. else 'Female'

            index_ethnicity = \
                np.where(model_ethnicity.predict([main])[0] == np.amax(model_ethnicity.predict([main])[0]))[0][0] + 1

            index_age = np.where(model_age.predict([main])[0] == 1.)[0][0]

            doc = form.save(commit=False)
            doc.gender = gender
            doc.age = ages[index_age]
            doc.ethnicity = ethnicity[index_ethnicity]
            doc.pixels = to_doc
            doc.save()
            return render(request, 'main/upload.html', {
                "form": DocumentForm(),
                "success": True,
                "gender": gender,
                "ethnicity": ethnicity[index_ethnicity],
                "age": ages[index_age],
            })
    else:
        form = DocumentForm()
    return render(request, 'main/upload.html', {"form": form})
