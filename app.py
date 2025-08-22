import sys
import subprocess

def insecure_eval(user_input: str):
    # 🚨 Falha: nunca usar eval() com input
    return eval(user_input)

def insecure_subprocess(command: str):
    # 🚨 Falha: command injection possível
    subprocess.Popen(command, shell=True)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        cmd = sys.argv[1]
        print(">> Executando eval inseguro")
        print(insecure_eval(cmd))

        print(">> Executando subprocess inseguro")
        insecure_subprocess(cmd)
    else:
        print("Passe um argumento!")
