# 🎵 Hand Music Controller - Controle Musical com as Mãos

Este projeto usa visão computacional com Python (OpenCV + MediaPipe) para controlar um buzzer passivo conectado ao Arduino. Cada dedo levantado na frente da webcam representa uma nota musical, que é tocada no buzzer.

## 🎯 Objetivo

Transformar gestos manuais em notas musicais reais, criando uma espécie de "piano de mão" com tecnologia acessível e divertida!

## 🖥️ Tecnologias Usadas

### Python (lado PC)
- OpenCV
- MediaPipe
- PySerial

### Arduino (lado microcontrolador)
- Arduino UNO ou similar 
- Buzzer passivo
- Comunicação Serial

---

## 🧰 Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/hand-music-controller.git
cd hand-music-controller
```

### 2. Instale as dependências do Python

```bash
pip install -r requirements.txt
```

> **Obs:** Requer Python 3.8+

---

## 🧠 Como Funciona

1. A webcam detecta sua mão usando a biblioteca MediaPipe.
2. Um script Python identifica quais dedos estão levantados.
3. Um caractere correspondente à nota é enviado via Serial para o Arduino.
4. O Arduino toca a nota no buzzer.

| Dedo      | Nota | Frequência (Hz) |
|-----------|------|-----------------|
| Indicador | Ré   | 294             |
| Médio     | Mi   | 330             |
| Anelar    | Fá   | 349             |
| Mínimo    | Sol  | 392             |

---

## 🔌 Circuito Arduino

- Buzzer no pino digital **11**
- GND do buzzer no **GND** do Arduino

---

## ▶️ Executando o Projeto

1. Carregue o código `arduino/buzzer_controller.ino` no Arduino.
2. Execute o script Python:

```bash
cd python
python main.py
```

3. Levante os dedos diante da webcam para tocar as notas!

---

## 📂 Estrutura do Projeto

```
hand-buzzer-controller/
├── arduino/
│   └── buzzer.ino
├── python/
│   ├── main.py
│   ├── hand_detector.py
│   └── serial.py
├── assets/
│   └── example.png
├── README.md
├── requirements.txt
└── .gitignore
```

---

## 🛠 Requisitos de Hardware

- 1 Arduino Uno ou similar
- 1 Buzzer passivo
- Cabo USB para comunicação serial
- Webcam (integrada ou USB)
- PC com Python 3.8+ instalado

---

🔁 Próximos passos:
Quero evoluir esse projeto para algo mais sofisticado, inspirando-me no conceito do Manosolfa ou similares — um método visual de representar notas com diferentes posições com a mão 🎼👐. Além de explorar outras fontes de saídas sonoras como alternativa ao buzzer.

---

## 📃 Licença

Distribuído sob a licença MIT. Veja `LICENSE` para mais informações.

---

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se livre para abrir issues, forks e pull requests.

---


