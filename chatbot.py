

import random
import json
import pickle
import numpy as np
import nltk
import tensorflow
import keras
from nltk.stem import WordNetLemmatizer
from keras.models import load_model
from datetime import datetime
from reportlab.pdfgen import canvas
from typing import List
from datetime import datetime
from reportlab.pdfgen import canvas

def make_Resume(history):
    # st.write(history)
    # pdf_filename = 'resume_{}.pdf'.format(datetime.now().strftime("%Y%m%d_%H%M%S"))
    user_responses = history
    res_name = user_responses[2]

    res_name = res_name.lower().split()

    res_name = [word for word in res_name if word not in ['my', 'name', 'is']]
    name = ' '.join(res_name)
    res_email = user_responses[3]
    res_link = user_responses[4]
    link =""
    #get words that start from https
    res_link = res_link.split()
    for i in res_link:
        if "http" in i:
            link = link + " "+ i
    link = link + " "+ res_email
    res_lanuage = user_responses[5]
    res_lanuage = res_lanuage.lower().split()
    #get names of languages
    res_lanuage = [word for word in res_lanuage if word in ['python', 'c++', "c", "r", "dart", "java", "javascript", "js", "c#", "rust", "go"]]
    lanuage = ", ".join(res_lanuage)
    res_degree = user_responses[6]

    #remove words like "I", "am"
    res_degree = res_degree.split()
    res_degree = [word for word in res_degree if word not in ['i', 'am', "I"]]
    degree = ' '.join(res_degree)

    res_post = user_responses[7]
    post=""
    res_post = res_post.split()
    #get words written after "for" or "as"
    i=0
    while i<len(res_post):
        if res_post[i] == "for" or res_post[i] == "as":
            j=i+1
            while j<len(res_post):
                post = post + " "+ res_post[j]
                j=j+1
        i=i+1
    res_project = user_responses[8]
    #remove words like I and have
    res_project = res_project.split()
    res_project = [word for word in res_project if word not in ['i', 'have', "I"]]
    project = ' '.join(res_project)
    res_exp = user_responses[9]
    #remove words like I and have
    res_exp = res_exp.split()
    res_exp = [word for word in res_exp if word not in ['i', 'have', "I"]]
    exp = ' '.join(res_exp)
    res_achievements = user_responses[10]
    #remove words like I and have
    res_achievements = res_achievements.split()
    res_achievements = [word for word in res_achievements if word not in ['i', 'have', "I"]]
    achievements = ' '.join(res_achievements)

    # displayPDF(pdf_filename)

    def create_resume_pdf(name, link):
        pdf_filename = 'resume_{}.pdf'.format(datetime.now().strftime("%Y%m%d_%H%M%S"))
        pdf_canvas = canvas.Canvas(pdf_filename)
        y = 750
        
        # Get the user's name and contact information from the input
        name = name
        github = ""
        linkedin = ""
        email=""
        for word in link.split():
            if "@" in word:
                email = word
            if "github" in word:
                github = word
            if "linkedin" in word:
                linkedin = word
        
        # Add the user's name and contact information to the PDF
        pdf_canvas.setFillColorRGB(0, 0, 0)
        pdf_canvas.setFont("Helvetica-Bold", 20)
        pdf_canvas.drawString(50, y, "{}".format(name.capitalize()))
        y -= 25
        pdf_canvas.setFillColorRGB(255/255, 20/255, 147/255)
        pdf_canvas.setFont("Helvetica", 12)
        pdf_canvas.drawString(50, y,"({})".format(post.strip()))
        y -= 35
        pdf_canvas.setFillColorRGB(59/255, 89/255, 152/255)
        pdf_canvas.setFont("Helvetica", 12)
        pdf_canvas.drawString(50, y, "Email: {}".format(email))
        y -= 25
        if(len(github) > 0):
            pdf_canvas.setFillColorRGB(0, 0, 0)
            pdf_canvas.drawString(50, y, "Github: {}".format(github))
            y -= 25
        if(len(linkedin) > 0):
            pdf_canvas.setFillColorRGB(59/255, 89/255, 152/255)
            pdf_canvas.drawString(50, y, "LinkedIn: {}".format(linkedin))
            y -= 50
        
        # Add a section for education
        pdf_canvas.setFillColorRGB(0, 0, 0)
        pdf_canvas.setFont("Helvetica-Bold", 14)
        pdf_canvas.drawString(50, y, "Education")
        y -= 25
        pdf_canvas.setFont("Helvetica", 12)
        pdf_canvas.drawString(50, y, degree)
        y -= 25
        y -= 25
        # Add a section for work experience
        # pdf_canvas.setFillColorRGB(0, 0, 255/255)
        pdf_canvas.setFont("Helvetica-Bold", 14)
        pdf_canvas.drawString(50, y, "Work Experience")
        y -= 25
        pdf_canvas.setFont("Helvetica", 12)
        pdf_canvas.drawString(50, y, exp)
        y -= 25
        y -= 25

        # Add a section for skills
        pdf_canvas.setFillColorRGB(0, 0, 0)
        pdf_canvas.setFont("Helvetica-Bold", 14)
        pdf_canvas.drawString(50, y, "Skills")
        y -= 25
        pdf_canvas.setFont("Helvetica", 12)
        pdf_canvas.drawString(50, y, lanuage)
        y -= 25
        y -= 25

        # Add a section for projects
        pdf_canvas.setFillColorRGB(0, 0, 0)
        pdf_canvas.setFont("Helvetica-Bold", 14)
        pdf_canvas.drawString(50, y, "Projects")
        y -= 25
        pdf_canvas.setFont("Helvetica", 12)
        pdf_canvas.drawString(50, y, project)
        y -= 25
        y -= 25

        # Add a section for achievements
        pdf_canvas.setFont("Helvetica-Bold", 14)
        pdf_canvas.drawString(50, y, "Achievements")
        y -= 25
        pdf_canvas.setFont("Helvetica", 12)
        pdf_canvas.drawString(50, y, achievements)
        y -= 25
        y -= 25
        #end the PDF
        pdf_canvas.save()
        print("PDF created successfully!", pdf_filename)
        st.success("Resume created successfully!")
        st.balloons()
        displayPDF(pdf_filename)
    create_resume_pdf(name, link)
    

