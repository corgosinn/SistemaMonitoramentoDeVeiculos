'''
 IMPORTANTE
ALTERAR CONSTANTES NOME DO BANCO E SENHA DE AMBOS ARQUIVOSANTES DE EXECUTAR
Thiago Corgosinho Silva - 20.2.8117 - BANCO DE DADOS 1
'''
DB_NAME = 'meuBanco'
DB_PW = '021945'

from tkinter import *
from tkinter.ttk import Treeview
from turtle import width
import psycopg2
from pyparsing import col
from operacoesBanco import *


# Display para Adicionar no BD


def addInfo():
    addInfo = Tk()
    addInfo.title("Adicionar Dados")

    addInfo.resizable(False, False)
    fPrinc = LabelFrame(addInfo, padx=50, pady=10)
    fPrinc.grid(padx=70, pady=30)
    texto = Label(fPrinc, text="Adicionar", font=('Arial', 13, 'bold'))
    texto.grid(column=0, row=0, columnspan=2)
    bAddCar = Button(fPrinc, text="Carro",
                     command=lambda: [labelCar(), addInfo.destroy()])
    bAddCar.grid(pady=6, column=0, row=1)

    bAddPessoa = Button(fPrinc, text="Pessoa",
                        command=lambda: [labelPessoa(), addInfo.destroy()])
    bAddPessoa.grid(pady=6, column=1, row=1)

    bLocal = Button(fPrinc, text="Local",
                    command=lambda: [labelLocal(), addInfo.destroy()])
    bLocal.grid(pady=6, column=0, row=2)

    bProd = Button(fPrinc, text="Produto",
                   command=lambda: [labelProduto(), addInfo.destroy()])
    bProd.grid(pady=6, column=1, row=2)

    bTransp = Button(fPrinc, text="Transportadora",
                     command=lambda: [labelTransportadora(), addInfo.destroy()])
    bTransp.grid(pady=6, column=0, row=3, columnspan=2)

    addInfo.mainloop()

# Display para remover do BD


def removeInfo():
    deleteInfo = Tk()
    deleteInfo.title("Remover Dados")

    deleteInfo.resizable(False, False)
    fPrinc = LabelFrame(deleteInfo, padx=50, pady=10)
    fPrinc.grid(padx=70, pady=30)
    texto = Label(fPrinc, text="Remover", font=('Arial', 13, 'bold'))
    texto.grid(column=0, row=0, columnspan=2)
    bAddCar = Button(fPrinc, text="Carro",
                     command=lambda: [deleteCar(), deleteInfo.destroy()])
    bAddCar.grid(pady=6, column=0, row=1)

    bAddPessoa = Button(fPrinc, text="Pessoa",
                        command=lambda: [deletePessoa(), deleteInfo.destroy()])
    bAddPessoa.grid(pady=6, column=1, row=1)

    bLocal = Button(fPrinc, text="Local",
                    command=lambda: [deleteLocal(), deleteInfo.destroy()])
    bLocal.grid(pady=6, column=0, row=2)

    bProd = Button(fPrinc, text="Produto",
                   command=lambda: [deleteProduto(), deleteInfo.destroy()])
    bProd.grid(pady=6, column=1, row=2)

    bTransp = Button(fPrinc, text="Transportadora",
                     command=lambda: [deleteTransportadora(), deleteInfo.destroy()])
    bTransp.grid(pady=6, column=0, row=3, columnspan=2)

    bMon = Button(fPrinc, text="Monitoramento",
                  command=lambda: [deleteMonitoramento(), deleteInfo.destroy()])
    bMon.grid(pady=6, column=0, row=4, columnspan=2)

    deleteInfo.mainloop()

# Qual funcionario carrega certo produto


