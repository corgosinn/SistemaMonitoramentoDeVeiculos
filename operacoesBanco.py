from tkinter import *
from unicodedata import name
import psycopg2

'''
 IMPORTANTE
ALTERAR CONSTANTES NOME DO BANCO E SENHA DE AMBOS ARQUIVOSANTES DE EXECUTAR
Thiago Corgosinho Silva - 20.2.8117 - BANCO DE DADOS 1
'''

DB_NAME = 'meuBanco'
DB_PW = '021945'


def analiza(nmr):
    janela = Tk()
    janela.title("Operação")
    janela.config(padx=5, pady=5)

    frame = LabelFrame(janela, padx=80, pady=30)
    frame.pack()

    if nmr == 0:

        textPlaca = Label(frame, text="Erro na operação!")
        textPlaca.pack()
    else:
        textPlaca = Label(frame, text="Sucesso!")
        textPlaca.pack()


# Remove e Add carro / return 0 se der errado e 1 se der certo


def carroManager(operation, placa, modelo='', cor='', obs='', cpf=''):
    conn = psycopg2.connect(f"dbname={DB_NAME} user=postgres password={DB_PW}")
    cur = conn.cursor()
    if operation == 0:  # add carro
        try:
            if len(placa) == 7 and len(modelo) > 3:
                cur.execute(
                    f"insert into carro values ('{placa}','{modelo}','{cor}','{obs}','{cpf}');")
                conn.commit()
                conn.close()
                return 1
            else:
                conn.close()
                return 0
        except:
            conn.close()
            return 0
    else:  # remover carro
        try:
            cur.execute(
                f"delete from carro c where c.placa = '{placa}' RETURNING c.placa;")
            conn.commit()
            retorno = cur.fetchall()
            if len(retorno) == 0:
                conn.close()
                return 0
            conn.close()
            return 1
        except:
            conn.close()
            print("Erro")
            return 0


# Remove e Add pessoas / return 0 se der errado e 1 se der certo


def pessoasManager(operation, cpf, nome='', endereco='', data='', cnpj=''):
    conn = psycopg2.connect(f"dbname={DB_NAME} user=postgres password={DB_PW}")
    cur = conn.cursor()
    if operation == 0:  # add
        try:
            if len(cpf) == 11 and len(nome) > 3 and len(endereco) > 3 and len(data) == 10:
                cur.execute(
                    f"insert into pessoa values ('{cpf}','{nome}','{endereco}','{data}','{cnpj}');")
                conn.commit()
                conn.close()
                return 1
            else:
                conn.close()
                return 0
        except:
            conn.close()
            return 0
    else:  # remover
        try:
            cur.execute(
                f"delete from pessoa p where p.cpf = '{cpf}' returning p.cpf;")
            conn.commit()
            retorno = cur.fetchall()
            if len(retorno) == 0:
                conn.close()
                return 0
            conn.close()
            return 1
        except:
            conn.close()
            print("Erro")
            return 0


# Remove e Add Monitoramento / return 0 se der errado e 1 se der certo

def localManager(operation, nome, x=0.0, y=0.0):
    conn = psycopg2.connect(f"dbname={DB_NAME} user=postgres password={DB_PW}")
    cur = conn.cursor()
    if operation == 0:  # add
        try:
            if len(nome) > 3 and len(x) > 1 and len(y) > 1:
                cur.execute(
                    f"insert into local values ('{x}','{y}','{nome}');")
                conn.commit()
                conn.close()
                return 1
            else:
                conn.close()
                return 0
        except:
            conn.close()
            return 0
    else:  # remover
        try:
            cur.execute(
                f"delete from local l where l.nome_local = '{nome}' RETURNING l.nome_local;")
            conn.commit()
            retorno = cur.fetchall()
            if len(retorno) == 0:
                conn.close()
                return 0
            conn.close()
            return 1
        except:
            conn.close()
            print("Erro")
            return 0


# Remove e Add Monitoramento / return 0 se der errado e 1 se der certo

