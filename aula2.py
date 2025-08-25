import tkinter as tk 

janela = tk.Tk() #janela 
janela.title("Calculadora simples")

entrada_var = tk.StringVar() #armazenar 
display = tk.Entry(
    janela,
    textvariable = entrada_var,
    font = ("Arial", 16),
    justify = "right"
)

display.pack(fill="both", padx=10, pady=10)

# Criar botões, cada botão adiciona um número ou operador ao display
tk.Button(janela, text="7", command=lambda: entrada_var.set(entrada_var.get()+"7")).pack(side="left")
tk.Button(janela, text="8", command=lambda: entrada_var.set(entrada_var.get()+"8")).pack(side="left")
tk.Button(janela, text="9", command=lambda: entrada_var.set(entrada_var.get()+"9")).pack(side="left")
tk.Button(janela, text="/", command=lambda: entrada_var.set(entrada_var.get()+"/")).pack(side="left")

tk.Button(janela, text="4", command=lambda: entrada_var.set(entrada_var.get()+"4")).pack(side="left")
tk.Button(janela, text="5", command=lambda: entrada_var.set(entrada_var.get()+"5")).pack(side="left")
tk.Button(janela, text="6", command=lambda: entrada_var.set(entrada_var.get()+"6")).pack(side="left")
tk.Button(janela, text="*", command=lambda: entrada_var.set(entrada_var.get()+"*")).pack(side="left")

tk.Button(janela, text="1", command=lambda: entrada_var.set(entrada_var.get()+"1")).pack(side="left")
tk.Button(janela, text="2", command=lambda: entrada_var.set(entrada_var.get()+"2")).pack(side="left")
tk.Button(janela, text="3", command=lambda: entrada_var.set(entrada_var.get()+"3")).pack(side="left")
tk.Button(janela, text="-", command=lambda: entrada_var.set(entrada_var.get()+"-")).pack(side="left")

tk.Button(janela, text="0", command=lambda: entrada_var.set(entrada_var.get()+"0")).pack(side="left")
tk.Button(janela, text=".", command=lambda: entrada_var.set(entrada_var.get()+"." )).pack(side="left")

# Botão "=" calcula a expressão que está no display
tk.Button(janela, text="=", command=lambda: entrada_var.set(str(eval(entrada_var.get())))).pack(side="left")

# Botão "+" adiciona o operador de soma
tk.Button(janela, text="+", command=lambda: entrada_var.set(entrada_var.get()+"+")).pack(side="left")

# Botão "C" limpa o display
tk.Button(janela, text="C", command=lambda: entrada_var.set("")).pack(side="left")

# Inicia o loop principal da interface, mantendo a janela aberta
janela.mainloop()
