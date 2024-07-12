from tkinter import *
from tkinter import messagebox
import random,os,tempfile,smtplib
# import fpdf
from fpdf import FPDF

#funtionality Part

# function party
def clear():
    bathsoapEntry.delete(0,END)
    facecreamEntry.delete(0,END)
    FacewashEntry.delete(0,END)
    hairSprayEntry.delete(0,END)
    hairGelEntry.delete(0,END)
    bodySprayEntry.delete(0,END)

    riceEntry.delete(0,END)
    daalEntry.delete(0,END)
    wheatEntry.delete(0,END)
    oilEntry.delete(0,END)
    teaEntry.delete(0,END)
    sugarEntry.delete(0,END)

    maazaEntry.delete(0,END)
    pepsiEntry.delete(0,END)
    frootiEntry.delete(0,END)
    cocacolaEntry.delete(0,END)
    spriteEntry.delete(0,END)
    dewEntry.delete(0,END)

    cosmeticTaxEntry.delete(0,END)
    groceryTaxEntry.delete(0,END)
    coldDrinksTaxEntry.delete(0,END)

    cosmeticPriceEntry.delete(0,END)
    groceryPriceEntry.delete(0,END)
    colddrinkPriceEntry.delete(0,END)

    phoneEntry.delete(0,END)
    billNumberEntry.delete(0,END)
    nameEntry.delete(0,END)
    textarea.delete(1.0,END)

def save_pdf():
    global billnumber
    result = messagebox.askyesno('Confirm', 'Do you want to save the Bill')
    if result:
        bill_content = textarea.get(1.0, END)
        pdf = FPDF()
        pdf.add_page()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 10, bill_content)
        pdf.output(f'bills/{billnumber}.pdf')
        messagebox.showinfo('Success', f'bill number {billnumber} is saved successfully')

def send_email():
    def send_gmail():
        try:
            obj=smtplib.SMTP('smtp.gmail.com',587)
            obj.starttls()
            obj.login(senderEntry.get(),passwordEntry.get())
            message=email_textarea.get(1.0,END)
            obj.sendmail(senderEntry.get(),recieverEntry.get(),message)
            obj.quit()
            messagebox.showinfo('Success','Bill is success fully sended.',parent=root1)
            root1.destroy()
        except:
            messagebox.showerror('Error','Something went wrong, Please try again',parent=root1)
    if textarea.get(1.0,END)=='\n':
        messagebox.showerror('Error','Bill is empty')
    else:
        root1=Toplevel()
        root1.grab_set()
        root1.title('Send Email')
        root1.config(bg='mediumpurple1')
        root1.resizable(0,0)

        senderFrame=LabelFrame(root1,text='SENDER',font=('arial',16,'bold'),bd=6,bg='mediumpurple1',fg='black')
        senderFrame.grid(row=0,column=0,padx=40,pady=20)

        senderLable=Label(senderFrame,text="Sender's Email",font=('arial',14,'bold'),bg='mediumpurple1',fg='black')
        senderLable.grid(row=0,column=0,padx=10,pady=8,sticky='w')

        senderEntry=Entry(senderFrame,font=('arial',14,'bold'),bd=2,width=23,relief=RIDGE)
        senderEntry.grid(row=0,column=1,padx=10,pady=8)

        passwordLable=Label(senderFrame,text="Password",font=('arial',14,'bold'),bg='mediumpurple1',fg='black')
        passwordLable.grid(row=1,column=0,padx=10,pady=8,sticky='w')

        passwordEntry=Entry(senderFrame,font=('arial',14,'bold'),bd=2,width=23,relief=RIDGE,show='$')
        passwordEntry.grid(row=1,column=1,padx=10,pady=8)

        recipientFrame = LabelFrame(root1, text='RECIPIENT', font=('arial', 16, 'bold'), bd=6, bg='mediumpurple1', fg='black')
        recipientFrame.grid(row=1, column=0, padx=40, pady=20)

        recieverLable = Label(recipientFrame, text="Email Address", font=('arial', 14, 'bold'), bg='mediumpurple1', fg='black')
        recieverLable.grid(row=0, column=0, padx=10, pady=8, sticky='w')

        recieverEntry = Entry(recipientFrame, font=('arial', 14, 'bold'), bd=2, width=23, relief=RIDGE)
        recieverEntry.grid(row=0, column=1, padx=10, pady=8)

        messageLable = Label(recipientFrame, text="Message", font=('arial', 14, 'bold'), bg='mediumpurple1', fg='black')
        messageLable.grid(row=1, column=0, padx=10, pady=8, sticky='w')

        email_textarea=Text(recipientFrame,font=('arial', 14, 'bold'),relief=SUNKEN,width=58,height=17)
        email_textarea.grid(row=2,column=0,columnspan=2)
        email_textarea.delete(1.0,END)
        email_textarea.insert(END,textarea.get(1.0,END))

        sendButton=Button(root1,text='SEND', font=('arial', 16, 'bold'),width=15,command=send_gmail)
        sendButton.grid(row=2,column=0,pady=20)



    root1.mainloop()



