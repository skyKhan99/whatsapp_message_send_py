from tkinter.colorchooser import askcolor

import pywhatkit
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog as fd


ana = Tk()
ana.geometry('600x200')
ana.resizable(False, False)
wpLogo = PhotoImage(file='phytonicns/whatsapp.png')
ana.iconphoto(True, wpLogo)
ana.title("Whatsapp Message Sender")

notebook = ttk.Notebook(ana)
notebook.pack(pady=0, expand=True)


frame1 = Frame(notebook, width=600, height=200)
frame2 = Frame(notebook, width=600, height=200)
frame3 = Frame(notebook, width=600, height=200)

frame1.pack(fill='both', expand=True)
frame2.pack(fill='both', expand=True)
frame3.pack(fill='both', expand=True)

notebook.add(frame1, text='Send Message')
notebook.add(frame2, text='For Fun')
notebook.add(frame3, text='Theme')

labelPhoneNum = Label(frame1,text="Recipient Phone No:")
labelPhoneNum.place(rely=0.2,relx=0)

labelMessage = Label(frame1, text="Message:")
labelMessage.place(rely=0.5, relx=0)

countryPhoneCodeList = ["+93 Afghanistan", "+355 Albania", "+213 Algeria", "+684 American Samoa", "+376 Andorra", "+244 Angola", "+809 Anguilla", "+268 Antigua",
                        "+54 Argentina", "+374 Armenia", "+297 Aruba", "+247 Ascension Island", "+61 Australia", "+672 Australian External Territories", "+43 Austria",
                        "+994 Azerbaijan", "+242 Bahamas", "+246 Barbados", "+973 Bahrain", "+880 Bangladesh", "+375 Belarus", "+32 Belgium", "+501 Belize", "+229 Benin",
                        "+809 Bermuda", "+975 Bhutan", "+284 British Virgin Islands", "+591 Bolivia", "+387 Bosnia and Hercegovina", "+267 Botswana", "+55 Brazil",
                        "+284 British V.I.", "+673 Brunei Darussalm" ,"+359 Bulgaria", "+226 Burkina Faso", "+257 Burundi", "+855 Cambodia", "+237 Cameroon", "+1 Canada",
                        "+238 CapeVerde Islands", "+1 Caribbean Nations", "+345 Cayman Islands", "+238 Cape Verdi", "+236 Central African Republic", "+235 Chad","+56 Chile",
                        "+86 China (People's Republic)", "+886 China-Taiwan", "+57 Colombia", "+269 Comoros and Mayotte", "+242 Congo","+682 Cook Islands", "+506 Costa Rica",
                        "+385 Croatia", "+53 Cuba", "+357 South Cyprus Greek Governance", "+420 Czech Republic", "+45 Denmark", "+246 Diego Garcia", "+767 Dominca", "+809 Dominican Republic",
                        "+253 Djibouti", "+593 Ecuador", "+20 Egypt", "+503 El Salvador", "+240 Equatorial Guinea", "+291 Eritrea", "+372 Estonia", "+251 Ethiopia", "+500 Falkland Islands",
                        "+298 Faroe Islands", "+679 Fiji", "+358 Finland", "+33 France", "+596 French Antilles", "+594 French Guiana", "+241 Gabon", "+220 Gambia", "+995 Georgia",
                        "+49 Germany", "+233 Ghana", "+350 Gibraltar", "+30 Greece", "+299 Greenland", "+473 Grenada/Carricou", "+671 Guam", "+502 Guatemala", "+224 Guinea",
                        "+245 Guinea-Bissau", "+592 Guyana", "+509 Haiti", "+504 Honduras", "+852 Hong Kong", "+36 Hungary", "+354 Iceland", "+91 India", "+62 Indonesia,", "+98 Iran",
                        "+964 Iraq", "+353 Ireland (Irish Republic)", "+972 Israel", "+39 Italy", "+225 Ivory Coast", "+876 Jamaica", "+81 Japan", "+962 Jordan", "+7 Kazakhstan",
                        "+254 Kenya", "+855 Khmer Republic (Cambodia/Kampuchea)", "+686 Kiribati Republic (Gilbert Islands)", "+82 Korea (South)", "+850 Korea (North)", "+965 Kuwait",
                        "+996 Kyrgyz Republic", "+371 Latvia", "+856 Laos", "+961 Lebanon", "+266 Lesotho", "+231 Liberia", "+370 Lithuania", "+218 Libya", "+423 Liechtenstein",
                        "+352 Luxembourg", "+853 Macao", "+389 Macedonia", "+261 Madagascar", "+265 Malawi", "+60 Malaysia", "+960 Maldives", "+223 Mali", "+356 Malta", "+692 Marshall Islands",
                        "+596 Martinique (French Antilles)", "+222 Mauritania", "+230 Mauritius", "+269 Mayolte", "+52 Mexico", "+691 Micronesia (F.S. of Polynesia)", "+373 Moldova",
                        "+33 Monaco", "+976 Mongolia", "+473 Montserrat", "+212 Morocco", "+258 Mozambique", "+95 Myanmar", "+264 Namibia", "+674 Nauru", "+977 Nepal", "+31 Netherlands",
                        "+599 Netherlands Antilles", "+869 Nevis", "+687 New Caledonia", "+64 New Zealand", "+505 Nicaragua", "+227 Niger", "+234 Nigeria", "+683 Niue",
                        "+1 670 North Mariana Islands (Saipan)", "+47 Norway", "+968 Oman", "+92 Pakistan", "+680 Palau", "+507 Panama", "+675 Papua New Guinea", "+595 Paraguay",
                        "+51 Peru", "+63 Philippines", "+48 Poland", "+351 Portugal (includes Azores)", "+1 787 Puerto Rico", "+974 Qatar", "+262 Reunion (France)", "+40 Romania",
                        "+7 Russia", "+250 Rwanda (Rwandese Republic)", "+670 Saipan", "+378 San Marino", "+239 Sao Tome and Principe", "+966 Saudi Arabia", "+221 Senegal",
                        "+381 Serbia and Montenegro", "+248 Seychelles", "+232 Sierra Leone", "+65 Singapore", "+421 Slovakia", "+386 Slovenia", "+677 Solomon Islands", "+252 Somalia",
                        "+27 South Africa", "+34 Spain", "+94 Sri Lanka", "+290 St. Helena", "+869 St. Kitts/Nevis", "+508 St. Pierre &(et) Miquelon (France)", "+249 Sudan",
                        "+597 Suriname", "+268 Swaziland", "+46 Sweden", "+41 Switzerland", "+963 Syrian Arab Republic (Syria)", "+689 Tahiti (French Polynesia)" ,"+886 Taiwan",
                        "+7 Tajikistan", "+255 Tanzania (includes Zanzibar)", "+66 Thailand", "+228 Togo (Togolese Republic)", "+690 Tokelau", "+676 Tonga","+1 868 Trinidad and Tobago",
                        "+216 Tunisia", "+90 Turkey", "+993 Turkmenistan", "+688 Tuvalu (Ellice Islands)", "+256 Uganda", "+380 Ukraine", "+971 United Arab Emirates", "+44 United Kingdom",
                        "+598 Uruguay", "+1 USA", "+7 Uzbekistan", "+678 Vanuatu (New Hebrides)", "+39 Vatican City", "+58 Venezuela", "+84 Vietnam", "+1 340 Virgin Islands",
                        "+681 Wallis and Futuna", "+685 Western Samoa", "+381 Yemen" , "+967 Yemen Arab Republic (North Yemen)", "+243 Zaire", "+260 Zambia", "+263 Zimbabwe"]