def ProdutosFunc():
    conn = psycopg2.connect(f"dbname={DB_NAME} user=postgres password={DB_PW}")
    cur = conn.cursor()
    cur.execute("Select * from mostra_produto;")
    arr = cur.fetchall()
    conn.close()
    display.delete(*display.get_children())
    display.config(columns=('c1', 'c2', 'c3', 'c4'))

    display.column("# 1", anchor=CENTER,  stretch=NO)
    display.heading("# 1", text="Funcionario")
    display.column("# 2", anchor=CENTER,  stretch=NO)
    display.heading("# 2", text="Carro")
    display.column("# 3", anchor=CENTER, stretch=NO)
    display.heading("# 3", text="Placa")
    display.column("# 4", anchor=CENTER,  stretch=NO)
    display.heading("# 4", text="Produto")

    for item in range(len(arr)):
        display.insert('', 'end', text=item, values=(arr[item]))
    return arr

# Conta a quantidade de funcionario por Transportadora


def contaFunc():
    conn = psycopg2.connect(f"dbname={DB_NAME} user=postgres password={DB_PW}")
    cur = conn.cursor()
    cur.execute("Select * from count_func ;")
    arr = cur.fetchall()
    conn.close()
    display.delete(*display.get_children())
    display.config(columns=('c1', 'c2'))

    display.column("# 1", anchor=CENTER,  stretch=NO)
    display.heading("# 1", text="Transportadora")
    display.column("# 2", anchor=CENTER,  stretch=NO)
    display.heading("# 2", text="Quantidade Funcionarios")

    for item in range(len(arr)):
        display.insert('', 'end', text=item, values=(arr[item]))
    return arr

# Mostra os produtos


def mostraProdutos():
    conn = psycopg2.connect(f"dbname={DB_NAME} user=postgres password={DB_PW}")
    cur = conn.cursor()
    cur.execute("select p.cod,p.nome,p.valor,p.qtd from produto p;")
    arr = cur.fetchall()
    conn.close()
    display.delete(*display.get_children())
    display.config(columns=('c1', 'c2', 'c3', 'c4'))

    display.column("# 1", anchor=CENTER,  stretch=NO)
    display.heading("# 1", text="Código")
    display.column("# 2", anchor=CENTER,  stretch=NO)
    display.heading("# 2", text="Produto")
    display.column("# 3", anchor=CENTER, stretch=NO)
    display.heading("# 3", text="Valor")
    display.column("# 4", anchor=CENTER,  stretch=NO)
    display.heading("# 4", text="Quantidade")

    for item in range(len(arr)):
        display.insert('', 'end', text=item, values=(arr[item]))
    return arr

# Mostra os funcionarios com seus carros


def verDonos():
    conn = psycopg2.connect(f"dbname={DB_NAME} user=postgres password={DB_PW}")
    cur = conn.cursor()
    cur.execute("Select * from ver_donos;")
    arr = cur.fetchall()
    conn.close()
    display.delete(*display.get_children())
    display.config(columns=('c1', 'c2'))

    display.column("# 1", anchor=CENTER)
    display.heading("# 1", text="Carro")
    display.column("# 2", anchor=CENTER)
    display.heading("# 2", text="Funcionario")

    for item in range(len(arr)):
        display.insert('', 'end', text=item, values=(arr[item]))
    return arr

# MOstra em qual transportadora está sendo transportada


def ProdutoCnpj():
    conn = psycopg2.connect(f"dbname={DB_NAME} user=postgres password={DB_PW}")
    cur = conn.cursor()
    cur.execute("select * from produto_cnpj ;")
    arr = cur.fetchall()
    conn.close()
    display.delete(*display.get_children())
    display.config(columns=('c1', 'c2'))

    display.column("# 1", anchor=CENTER,  stretch=NO)
    display.heading("# 1", text="Produto")
    display.column("# 2", anchor=CENTER,  stretch=NO)
    display.heading("# 2", text="Transportadora")

    for item in range(len(arr)):
        display.insert('', 'end', text=item, values=(arr[item]))
    return arr

# Mostra o monitoramento de onde o produto esteve


