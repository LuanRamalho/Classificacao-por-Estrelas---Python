import tkinter as tk
from tkinter import messagebox

# Função para verificar se é dispositivo de toque
def is_touch_device():
    try:
        # Tentamos criar um TouchEvent (falharia em dispositivos desktop)
        tk.Tk().getboolean("touch")
        return True
    except:
        return False

# Função para atualizar as estrelas e o texto da mensagem
def rating_update(start, end, active):
    for i in range(start, end + 1):
        if active:
            star_containers[i].config(text="★", fg="gold")  # Estrela preenchida
        else:
            star_containers[i].config(text="☆", fg="gray")  # Estrela desativada

    # Atualizar a mensagem com base no número de estrelas ativas
    active_elements = [c for c in star_containers if c.cget("text") == "★"]
    if len(active_elements) > 0:
        if len(active_elements) == 1:
            message_var.set("Terrível")
        elif len(active_elements) == 2:
            message_var.set("Ruim")
        elif len(active_elements) == 3:
            message_var.set("Satisfeito")
        elif len(active_elements) == 4:
            message_var.set("Bom")
        elif len(active_elements) == 5:
            message_var.set("Excelente")
    else:
        message_var.set("")

# Função para lidar com o clique no botão de envio
def submit_rating():
    submit_section.pack_forget()  # Esconde o formulário
    messagebox.showinfo("Obrigado", "Obrigado pela sua classificação")  # Mostra a mensagem de agradecimento
    submit_button.config(state="disabled")

# Configuração da janela principal
root = tk.Tk()
root.title("Star Rating")
root.geometry("400x300")
root.configure(bg="#ffffff")

# Variáveis para controlar a mensagem
message_var = tk.StringVar()
message_var.set("Avalie sua experiência")

# Mensagem
message_label = tk.Label(root, textvariable=message_var, font=("Poppins", 14), bg="#ffffff")
message_label.pack(pady=10)

# Container das estrelas
star_containers = []
for i in range(5):
    star_container = tk.Frame(root, bg="#ffffff")
    star_label = tk.Label(star_container, text="☆", font=("Font Awesome 5 Free Solid", 20), fg="gray", bg="#ffffff")
    star_label.pack(side="left")
    star_container.pack(side="top", fill="x")
    star_containers.append(star_label)

# Botão de envio
submit_button = tk.Button(root, text="Enviar", command=submit_rating, state="disabled", bg="#fe3b5a", fg="#ffffff", font=("Poppins", 12), pady=10)
submit_button.pack(pady=20)

# Divisão para a mensagem de agradecimento
submit_section = tk.Frame(root, bg="#ffffff", height=150, width=400)
submit_message_label = tk.Label(submit_section, text="Obrigado pela sua classificação", font=("Poppins", 14), bg="#ffffff")
submit_message_label.pack(expand=True)

# Verificação de dispositivo e atribuição de eventos
device_type = "touch" if is_touch_device() else "mouse"
events = {
    "mouse": {"over": "<Button-1>"},
    "touch": {"over": "<ButtonPress-1>"}
}

# Função para definir a interação com as estrelas
def set_stars_event(index):
    def click_star(event):
        submit_button.config(state="normal")
        if star_containers[index].cget("text") == "☆":
            rating_update(index, 4, True)
        else:
            rating_update(index, 4, False)
    star_containers[index].bind(events[device_type]["over"], click_star)

# Atribuir eventos às estrelas
for i in range(5):
    set_stars_event(i)

# Loop principal
root.mainloop()