def print_bill():
    if textarea.get(1.0,END)=='\n':
        messagebox.showerror('Error','Bill is empty')
    else:
        file=tempfile.mktemp('.txt')
        open(file,'w').write(textarea.get(1.0,END))
        os.startfile(file,'print')

def search_bill():
    for i in os.listdir('bills/'):
        if i.split('.')[0]==billNumberEntry.get():
            f=open(f'bills/{i}','r')
            textarea.delete('1.0',END)
            for data in f:
                textarea.insert(END,data)
            f.close()
            break
    else:
        messagebox.showerror('Error', 'Invalid Bill Number')


if not os.path.exists('bills'):
    os.mkdir('bills')

def save_bill():
    global billnumber
    result=messagebox.askyesno('Confirm','Do you want to save the Bill')
    if result:
        bill_content=textarea.get(1.0,END)
        file=open(f'bills/{billnumber}.txt','w')
        file.write(bill_content)
        file.close()
        messagebox.showinfo('Success',f'bill number {billnumber} is saved successfully')

billnumber=random.randint(500,1000)

# bill area // popup
def bill_area():
    if nameEntry.get()=='' or phoneEntry.get()=='': #it means mt
        messagebox.showerror('Error','Customer Details Are Required')
    elif cosmeticPriceEntry.get()=='' and groceryPriceEntry.get()=='' and colddrinkPriceEntry.get()=='':
        messagebox.showerror('Error', 'No Products are Selected')
    elif cosmeticPriceEntry.get()=='0 Rs' and groceryPriceEntry.get()=='0 Rs' and colddrinkPriceEntry.get()=='0 Rs':
        messagebox.showerror('Error', 'Still You Not select any products')
    else:
        textarea.delete(1.0,END)

        textarea.insert(END,'\t\t**Welcome Customer**')
        textarea.insert(END,f'\nBill Number:{billnumber}')
        textarea.insert(END,f'\nCustomer Name: {nameEntry.get()}')
        textarea.insert(END,f'\nCustomer Phone Number: {phoneEntry.get()}')
        textarea.insert(END,'\n========================================================')
        textarea.insert(END,'\nProduct\t\t\tQuantity\t\t\tPrice')
        textarea.insert(END,'\n========================================================')
        if bathsoapEntry.get()!='0':
            textarea.insert(END,f'\nBath Soap\t\t\t{bathsoapEntry.get()}\t\t\t{soapprice} Rs')
        if facecreamEntry.get() != '0':
            textarea.insert(END, f'\nFace Cream\t\t\t{facecreamEntry.get()}\t\t\t{faceCreamPrice} Rs')
        if FacewashEntry.get()!='0':
            textarea.insert(END,f'\nFace Wash\t\t\t{FacewashEntry.get()}\t\t\t{FacewashPrice} Rs')
        if hairSprayEntry.get()!='0':
            textarea.insert(END,f'\nHair Spray\t\t\t{hairSprayEntry.get()}\t\t\t{hairSprayPrice} Rs')
        if bodySprayEntry.get()!='0':
            textarea.insert(END,f'\nHair Gel\t\t\t{bodySprayEntry.get()}\t\t\t{hairGelPrice} Rs')

        # grocery if condition
        if riceEntry.get()!='0':
            textarea.insert(END,f'\nRice\t\t\t{riceEntry.get()}\t\t\t{ricePrice} Rs')
        if oilEntry.get()!='0':
            textarea.insert(END,f'\nOil\t\t\t{oilEntry.get()}\t\t\t{oilPrice} Rs')
        if daalEntry.get()!='0':
            textarea.insert(END,f'\nDaal\t\t\t{daalEntry.get()}\t\t\t{daalPrice} Rs')
        if wheatEntry.get()!='0':
            textarea.insert(END,f'\nWheat\t\t\t{wheatEntry.get()}\t\t\t{wheatPrice} Rs')
        if sugarEntry.get()!='0':
            textarea.insert(END,f'\nSugar\t\t\t{sugarEntry.get()}\t\t\t{sugarPrice} Rs')
        if teaEntry.get()!='0':
            textarea.insert(END,f'\nTea\t\t\t{teaEntry.get()}\t\t\t{teaPrice} Rs')

        # colddrinks if condition
        if maazaEntry.get()!='0':
            textarea.insert(END,f'\nMaaza\t\t\t{maazaEntry.get()}\t\t\t{maazaPrice} Rs')
        if pepsiEntry.get()!='0':
            textarea.insert(END,f'\nPepsi\t\t\t{pepsiEntry.get()}\t\t\t{pepsiPrice} Rs')
        if spriteEntry.get()!='0':
            textarea.insert(END,f'\nSprite\t\t\t{spriteEntry.get()}\t\t\t{spritePrice} Rs')
        if dewEntry.get()!='0':
            textarea.insert(END,f'\nDew\t\t\t{dewEntry.get()}\t\t\t{dewPrice} Rs')
        if frootiEntry.get()!='0':
            textarea.insert(END,f'\nFrooti\t\t\t{frootiEntry.get()}\t\t\t{frootiPrice} Rs')
        if cocacolaEntry.get()!='0':
            textarea.insert(END,f'\nCocaCola\t\t\t{cocacolaEntry.get()}\t\t\t{cocacolaPrice} Rs')


        textarea.insert(END,'\n--------------------------------------------------------')

        if cosmeticTaxEntry.get()!='0.0 Rs':
            textarea.insert(END,f'\n Cosmetic Tax\t\t\t\t{cosmeticTaxEntry.get()}')
        if groceryTaxEntry.get()!='0.0 Rs':
            textarea.insert(END,f'\n Grocery Tax\t\t\t\t{groceryTaxEntry.get()}')
        if coldDrinksTaxEntry.get()!='0.0 Rs':
            textarea.insert(END,f'\n Cold Drink Tax\t\t\t\t{coldDrinksTaxEntry.get()}')

        textarea.insert(END,f'\n Total Bill \t\t\t\t{totalbill}')
        textarea.insert(END,'\n--------------------------------------------------------')
        save_bill()







