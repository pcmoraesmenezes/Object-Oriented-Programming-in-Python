"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra.
Conta (ABC)
    ContaCorrente
    ContaPoupanca
Pessoa (ABC)
    Cliente
        Clente -> Conta
Banco
    Banco -> Cliente
    Banco -> Conta
Dicas:
Criar classe Cliente que herda da classe Pessoa (Herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas têm agência, número da conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter o método sacar abstrato (Abstração e
    polimorfismo - as subclasses que implementam o método sacar)
Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clentes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)
Banco autentica por um método.
"""
import tkinter as tk
from contas import ContaPoupanca, ContaCorrente
from pessoa import Cliente
from banco import Banco

# Criando instâncias de contas
cp1 = ContaPoupanca(111, 222, 1000)
cc1 = ContaCorrente(111, 333, 2000, 1000)

# Criando instâncias de clientes
cliente1 = Cliente("João", 30)
cliente2 = Cliente("Maria", 25)

# Associando contas aos clientes
cliente1.conta = cp1
cliente2.conta = cc1

# Criando instância de banco
banco = Banco()

# Adicionando agência, clientes e contas ao banco
banco.agencias = [111]
banco.clientes = [cliente1, cliente2]
banco.contas = [cp1, cc1]

# Função para realizar depósito
def depositar():
    valor = float(entry_valor.get())
    cp1.depositar(valor)
    label_saldo["text"] = f"Saldo: R${cp1.saldo}"

# Função para realizar saque
def sacar():
    valor = float(entry_valor.get())
    cp1.sacar(valor)
    label_saldo["text"] = f"Saldo: R${cp1.saldo}"

# Configuração da janela
window = tk.Tk()
window.title("Banco")
window.geometry("300x200")

# Componentes da interface
label_saldo = tk.Label(window, text=f"Saldo: R${cp1.saldo}")
label_saldo.pack(pady=10)

label_valor = tk.Label(window, text="Valor:")
label_valor.pack()

entry_valor = tk.Entry(window)
entry_valor.pack()

btn_depositar = tk.Button(window, text="Depositar", command=depositar)
btn_depositar.pack(pady=5)

btn_sacar = tk.Button(window, text="Sacar", command=sacar)
btn_sacar.pack(pady=5)

# Loop principal da interface gráfica
window.mainloop()