comboPhoneCode = ttk.Combobox(frame1, width=30, values=countryPhoneCodeList, state='readonly')
comboPhoneCode.place(rely=0.0, relx=0.1)
labelPhoneCode = Label(frame1, text="Select↑\n Country", font="Arial, 8", width=9)
labelPhoneCode.place(rely=0.2, relx=0.25)
entryPhoneNum = Entry(frame1, width=10)
entryPhoneNum.place(rely=0.2, relx=0.35)

entryMessage = Entry(frame1, width=35)
entryMessage.place(rely=0.5, relx=0.25)

selected = StringVar(frame1, "1")
selects = (
    ("Direct Send", "0"),
    ("Send Specific Time", "1")
)
rdy1 = selects[1]
rdy2 = selects[0]

radioTimed = Radiobutton(frame1, text=rdy1[0], value=rdy1[1],variable=selected)
radioTimed.place(relx=0.55, rely=0.1)

radioDirect = Radiobutton(frame1, text=rdy2[0], value=rdy2[1],variable=selected)
radioDirect.place(relx=0.55, rely=0.3)

labelHour = Label(frame1, text="Hour")
labelHour.place(rely=0.1, relx=0.84)

labelMinute = Label(frame1, text="Minute")
labelMinute.place(rely=0.3, relx=0.84)