def monitoramentoManager(operation, data, hora, placa='', local=''):
    conn = psycopg2.connect(f"dbname={DB_NAME} user=postgres password={DB_PW}")
    cur = conn.cursor()
    if operation == 0:  # add
        try:
            if len(placa) == 7 and len(local) > 2 and len(data) == 10 and len(hora) == 5:
                cur.execute(
                    f"insert into monitoramento values ('{placa}','{local}','{data}','{hora}');")
                conn.commit()
                conn.close()
                return 1
            else:
                conn.close()
                return 0
        except:
            conn.close()
            return 0
    else:  # remover
        try:
            cur.execute(
                f"delete from monitoramento m where m.data = '{data}' and m.hora = '{hora}' RETURNING m.data;")
            conn.commit()
            retorno = cur.fetchall()
            if len(retorno) == 0:
                conn.close()
                return 0
            conn.close()
            return 1
        except:
            conn.close()
            print("Erro")
            return 0

# Remove e Add produto / return 0 se der errado e 1 se der certo


def produtoManager(operation, cod, nome='', valor='', qtd='', placa=''):
    conn = psycopg2.connect(f"dbname={DB_NAME} user=postgres password={DB_PW}")
    cur = conn.cursor()
    if operation == 0:  # add
        try:
            if len(cod) > 1 and len(nome) > 2:
                cur.execute(
                    f"insert into produto values ('{nome}','{cod}','{valor}','{qtd}','{placa}');")
                conn.commit()
                conn.close()
                return 1
            else:
                conn.close()
                return 0
        except:
            conn.close()
            return 0
    else:  # remover
        try:
            cur.execute(
                f"delete from produto p where p.cod = '{cod}' RETURNING p.cod ;")
            conn.commit()
            retorno = cur.fetchall()
            if len(retorno) == 0:
                conn.close()
                return 0
            conn.close()
            return 1
        except:
            conn.close()
            print("Erro")
            return 0


# Remove e Add Transportadora / return 0 se der errado e 1 se der certo


def transportadoraManager(operation, cnpj, nome='', endereco=''):
    conn = psycopg2.connect(f"dbname={DB_NAME} user=postgres password={DB_PW}")
    cur = conn.cursor()
    if operation == 0:  # Adiciona
        try:
            # Se o CNPJ tiver exatamente 14 números
            if len(cnpj) == 14 and len(nome) > 3 and len(endereco) > 5:
                cur.execute(
                    f"insert into transportadora values ('{cnpj}','{nome}','{endereco}');")
                conn.commit()
                conn.close()
                return 1
            else:
                conn.close()
                return 0
        except:
            conn.close()
            return 0
    else:  # remover
        try:
            cur.execute(
                f"delete from transportadora m where m.cnpj = '{cnpj}' RETURNING m.cnpj;")
            conn.commit()
            retorno = cur.fetchall()
            if len(retorno) == 0:
                conn.close()
                return 0
            conn.close()
            return 1
        except:
            conn.close()
            print("Erro")
            return 0

# LABELS PARA ADICIONAR E REMOVER


def labelTransportadora():
    janela = Tk()
    janela.title("Transportadora")
    janela.config(padx=5, pady=5)

    frame = LabelFrame(janela, padx=30, pady=30)
    frame.pack()

    tCnpj = Label(frame, text="CNPJ (14 digitos sem pontos)")
    tCnpj.pack()
    iCnpj = Entry(frame, width=35, borderwidth=5)
    iCnpj.pack()

    tNome = Label(frame, text="Nome")
    tNome.pack()
    iNome = Entry(frame, width=35, borderwidth=5)
    iNome.pack()

    tEnd = Label(frame, text="Endereço")
    tEnd.pack()
    iEnd = Entry(frame, width=35, borderwidth=5)
    iEnd.pack()

    submit = Button(frame, text="Adicionar",
                    command=lambda: [analiza(transportadoraManager(0, iCnpj.get(), iNome.get(), iEnd.get())), print(iEnd.get()), janela.destroy()])
    submit.pack(pady=6)


