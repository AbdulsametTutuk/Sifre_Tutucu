from tkinter import *
from tkinter import messagebox
import random
# ---------------------------- ŞİFRE OLUŞTURUCU ------------------------------- #
def olusturucu():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for i in range(nr_letters)]
    password_list += [random.choice(symbols) for i in range(nr_symbols)]
    password_list += [random.choice(numbers) for i in range(nr_numbers)]

    random.shuffle(password_list)
    password = "".join(password_list)


    sifre_giris.insert(0,password)
# ---------------------------- ŞİFRE KAYDEDİCİ ------------------------------- #
def kaydedici():
    website_uzunluk = len(giris.get())
    sifre_uzunluk = len(sifre_giris.get())
    kullanici_giris_uzunluk = len(kullanici_giris.get())
    if website_uzunluk == 0 or sifre_uzunluk == 0 or kullanici_giris_uzunluk == 0:
        messagebox.showinfo(title="Uyarı",message="Lütfen boş bilgileri doldurunuz.")
    else:
        emin_misin = messagebox.askokcancel(title="Uyarı",message=f"Girdiğiniz bilgiler:\nEmail:{kullanici_giris.get()}\nSifre:{sifre_giris.get()}\nWebsite:{giris.get()}\nemin misiniz?")

        if emin_misin == True:
            with open("Sifreler.txt",mode="a") as file:
                file.write(giris.get())
                file.write(" |")
                file.write(kullanici_giris.get())
                file.write(" |")
                file.write(sifre_giris.get()+"\n")
                giris.delete(0,END)
                sifre_giris.delete(0,END)
        else:
            giris.delete(0,END)
            sifre_giris.delete(0,END)



# ---------------------------- UI KURULUMU ------------------------------- #
pencere = Tk()
pencere.title("Password Manager")
pencere.config(padx=50,pady=50)
logo = PhotoImage(file="logo.png")
canvas = Canvas(width=200,height=200)
canvas.create_image(100,100,image = logo)
canvas.grid(row = 0,column=1)

website = Label(text="Website:")
website.grid(row=1,column=0)
giris = Entry(width=35)
giris.grid(row = 1,column=1,columnspan=2)
kullanici = Label(text="Email/Username:")
kullanici.grid(row = 2,column = 0)
kullanici_giris = Entry(width=35)
kullanici_giris.grid(row = 2,column = 1,columnspan = 2)
sifre = Label(text="Sifre:")
sifre.grid(row = 3,column = 0)
sifre_giris = Entry(width=21)
sifre_giris.grid(row = 3,column = 1)

sifre_olusturucu = Button(text="Sifre Olusturucu",command=olusturucu)
sifre_olusturucu.grid(row =3,column = 2)

ekle = Button(text="Ekle",width=30,command=kaydedici)
ekle.grid(row = 4 ,column = 1,columnspan=2)

pencere.mainloop()