import zmq
import time

def run_server():
    context = zmq.Context()
    socket = context.socket(zmq.REP)  # REP para o lado da Resposta
    socket.bind("tcp://*:5555")       # Escuta na porta 5555 em todas as interfaces

    print("Servidor REQ-REP iniciado na porta 5555...")

    while True:
        # Espera por uma requisição do cliente
        message = socket.recv_string()
        print(f"Servidor: Recebido '{message}'")

        # Simula algum processamento
        time.sleep(1)

        # Envia a resposta de volta para o cliente
        reply = f"Mundo (resposta para: {message})"
        socket.send_string(reply)
        print(f"Servidor: Enviado '{reply}'")

if __name__ == "__main__":
    run_server()