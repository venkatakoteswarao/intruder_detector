# 👁️ Laptop Intruder Alert System Using DeepFace + Email Notifications

This Python script uses your webcam to detect and verify faces using **DeepFace**. If it detects an **unauthorized person**, it captures the image and sends an **alert email** with the snapshot attached.

Perfect for laptops where you want an extra layer of security when someone opens or unlocks your system.

---

## 🔐 Features

- 🧠 Uses DeepFace with ArcFace model for facial recognition
- 📸 Captures photo of the person opening your laptop
- 🟢 If known → does nothing
- 🔴 If unknown → sends an alert email with image
- 💌 Sends alerts using Gmail via Yagmail
- 🖥️ Can be scheduled to run at unlock using **Windows Task Scheduler**

---

## 🧪 Requirements

- Install the required Python libraries:
- pip install opencv-python deepface yagmail
- configure these variables YOUR_EMAIL,APP_PASSWORD,RECEIVER_EMAIL.

## steps to add Task  in Task scheduler 

- open Task Scheduler
- create new Task
- set trigger,action, and finally click on Save and finish
- now you added successfully Task .
- 