def deleteTransportadora():
    sentmsg = StringVar()

    janela = Tk()
    janela.title("Transportadora")
    janela.config(padx=5, pady=5)

    frame = LabelFrame(janela, padx=30, pady=30)
    frame.pack()

    conn = psycopg2.connect(f"dbname={DB_NAME} user=postgres password={DB_PW}")
    cur = conn.cursor()
    cur.execute("Select p.cnpj,p.nome from transportadora p;")
    nomes = cur.fetchall()
    scrollbar = Scrollbar(frame, orient='vertical')
    scrollbar.pack(side=RIGHT, fill=Y)

    iCNPJ = Listbox(frame, height=5, yscrollcommand=scrollbar.set)
    scrollbar.config(command=iCNPJ.yview)
    for q in range(len(nomes)):
        iCNPJ.insert(q, nomes[q][0])
    conn.close()
    iCNPJ.selection_set(0)
    iCNPJ.pack()
    sentlbl = Label(frame, text=sentmsg.get())
    sentlbl.pack()

    def sendName(self=''):
        indx = iCNPJ.curselection()
        if(len(indx) == 1):
            sentmsg.set(f'Transportadora: {nomes[indx[0]][1]}')
        else:
            sentmsg.set('')

        sentlbl.config(text=sentmsg.get())
    sendName()

    iCNPJ.bind('<<ListboxSelect>>', sendName)

    submit = Button(frame, text="Remover",
                    command=lambda: [analiza(transportadoraManager(1, iCNPJ.get(ACTIVE))), janela.destroy()])
    submit.pack(pady=6)


def labelCar():
    sentmsg = StringVar()
    janela = Tk()
    janela.title("Carro")
    janela.config(padx=5, pady=5)

    frame = LabelFrame(janela, padx=30, pady=30)
    frame.pack()

    textPlaca = Label(frame, text="Placa (7 digitos sem pontuação)")
    textPlaca.pack()
    inputPlaca = Entry(frame, width=35, borderwidth=5)
    inputPlaca.pack()

    textModelo = Label(frame, text="Modelo")
    textModelo.pack()

    inputModelo = Entry(frame, width=35, borderwidth=5)
    inputModelo.pack()
    textCor = Label(frame, text="Cor")
    textCor.pack()
    iptCor = Entry(frame, width=35, borderwidth=5)
    iptCor.pack()
    txObs = Label(frame, text="Observacoes")
    txObs.pack()
    inpObs = Entry(frame, width=35, borderwidth=5)
    inpObs.pack()
    txCpf = Label(frame, text="Funcionario")
    txCpf.pack()

    frameInside = LabelFrame(frame, padx=10, pady=10)
    frameInside.pack()

    conn = psycopg2.connect(f"dbname={DB_NAME} user=postgres password={DB_PW}")
    cur = conn.cursor()
    cur.execute("Select p.cpf,p.nome from pessoa p;")
    nomes = cur.fetchall()

    scrollbar = Scrollbar(frameInside, orient='vertical')
    scrollbar.pack(side=RIGHT, fill=Y)

    lbox = Listbox(frameInside, height=5, yscrollcommand=scrollbar.set)
    scrollbar.config(command=lbox.yview)
    for q in range(len(nomes)):
        lbox.insert(q, nomes[q][0])
    conn.close()
    lbox.selection_set(0)
    lbox.pack()
    sentlbl = Label(frame, text=sentmsg.get())
    sentlbl.pack()

    def sendName(self=''):
        indx = lbox.curselection()
        if(len(indx) == 1):
            sentmsg.set(f'Nome: {nomes[indx[0]][1]}')
        else:
            sentmsg.set('')

        sentlbl.config(text=sentmsg.get())
    sendName()

    lbox.bind('<<ListboxSelect>>', sendName)

    submit = Button(frame, text="Adicionar",
                    command=lambda: [analiza(carroManager(0, inputPlaca.get(), inputModelo.get(), iptCor.get(), inpObs.get(), lbox.get(ACTIVE))), janela.destroy()])
    submit.pack(pady=7)


def deleteCar():
    sentmsg = StringVar()
    janela = Tk()
    janela.title("Carro")
    janela.config(padx=5, pady=5)

    frame = LabelFrame(janela, padx=30, pady=30)
    frame.pack()

    conn = psycopg2.connect(f"dbname={DB_NAME} user=postgres password={DB_PW}")
    cur = conn.cursor()
    cur.execute("Select p.placa,p.modelo from carro p;")
    nomes = cur.fetchall()
    scrollbar = Scrollbar(frame, orient='vertical')
    scrollbar.pack(side=RIGHT, fill=Y)

    iPlaca = Listbox(frame, height=5, yscrollcommand=scrollbar.set)
    scrollbar.config(command=iPlaca.yview)
    for q in range(len(nomes)):
        iPlaca.insert(q, nomes[q][0])
    conn.close()
    iPlaca.selection_set(0)
    iPlaca.pack()
    sentlbl = Label(frame, text=sentmsg.get())
    sentlbl.pack()

    def sendName(self=''):
        indx = iPlaca.curselection()
        if(len(indx) == 1):
            sentmsg.set(f'Carro: {nomes[indx[0]][1]}')
        else:
            sentmsg.set('')

        sentlbl.config(text=sentmsg.get())
    sendName()

    iPlaca.bind('<<ListboxSelect>>', sendName)

    submit = Button(frame, text="Remover",
                    command=lambda: [analiza(carroManager(1, iPlaca.get(ACTIVE))), janela.destroy()])
    submit.pack(pady=7)


