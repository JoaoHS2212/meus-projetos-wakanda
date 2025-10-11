import subprocess
import sys
from cifrador_simples import cifrar  # Importa teu cifrador (ajusta o caminho se precisar)

def scan_target(ip):
    print(f"Wakanda Scan: Iniciando nmap em {ip}...")
    try:
        # Roda nmap -sV (versões de services)
        result = subprocess.run(['nmap', '-sV', ip], capture_output=True, text=True)
        output = result.stdout
        if result.returncode != 0:
            print("Erro no nmap – instala com sudo apt install nmap?")
            return
        print(output)
        
        # Checa se porta 23 (telnet) tá open
        if '23/tcp open telnet' in output:
            resposta = input("Porta 23 (telnet) open! Conectar? (s/n): ")
            if resposta.lower() == 's':
                subprocess.run(['telnet', ip])
        else:
            print("Telnet não open – tenta outro port ou lab!")
        
        # Salva relatório cifrado
        relatorio = output + "\n--- Wakanda Report: Scan completo ---"
        relatorio_cifrado = cifrar(relatorio)
        with open('relatorio_scan.txt', 'w') as f:
            f.write(relatorio_cifrado)
        print("Relatório cifrado salvo em relatorio_scan.txt – decifra pra ver!")
        
    except Exception as e:
        print(f"Erro no scan: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        ip = input("Digite o IP alvo: ")
    else:
        ip = sys.argv[1]
    scan_target(ip)