# Cosmetic funtion
def total():
    global soapprice,hairSprayPrice,faceCreamPrice,FacewashPrice,hairGelPrice,bodySprayPrice
    global ricePrice,oilPrice,daalPrice,wheatPrice,sugarPrice,teaPrice
    global maazaPrice,pepsiPrice,spritePrice,dewPrice,frootiPrice,cocacolaPrice
    global totalbill

    soapprice=int (bathsoapEntry.get())*20
    faceCreamPrice=int (facecreamEntry.get())*100
    FacewashPrice =int(FacewashEntry.get())*70
    hairSprayPrice=int(hairSprayEntry.get())*105
    hairGelPrice=int(hairGelEntry.get())*89
    bodySprayPrice=int(bodySprayEntry.get())*55
    totalCosmeticPrice=soapprice+faceCreamPrice+FacewashPrice+hairSprayPrice+hairGelPrice+bodySprayPrice
    cosmeticPriceEntry.delete(0,END)
    cosmeticPriceEntry.insert(0,f'{totalCosmeticPrice} Rs')
    cosmeticTaxPrice=totalCosmeticPrice*0.12
    cosmeticTaxEntry.delete(0,END)
    cosmeticTaxEntry.insert(0,str(cosmeticTaxPrice)+'Rs')

# grocery funtion
    ricePrice=int(riceEntry.get())*40
    oilPrice=int(oilEntry.get())*72
    daalPrice=int(daalEntry.get())*45
    wheatPrice=int(wheatEntry.get())*33
    sugarPrice=int(sugarEntry.get())*30
    teaPrice=int(teaEntry.get())*25
    totalGroceryPrice=ricePrice+oilPrice+daalPrice+wheatPrice+sugarPrice+teaPrice
    groceryPriceEntry.delete(0,END)
    groceryPriceEntry.insert(0,f'{totalGroceryPrice} Rs')
    groceryTaxPrice = totalGroceryPrice * 0.12
    groceryTaxEntry.delete(0, END)
    groceryTaxEntry.insert(0, str(groceryTaxPrice) + 'Rs')

    # cold funtion
    maazaPrice=int(maazaEntry.get())*10
    pepsiPrice=int(pepsiEntry.get())*15
    spritePrice=int(spriteEntry.get())*10
    dewPrice=int(dewEntry.get())*20
    frootiPrice=int(frootiEntry.get())*10
    cocacolaPrice=int(cocacolaEntry.get())*10
    totalColdDrinksPrice=maazaPrice+pepsiPrice+spritePrice+dewPrice+frootiPrice+cocacolaPrice
    colddrinkPriceEntry.delete(0,END)
    colddrinkPriceEntry.insert(0,f'{totalColdDrinksPrice} Rs')
    colddrinkTaxPrice = totalColdDrinksPrice * 0.5
    coldDrinksTaxEntry.delete(0, END)
    coldDrinksTaxEntry.insert(0, str(colddrinkTaxPrice) + 'Rs')

    totalbill = totalCosmeticPrice+totalGroceryPrice+totalColdDrinksPrice+cosmeticTaxPrice+groceryTaxPrice+colddrinkTaxPrice