def labelPessoa():
    sentmsg = StringVar()
    janela = Tk()
    janela.title("Pessoa")
    janela.config(padx=5, pady=5)

    frame = LabelFrame(janela, padx=30, pady=30)
    frame.pack()

    tNome = Label(frame, text="Nome")
    tNome.pack()
    iNome = Entry(frame, width=35, borderwidth=5)
    iNome.pack()

    tCpf = Label(frame, text="CPF (11 dígitos sem pontuação)")
    tCpf.pack()
    iCpf = Entry(frame, width=35, borderwidth=5)
    iCpf.pack()

    tEnd = Label(frame, text="Endereço")
    tEnd.pack()
    iEnd = Entry(frame, width=35, borderwidth=5)
    iEnd.pack()

    tData = Label(frame, text="Data de Nascimento (../../....)")
    tData.pack()
    iData = Entry(frame, width=35, borderwidth=5)
    iData.pack()

    txCpf = Label(frame, text="Transportadora")
    txCpf.pack()

    frameInside = LabelFrame(frame, padx=10, pady=10)
    frameInside.pack()

    conn = psycopg2.connect(f"dbname={DB_NAME} user=postgres password={DB_PW}")
    cur = conn.cursor()
    cur.execute("Select p.cnpj,p.nome from transportadora p;")
    nomes = cur.fetchall()
    scrollbar = Scrollbar(frameInside, orient='vertical')
    scrollbar.pack(side=RIGHT, fill=Y)

    iCNPJ = Listbox(frameInside, height=5, yscrollcommand=scrollbar.set)
    scrollbar.config(command=iCNPJ.yview)
    for q in range(len(nomes)):
        iCNPJ.insert(q, nomes[q][0])
    conn.close()
    iCNPJ.selection_set(0)
    iCNPJ.pack()
    sentlbl = Label(frame, text=sentmsg.get())
    sentlbl.pack()

    def sendName(self=''):
        indx = iCNPJ.curselection()
        if(len(indx) == 1):
            sentmsg.set(f'Transportadora: {nomes[indx[0]][1]}')
        else:
            sentmsg.set('')

        sentlbl.config(text=sentmsg.get())
    sendName()

    iCNPJ.bind('<<ListboxSelect>>', sendName)

    submit = Button(frameInside, text="Adicionar",
                    command=lambda: [analiza(pessoasManager(0, iCpf.get(), iNome.get(), iEnd.get(), iData.get(), iCNPJ.get(ACTIVE))), janela.destroy()])
    submit.pack(pady=7)


def deletePessoa():
    sentmsg = StringVar()

    janela = Tk()
    janela.title("Delete Pessoa")
    janela.config(padx=5, pady=5)

    frame = LabelFrame(janela, padx=30, pady=30)
    frame.pack()
    conn = psycopg2.connect(f"dbname={DB_NAME} user=postgres password={DB_PW}")
    cur = conn.cursor()
    cur.execute("Select p.cpf,p.nome from pessoa p;")
    nomes = cur.fetchall()
    scrollbar = Scrollbar(frame, orient='vertical')
    scrollbar.pack(side=RIGHT, fill=Y)

    iCpf = Listbox(frame, height=5, yscrollcommand=scrollbar.set)
    scrollbar.config(command=iCpf.yview)
    for q in range(len(nomes)):
        iCpf.insert(q, nomes[q][0])
    conn.close()
    iCpf.selection_set(0)
    iCpf.pack()
    sentlbl = Label(frame, text=sentmsg.get())
    sentlbl.pack()

    def sendName(self=''):
        indx = iCpf.curselection()
        if(len(indx) == 1):
            sentmsg.set(f'Nome: {nomes[indx[0]][1]}')
        else:
            sentmsg.set('')

        sentlbl.config(text=sentmsg.get())
    sendName()

    iCpf.bind('<<ListboxSelect>>', sendName)

    submit = Button(frame, text="Remover",
                    command=lambda: [analiza(pessoasManager(1, iCpf.get(ACTIVE))), janela.destroy()])
    submit.pack(pady=7)