entryHour = Entry(frame1,width=3)
entryHour.place(relx=0.93, rely=0.1)

entryMinute = Entry(frame1,width=3)
entryMinute.place(relx=0.93, rely=0.3)

labelWPLogo = Label(frame1, image=wpLogo)
labelWPLogo.place(relx=0, rely=0)


def callbackFunc(event):
    selectedCountry = event.widget.get()
    selectedCountryList = selectedCountry.split(" ")
    selectedCode = selectedCountryList[0]
    labelPhoneCode.configure(text=selectedCode, font="Arial, 9")
    print(selectedCode)


comboPhoneCode.current()
comboPhoneCode.bind("<<ComboboxSelected>>", callbackFunc)

def f(x):
    match x:
        case '0':
            try:
                selectedCountry = comboPhoneCode.get()
                selectedCountryList = selectedCountry.split(" ")
                selectedCode = selectedCountryList[0]
                pywhatkit.sendwhatmsg_instantly(f"{selectedCode}{entryPhoneNum.get()}",
                                                entryMessage.get(), 5, True, 3)
            except: messagebox.showerror("error", "¯\_(ツ)_/¯")
            return
        case '1':
            try:
                hour = int(entryHour.get())
                minute = int(entryMinute.get())
                if hour > 24:
                    messagebox.showinfo("Check the hour", "There is 24 hours in a day \n¯\_(ツ)_/¯")
                elif minute > 60:
                    messagebox.showinfo("Check the minute", "There is 60 minutes in an hour \n¯\_(ツ)_/¯")
                else:
                    selectedCountry = comboPhoneCode.get()
                    selectedCountryList = selectedCountry.split(" ")
                    selectedCode = selectedCountryList[0]
                    pywhatkit.sendwhatmsg(f"{selectedCode}{entryPhoneNum.get()}",
                                          entryMessage.get(),
                                          hour,
                                          minute)
            except: messagebox.showerror("error","¯\_(ツ)_/¯")
            return


def sendMessage():
    x = selected.get()
    f(x)


sendIcon = PhotoImage(file='C:/phytonicns/sendmessage.png')

btnSend = Button(frame1, text="Send", image=sendIcon, command=sendMessage)
btnSend.place(relx=0.85, rely=0.6)

labelHandWrite = Label(frame2, text="Print Handwrite:")
labelHandWrite.place(rely=0.2, relx=0)

textHandWrite = Text(frame2, width=20, height=10)
textHandWrite.place(relx=0.2, rely=0.1)


def handwrite():
    elyazisi = textHandWrite.get(0.0, 'end')
    pywhatkit.text_to_handwriting(elyazisi, "C:/Users/gokhan.hacioglu/Desktop/el_yazim.png", (0,0,138))


btnHandWrite = Button(frame2, text="Print", command=handwrite)
btnHandWrite.place(rely=0.5, relx=0.1)

