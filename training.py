# import nltk
# from nltk.stem import WordNetLemmatizer
# import json
# import pickle
# import numpy as np

# lemmatizer = WordNetLemmatizer()

# intents_file = open('intents.json').read()
# intents = json.loads(intents_file)

# words = []
# classes = []
# documents = []
# ignore_words = ['?', '!']

# for intent in intents['intents']:
#     for pattern in intent['patterns']:
#         # tokenize each word in the pattern
#         w = nltk.word_tokenize(pattern)
#         words.extend(w)
#         # add the pattern and its associated intent to the documents list
#         documents.append((w, intent['tag']))
#         # add the intent to the classes list
#         if intent['tag'] not in classes:
#             classes.append(intent['tag'])

# # add the new intents to the words and classes lists
# new_intents = ['languages', 'tech', 'projects', 'experience', 'achievements']
# for intent in new_intents:
#     classes.append(intent)

# # lemmatize and lowercase each word, and remove duplicates
# words = [lemmatizer.lemmatize(w.lower()) for w in words if w not in ignore_words]
# words = sorted(list(set(words)))

# # sort classes alphabetically
# classes = sorted(list(set(classes)))

# # save the words, classes, and documents to a file
# with open('words.pickle', 'wb') as f:
#     pickle.dump(words, f)

# with open('classes.pickle', 'wb') as f:
#     pickle.dump(classes, f)

# training = []
# output_empty = [0] * len(classes)

# for doc in documents:
#     # create a bag of words for each document
#     bag = []
#     pattern_words = doc[0]
#     pattern_words = [lemmatizer.lemmatize(word.lower()) for word in pattern_words]
#     for word in words:
#         bag.append(1) if word in pattern_words else bag.append(0)
#     # create a one-hot encoded output for each document
#     output_row = list(output_empty)
#     output_row[classes.index(doc[1])] = 1
#     training.append([bag, output_row])

# # add training data for the new intents
# for intent in intents['intents']:
#     if intent['tag'] in new_intents:
#         for pattern in intent['patterns']:
#             # create a bag of words for each pattern
#             bag = []
#             pattern_words = nltk.word_tokenize(pattern)
#             pattern_words = [lemmatizer.lemmatize(word.lower()) for word in pattern_words]
#             for word in words:
#                 bag.append(1) if word in pattern_words else bag.append(0)
#             # create a one-hot encoded output for the intent
#             output_row = list(output_empty)
#             output_row[classes.index(intent['tag'])] = 1
#             training.append([bag, output_row])

# # shuffle the training data
# import random
# random.shuffle(training)

# # split the training data into input and output arrays
# X = []
# y = []
# for i in range(len(training)):
#     X.append(training[i][0])
#     y.append(training[i][1])

# # convert the input and output arrays to numpy arrays
# X = np.array(X)
# y = np.array(y)

# # create a neural network model using TensorFlow
# import tensorflow
# import keras
# from keras.models import Sequential
# from keras.layers import Dense, Activation, Dropout
# from keras.optimizers import SGD

# # print(tensorflow.__version__)
# # print(keras.__version__)



# # define the model architecture
# model = Sequential()
# model.add(Dense(128, input_shape=(len(words),), activation='relu'))
# model.add(Dropout(0.5))
# model.add(Dense(64, activation='relu'))
# model.add(Dropout(0.5))
# model.add(Dense(len(classes), activation='softmax'))

# # compile the model
# sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
# model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

# # train the model
# model.fit(X, y, epochs=200, batch_size=5, verbose=1)
# model.save('chatbot_model.h5')
# print("Done")

import random
import json
import pickle
import numpy as np
import nltk
import tensorflow
import keras
from nltk.stem import WordNetLemmatizer

from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.optimizers import SGD

lemmatizer = WordNetLemmatizer()

intents = json.loads(open('intents.json').read())

words = []
classes = []
documents = []
ignore_letters = ['?','!','.',',']

for intent in intents['intents']:
    for pattern in intent['patterns']:
        word_list = nltk.word_tokenize(pattern)
        words.extend(word_list)
        documents.append((word_list, intent['tag']))
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

#print(documents)

words = [lemmatizer.lemmatize(word) for word in words if word not in ignore_letters]
words = sorted(set(words))

classes = sorted(set(classes))
pickle.dump(words, open('words.pk1','wb'))
pickle.dump(classes, open('classes.pk1','wb'))

training = []
output_empty = [0] * len(classes)

for document in documents:
    bag = []
    word_patterns = document[0]
    word_patterns = [lemmatizer.lemmatize(word.lower()) for word in word_patterns]
    for word in words:
        bag.append(1) if word in word_patterns else bag.append(0)

    output_row = list(output_empty)
    output_row[classes.index(document[1])] = 1
    training.append([bag, output_row])

random.shuffle(training)
training = np.array(training)

train_x = list(training[:, 0])
train_y = list(training[:, 1])

model = Sequential()
model.add(Dense(128, input_shape=(len(train_x[0]),), activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(len(train_y[0]), activation='softmax'))

sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

hist = model.fit(np.array(train_x), np.array(train_y), epochs=200, batch_size=5, verbose=1)
model.save('chatbotmodel.h5', hist)
print("Done")