import cv2
import os
import yagmail
from deepface import DeepFace
from datetime import datetime

# Configuration
YOUR_EMAIL = "***********@gmail.com"
APP_PASSWORD = "*********digdmhf"
RECEIVER_EMAIL = "*****boina@gmail.com"
KNOWN_FOLDER = "known_faces"
CAPTURED_IMAGE = "captured.jpg"

def is_known_face(image_path):
    for known_img in os.listdir(KNOWN_FOLDER):
        try:
            result = DeepFace.verify(img1_path=image_path,
                                     img2_path=os.path.join(KNOWN_FOLDER, known_img),
                                     model_name='ArcFace',
                                     enforce_detection=False)
            if result['verified']:
                return True
        except Exception as e:
            print(f"[Error] Comparing with {known_img}: {e}")
    return False

def send_email(image_path):
    try:
        yag = yagmail.SMTP(user=YOUR_EMAIL, password=APP_PASSWORD)
        subject = "🚨 Unknown person opened your laptop!"
        body = f"Suspicious login detected at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}."
        yag.send(to=RECEIVER_EMAIL, subject=subject, contents=[body, image_path])
        print("[✔] Alert email sent successfully.")
    except Exception as e:
        print("[❌] Failed to send email:", e)

def capture_and_verify():
    print("[🎥] Starting webcam... Waiting for face.")
    cap = cv2.VideoCapture(0)
    face_detected = False

    while not face_detected:
        ret, frame = cap.read()
        if not ret:
            continue

        # Convert to grayscale to detect faces
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        if len(faces) > 0:
            face_detected = True
            print("[👤] Face detected! Capturing image...")
            cv2.imwrite(CAPTURED_IMAGE, frame)
            cap.release()
            cv2.destroyAllWindows()

            if is_known_face(CAPTURED_IMAGE):
                print("[🟢] Known person. No alert sent.")
            else:
                print("[🔴] Unknown person detected!")
                send_email(CAPTURED_IMAGE)

            break

    # Clean up
    if os.path.exists(CAPTURED_IMAGE):
        os.remove(CAPTURED_IMAGE)

# Entry point
if __name__ == "__main__":
    capture_and_verify()
