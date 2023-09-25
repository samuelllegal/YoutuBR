import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube
from pytube import Playlist
from urllib.request import urlopen
from PIL import Image, ImageTk

label1 = ''
visualizar_descricao = ''
mais = []
INPUT = ''

def atualizar():
    return root.update()

def mp():
    ss = str(vart1.get())
    print(ss)



def url_to_image(url):
    # return the image
    print('a')


def baixarImg(link):
    a = Image.open(urlopen(link))
    a.save("visualizar.jpg")
    atualizar()


def adicionar():
    INPUT = url.get("1.0", "end-1c")
    if(INPUT != ''):
        atualizar()
        if(str(vart1.get()) == '1' or str(vart1.get()) == '2'):
            if(str(var1.get()) == '0'):
                video(INPUT)
            if(str(var1.get()) == '1'):
                lista = Playlist(INPUT)
                n = 0
                for dado in lista.videos:
                    video(lista[n])
                    n += 1
                n = 0

        else:
            print('precisa escolher se vai baixar como audio ou vídeo.')
    else:
        print('precisa colocar uma URL válida.')

def baixar(mais):
    local = tkinter.filedialog.askdirectory()
    for item in mais:
        atualizar()
        ytu = YouTube(item[0])
        if(item[3] == '1'):
            atualizar()
            stream = ytu.streams.get_audio_only()
        elif(item[3] == '2'):
            atualizar()
            stream = ytu.streams.get_highest_resolution()
        stream.download(output_path=local)
        atualizar()
    mais.clear()



def video(INPUT):
    atualizar()
    global mais
    ytu = YouTube(INPUT)
    conjunto = [INPUT, ytu.title, ytu.thumbnail_url, str(vart1.get()) ]
    mais.append(conjunto)
    lista.set(ytu.title)


    #conjunto.clear()


def Take_input():
    atualizar()
    global INPUT
    INPUT = url.get("1.0", "end-1c")
    ytu = YouTube(INPUT)
    link= ytu.thumbnail_url
    baixarImg(link)

    global label1
    global visualizar_descricao
    if (label1 != ''):
        label1.destroy()
        visualizar_descricao.destroy()


    image1 = Image.open("visualizar.jpg")
    image1 = image1.resize((100, 55))
    test = ImageTk.PhotoImage(image1)
    label1 = tkinter.Label(image=test)
    label1.image = test
    label1.grid(column=3, row=1)
    visualizar_descricao = Label(root, text=ytu.title)
    visualizar_descricao.grid(column=3, row=2)







root = Tk()
var1 = IntVar()
vart1 = IntVar()
lista = StringVar()


root.geometry("800x500+400+200")
root.resizable(True, True)
root.minsize(300, 300)
root.maxsize(7000, 7000)
root.title("Baixar Videos do YouTube")
frm = ttk.Frame(root, padding=10)
frm.grid()

texto_base = Label(root, text="Baixar Videos do YouTube", font="Arial 25")
text1 = Label(root, text="URL:", anchor=E, bg='red')
url = Text(root, height=4, width=48, bg="light yellow")

visualizar = Label(root, text="imagem", height=4, width=48)

selecionar = Button(root, text="enviar", command=lambda: Take_input())
adiciona = Button(root, text="adicionar na fila", command=lambda: adicionar())
baixa = Button(root, text="Baixar", command=lambda: baixar(mais))
visao_geral = Label(root, textvariable=lista)
playlist = Checkbutton(root, text='PlayList', variable=var1, onvalue=1, offvalue=0)
mp3 = Radiobutton(root, text='MP3', variable=vart1, value=1, command=mp)
mp4 = Radiobutton(root, text='MP4', variable=vart1, value=2, command=mp)

texto_base.grid(column=0, row=0, columnspan=4)
text1.grid(column=0, row=1)
url.grid(column=1, row=1)


selecionar.grid(column=3, row=3)
adiciona.grid(column=3, row=4)
baixa.grid(column=3, row=5)
visao_geral.grid(column=4, row=1)
playlist.grid(column=1, row=2)
mp3.grid(column=1, row=3)
mp4.grid(column=1, row=4)


root.mainloop()






