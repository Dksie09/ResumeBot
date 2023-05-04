
import streamlit as st
from streamlit_chat import message as st_message

st.title("Resume Builder")
st.subheader("Please enter the following details to build your resume")

st.session_state
{
    "history" : [{
    "message" : "Hello bot",
    "is_user" : True
},
{"message" : "Hello user",
    "is_user" : False}]
}

def generate_answer(input):
    if "history" not in st.session_state:
        st.session_state.history = []
    ans  ="fofo"
    #store ans in history
    st.session_state.history.append({"message":input,"is_user":True})
    st.session_state.history.append({"message":ans,"is_user":False})


input = st.text_input("Talk to the bot", key="input_text", on_change=generate_answer(input))



# if st.button("Send", key="send"):

    # history.append({
    #     "message" : input,
    #     "is_user" : True
    # })
    # history.append({
    #     "message" : "meme",
    #     "is_user" : False
    # })
    # st.session_state["history"] = history
    # st_message(input, is_user=True)
    # st_message("Hello user!")
    

# for chat in st.session_state.get("history", ):
#     st_message(**chat)
# from streamlit_chat import message

# # message("My message") 
# # message("Hello bot!", is_user=True)

# input = st.text_input("Your message", key="input")
# if st.button("Send", key="send"):
#     message(input, is_user=True)
#     message("Hello user!")

# from datetime import datetime
# from reportlab.pdfgen import canvas


# def create_resume_pdf(user_input):
#     pdf_filename = 'resume_{}.pdf'.format(datetime.now().strftime("%Y%m%d_%H%M%S"))
#     pdf_canvas = canvas.Canvas(pdf_filename)
#     y = 750
    
#     # Get the user's name and contact information from the input
#     name = ""
#     email = ""
#     phone = ""
#     for word in user_input.split():
#         if "@" in word:
#             email = word
#         elif word.isnumeric() and len(word) == 10:
#             phone = word
#         else:
#             name += word.capitalize() + " "
    
#     # Add the user's name and contact information to the PDF
#     pdf_canvas.setFont("Helvetica-Bold", 16)
#     pdf_canvas.drawString(50, y, "Name: {}".format(name))
#     y -= 25
#     pdf_canvas.setFont("Helvetica", 12)
#     pdf_canvas.drawString(50, y, "Email: {}".format(email))
#     y -= 25
#     pdf_canvas.drawString(50, y, "Phone: {}".format(phone))
#     y -= 50
    
#     # Add a section for education
#     pdf_canvas.setFont("Helvetica-Bold", 14)
#     pdf_canvas.drawString(50, y, "Education")
#     y -= 25
#     pdf_canvas.setFont("Helvetica", 12)
#     pdf_canvas.drawString(50, y, "School name, Degree")
#     y -= 25

#     # Add a section for work experience
#     pdf_canvas.setFont("Helvetica-Bold", 14)
#     pdf_canvas.drawString(50, y, "Work Experience")
#     y -= 25
#     pdf_canvas.setFont("Helvetica", 12)
#     pdf_canvas.drawString(50, y, "Company name, Job title")
#     y -= 25

#     # Add a section for skills
#     pdf_canvas.setFont("Helvetica-Bold", 14)
#     pdf_canvas.drawString(50, y, "Skills")
#     y -= 25
#     pdf_canvas.setFont("Helvetica", 12)
#     pdf_canvas.drawString(50, y, "Skill name")
#     y -= 25

#     # Add a section for projects
#     pdf_canvas.setFont("Helvetica-Bold", 14)
#     pdf_canvas.drawString(50, y, "Projects")
#     y -= 25
#     pdf_canvas.setFont("Helvetica", 12)
#     pdf_canvas.drawString(50, y, "Project name")
#     y -= 25

#     # Add a section for achievements
#     pdf_canvas.setFont("Helvetica-Bold", 14)
#     pdf_canvas.drawString(50, y, "Achievements")
#     y -= 25
#     pdf_canvas.setFont("Helvetica", 12)
#     pdf_canvas.drawString(50, y, "Achievement name")
#     y -= 25

#     #end the PDF
#     pdf_canvas.save()
#     return pdf_filename


# create_resume_pdf("Dakshi goel dakshiegoel@gmail.com 1234567890")