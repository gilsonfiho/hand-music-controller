import cv2
from hand_detector import HandDetector
from serial_comm import SerialSender  # se sua classe está em serial_comm.py
import time

detector = HandDetector()
sender = SerialSender('COM6')  # ajuste para sua porta serial Windows

notas = ['B', 'C', 'D', 'E', 'F']  # Agora 5 notas para 5 dedos

# Para evitar enviar repetidamente a mesma nota:
estado_anteriores = [False] * 5

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    if not success:
        print("Erro ao capturar vídeo")
        break

    img = detector.findHands(img)
    fingers = detector.fingersUp()

    for i, finger in enumerate(fingers):
        # Só enviar se o dedo estiver levantado agora e estava abaixado antes
        if finger and not estado_anteriores[i]:
            sender.send(notas[i])
            print(f"Enviado: {notas[i]}")
    estado_anteriores = fingers.copy()

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
