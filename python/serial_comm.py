import serial
import time

class SerialSender:
    def __init__(self, port='COM6', baudrate=9600, timeout=1):
        try:
            self.arduino = serial.Serial(port, baudrate, timeout=timeout)
            time.sleep(2)  # tempo para o Arduino resetar após conexão
            print(f"Conectado na porta {port} com baudrate {baudrate}")
        except serial.SerialException as e:
            print(f"Erro ao abrir a porta serial: {e}")
            self.arduino = None

    def send(self, char):
        if self.arduino and self.arduino.is_open:
            try:
                self.arduino.write(char.encode())
            except Exception as e:
                print(f"Erro ao enviar dados: {e}")
        else:
            print("Porta serial não está aberta")
