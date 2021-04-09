from Apartemen import Apartemen
from Rumah import Rumah
from Kontrakan import Kontrakan
from tkinter import *
from tkinter import messagebox
import tkinter as tk
import tkinter.filedialog

listOfHunian = []

def submit_handler():
    namaPemilik = str(ent_nama.get())
    jmlhPenghuni = str(ent_jmlhPenghuni.get())
    jmlhKamar = str(ent_jmlhKamar.get())
    #variabel untuk check button
    list_checkbtn = []
    fiturTotal = ''
    if var_checkbtn1.get() == 1:
        list_checkbtn.append("Wifi")
    if var_checkbtn2.get() == 1:
        list_checkbtn.append("Air Conditioning")
    if var_checkbtn3.get() == 1:
        list_checkbtn.append("Kolam Renang")

    i = 0
    for output in list_checkbtn:
        if i == 0:
            fiturTotal = fiturTotal + output
        else:
            fiturTotal = fiturTotal + ',' + output
        i = i + 1

    hargaDrpDwn = hargaVar.get()
    jenisHunianAngka = varJk.get()
    
    if namaPemilik == '' or jmlhPenghuni=='' or jmlhKamar=='' or fiturTotal=='' or jenisHunianAngka==0:
        tk.messagebox.showwarning("Empty Entry Warning", "Entry is still empty!")
    else:
        if jenisHunianAngka == 1:
            listOfHunian.append(Apartemen(namaPemilik, jmlhPenghuni, jmlhKamar, hargaDrpDwn, fiturTotal))
        elif jenisHunianAngka == 2:
            listOfHunian.append(Rumah(namaPemilik, jmlhPenghuni, jmlhKamar, hargaDrpDwn, fiturTotal))
        elif jenisHunianAngka == 3:
            listOfHunian.append(Kontrakan(namaPemilik, jmlhPenghuni, jmlhKamar, hargaDrpDwn, fiturTotal))

        tk.messagebox.showinfo("Action Succesful", "Submit Succesful")
        ent_nama.delete(0, END)
        ent_jmlhPenghuni.delete(0, END)
        ent_jmlhKamar.delete(0, END)
        var_checkbtn1.set(0)
        var_checkbtn2.set(0)
        var_checkbtn3.set(0)
        varJk.set(0)

def output_submission():
    if listOfHunian == []:
        tk.messagebox.showwarning("Empty Submissions", "Submissions is still empty!")
    else:    
        topWindow = tk.Tk()
        topWindow.title("Show All Submissions")

        for output in listOfHunian:
            frm_cell = tk.Frame(topWindow, relief=tk.RAISED, borderwidth=1)
            frm_cell.pack(pady=25, padx=100, expand=True)
            lbl_output = tk.Label(frm_cell, 
            text="Nama Pemilik :" + str(output.get_nama_pemilik())
            + "\nNama Hunian :" + str(output.get_jenis())
            + "\nJumlah Kamar :" + str(output.get_jml_kamar())
            + "\nJumlah Penghuni :" + str(output.get_jml_penghuni())
            + "\nFitur Hunian :" + str(output.get_fitur())
            + "\nHarga Hunian :" + str(output.get_harga_hunian())
            )
            lbl_output.pack(side=tk.LEFT)

def clear_handler():
    ask = tk.messagebox.askquestion ('Clear Data','Are you sure you want to clear all the data',icon = 'warning')
    if ask == 'yes':
        listOfHunian.clear()
        
def exit_handler():
    MsgBox = tk.messagebox.askquestion ('Exit Application','Are you sure you want to exit the application',icon = 'warning')
    if MsgBox == 'yes':
       mainWindow.quit()

def about_handler():
    topWindow = tk.Tk()
    topWindow.title("About")
    frm_cell = tk.Frame(topWindow, relief=tk.RAISED, borderwidth=1)
    frm_cell.pack(pady=25, padx=25, expand=True)
    lbl_namaApp = tk.Label(frm_cell, text="Hunian Inputter", font="Helvetica 16 bold italic", fg="green")
    lbl_namaApp.pack()
    lbl_output = tk.Label(frm_cell, text="Hunian inputer adalah sebuah aplikasi"
                    +"\nyang digunakan untuk menginput data"
                    +"\nhunian yang ada di sekitar kampusmu"
                    +"\nCreator:Muhammad Ilham Malik"
                    +"\n1902563"
                    +"\nIlmu Komputer C1")
    lbl_output.pack(side=tk.LEFT)

def image_handler():
    file_path = tkinter.filedialog.askopenfile()

#output tampilan
mainWindow = tk.Tk()
mainWindow.title("Window Utama")

frm_input = tk.Frame(relief=tk.SUNKEN, borderwidth=5)
frm_input.grid(row=0, column=0, padx=25 ,ipadx=25, pady=25, ipady=25)

#label untuk nama pemilik
lbl_nama = tk.Label(master=frm_input, text="Nama Pemilik:")
ent_nama = tk.Entry(master=frm_input, width=50)
#masukan posisi gridnya
lbl_nama.grid(row=0, column=0, sticky="e")
ent_nama.grid(row=0, column=1)

