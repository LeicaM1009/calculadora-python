import tkinter as tk

window = tk.Tk()
window.title('Calculadora Simples')
window.geometry('350x250')

# Variáveis de controle
valor_display = tk.StringVar(value="0") # O que aparece na tela
primeiro_numero = 0
operacao = ""

# --- Funções de Lógica ---

def digitar_numero(num):
    # Se o display for "0", substitui. Se não, concatena (junta os números)
    atual = valor_display.get()
    if atual == "0":
        valor_display.set(str(num))
    else:
        valor_display.set(atual + str(num))

def escolher_operacao(op):
    global primeiro_numero, operacao
    primeiro_numero = int(valor_display.get()) # Salva o que está na tela
    operacao = op                              # Salva o sinal (+ ou -)
    valor_display.set("0")                     # Limpa a tela para o próximo número

def limpar():
    global primeiro_numero, operacao
    valor_display.set("0")
    primeiro_numero = 0
    operacao = ""

def limpar_entrada():
    valor_display.set("0")

def calcular_resultado():

    global primeiro_numero, operacao

    # Se não houver operação, não faz nada
    if operacao == "":
        return

    segundo_numero = int(valor_display.get())
    
    if operacao == "+":
        resultado = primeiro_numero + segundo_numero
    elif operacao == "-":
        resultado = primeiro_numero - segundo_numero
    elif operacao == "*":
        resultado = primeiro_numero * segundo_numero  
    elif operacao == "/":
        if segundo_numero == 0:
            valor_display.set("Erro")
            limpar()
            return
        resultado = primeiro_numero / segundo_numero  
    else:
        resultado = segundo_numero # Caso nenhuma operação tenha sido escolhida
        
    valor_display.set(str(resultado))

    primeiro_numero = resultado
    operacao = ""

# --- Interface ---

# Display (Label)
label = tk.Label(window, textvariable=valor_display, font=("Arial", 30), bg="lightgray", width=15)
label.pack(pady=20)

# Botões de Números (Exemplos)
frame_numeros = tk.Frame(window)
frame_numeros.pack()

# Linha 0
tk.Button(frame_numeros, text="7", width=5, command=lambda: digitar_numero(7)).grid(row=0, column=0)
tk.Button(frame_numeros, text="8", width=5, command=lambda: digitar_numero(8)).grid(row=0, column=1)
tk.Button(frame_numeros, text="9", width=5, command=lambda: digitar_numero(9)).grid(row=0, column=2)

# Linha 1
tk.Button(frame_numeros, text="4", width=5, command=lambda: digitar_numero(4)).grid(row=1, column=0)
tk.Button(frame_numeros, text="5", width=5, command=lambda: digitar_numero(5)).grid(row=1, column=1)
tk.Button(frame_numeros, text="6", width=5, command=lambda: digitar_numero(6)).grid(row=1, column=2)

# Linha 2
tk.Button(frame_numeros, text="1", width=5, command=lambda: digitar_numero(1)).grid(row=2, column=0)
tk.Button(frame_numeros, text="2", width=5, command=lambda: digitar_numero(2)).grid(row=2, column=1)
tk.Button(frame_numeros, text="3", width=5, command=lambda: digitar_numero(3)).grid(row=2, column=2)

# Linha 3 (Zero centralizado ou embaixo do 1)
tk.Button(frame_numeros, text="0", width=5, command=lambda: digitar_numero(0)).grid(row=3, column=1)

tk.Button(frame_numeros, text="+", width=5, bg="green", fg="white", command=lambda: escolher_operacao("+")).grid(row=0, column=3, padx=2, pady=2)
tk.Button(frame_numeros, text="-", width=5, bg="green", fg="white", command=lambda: escolher_operacao("-")).grid(row=1, column=3, padx=2, pady=2)
tk.Button(frame_numeros, text="x", width=5, bg="green", fg="white", command=lambda: escolher_operacao("*")).grid(row=2, column=3, padx=2, pady=2)
tk.Button(frame_numeros, text="÷", width=5, bg="green", fg="white", command=lambda: escolher_operacao("/")).grid(row=3, column=3, padx=2, pady=2)

# Botão de Igual
tk.Button(
    frame_numeros,
    text="=",
    width=5,
    bg="orange",
    command=calcular_resultado
    ).grid(row=3, column=2, padx=2, pady=2)

# Botão C para limpar
tk.Button(
    frame_numeros,
    text="C",
    width=5,bg="red",
    fg="white",
    command=limpar
    ).grid(row=0, column=4, padx=2, pady=2)

# Botão CE para limpar entrada
tk.Button(
    frame_numeros,
    text="CE",
    width=5,
    bg="darkorange",
    fg="white",
    command=limpar_entrada
).grid(row=1, column=4, padx=2, pady=2)

window.mainloop()