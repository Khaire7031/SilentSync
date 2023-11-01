











# from django.http import JsonResponse
# import threading
# import cv2
# from django.shortcuts import render
# from django.http import StreamingHttpResponse
# from django.views.decorators import gzip
# import mediapipe as mp
# import numpy as np
# import tensorflow as tf
# from translate import Translator
# import time
# from gtts import gTTS
# import pygame
# import os
# from django.conf import settings
# from keras.models import load_model



# # initialize mediapipe
# mpHands = mp.solutions.hands
# hands = mpHands.Hands(max_num_hands=1, min_detection_confidence=0.7)
# mpDraw = mp.solutions.drawing_utils
# output = []


# # Initialize voice converter
# def voiceConverter(text):
#     tts = gTTS(text=text, lang='mr', slow=False)
#     tts.save("voice.mp3")
#     pygame.mixer.init()
#     sound = pygame.mixer.Sound("voice.mp3")
#     sound.play()
#     pygame.time.wait(int(sound.get_length() * 1000))
#     pygame.mixer.quit()
#     os.remove("voice.mp3")

# # Load the gesture recognizer model
# model = load_model('C:\\Users\\Pranav\\Music\\SlientSync\\SilentSync\\basicConcept\\mp_hand_gesture')


# classNames = ['Nice I liked very much', 'keep peace ', 'All the best to you', 'i did not like ', 'call me When you free', 'Stop Do Not go ahead', 'Look at the sky', 'live long', 'unity is power', 'Be Happy']


# def home(request):
#     return render(request,'base.html')

# def about(request):
#     return render(request,'about.html')

# def services(request):
#     return render(request,'services.html')

# def index(request):
#     return render(request,'index.html')

# def contact(request):
#     return render(request,'contact.html')

# def user(request):
#     username = request.GET['Username']
#     print(username)
#     return render(request,'user.html',{'name':username})


# def camera(request):
#     return render(request, 'camera.html')




# # Function to perform gesture recognition
# def recognize_gesture(frame):
#     x,y,c = frame.shape

#     # Flip the frame vertically
#     frame = cv2.flip(frame, 1)
#     framergb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

#     # Get hand landmark prediction
#     result = hands.process(framergb)

#     className = ''
#     text = ''
#     # post process the result
#     if result.multi_hand_landmarks:
#         landmarks = []
#         for handslms in result.multi_hand_landmarks:
#             for lm in handslms.landmark:
#                 # print(id, lm)
#                 lmx = int(lm.x * x)
#                 lmy = int(lm.y * y)

#                 landmarks.append([lmx, lmy])

#             # Drawing landmarks on frames
#             mpDraw.draw_landmarks(frame, handslms, mpHands.HAND_CONNECTIONS)

#             # Predict gesture
#             prediction = model.predict([landmarks])
#             # print(prediction)
#             classID = np.argmax(prediction)
#             className = classNames[classID]
#             translator = Translator(to_lang="mr")
            
#             # Using List

#             if not output:
#                 output.append(className)
#                 text = translator.translate(className)
#                 # voiceConverter(text)
#                 voice_thread = threading.Thread(target=voiceConverter, args=(text,))
#                 voice_thread.start()
                
#             elif output[-1]!=className:
#                 output.append(className)
#                 text = translator.translate(className)
#                 # voiceConverter(text)
#                 voice_thread = threading.Thread(target=voiceConverter, args=(text,))
#                 voice_thread.start()
                

#     # show the prediction on the frame
#     cv2.putText(frame, className, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 
#                    1, (0,0,255), 2, cv2.LINE_AA)

#     # Show the final output
#     cv2.imshow("Output", frame) 

#     return frame,className,text
    


# def generate_frames():
#     camera = cv2.VideoCapture(0)
#     while True:
#         success, frame = camera.read()
#         if not success:
#             break 
#         else:
#             # Your gesture recognition logic
#             processed_frame, english, marathi = recognize_gesture(frame)

#             # Convert the processed frame to JPEG format
#             _, buffer = cv2.imencode('.jpg', processed_frame)
#             frame_bytes = buffer.tobytes()

#             # Combine frame bytes and additional information into a single response
#             response_content = b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n'
#             response_content += f'English: {english}\r\n'.encode('utf-8')
#             response_content += f'Marathi: {marathi}\r\n'.encode('utf-8')

#             # Yield the combined response
#             yield response_content



# @gzip.gzip_page
# def video(request):
#     return StreamingHttpResponse(generate_frames(), content_type='multipart/x-mixed-replace; boundary=frame')

























from django.http import JsonResponse
import threading
import cv2
from django.shortcuts import render
from django.http import StreamingHttpResponse
from django.views.decorators import gzip
import mediapipe as mp
import numpy as np
import tensorflow as tf
from translate import Translator
import time
from gtts import gTTS
import pygame
import os
from django.conf import settings
from keras.models import load_model
from .models import Text  # Import your Text model