#label & entry untuk jumlahpenghuni
lbl_jmlhPenghuni = tk.Label(master=frm_input, text="Jumlah Penghuni:")
ent_jmlhPenghuni = tk.Entry(master=frm_input, width=10)
#posisi grid pada form
lbl_jmlhPenghuni.grid(row=1, column=0, sticky="e")
ent_jmlhPenghuni.grid(row=1, column=1, sticky="w")

#label & entry untuk jumlah kamar
lbl_jmlhKamar = tk.Label(master=frm_input, text="Jumlah Kamar:")
ent_jmlhKamar = tk.Entry(master=frm_input, width=10)
#posisi grid pada form
lbl_jmlhKamar.grid(row=2, column=0, sticky="e")
ent_jmlhKamar.grid(row=2, column=1, sticky="w")

#label & entry untuk checkbox
frm_checkbtn = tk.Frame(master=frm_input)
frm_checkbtn.grid(row=3, column=1)
#posisi button
var_checkbtn1 = IntVar()
var_checkbtn2 = IntVar()
var_checkbtn3 = IntVar()
lbl_fitur = tk.Label(master=frm_input, text="Fitur:")
tk.Checkbutton(master=frm_checkbtn, text="Wifi", var=var_checkbtn1).pack(side=tk.LEFT)
tk.Checkbutton(master=frm_checkbtn, text="Air Conditioning", var=var_checkbtn2).pack(side=tk.LEFT)
tk.Checkbutton(master=frm_checkbtn, text="Kolam Renang", var=var_checkbtn3).pack(side=tk.LEFT)

#posisi grid pada form
lbl_fitur.grid(row=3, column=0, sticky="e")

#label & dropdown menu
hargaVar = StringVar(mainWindow)
options = {
    '1.500.000',
    '2.000.000',
    '3.000.000'
}
hargaVar.set('1.500.000')
lbl_harga = tk.Label(master=frm_input, text="Harga:")
drp_harga = tk.OptionMenu(frm_input, hargaVar, *options)
#posisi grid
lbl_harga.grid(row=4, column=0, sticky="e")
drp_harga.grid(row=4, column=1, sticky="w")

#label & menu radio
varJk = IntVar()
lbl_jenisKelamin = tk.Label(master=frm_input, text="Jenis Kelamin Pemilik:")
#untuk membatasi widget radiobutton
frm_radio = tk.Frame(master=frm_input)
frm_radio.grid(row=5, column=1)
tk.Radiobutton(frm_radio, text="Apartemen", variable=varJk, value=1).pack(side=tk.LEFT)
tk.Radiobutton(frm_radio, text="Rumah", variable=varJk, value=2).pack(side=tk.LEFT)
tk.Radiobutton(frm_radio, text="Kontrakan", variable=varJk, value=3).pack(side=tk.LEFT)
#posisi grid
lbl_jenisKelamin.grid(row=5, column=0, sticky="e")


#membuat frame button
frm_button = tk.Frame()
frm_button.grid(row=1, column=0,ipadx=100, ipady=10, pady=10)

btn_open = tk.Button(master=frm_button, text="Open Photo File", command=image_handler)
btn_open.pack(fill=tk.BOTH)
#FORM SUBMIT BUTTON
#untuk mensubmit data
btn_submit = tk.Button(master=frm_button, text="Submit", command=submit_handler)
btn_submit.pack(fill=tk.BOTH)
#beres

#form untuk deskripsi
frm_description = tk.Frame(relief=tk.SUNKEN, borderwidth=5, width=100, height=200)
frm_description.grid(row=0, column=1, ipady=18)

#label untuk judul aplikasi
lbl_namaApp = tk.Label(master=frm_description, text="Hunian Inputter", font="Helvetica 16 bold italic", fg="green")
lbl_namaApp.pack()
#label untuk deskripsi
lbl_desc = tk.Label(master=frm_description, text="Hunian inputer adalah sebuah aplikasi"
                    +"\nyang digunakan untuk menginput data"
                    +"\nhunian yang ada di sekitar kampusmu")
lbl_desc.pack()

#button untuk melihat seluruh inputan
btn_see = tk.Button(master=frm_description, text="See All Submissions", command=output_submission)
btn_see.pack(fill=tk.BOTH)
#button untuk menghapus list masukan
btn_clear = tk.Button(master=frm_description, text="Clear All Submissions", command=clear_handler)
btn_clear.pack(fill=tk.BOTH)
#button tentang about aplikasi
btn_about = tk.Button(master=frm_description, text="About", command=about_handler)
btn_about.pack(fill=tk.BOTH)
#frame untuk button exit agar sejajar dengan button yang di sebelahnya
frm_button_exit = tk.Frame()
frm_button_exit.grid(row=1, column=1, ipadx=50)
#frm btn exit
btn_exit = tk.Button(master=frm_button_exit, text="Exit", command=exit_handler)
btn_exit.pack(fill=tk.BOTH, expand=True)

#program desain tampilan selesai di sini

mainWindow.mainloop()
#Daftar nama(text), jumlahpenghuni(text), jumlahKamar(text), checkbox(wifi, ac, tv-satelit, sarapangratis), hargadropdown