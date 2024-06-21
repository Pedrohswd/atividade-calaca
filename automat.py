import pyautogui
import time

def auto_click(interval, duration):
    """
    Função que realiza cliques automáticos.

    Args:
        interval (float): Intervalo entre os cliques em segundos.
        duration (float): Duração total que o auto clicker deve funcionar em segundos.
    """
    end_time = time.time() + duration
    while time.time() < end_time:
        pyautogui.click()
        time.sleep(interval)  # Espera pelo intervalo especificado

if __name__ == "__main__":
    interval = float(input("Digite o intervalo entre os cliques (em segundos): "))
    duration = float(input("Digite a duração total do auto clicker (em segundos): "))
    print("O auto clicker começará em 5 segundos...")
    time.sleep(5)  # Espera 5 segundos antes de começar
    auto_click(interval, duration)
    print("Auto clicker finalizado.")