root = Tk()
root.title("BILLING PAGE")
root.geometry('1270x685')
root.iconbitmap('billicon.ico')
headingLabel = Label(root,text='Retail Billing System', font=('time new roman',20, 'bold')
                     ,bg="mediumpurple1",fg='black', bd=12, relief=FLAT)
headingLabel.pack(fill='x')

#  container customer detailes box 1
customer_details_frame= LabelFrame(root, text='CUSTOMER DETAILS', font=('time new roman',15, 'bold'), bg="mediumpurple1", fg='black', bd=8, relief=GROOVE)
customer_details_frame.pack(fill='x')

# customer name
nameLabel = Label(customer_details_frame, text="CUSTOMER NAME", font=('time new roman',11, 'bold'), bg="mediumpurple1", fg='black', relief=FLAT)
nameLabel.grid(row=0,column=0, padx=20, pady=2)
# -- customer name entry
nameEntry=Entry(customer_details_frame,font=('arial',15),bd=7,width=18)
nameEntry.grid(row=0,column=1, padx=8)

# contact name
phoneLabel = Label(customer_details_frame, text="CONTACT NO", font=('time new roman',11, 'bold'),bg="mediumpurple1", fg='black')
phoneLabel.grid(row=0,column=2, padx=20, pady=2)
# -- customer phone number entry
phoneEntry=Entry(customer_details_frame,font=('arial',15),bd=7,width=18)
phoneEntry.grid(row=0,column=3, padx=8, pady=2)

# bill number
billNumberLabel = Label(customer_details_frame, text="BILL NO", font=('time new roman',11, 'bold'),bg="mediumpurple1", fg='black')
billNumberLabel.grid(row=0,column=4, padx=20, pady=2)
# -- customer phone entry
billNumberEntry=Entry(customer_details_frame,font=('arial',15),bd=7,width=18)
billNumberEntry.grid(row=0,column=5, padx=8, pady=2)