lemmatizer = WordNetLemmatizer()
intents = json.loads(open('intents.json').read())
chat_history = []
words = pickle.load(open('words.pk1','rb'))
classes = pickle.load(open('classes.pk1','rb'))
model = load_model('chatbotmodel.h5')

def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]
    return sentence_words

def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i]=1
    return np.array(bag)

def predict_class(sentence):
    bow = bag_of_words(sentence)
    res = model.predict(np.array([bow]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]

    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({'intent': classes[r[0]], 'probability': str(r[1])})
    return return_list

def get_response(intents_list, intents_json):
    tag = intents_list[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if i['tag'] == tag:
            result = random.choice(i['responses'])
            break
    return result

import base64
def displayPDF(file):
    with open(file, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

import streamlit as st
from streamlit_chat import message
import requests

st.set_page_config(
    page_title="Streamlit Chat - Demo",
    page_icon=":robot:"
)

st.header("Coofee")
st.write("Your resume bot")


if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

def query(user_input):
    ints = predict_class(user_input)
    res = get_response(ints, intents)
    return res

def get_text():
    input_text = st.text_input("You", key="input")
    chat_history.append(('User', input_text))
    return input_text 



while(True):
    user_input = get_text()
    
    if user_input:
        if user_input.lower() == 'exit':
            # st.write(chat_history)
            # st.write(st.session_state['past'])
            make_Resume(st.session_state['past'])
            
            break
        output = query(user_input)
        # st.write(chat_history)
        
        st.session_state.past.append(user_input)
        st.session_state.generated.append(output)
        # st.write(st.session_state['past'])
    if st.session_state['generated']:
        
        for i in range(len(st.session_state['generated'])-1, -1, -1):
            message(st.session_state["generated"][i], key=str(i))
            message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