# initialize mediapipe
mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mpDraw = mp.solutions.drawing_utils
output = []
output.append("Pranav")
map = {}

# Initialize voice converter
def voiceConverter(text):
    tts = gTTS(text=text, lang='mr', slow=False)
    tts.save("voice.mp3")
    pygame.mixer.init()
    sound = pygame.mixer.Sound("voice.mp3")
    sound.play()
    pygame.time.wait(int(sound.get_length() * 1000))
    pygame.mixer.quit()
    os.remove("voice.mp3")

# Load the gesture recognizer model
model = load_model('C:\\Users\\Pranav\\Music\\SlientSync\\SilentSync\\basicConcept\\mp_hand_gesture')


classNames = ['Nice I liked very much', 'I Win victory Today', 'All the best to you', 'i did not like ', 'call me When you free', 'Stop Do Not go ahead', 'Look at the sky', 'live long', 'unity is power', 'Be Happy']


def home(request):
    return render(request,'base.html')

def about(request):
    return render(request,'about.html')

def services(request):
    # eng_sentence = "I can not speak english sentence."
    # mar_sentence = "यह मराठी मराठी मराठी मराठी वाक्य आहे."

    # result = insertData(eng_sentence, mar_sentence)
    # print("result",result)
    # db()
    return render(request,'services.html')

def index(request):
    return render(request,'index.html')

def contact(request):
    return render(request,'contact.html')

def user(request):
    username = request.GET['Username']
    print(username)
    return render(request,'user.html',{'name':username})


def camera(request):
    return render(request, 'camera.html')


def insertData(eng, mar):
    # Assuming the IDs are 1 for English and 2 for Marathi
    english_text = Text(id=1, action=eng)
    marathi_text = Text(id=2, action=mar)

    # Save the English and Marathi texts to the database
    english_text.save()
    marathi_text.save()

    return f'Successfully added English: {eng} and Marathi: {mar} to the database.'


# Print Data From DataBase
def db():
    # Retrieve all records from the text table
    all_texts = Text.objects.all()

    # Assuming id 1 is for English and id 2 is for Marathi
    eng_text = Text.objects.filter(id=1).first()
    mar_text = Text.objects.filter(id=2).first()

    # Check if the objects exist before accessing their attributes
    eng = eng_text.action if eng_text else None
    mar = mar_text.action if mar_text else None

    # print("\nEnglish Sentence Count:", Text.objects.filter(id=1).count())
    # print("Marathi Sentence Count:", Text.objects.filter(id=2).count())
    print("English Sentence : ", eng)
    print("Marathi Sentence : ", mar)

    return eng, mar




# Function to perform gesture recognition
def recognize_gesture(frame):
    x,y,c = frame.shape

    # Flip the frame vertically
    frame = cv2.flip(frame, 1)
    framergb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Get hand landmark prediction
    result = hands.process(framergb)

    className = ''
    text = ''
    # post process the result
    if result.multi_hand_landmarks:
        landmarks = []
        for handslms in result.multi_hand_landmarks:
            for lm in handslms.landmark:
                # print(id, lm)
                lmx = int(lm.x * x)
                lmy = int(lm.y * y)

                landmarks.append([lmx, lmy])

            # Drawing landmarks on frames
            mpDraw.draw_landmarks(frame, handslms, mpHands.HAND_CONNECTIONS)

            # Predict gesture
            prediction = model.predict([landmarks])
            # print(prediction)
            classID = np.argmax(prediction)
            className = classNames[classID]
            translator = Translator(to_lang="mr")
            
            # Using List
            
            map[className] = map.get(className, 0) + 1

            if not output:
                output.append(className)
                if map[className] > 5 and output[-1]!=className:
                    print("---------===========------------")
                    map[className] = 0 
                    map.clear()
                    output.append(className)
                    text = translator.translate(className)
                    # voiceConverter(text)
                    result = insertData(className, text)
                    print("result",result)
                    db()
                    voice_thread = threading.Thread(target=voiceConverter, args=(text,))
                    voice_thread.start()

            elif map[className] > 5 and output[-1]!=className:
                print("=============")
                map[className] = 0 
                map.clear()
                output.append(className)
                text = translator.translate(className)
                # voiceConverter(text)
                result = insertData(className, text)
                print("result",result)
                db()
                voice_thread = threading.Thread(target=voiceConverter, args=(text,))
                voice_thread.start()   
                             
            print(className)
    # show the prediction on the frame
    cv2.putText(frame, className, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 
                   1, (0,0,255), 2, cv2.LINE_AA)

    # Show the final output
    cv2.imshow("Output", frame) 

    return frame,className,text
    

def generate_frames():
    camera = cv2.VideoCapture(0)
    while True:
        success, frame = camera.read()
        if not success:
            break 
        else:
            # Your gesture recognition logic
            processed_frame, english, marathi = recognize_gesture(frame)

            # Convert the processed frame to JPEG format
            _, buffer = cv2.imencode('.jpg', processed_frame)
            frame_bytes = buffer.tobytes()

            # Combine frame bytes and additional information into a single response
            response_content = b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n'
            response_content += f'English: {english}\r\n'.encode('utf-8')
            response_content += f'Marathi: {marathi}\r\n'.encode('utf-8')

            # Yield the combined response
            yield response_content



