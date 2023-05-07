#Import
import sqlite3
from tkinter import* 


root = Tk()
root.title("NATO PHOTOGRAPHY DATA")
root.iconbitmap("Nathan.bmp")
root.geometry("500x800")
#Define image
bg = PhotoImage(file='Nathan.png')
#Create a label
Photo_label = Label( image=bg)
Photo_label.place(x=0, y=0, relwidth=1, relheight=1)

#Create a database or connect to one
conn = sqlite3.connect('Customer_Info.db')
#Create cursor
c = conn.cursor()


#Create the Table for the data
'''c.execute("""CREATE TABLE addresses (
            first_Name text,
            last_Name text,
            Email integer,
            Phone integer
    )""")
'''

#Create Submit Function
def submit():
    #Create a database or connect to one
    conn = sqlite3.connect('Customer_Info.db')
    #Create cursor
    c = conn.cursor()
    #Insert into table
    c.execute("INSERT INTO addresses Values (:first_Name, :last_Name, :Email, :Phone)",
        {
        'first_Name': first_Name.get(),
        'last_Name': last_Name.get(),
        'Email': Email.get(),
        'Phone': Phone.get()
        })
    #Commit Changes
    conn.commit()

    conn.close()




    #Clear the text boxes
    first_Name.delete(0,END)
    last_Name.delete(0,END)
    Email.delete(0,END)
    Phone.delete(0,END)

#Create Query Function
def query():
    #Create a database or connect to one
    conn = sqlite3.connect('Customer_Info.db')
    #Create cursor
    c = conn.cursor()
    #Query the datebase
    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall()
    print(records)
    #loop thru results
    print_records = ''
    for record in records: 
        print_records += str(record) + "\n"
    
    query_label = Label(root, text=print_records)
    query_label.grid(row=8, column=0, columnspan=2, )

    #Commit Changes
    conn.commit()
    #close connection 
    conn.close()
     

#Create text boxes
first_Name = Entry(root, width= 30)
first_Name.grid(row = 0, column=1, padx=20)
last_Name = Entry(root, width= 30)
last_Name.grid(row = 1, column=1, padx=20)
Email = Entry(root, width= 30)
Email.grid(row = 2, column=1, padx=20)
Phone = Entry(root, width= 30)
Phone.grid(row = 3, column=1, padx=20)

#Create Text BOX LABELS
first_Name_label = Label(root, text="First Name")
first_Name_label.grid(row=0, column=0)
last_Name_label = Label(root, text="Last Name")
last_Name_label.grid(row=1, column=0)
Email_label = Label(root, text="Email")
Email_label.grid(row=2, column=0)
Phone_label = Label(root, text="Phone number")
Phone_label.grid(row=3, column=0)

#Create Submit Button
submit_btn = Button(root, text="Add Customer to database", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx= 10, ipadx= 100)
#Create a Query Button
query_btn= Button(root, text="Show Records", command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx= 10, ipadx= 137)


#Commit Changes
conn.commit()
#close connection 
conn.close()



root.mainloop()