# button class
searchButton=Button(customer_details_frame,text='SEARCH',
                    font=('arial', 12, 'bold'), bd=7, width=7,command=search_bill)
searchButton.grid(row=0,column=6, padx=20, pady=8)

# container box 2 / Products Box
productsFrame=Frame(root)
productsFrame.pack(padx=0)

# cosmetics names
cosmeticsFrame=LabelFrame(productsFrame,text="COSMETICS", font=('time new roman',15, 'bold'), bg="mediumpurple1", fg='black', bd=8, relief=GROOVE)
cosmeticsFrame.grid(row=0, column=0,padx=0,pady=0)

# cosmetic name list 1
bathsoapLabel=Label(cosmeticsFrame, text='Bath Soap' , font=('time new roman',13), bg="mediumpurple1", fg='black', bd=8)
bathsoapLabel.grid(row=0, column=0, pady=6, padx=9, sticky='w')
bathsoapEntry=Entry(cosmeticsFrame,font=('times new roman', 15, 'bold'),width=10,bd=5)
bathsoapEntry.grid(row=0, column=1, pady=6, padx=9, sticky='w')
bathsoapEntry.insert(0,0)

# cosmetic name list 2
facecreamLabel=Label(cosmeticsFrame, text='Face Cream' , font=('time new roman',13), bg="mediumpurple1", fg='black', bd=8)
facecreamLabel.grid(row=1, column=0, pady=6, padx=9, sticky='w')
facecreamEntry=Entry(cosmeticsFrame,font=('times new roman', 15, 'bold'),width=10,bd=5)
facecreamEntry.grid(row=1, column=1, pady=6, padx=9, sticky='w')
facecreamEntry.insert(0,0)

# cosmetic name list 3
FacewashLabel=Label(cosmeticsFrame, text='Face wash' , font=('time new roman',13), bg="mediumpurple1", fg='black', bd=8)
FacewashLabel.grid(row=2, column=0, pady=6, padx=9, sticky='w')
FacewashEntry=Entry(cosmeticsFrame,font=('times new roman', 15, 'bold'),width=10,bd=5)
FacewashEntry.grid(row=2, column=1, pady=6, padx=9, sticky='w')
FacewashEntry.insert(0,0)

# cosmetic name list 4
hairSprayLabel=Label(cosmeticsFrame, text='Hair Spray' , font=('time new roman',13), bg="mediumpurple1", fg='black', bd=8)
hairSprayLabel.grid(row=3, column=0, pady=6, padx=9, sticky='w')
hairSprayEntry=Entry(cosmeticsFrame,font=('times new roman', 15, 'bold'),width=10,bd=5)
hairSprayEntry.grid(row=3, column=1, pady=6, padx=9, sticky='w')
hairSprayEntry.insert(0,0)

# cosmetic name list 5
hairGelLabel=Label(cosmeticsFrame, text='Hair Gel' , font=('time new roman',13), bg="mediumpurple1", fg='black', bd=8)
hairGelLabel.grid(row=4, column=0, pady=6, padx=9, sticky='w')
hairGelEntry=Entry(cosmeticsFrame,font=('times new roman', 15, 'bold'),width=10,bd=5)
hairGelEntry.grid(row=4, column=1, pady=6, padx=9, sticky='w')
hairGelEntry.insert(0,0)

# cosmetic name list 6
bodySprayLabel=Label(cosmeticsFrame, text='Body Spray' , font=('time new roman',13), bg="mediumpurple1", fg='black', bd=8)
bodySprayLabel.grid(row=5, column=0, pady=6, padx=9, sticky='w')
bodySprayEntry=Entry(cosmeticsFrame,font=('times new roman', 15, 'bold'),width=10,bd=5)
bodySprayEntry.grid(row=5, column=1, pady=6, padx=9, sticky='w')
bodySprayEntry.insert(0,0)


# Grocery names
groceryFrame=LabelFrame(productsFrame,text="Grocery", font=('time new roman',15, 'bold'), bg="mediumpurple1", fg='black', bd=8, relief=GROOVE)
groceryFrame.grid(row=0, column=1)

