import tensorflow as tf
from PIL import Image
import numpy as np

im = Image.open('kk.jpg')
loaded_model = tf.keras.models.load_model('model_gender.h5')
im = im.resize((48, 48))
main = []
pixels = np.array(im.getdata())
for i in pixels:
    main.append(np.array(i).mean(dtype='int'))
main = np.array([np.array(main, 'int')])
main = main.reshape(main.shape[0], 48, 48, 1)

print(loaded_model.predict([main]))