def produtoLocal():
    conn = psycopg2.connect(f"dbname={DB_NAME} user=postgres password={DB_PW}")
    cur = conn.cursor()
    cur.execute("select * from produto_local;")
    arr = cur.fetchall()
    conn.close()
    display.delete(*display.get_children())
    display.config(columns=('c1', 'c2', 'c3', 'c4'))

    display.column("# 1", anchor=CENTER,  stretch=NO)
    display.heading("# 1", text="Produto")
    display.column("# 2", anchor=CENTER,  stretch=NO)
    display.heading("# 2", text="Local")
    display.column("# 3", anchor=CENTER, stretch=NO)
    display.heading("# 3", text="Data")
    display.column("# 4", anchor=CENTER,  stretch=NO)
    display.heading("# 4", text="Hora")

    for item in range(len(arr)):
        display.insert('', 'end', text=item, values=(arr[item]))
    return arr

# Monitoramento de local


def monitoramento1():
    conn = psycopg2.connect(f"dbname={DB_NAME} user=postgres password={DB_PW}")
    cur = conn.cursor()
    cur.execute("Select * from monitoramento1 ;")
    arr = cur.fetchall()
    conn.close()

    display.delete(*display.get_children())
    display.config(
        columns=('c1', 'c2', 'c3', 'c4', 'c5'), show="headings")
    display.column("#0", anchor=CENTER, width=0,
                   minwidth=25, stretch=NO)
    display.column("c1", anchor=CENTER,
                   minwidth=25, stretch=NO)
    display.heading("c1", text="Nome")
    display.column("c2", anchor=CENTER, stretch=NO)
    display.heading("c2", text="Carro")
    display.column("c3", anchor=CENTER, stretch=NO)
    display.heading("c3", text="Local")
    display.column("c4", anchor=CENTER,  stretch=NO)
    display.heading("c4", text="Data")
    display.column("# 5", anchor=CENTER, stretch=NO)
    display.heading("# 5", text="Hora")

    for item in range(len(arr)):
        display.insert('', 'end', text=item,
                       values=(arr[item]))

    return arr

# Monitoramento de local


def monitoramento2():
    conn = psycopg2.connect(f"dbname={DB_NAME} user=postgres password={DB_PW}")
    cur = conn.cursor()
    cur.execute("Select * from monitoramento2 ;")
    arr = cur.fetchall()
    conn.close()

    display.delete(*display.get_children())
    display.config(
        columns=('c1', 'c2', 'c3', 'c4', 'c5'), show="headings")
    display.column("#0", anchor=CENTER, width=0,
                   minwidth=25, stretch=NO)
    display.column("c1", anchor=CENTER,
                   minwidth=25, stretch=NO)
    display.heading("c1", text="Placa")
    display.column("c2", anchor=CENTER, stretch=NO)
    display.heading("c2", text="Latitude")
    display.column("c3", anchor=CENTER, stretch=NO)
    display.heading("c3", text="Longitude")
    display.column("c4", anchor=CENTER,  stretch=NO)
    display.heading("c4", text="Data")
    display.column("# 5", anchor=CENTER, stretch=NO)
    display.heading("# 5", text="Hora")

    for item in range(len(arr)):
        display.insert('', 'end', text=item,
                       values=(arr[item]))

    return arr

# Mostra o endereço das garagens dos carros e suas transportadoras


def carrosTransp():
    conn = psycopg2.connect(f"dbname={DB_NAME} user=postgres password={DB_PW}")
    cur = conn.cursor()
    cur.execute("select c.modelo,t.nome,t.endereco from carro c,transportadora t,pessoa p where c.fkcpf = p.cpf and p.fkcnpj = t.cnpj;")
    arr = cur.fetchall()
    conn.close()

    display.delete(*display.get_children())
    display.config(
        columns=('c1', 'c2', 'c3'), show="headings")
    display.column("#0", anchor=CENTER, width=0,
                   minwidth=25, stretch=NO)
    display.column("c1", anchor=CENTER,
                   minwidth=25, stretch=NO, width=120)
    display.heading("c1", text="Modelo")
    display.column("c2", anchor=CENTER, stretch=NO, width=120)
    display.heading("c2", text="Transportadora")
    display.column("c3", anchor=CENTER, stretch=NO, width=350)
    display.heading("c3", text="Garagem")

    for item in range(len(arr)):
        display.insert('', 'end', text=item,
                       values=(arr[item]))

    return arr

