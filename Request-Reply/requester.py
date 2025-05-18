import zmq

def run_client():
    context = zmq.Context()
    socket = context.socket(zmq.REQ)  # REQ para o lado da Requisição
    socket.connect("tcp://localhost:5555") # Conecta ao servidor

    print("Cliente REQ-REP conectado ao servidor...")

    for i in range(5):
        message = f"Olá do cliente {i}"
        print(f"Cliente: Enviando '{message}'...")
        socket.send_string(message)

        # Espera pela resposta do servidor
        reply = socket.recv_string()
        print(f"Cliente: Recebido '{reply}'")
        print("-" * 20)

if __name__ == "__main__":
    run_client()