seperator = ttk.Separator(frame2, orient="vertical")
seperator.place(relx=0.55, rely=0, relheight=1, relwidth=0.4)


def select_files():
    filetypes = (
        ('Resim Dosyaları(png)', '*.png'),
    )

    filenames = fd.askopenfilenames(
        title='Open files',
        initialdir='/',
        filetypes=filetypes)
    pywhatkit.image_to_ascii_art(filenames[0], "C:/Users/gokhan.hacioglu/Desktop/ascii.txt")


btnFile = Button(frame2, text='Choose File', command=select_files)
btnFile.place(rely=0.4, relx=0.7)

labelAsciiFileChoose = Label(frame2, text = "Convert your picture to ASCII")
labelAsciiFileChoose.place(relx=0.6, rely=0.1)


def change_color():
    colors = askcolor(title="Choose Theme")
    print(colors)
    ana.configure(bg=colors[1])
    frame1.configure(bg=colors[1])
    frame2.configure(bg=colors[1])
    frame3.configure(bg=colors[1])
    entryHour.configure(bg=colors[1], fg='#16650b')
    entryMinute.configure(bg=colors[1], fg='#16650b')
    entryMessage.configure(bg=colors[1], fg='#16650b')
    entryPhoneNum.configure(bg=colors[1], fg='#16650b')
    labelHour.configure(bg=colors[1], fg='#16650b')
    labelMinute.configure(bg=colors[1], fg='#16650b')
    labelAsciiFileChoose.configure(bg=colors[1], fg='#16650b')
    labelMessage.configure(bg=colors[1], fg='#16650b')
    labelHandWrite.configure(bg=colors[1], fg='#16650b')
    labelWPLogo.configure(bg=colors[1], fg='#16650b')
    labelPhoneNum.configure(bg=colors[1], fg='#16650b')
    radioDirect.configure(bg=colors[1], fg='#16650b')
    radioTimed.configure(bg=colors[1], fg='#16650b')
    btnTheme.configure(bg=colors[1], fg='#16650b')
    btnFile.configure(bg=colors[1], fg='#16650b')
    btnSend.configure(bg=colors[1], fg='#16650b')
    btnHandWrite.configure(bg=colors[1], fg='#16650b')
    textHandWrite.configure(bg=colors[1], fg='#16650b')
    labelPhoneCode.configure(bg=colors[1], fg='#16650b')
    comboPhoneCode.configure(background=colors[1], foreground='#16650b')
    colorsRGB = colors[0]
    if (colorsRGB[0] < 100 and colorsRGB[1] < 100) or (colorsRGB[2] < 100 and colorsRGB[1] < 100) or (colorsRGB[2] < 100 and colorsRGB[0] < 100):
        entryHour.configure(foreground='#8fff80')
        entryMinute.configure(foreground='#8fff80')
        entryMessage.configure(foreground='#8fff80')
        entryPhoneNum.configure(foreground='#8fff80')
        labelHour.configure(foreground='#8fff80')
        labelMinute.configure(foreground='#8fff80')
        labelAsciiFileChoose.configure(foreground='#8fff80')
        labelMessage.configure(foreground='#8fff80')
        labelHandWrite.configure(foreground='#8fff80')
        labelWPLogo.configure(foreground='#8fff80')
        labelPhoneNum.configure(foreground='#8fff80')
        btnTheme.configure(foreground='#8fff80')
        btnFile.configure(foreground='#8fff80')
        btnSend.configure(foreground='#8fff80')
        btnHandWrite.configure(foreground='#8fff80')
        textHandWrite.configure(foreground='#8fff80')
        radioDirect.configure(fg='#6bda5c')
        radioTimed.configure(fg='#6bda5c')
        labelPhoneCode.configure(fg='#6bda5c')
        comboPhoneCode.configure(foreground='#6bda5c')


btnTheme = Button(frame3, text='Change Theme', command=change_color)
btnTheme.pack()
mainloop()