@gzip.gzip_page
def video(request):
    # db()
    return StreamingHttpResponse(generate_frames(), content_type='multipart/x-mixed-replace; boundary=frame')












































'''======================  List ======================'''





# from django.http import JsonResponse
# import threading
# import cv2
# from django.shortcuts import render
# from django.http import StreamingHttpResponse
# from django.views.decorators import gzip
# import mediapipe as mp
# import numpy as np
# import tensorflow as tf
# from translate import Translator
# import time
# from gtts import gTTS
# import pygame
# import os
# from django.conf import settings
# from keras.models import load_model



# # initialize mediapipe
# mpHands = mp.solutions.hands
# hands = mpHands.Hands(max_num_hands=1, min_detection_confidence=0.7)
# mpDraw = mp.solutions.drawing_utils
# output = []



# def example_view(request):
#     # Your view logic here
#     data = {'key': 2}
#     return JsonResponse(data)

# # Initialize voice converter
# def voiceConverter(text):
#     tts = gTTS(text=text, lang='mr', slow=False)
#     tts.save("voice.mp3")
#     pygame.mixer.init()
#     sound = pygame.mixer.Sound("voice.mp3")
#     sound.play()
#     pygame.time.wait(int(sound.get_length() * 1000))
#     pygame.mixer.quit()
#     os.remove("voice.mp3")

# # Load the gesture recognizer model
# model = load_model('C:\\Users\\Pranav\\Music\\SlientSync\\SilentSync\\basicConcept\\mp_hand_gesture')


# classNames = ['Nice I liked very much', 'keep peace ', 'All the best to you', 'i did not like ', 'call me When you free', 'Stop Do Not go ahead', 'Look at the sky', 'live long', 'unity is power', 'Be Happy']


# def home(request):
#     return render(request,'base.html')

# def about(request):
#     return render(request,'about.html')

# def services(request):
#     return render(request,'services.html')

# def index(request):
#     return render(request,'index.html')

# def contact(request):
#     return render(request,'contact.html')

# def user(request):
#     username = request.GET['Username']
#     print(username)
#     return render(request,'user.html',{'name':username})


# def camera(request):
#     return render(request, 'camera.html')




# # Function to perform gesture recognition
# def recognize_gesture(frame):
#     x,y,c = frame.shape

#     # Flip the frame vertically
#     frame = cv2.flip(frame, 1)
#     framergb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

#     # Get hand landmark prediction
#     result = hands.process(framergb)

#     className = ''
#     # post process the result
#     if result.multi_hand_landmarks:
#         landmarks = []
#         for handslms in result.multi_hand_landmarks:
#             for lm in handslms.landmark:
#                 # print(id, lm)
#                 lmx = int(lm.x * x)
#                 lmy = int(lm.y * y)

#                 landmarks.append([lmx, lmy])

#             # Drawing landmarks on frames
#             mpDraw.draw_landmarks(frame, handslms, mpHands.HAND_CONNECTIONS)

#             # Predict gesture
#             prediction = model.predict([landmarks])
#             # print(prediction)
#             classID = np.argmax(prediction)
#             className = classNames[classID]
#             translator = Translator(to_lang="mr")
#             # text = translator.translate(className)
#             # voiceConverter(text)
#             # Using List

#             if not output:
#                 output.append(className)
#                 text = translator.translate(className)
#                 # voiceConverter(text)
#                 voice_thread = threading.Thread(target=voiceConverter, args=(text,))
#                 voice_thread.start()
#                 print("++++++++++++++++++++++++++")
#             elif output[-1]!=className:
#                 output.append(className)
#                 text = translator.translate(className)
#                 # voiceConverter(text)
#                 voice_thread = threading.Thread(target=voiceConverter, args=(text,))
#                 voice_thread.start()
#                 print("-------------------")

#     # send classname and text to camera.html


#     # show the prediction on the frame
#     cv2.putText(frame, className, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 
#                    1, (0,0,255), 2, cv2.LINE_AA)

#     # Show the final output
#     cv2.imshow("Output", frame) 

#     return frame
    


# def generate_frames():
#     camera = cv2.VideoCapture(0)
#     while True:
#         success, frame = camera.read()
#         if not success:
#             break 
#         else:
#             # Your gesture recognition logic
#             processed_frame,english_text,marathi_text = recognize_gesture(frame)

#             # Convert the processed frame to JPEG format
#             _, buffer = cv2.imencode('.jpg', processed_frame)
#             frame_bytes = buffer.tobytes()

#         # Yield the frame
#         yield (b'--frame\r\n'
#                b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')


# @gzip.gzip_page
# def video(request):
#     return StreamingHttpResponse(generate_frames(), content_type='multipart/x-mixed-replace; boundary=frame')