# grocery name list 1
riceLabel=Label(groceryFrame, text='Rice' , font=('time new roman',13), bg="mediumpurple1", fg='black', bd=8)
riceLabel.grid(row=0, column=0, pady=6, padx=9, sticky='w')
riceEntry=Entry(groceryFrame, font=('times new roman', 15, 'bold'),width=10,bd=5)
riceEntry.grid(row=0, column=1, pady=6, padx=9, sticky='w')
riceEntry.insert(0,0)

# grocery name list 2
oilLabel=Label(groceryFrame, text='Oil' , font=('time new roman',13), bg="mediumpurple1", fg='black', bd=8)
oilLabel.grid(row=1, column=0, pady=6, padx=9, sticky='w')
oilEntry=Entry(groceryFrame, font=('times new roman', 15, 'bold'),width=10,bd=5)
oilEntry.grid(row=1, column=1, pady=6, padx=9, sticky='w')
oilEntry.insert(0,0)

# grocery name list 3
daalLabel=Label(groceryFrame, text='Daal' , font=('time new roman',13), bg="mediumpurple1", fg='black', bd=8)
daalLabel.grid(row=2, column=0, pady=6, padx=9, sticky='w')
daalEntry=Entry(groceryFrame, font=('times new roman', 15, 'bold'),width=10,bd=5)
daalEntry.grid(row=2, column=1, pady=6, padx=9, sticky='w')
daalEntry.insert(0,0)

# grocery name list 4
wheatLabel=Label(groceryFrame, text='Wheat' , font=('time new roman',13), bg="mediumpurple1", fg='black', bd=8)
wheatLabel.grid(row=3, column=0, pady=6, padx=9, sticky='w')
wheatEntry=Entry(groceryFrame, font=('times new roman', 15, 'bold'),width=10,bd=5)
wheatEntry.grid(row=3, column=1, pady=6, padx=9, sticky='w')
wheatEntry.insert(0,0)

# grocery name list 5
sugarLabel=Label(groceryFrame, text='Sugar' , font=('time new roman',13), bg="mediumpurple1", fg='black', bd=8)
sugarLabel.grid(row=4, column=0, pady=6, padx=9, sticky='w')
sugarEntry=Entry(groceryFrame, font=('times new roman', 15, 'bold'),width=10,bd=5)
sugarEntry.grid(row=4, column=1, pady=6, padx=9, sticky='w')
sugarEntry.insert(0,0)

# grocery name list 6
teaLabel=Label(groceryFrame, text='Tea' , font=('time new roman',13), bg="mediumpurple1", fg='black', bd=8)
teaLabel.grid(row=5, column=0, pady=6, padx=9, sticky='w')
teaEntry=Entry(groceryFrame, font=('times new roman', 15, 'bold'),width=10,bd=5)
teaEntry.grid(row=5, column=1, pady=6, padx=9, sticky='w')
teaEntry.insert(0,0)

# Cold drinks names
colddrinksFrame=LabelFrame(productsFrame,text="Cold Drinks", font=('time new roman',15, 'bold'), bg="mediumpurple1", fg='black', bd=8, relief=GROOVE)
colddrinksFrame.grid(row=0, column=2)

# cold drinks name list 1
maazaLabel=Label(colddrinksFrame, text='Maaza' , font=('time new roman',13), bg="mediumpurple1", fg='black', bd=8)
maazaLabel.grid(row=0, column=0, pady=6, padx=9, sticky='w')
maazaEntry=Entry(colddrinksFrame, font=('times new roman', 15, 'bold'),width=10,bd=5)
maazaEntry.grid(row=0, column=1, pady=6, padx=9, sticky='w')
maazaEntry.insert(0,0)

# cold drinks name list 2
pepsiLabel=Label(colddrinksFrame, text='Pepsi' , font=('time new roman',13), bg="mediumpurple1", fg='black', bd=8)
pepsiLabel.grid(row=1, column=0, pady=6, padx=9, sticky='w')
pepsiEntry=Entry(colddrinksFrame, font=('times new roman', 15, 'bold'),width=10,bd=5)
pepsiEntry.grid(row=1, column=1, pady=6, padx=9, sticky='w')
pepsiEntry.insert(0,0)

