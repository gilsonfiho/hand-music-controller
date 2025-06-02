import mediapipe as mp
import cv2

class HandDetector:
    def __init__(self, mode=False, maxHands=2, detectionCon=0.5, trackCon=0.5):
        self.handsModule = mp.solutions.hands
        self.hands = self.handsModule.Hands(
            static_image_mode=mode,
            max_num_hands=maxHands,
            min_detection_confidence=detectionCon,
            min_tracking_confidence=trackCon
        )
        self.draw = mp.solutions.drawing_utils
        self.results = None

    def findHands(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.draw.draw_landmarks(img, handLms, self.handsModule.HAND_CONNECTIONS)
        return img

    def fingersUp(self):
        # Índices das pontas dos dedos no modelo MediaPipe
        tips = [4, 8, 12, 16, 20]
        fingers = []

        if self.results and self.results.multi_hand_landmarks:
            hand = self.results.multi_hand_landmarks[0]
            landmarks = hand.landmark

            # Polegar: comparando coordenada X (porque o polegar abre lateralmente)
            # Nota: precisa adaptar para mão direita/esquerda, aqui assumimos mão direita
            if landmarks[tips[0]].x < landmarks[tips[0] - 1].x:
                fingers.append(True)
            else:
                fingers.append(False)

            # Para os outros 4 dedos (indicador, médio, anelar, mínimo), comparar Y das pontas com Y de dois níveis abaixo
            for i in range(1, 5):
                fingers.append(landmarks[tips[i]].y < landmarks[tips[i] - 2].y)

            return fingers  # [Polegar, Indicador, Médio, Anelar, Mínimo]

        return [False, False, False, False, False]
