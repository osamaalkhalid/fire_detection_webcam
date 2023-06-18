import cv2
import pygame

fire_cascade = cv2.CascadeClassifier('fire_detection.xml')
cap = cv2.VideoCapture(0)

# Initialize pygame audio
pygame.mixer.init()

# Load the audio file
pygame.mixer.music.load('audio.mp3')

while True:
    ret, frame = cap.read()

    # Check if frame read is successful
    if not ret:
        # Either end of video or an error occurred
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    fire = fire_cascade.detectMultiScale(frame, 1.2, 5)

    for (x, y, w, h) in fire:
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        print('Fire is detected')
        pygame.mixer.music.play()

    cv2.imshow('Osama', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Stop and quit pygame audio
pygame.mixer.music.stop()
pygame.quit()

cap.release()
cv2.destroyAllWindows()