# cold drinks name list 3
spriteLabel=Label(colddrinksFrame, text='Sprite' , font=('time new roman',13), bg="mediumpurple1", fg='black', bd=8)
spriteLabel.grid(row=2, column=0, pady=6, padx=9, sticky='w')
spriteEntry=Entry(colddrinksFrame, font=('times new roman', 15, 'bold'),width=10,bd=5)
spriteEntry.grid(row=2, column=1, pady=6, padx=9, sticky='w')
spriteEntry.insert(0,0)

# cold drinks name list 4
dewLabel=Label(colddrinksFrame, text='Dew' , font=('time new roman',13), bg="mediumpurple1", fg='black', bd=8)
dewLabel.grid(row=3, column=0, pady=6, padx=9, sticky='w')
dewEntry=Entry(colddrinksFrame, font=('times new roman', 15, 'bold'),width=10,bd=5)
dewEntry.grid(row=3, column=1, pady=6, padx=9, sticky='w')
dewEntry.insert(0,0)

# cold drinks name list 5
frootiLabel=Label(colddrinksFrame, text='Frooti' , font=('time new roman',13), bg="mediumpurple1", fg='black', bd=8)
frootiLabel.grid(row=4, column=0, pady=6, padx=9, sticky='w')
frootiEntry=Entry(colddrinksFrame, font=('times new roman', 15, 'bold'),width=10,bd=5)
frootiEntry.grid(row=4, column=1, pady=6, padx=9, sticky='w')
frootiEntry.insert(0,0)

# cold drinks name list 6
cocacolaLabel=Label(colddrinksFrame, text='Coca Cola' , font=('time new roman',13), bg="mediumpurple1", fg='black', bd=8)
cocacolaLabel.grid(row=5, column=0, pady=6, padx=9, sticky='w')
cocacolaEntry=Entry(colddrinksFrame, font=('times new roman', 15, 'bold'),width=10,bd=5)
cocacolaEntry.grid(row=5, column=1, pady=6, padx=9, sticky='w')
cocacolaEntry.insert(0,0)

# Bill Frame
billFrame=Frame(productsFrame,bd=8,relief=GROOVE)
billFrame.grid(row=0, column=3)

billareaLabel=Label(billFrame, text='Bill Area', font=('times new roman',15, 'bold'),bd=7, relief=GROOVE)
billareaLabel.pack(fill=X)

scrollbar=Scrollbar(billFrame,orient=VERTICAL)
scrollbar.pack(side=RIGHT,fill=Y)

textarea=Text(billFrame,width=58,height=17,yscrollcommand=scrollbar.set)
textarea.pack()

scrollbar.config(command=textarea.yview)

# Bill menu
billmenuFrame=LabelFrame(root, text="Bill Menu", font=('time new roman',15, 'bold'), bg="mediumpurple1", fg='black', bd=8, relief=GROOVE)
billmenuFrame.pack(fill=X)

# menu no 1
cosmeticPriceLabel=Label(billmenuFrame, text='Cosmetic Price' , font=('time new roman',13), bg="mediumpurple1", fg='black', bd=8)
cosmeticPriceLabel.grid(row=0, column=0, pady=6, padx=9, sticky='w')
cosmeticPriceEntry=Entry(billmenuFrame, font=('times new roman', 15, 'bold'),width=10,bd=5)
cosmeticPriceEntry.grid(row=0, column=1, pady=6, padx=9, sticky='w')

# menu no 2
groceryPriceLabel=Label(billmenuFrame, text='Grocery Price' , font=('time new roman',13), bg="mediumpurple1", fg='black', bd=8)
groceryPriceLabel.grid(row=1, column=0, pady=6, padx=9, sticky='w')
groceryPriceEntry=Entry(billmenuFrame, font=('times new roman', 15, 'bold'),width=10,bd=5)
groceryPriceEntry.grid(row=1, column=1, pady=6, padx=9, sticky='w')

