from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title("Happy Pongal")
root.geometry("900x900")

root.configure(background="red")

Img = ImageTk.PhotoImage(Image.open("img1.jpg"))
Img1 = ImageTk.PhotoImage(Image.open("img2.jpg"))

label = Label(root,text="Enter Your Registration Details Below",bg="blue",fg="white",font=('Josefin Sans',16))
label.place(relx=0.5,rely=0.64,anchor=CENTER)

label_name = Label(root,text="Enter your Name :- ",bg="red",fg="white",font=('Lora',18))
label_name.place(relx=0.4,rely=0.7,anchor=CENTER)

label_message = Label(root,text="Message you want to send :- ",bg="red",fg="white",font=('Lora',18))
label_message.place(relx=0.4,rely=0.8,anchor=CENTER)

label_receiver_name = Label(root,text="Enter Reciever's Name :- ",bg="red",fg="white",font=('Lora',18))
label_receiver_name.place(relx=0.4,rely=0.9,anchor=CENTER)

label_sankranti_image = Label(root,bg="red")
label_sankranti_image1 = Label(root,bg="red")

input_word = Entry(root)
input_word.place(relx=0.6,rely=0.7,anchor=CENTER)

my_text = Text(root,height=5,width=15)
my_text.place(relx=0.6,rely=0.8,anchor=CENTER)

input_word1 = Entry(root)
input_word1.place(relx=0.6,rely=0.9,anchor=CENTER)

canvas = Canvas(root,width=590,height=420,bg="yellow")

label_display_name = Label(root,bg="yellow",fg="purple",font=('Pacifico',16))
label_display_message = Label(root,bg="yellow",fg="purple",font=('Pacifico',16))
label_display_receiver_name = Label(root,bg="yellow",fg="purple",font=('Pacifico',16))

def click():
    entry_word = input_word.get()
    label_display_name["text"] = "From, \n"+entry_word
    textarea = my_text.get(1.0,END)
    label_display_message["text"] = textarea
    entry_word1 = input_word1.get()
    label_display_receiver_name["text"] = "To, \n"+entry_word1
    label_sankranti["text"] = "Happy \n Makara \n Sankranti"
    label_sankranti1["text"] = "Happy \n Makara \n Sankranti"
    label_sankranti_image["image"] = Img
    label_sankranti_image1["image"] = Img1

label_display_name.place(relx=0.5,rely=0.5,anchor=CENTER)
label_display_message.place(relx=0.5,rely=0.3,anchor=CENTER)
label_display_receiver_name.place(relx=0.5,rely=0.1,anchor=CENTER)

label_sankranti = Label(root,bg="cyan",fg="black",font=('PT Sans',16))
label_sankranti.place(relx=0.33,rely=0.3,anchor=CENTER)

label_sankranti1 = Label(root,bg="cyan",fg="black",font=('PT Sans',16))
label_sankranti1.place(relx=0.67,rely=0.3,anchor=CENTER)

label_sankranti_image.place(relx=0.14,rely=0.3,anchor=CENTER)
label_sankranti_image1.place(relx=0.86,rely=0.3,anchor=CENTER)

canvas.pack()

btn = Button(root,text="Create Card",command=click,bg="green",fg="black")
btn.place(relx=0.5,rely=0.96,anchor=CENTER)

root.mainloop()