# Mostra as informações dos Carros


def infoPessoas():
    conn = psycopg2.connect(f"dbname={DB_NAME} user=postgres password={DB_PW}")
    cur = conn.cursor()
    cur.execute(
        "Select c.cpf,c.nome,c.endereco,c.data_nascimento from pessoa c ;")
    arr = cur.fetchall()
    conn.close()

    display.delete(*display.get_children())
    display.config(
        columns=('c1', 'c2', 'c3', 'c4'), show="headings")
    display.column("#0", anchor=CENTER, width=0,
                   minwidth=25, stretch=NO)
    display.column("c1", anchor=CENTER,
                   minwidth=25, stretch=NO)
    display.heading("c1", text="CPF")
    display.column("c2", anchor=CENTER, stretch=NO, width=120)
    display.heading("c2", text="Nome")
    display.column("c3", anchor=CENTER, stretch=NO, width=300)
    display.heading("c3", text="Endereço")
    display.column("c4", anchor=CENTER,  stretch=NO, width=120)
    display.heading("c4", text="Data")

    for item in range(len(arr)):
        display.insert('', 'end', text=item,
                       values=(arr[item]))

    return arr


def infoTransportadoras():
    conn = psycopg2.connect(f"dbname={DB_NAME} user=postgres password={DB_PW}")
    cur = conn.cursor()
    cur.execute(
        "Select * from transportadora c ;")
    arr = cur.fetchall()
    conn.close()

    display.delete(*display.get_children())
    display.config(
        columns=('c1', 'c2', 'c3'), show="headings")
    display.column("#0", anchor=CENTER, width=0,
                   minwidth=25, stretch=NO)
    display.column("c1", anchor=CENTER,
                   minwidth=25, stretch=NO, width=120)
    display.heading("c1", text="CNPJ")
    display.column("c2", anchor=CENTER, stretch=NO, width=120)
    display.heading("c2", text="Transportadora")
    display.column("c3", anchor=CENTER, stretch=NO, width=300)
    display.heading("c3", text="Endereço")

    for item in range(len(arr)):
        display.insert('', 'end', text=item,
                       values=(arr[item]))

    return arr


def infoCarro():
    conn = psycopg2.connect(f"dbname={DB_NAME} user=postgres password={DB_PW}")
    cur = conn.cursor()
    cur.execute("Select c.modelo,c.cor,c.placa,c.observacoes from carro c ;")
    arr = cur.fetchall()
    conn.close()

    display.delete(*display.get_children())
    display.config(
        columns=('c1', 'c2', 'c3', 'c4'), show="headings")
    display.column("#0", anchor=CENTER, width=0,
                   minwidth=25, stretch=NO)
    display.column("c1", anchor=CENTER,
                   minwidth=25, stretch=NO)
    display.heading("c1", text="Modelo")
    display.column("c2", anchor=CENTER, stretch=NO)
    display.heading("c2", text="Cor")
    display.column("c3", anchor=CENTER, stretch=NO)
    display.heading("c3", text="Placa")
    display.column("c4", anchor=CENTER,  stretch=NO)
    display.heading("c4", text="Obs")

    for item in range(len(arr)):
        display.insert('', 'end', text=item,
                       values=(arr[item]))

    return arr


# Configurações da Janela

janela = Tk()
janela.config(padx=10, pady=10)
janela.title("Monitoramento de Veículos")
janela.minsize(270, 180)
janela.resizable(False, False)
janela.grid_columnconfigure((0, 1, 2, 3), weight=1)
janela.grid_rowconfigure((0, 1, 2), weight=1)