# menu no 3
colddrinkPriceLabel=Label(billmenuFrame, text='Cold Drinks Price' , font=('time new roman',13), bg="mediumpurple1", fg='black', bd=8)
colddrinkPriceLabel.grid(row=2, column=0, pady=6, padx=9, sticky='w')
colddrinkPriceEntry=Entry(billmenuFrame, font=('times new roman', 15, 'bold'),width=10,bd=5)
colddrinkPriceEntry.grid(row=2, column=1, pady=6, padx=9, sticky='w')

colddrinkPriceLabel=Label(billmenuFrame, text='Cold Drinks Price' , font=('time new roman',13), bg="mediumpurple1", fg='black', bd=8)
colddrinkPriceLabel.grid(row=2, column=0, pady=6, padx=9, sticky='w')
colddrinkPriceEntry=Entry(billmenuFrame, font=('times new roman', 15, 'bold'),width=10,bd=5)
colddrinkPriceEntry.grid(row=2, column=1, pady=6, padx=9, sticky='w')

# menu no 4
cosmeticTaxLabel=Label(billmenuFrame, text='Cosmetic Tax' , font=('time new roman',13), bg="mediumpurple1", fg='black', bd=8)
cosmeticTaxLabel.grid(row=0, column=2, pady=6, padx=9, sticky='w')
cosmeticTaxEntry=Entry(billmenuFrame, font=('times new roman', 15, 'bold'),width=10,bd=5)
cosmeticTaxEntry.grid(row=0, column=3, pady=6, padx=9, sticky='w')

# menu no 5
groceryTaxLabel=Label(billmenuFrame, text='Grocery Tax' , font=('time new roman',13), bg="mediumpurple1", fg='black', bd=8)
groceryTaxLabel.grid(row=1, column=2, pady=6, padx=9, sticky='w')
groceryTaxEntry=Entry(billmenuFrame, font=('times new roman', 15, 'bold'),width=10,bd=5)
groceryTaxEntry.grid(row=1, column=3, pady=6, padx=9, sticky='w')

# menu no 6
coldDrinksTaxLabel=Label(billmenuFrame, text='Cold Drinks Tax' , font=('time new roman',13), bg="mediumpurple1", fg='black', bd=8)
coldDrinksTaxLabel.grid(row=2, column=2, pady=6, padx=9, sticky='w')
coldDrinksTaxEntry=Entry(billmenuFrame, font=('times new roman', 15, 'bold'),width=10,bd=5)
coldDrinksTaxEntry.grid(row=2, column=3, pady=6, padx=9, sticky='w')

# last button
buttonFrame=Frame(billmenuFrame,bd=8,relief=GROOVE)
buttonFrame.grid(row=0,column=4,rowspan=3,pady=30)

# button no 1
totalButton=Button(buttonFrame,text='Total', font=('arial', 12, 'bold'),bd=5,width=8,pady=10,command=total)
totalButton.grid(row=0,column=0,pady=20,padx=10)
# button no 2
billButton=Button(buttonFrame,text='Bill', font=('arial', 12, 'bold'),bd=5,width=8,pady=10,command=bill_area)
billButton.grid(row=0,column=1,pady=20,padx=5)
# button no 3
EmailButton=Button(buttonFrame,text='Email', font=('arial', 12, 'bold'),bd=5,width=8,pady=10,command=send_email)
EmailButton.grid(row=0,column=2,pady=20,padx=5)
# button no 4
PrintButton=Button(buttonFrame,text='Print', font=('arial', 12, 'bold'),bd=5,width=8,pady=10,command=print_bill)
PrintButton.grid(row=0,column=3,pady=20,padx=5)
# button no 4
SavePDFButton=Button(buttonFrame,text='PDF', font=('arial', 12, 'bold'),bd=5,width=8,pady=10,command=save_pdf)
SavePDFButton.grid(row=0,column=4,pady=20,padx=5)
# button no 5
ClearButton=Button(buttonFrame,text='Clear', font=('arial', 12, 'bold'),bd=5,width=8,pady=10,command=clear)
ClearButton.grid(row=0,column=5,pady=20,padx=5)

root.mainloop()