def labelLocal():
    janela = Tk()
    janela.title("Local")
    janela.config(padx=5, pady=5)

    frame = LabelFrame(janela, padx=30, pady=30)
    frame.pack()

    tNome = Label(frame, text="Nome")
    tNome.pack()
    iNome = Entry(frame, width=35, borderwidth=5)
    iNome.pack()

    tX = Label(frame, text="Coordenada X")
    tX.pack()
    iX = Entry(frame, width=35, borderwidth=5)
    iX.pack()

    tY = Label(frame, text="Coordenada Y")
    tY.pack()
    iY = Entry(frame, width=35, borderwidth=5)
    iY.pack()

    submit = Button(frame, text="Adicionar",
                    command=lambda: [analiza(localManager(0, iNome.get(), iX.get(), iY.get())), janela.destroy()])
    submit.pack(pady=15)


def deleteLocal():
    janela = Tk()
    sentmsg = StringVar()
    janela.title("Local")
    janela.config(padx=5, pady=5)

    frame = LabelFrame(janela, padx=30, pady=30)
    frame.pack()

    conn = psycopg2.connect(f"dbname={DB_NAME} user=postgres password={DB_PW}")
    cur = conn.cursor()
    cur.execute("Select p.nome_local from local p;")
    arrLocais = cur.fetchall()

    scrollbar2 = Scrollbar(frame, orient='vertical')
    scrollbar2.pack(side=RIGHT, fill=Y)

    iLocal = Listbox(frame, height=5, exportselection=False,
                     yscrollcommand=scrollbar2.set)
    scrollbar2.config(command=iLocal.yview)
    for q in range(len(arrLocais)):
        iLocal.insert(q, arrLocais[q][0])
    conn.close()
    iLocal.selection_set(0)
    iLocal.pack()

    submit = Button(frame, text="Remover",
                    command=lambda: [analiza(localManager(1, iLocal.get(ACTIVE))), janela.destroy()])
    submit.pack(pady=15)


def labelMonitoramento():
    sentmsg = StringVar()
    janela = Tk()
    janela.resizable(False, False)
    janela.title("Monitoramento")
    janela.config(padx=50, pady=20)

    frame = LabelFrame(janela, padx=30, pady=30)
    frame.pack()

    tData = Label(frame, text="Data do monitoramento (../../....)")
    tData.pack()
    iData = Entry(frame, width=35, borderwidth=5)
    iData.pack()

    tHora = Label(frame, text="Hora (formato 00:00))")
    tHora.pack()
    iHora = Entry(frame, width=35, borderwidth=5)
    iHora.pack()

    tLocal = Label(frame, text="Local")
    tLocal.pack()

    frameLocal = LabelFrame(frame, padx=10, pady=10)
    frameLocal.pack()

    conn = psycopg2.connect(f"dbname={DB_NAME} user=postgres password={DB_PW}")
    cur = conn.cursor()
    cur.execute("Select p.nome_local from local p;")
    arrLocais = cur.fetchall()

    scrollbar2 = Scrollbar(frameLocal, orient='vertical')
    scrollbar2.pack(side=RIGHT, fill=Y)

    iLocal = Listbox(frameLocal, height=5, exportselection=False,
                     yscrollcommand=scrollbar2.set)
    scrollbar2.config(command=iLocal.yview)
    for q in range(len(arrLocais)):
        iLocal.insert(q, arrLocais[q][0])
    conn.close()
    iLocal.selection_set(0)
    iLocal.pack()

    tPlaca = Label(frame, text="Placa")
    tPlaca.pack(pady=10)
    frameInside = LabelFrame(frame, padx=10, pady=10)
    frameInside.pack()

    scrollbar = Scrollbar(frameInside, orient='vertical')
    scrollbar.pack(side=RIGHT, fill=Y)

    conn = psycopg2.connect(f"dbname={DB_NAME} user=postgres password={DB_PW}")
    cur = conn.cursor()
    cur.execute("Select p.placa,p.modelo from carro p;")
    nomes = cur.fetchall()

    iCarro = Listbox(frameInside, height=5,
                     exportselection=False, yscrollcommand=scrollbar.set)
    scrollbar.config(command=iCarro.yview)
    for q in range(len(nomes)):
        iCarro.insert(q, nomes[q][0])
    conn.close()
    iCarro.selection_set(0)
    iCarro.pack()
    sentlbl = Label(frame, text=sentmsg.get())
    sentlbl.pack()

    def sendName(self=''):
        indx = iCarro.curselection()
        if(len(indx) == 1):
            sentmsg.set(f'Carro: {nomes[indx[0]][1]}')
        else:
            sentmsg.set('')

        sentlbl.config(text=sentmsg.get())
    sendName()

    iCarro.bind('<<ListboxSelect>>', sendName)

    submit = Button(janela, text="Adicionar",
                    command=lambda: [analiza(monitoramentoManager(0, iData.get(), iHora.get(), iCarro.get(ACTIVE), iLocal.get(ACTIVE))), janela.destroy()])
    submit.pack()