frameLeftTop = LabelFrame(janela, padx=10)
frameLeftTop.grid(column=0, row=0, rowspan=2, sticky=N)
frameLeftBottom = LabelFrame(frameLeftTop, padx=20)
frameLeftBottom.grid(column=0, row=3, rowspan=2, pady=6)

# Inserção e Remoção de dados

txtLeft = Label(frameLeftTop, text='Dados', font=('Arial', 13, 'bold'))
txtLeft.grid(column=0, row=0, pady=10,)
btnAdd = Button(frameLeftTop, text='Adicionar',
                command=addInfo)
btnAdd.grid(column=0, row=1, pady=6)
btnRemove = Button(frameLeftBottom, text='Remover',
                   command=removeInfo)
btnRemove.grid(column=0, row=0, pady=6)

btnMonitoramento = Button(frameLeftTop, text='Monitorar',
                          command=labelMonitoramento)
btnMonitoramento.grid(column=0, row=2, pady=6)
# Consultas
frameConsultas = LabelFrame(janela, padx=10, pady=10)
frameConsultas.grid(column=1, row=1, rowspan=3,
                    columnspan=3, pady=10,  padx=10)
frameConsultas.grid_columnconfigure((0, 1, 2, 3), weight=1)
txtRight = Label(frameConsultas, text='Aparecer consultas',
                 font=('Arial', 13, 'bold'))
txtRight.grid(column=0, columnspan=4, row=0, pady=10)
# Botões
btnMonitoramentos1 = Button(frameConsultas, text='Monitoramentos',
                            command=monitoramento2)
btnMonitoramentos1.grid(column=0, row=1, padx=10)

btnMonitoramentos2 = Button(frameConsultas, text='Monitoramento por nome',
                            command=monitoramento1)
btnMonitoramentos2.grid(column=1, row=1, padx=10)

btnMostraProdutor = Button(frameConsultas, text='Funcionarios/Tranportadoras',
                           command=contaFunc)
btnMostraProdutor.grid(column=2, row=1, padx=10)

btnVerDonos = Button(frameConsultas, text='Funcionarios/Carros',
                     command=verDonos)
btnVerDonos.grid(column=3, row=1, padx=10)
btnVerProdutos = Button(
    frameConsultas, text='Ver Produtos', command=mostraProdutos)
btnVerProdutos.grid(column=0, row=2, padx=10, pady=10)

btnProdutosCar = Button(
    frameConsultas, text='Produtos/Carro', command=ProdutosFunc)
btnProdutosCar.grid(column=1, row=2, padx=10, pady=10)

btnProdutosTransp = Button(
    frameConsultas, text='Produtos/Transportadora', command=ProdutoCnpj)
btnProdutosTransp.grid(column=2, row=2, padx=10, pady=10)

btnProdutosTransp = Button(
    frameConsultas, text='Produtos/GPS', command=produtoLocal)
btnProdutosTransp.grid(column=3, row=2, padx=10, pady=10)
btnInfoCar = Button(
    frameConsultas, text='Ver Carros', command=infoCarro)
btnInfoCar.grid(column=0, row=3, padx=10, pady=10)

btnInfoCar = Button(
    frameConsultas, text='Ver Pessoas', command=infoPessoas)
btnInfoCar.grid(column=1, row=3, padx=10, pady=10)

btnCarTrans = Button(
    frameConsultas, text='Carros/Transportadoras', command=carrosTransp)
btnCarTrans.grid(column=3, row=3, padx=10, pady=10)

btnInfoCar = Button(
    frameConsultas, text='Ver Transportadoras', command=infoTransportadoras)
btnInfoCar.grid(column=2, row=3, padx=10, pady=10)


# Display da tela

display = Treeview(janela, columns=(
    'c1'), show='headings', height=5)
display.grid(column=1, row=0, padx=5)
monitoramento2()
janela.mainloop()
