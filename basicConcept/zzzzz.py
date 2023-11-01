


# import threading
# import cv2
# import numpy as np
# import mediapipe as mp
# import tensorflow as tf
# from tensorflow.keras.models import load_model
# import time
# import pygame
# import os
# from translate import Translator
# from gtts import gTTS


# # initialize mediapipe
# mpHands = mp.solutions.hands
# hands = mpHands.Hands(max_num_hands=1, min_detection_confidence=0.7)
# mpDraw = mp.solutions.drawing_utils

# # Load the pre-trained model for hand gesture recognition
# m = tf.keras.models.load_model("action2.h5")

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
# model = load_model('mp_hand_gesture')

# # Load class names
# f = open('gesture.names', 'r')
# classNames = f.read().split('\n')
# f.close()
# print(classNames)


# # Initialize the webcam
# cap = cv2.VideoCapture(0)
# output = []

# while True:
#     # Read each frame from the webcam
#     _, frame = cap.read()

#     x, y, c = frame.shape

#     # Flip the frame vertically
#     frame = cv2.flip(frame, 1)
#     framergb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

#     # Get hand landmark prediction
#     result = hands.process(framergb)

#     # print(result)
    
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
#             # res = m.predict(np.expand_dims(1, axis=0))[0]

#             # Predict gesture
#             prediction = model.predict([landmarks])
#             # print(prediction)
#             classID = np.argmax(prediction)
#             className = classNames[classID]
#             translator = Translator(to_lang="mr")

#             # Using List

#             # if not output:
#             #     output.append(className)
#             #     text = translator.translate(className)
#             #     voiceConverter(text)
#             #     print("++++++++++++++++++++++++++")
#             # elif output[-1]!=className:
#             #     output.append(className)
#             #     text = translator.translate(className)
#             #     voiceConverter(text)
#             #     print("-------------------")

#             # time.sleep(1)
#             print(className,"   ",output)
#             text = translator.translate(className)
#             # voiceConverter(text)

#             # using threading
#             # voice_thread = threading.Thread(target=voiceConverter, args=(text,))
#             # voice_thread.start()

#     # show the prediction on the frame
#     cv2.putText(frame, className, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 
#                    1, (0,0,255), 2, cv2.LINE_AA)

#     # output is on the camera
#     cv2.imshow("Output", frame) 
#     if cv2.waitKey(1) == ord('q'):
#         break
#     # time.sleep(3)

# # release the webcam and destroy all active windows
# cap.release()

# cv2.destroyAllWindows()





# TechVidvan hand Gesture Recognizer

# import necessary packages





import threading
import cv2
import numpy as np
import mediapipe as mp
import tensorflow as tf
from tensorflow.keras.models import load_model
import time
import pygame
import os
from translate import Translator
from gtts import gTTS

# # Initialize voice converter
def voiceConverter(text):
    tts = gTTS(text=text, lang='mr', slow=False)
    tts.save("voice.mp3")
    pygame.mixer.init()
    sound = pygame.mixer.Sound("voice.mp3")
    sound.play()
    pygame.time.wait(int(sound.get_length() * 1000))
    pygame.mixer.quit()
    os.remove("voice.mp3")


# initialize mediapipe
mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mpDraw = mp.solutions.drawing_utils

# Load the gesture recognizer model
model = load_model('mp_hand_gesture')

# Load class names
f = open('gesture.names', 'r')
classNames = f.read().split('\n')
f.close()
print(classNames)


# Initialize the webcam
cap = cv2.VideoCapture(0)

while True:
    # Read each frame from the webcam
    _, frame = cap.read()

    x, y, c = frame.shape

    # Flip the frame vertically
    frame = cv2.flip(frame, 1)
    framergb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Get hand landmark prediction
    result = hands.process(framergb)

    # print(result)
    
    className = ''

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
            text = translator.translate(className)
            voiceConverter(text)

    # show the prediction on the frame
    cv2.putText(frame, className, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 
                   1, (0,0,255), 2, cv2.LINE_AA)

    # Show the final output
    cv2.imshow("Output", frame) 

    if cv2.waitKey(1) == ord('q'):
        break

# release the webcam and destroy all active windows
cap.release()

cv2.destroyAllWindows()