def deleteMonitoramento():
    sentmsg = StringVar()
    janela = Tk()
    janela.resizable(False, False)
    janela.title("Monitoramento")
    janela.config(padx=50, pady=20)

    frame = LabelFrame(janela, padx=30, pady=30)
    frame.pack()

    tData = Label(frame, text="Data do monitoramento")
    tData.pack()
    iData = Entry(frame, width=35, borderwidth=5)
    iData.pack()

    tHora = Label(frame, text="Hora")
    tHora.pack()
    iHora = Entry(frame, width=35, borderwidth=5)
    iHora.pack()

    submit = Button(janela, text="Remover",
                    command=lambda: [analiza(monitoramentoManager(1, iData.get(), iHora.get())), janela.destroy()])
    submit.pack()


def labelProduto():
    sentmsg = StringVar()
    janela = Tk()
    janela.title("Produto")
    janela.config(padx=5, pady=5)

    frame = LabelFrame(janela, padx=30, pady=30)
    frame.pack()

    tCod = Label(frame, text="Código")
    tCod.pack()
    iCod = Entry(frame, width=35, borderwidth=5)
    iCod.pack()

    tNome = Label(frame, text="Nome")
    tNome.pack()
    iNome = Entry(frame, width=35, borderwidth=5)
    iNome.pack()

    tValor = Label(frame, text="Valor")
    tValor.pack()
    iValor = Entry(frame, width=35, borderwidth=5)
    iValor.pack()

    tQtd = Label(frame, text="Quantidade")
    tQtd.pack()
    iQtd = Entry(frame, width=35, borderwidth=5)
    iQtd.pack()

    tPlaca = Label(frame, text="Placa")
    tPlaca.pack()

    frameInside = LabelFrame(frame, padx=10, pady=10)
    frameInside.pack()

    conn = psycopg2.connect(f"dbname={DB_NAME} user=postgres password={DB_PW}")
    cur = conn.cursor()
    cur.execute("Select p.placa,p.modelo from carro p;")
    nomes = cur.fetchall()
    scrollbar = Scrollbar(frameInside, orient='vertical')
    scrollbar.pack(side=RIGHT, fill=Y)

    iPlaca = Listbox(frameInside, height=5, yscrollcommand=scrollbar.set)
    scrollbar.config(command=iPlaca.yview)
    for q in range(len(nomes)):
        iPlaca.insert(q, nomes[q][0])
    conn.close()
    iPlaca.selection_set(0)
    iPlaca.pack()
    sentlbl = Label(frame, text=sentmsg.get())
    sentlbl.pack()

    def sendName(self=''):
        indx = iPlaca.curselection()
        if(len(indx) == 1):
            sentmsg.set(f'Carro: {nomes[indx[0]][1]}')
        else:
            sentmsg.set('')

        sentlbl.config(text=sentmsg.get())
    sendName()

    iPlaca.bind('<<ListboxSelect>>', sendName)

    submit = Button(frame, text="Adicionar",
                    command=lambda: [analiza(produtoManager(0, iCod.get(), iNome.get(), iValor.get(), iQtd.get(), iPlaca.get(ACTIVE))), janela.destroy()])
    submit.pack(pady=10)


def deleteProduto():

    janela = Tk()
    janela.title("Produto")
    janela.config(padx=5, pady=5)

    frame = LabelFrame(janela, padx=30, pady=30)
    frame.pack()

    tCod = Label(frame, text="Código")
    tCod.pack()
    iCod = Entry(frame, width=35, borderwidth=5)
    iCod.pack()

    submit = Button(frame, text="Remover",
                    command=lambda: [analiza(produtoManager(1, iCod.get())), janela.destroy()])
    submit.pack(pady=10)
