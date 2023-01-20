from tkinter import *
import mysql.connector
from tkinter import messagebox

root = Tk()
root.title("Bank Management System")
root.geometry("500x300")


def customer_section():
    root.withdraw()

    def back_from_c_win():
        root.deiconify()
        c_win.destroy()

    def new_cust():
        c_win.withdraw()

        def back_from_c_win3():
            c_win.deiconify()
            c_win3.destroy()

        def submit_button_command():
            mydb = mysql.connector.connect(host="localhost", user="root", passwd="mitkumar@345", database="bank_data")
            mycursor = mydb.cursor()

            insert_cutomer = ("insert into customer_details" "(username, passwd, fullname, dob, mob_no) "  "values(%s, %s, %s, %s, %s)")
            new_cust = (new_username_entry.get(), new_pass_entry.get(), full_name_entry.get(), dob_entry.get(), mob_no_entry.get() )

            mycursor.execute(insert_cutomer, new_cust)
            mydb.commit()

            
            messagebox.showinfo("Alert box", "Account created successfully")
            
        #customer window 3
        c_win3 = Tk()
        c_win3.geometry("400x250")
        c_win3.title("New customer registration")

        new_username_label = Label(c_win3, text="Set Username: ")
        new_username_label.grid(row=1, column=1)
    
        new_username_entry = Entry(c_win3)
        new_username_entry.grid(row=1, column=2)
    
        new_pass_label = Label(c_win3, text="Set Password: ")
        new_pass_label.grid(row=2, column=1)
    
        new_pass_entry = Entry(c_win3)
        new_pass_entry.grid(row=2, column=2)

        full_name_label = Label(c_win3, text="Enter full name: ")
        full_name_label.grid(row=3, column=1)

        full_name_entry = Entry(c_win3)
        full_name_entry.grid(row=3, column=2)

        dob_label = Label(c_win3, text="Enter date of birth: ")
        dob_label.grid(row=4, column=1)

        dob_entry = Entry(c_win3)
        dob_entry.grid(row=4, column=2)

        mob_no_label = Label(c_win3, text="Enter mobile number: ")
        mob_no_label.grid(row=5, column=1)

        mob_no_entry = Entry(c_win3)
        mob_no_entry.grid(row=5, column=2)

        submit_button = Button(c_win3, text="Submit", command=submit_button_command)
        submit_button.grid(row=6, column=1)

        back_button = Button(c_win3, text=" <-- ", padx=10, pady=10, command=back_from_c_win3)
        back_button.grid(row=0, column=0)

    def cust_login():

        mydb = mysql.connector.connect(host="localhost", user="root", passwd="mitkumar@345", database="bank_data")
        mycursor1 = mydb.cursor()
        mycursor2 = mydb.cursor()

        mycursor1.execute("select username from customer_details")
        temp1 = mycursor1.fetchall()

        mycursor2.execute("select passwd from customer_details")
        temp2 = mycursor2.fetchall()

        #just a variable to control the loop properly
        ptr = 0
        iteration1 = 1
        iteration2 = 1
        for i1 in temp1:
            for j1 in i1:
                if j1 == username_entry.get():
                    for i2 in temp2:
                        for j2 in i2:
                            if iteration1 == iteration2:
                                if j2 == pass_entry.get():
                                    c_win.withdraw()
    
                                    def view_acc_details():
                                        mydb = mysql.connector.connect(host="localhost", user="root", passwd="mitkumar@345", database="bank_data")
                                        cursor = mydb.cursor()
    
                                        cursor.execute("select * from customer_details")
                                        temp = cursor.fetchall()
    
                                        for i in temp:
                                            if i[1] == j2:
                                                label = Label(c_win2, text=i[0]).grid(row=5, column=1)
                                                label = Label(c_win2, text=i[1]).grid(row=6, column=1)
                                                label = Label(c_win2, text=i[2]).grid(row=7, column=1)
                                                label = Label(c_win2, text=i[3]).grid(row=8, column=1)
                                                label = Label(c_win2, text=i[4]).grid(row=9, column=1)

                                            
                                    def back_from_c_win2():
                                        c_win2.destroy()
                                        c_win.deiconify()


                                    def send_money():

                                        def back_from_sm_win():
                                            c_win_sm.destroy()
                                            c_win2.deiconify()

                                        

                                        def transfer():
                                            rec_username = receiver_username_entry.get()
                                            amount_sent = amount_entry.get()

                                            t1 = temp1[0][0]
                                            t1 = t1 - int(amount_sent)

                                            cursor.execute("select balance from customer_details where username='" + rec_username + "'")
                                            temp2 = cursor.fetchall()
                                            t2 = temp2[0][0]
                                            t2 = t2 + int(amount_sent)

                                            #i was here 16/01/23
                                            query1 = "update customer_details set balance=" + str(t1) + " where username='" + username_entry.get() + "'"
                                            query2 = "update customer_details set balance=" + str(t2) + "where username='" + rec_username + "'"
                                            try:
                                                cursor.execute(query1)
                                                cursor.execute(query2)
                                                mydb.commit()

                                            except:
                                                mydb.rollback()

                               

                                        c_win2.withdraw()
                                        c_win_sm = Tk()
                                        c_win_sm.geometry("400x300")
                                        c_win_sm.title("Send Money")

                                        back_from_sm = Button(c_win_sm, text=" <-- ", padx=10, pady=10, command=back_from_sm_win).grid(row=0, column=0)

                                        mydb = mysql.connector.connect(host="localhost", user="root", passwd="mitkumar@345", database="bank_data")
                                        cursor = mydb.cursor()
                                        query = "select balance from customer_details where username='"+username_entry.get()+"'"
                                        cursor.execute(query)
                                        temp1 = cursor.fetchall()

                                        display_amt = Label(c_win_sm, text="   Available amount: "+str(temp1[0][0])).grid(row=1, column=1)
                                        
                                        receiver_username = Label(c_win_sm, text="   Enter Receiver Username: ").grid(row=2, column=1)
                                        receiver_username_entry = Entry(c_win_sm)
                                        receiver_username_entry.grid(row=2, column=2)
                                        
                                    
                                        amount = Label(c_win_sm, text="   Enter amount: ").grid(row=3, column=1)                                
                                        amount_entry = Entry(c_win_sm)
                                        amount_entry.grid(row=3, column=2)

                                        transfer = Button(c_win_sm, text="transfer", command=transfer).grid(row=4, column=1)

                                        


                                    def view_balance_fn():
                                        mydb = mysql.connector.connect(host="localhost", user="root", passwd="mitkumar@345", database="bank_data")
                                        cursor = mydb.cursor()
                                        query = "select balance from customer_details where username='"+username_entry.get()+"'"
                                        cursor.execute(query)
                                        temp = cursor.fetchall()

                                        balance = Label(c_win2, text=str(temp[0][0])).grid(row=3, column=2)
                                        
                                     

                                    c_win2 = Tk()
                                    c_win2.geometry("400x250")
                                    c_win2.title("Customer operations")
                        
                                
                                    hello_label = Label(c_win2, text="Hello " +j1+ "!").grid(row=0, column=1)
                                    back_button2 = Button(c_win2, text=" <-- ", padx=10, pady=10, command=back_from_c_win2).grid(row=0, column=0)
                                    view_balance_button = Button(c_win2, text="View Balance", command=view_balance_fn).grid(row=3, column=1)

                                    view_details_button = Button(c_win2, text="View Account Details", command=view_acc_details).grid(row=4, column=1)
                                    send_money_button = Button(c_win2, text="Send Money", command=send_money).grid(row=5, column=1)
                                    ptr = 1
                                    break

                                else:
                                    messagebox.showinfo("Alert box", "Incorrect password")
                                    ptr = 1
                                    break
                            else:
                                iteration2 = iteration2+1

                        if ptr==1:
                            break
                else:
                    iteration1 = iteration1+1
                                
         
            
    # customer window
    c_win = Tk() 
    c_win.geometry("400x250")
    c_win.title("Customer Login")

    username_label = Label(c_win, text="   Enter Username: ")
    username_label.grid(row=1, column=1)

    username_entry = Entry(c_win)
    username_entry.grid(row=1, column=2)

    pass_label = Label(c_win, text="   Enter Password: ")
    pass_label.grid(row=2, column=1)

    pass_entry = Entry(c_win)
    pass_entry.grid(row=2, column=2)

    submit_button = Button(c_win, text="Submit", command=cust_login)
    submit_button.grid(row=3, column=1)

    new_cust_button = Button(c_win, text="New customer?", command=new_cust)
    new_cust_button.grid(row=4, column=1)

    back_button = Button(c_win, text=" <-- ", padx=10, pady=10, command=back_from_c_win)
    back_button.grid(row=0, column=0)

    blacnk_space = Label(c_win, text="             ").grid(row=1, column=0)
    
    
####################################################################################################################


def employee_section():
    root.withdraw()

    def back_from_e_win():
        root.deiconify()
        e_win.destroy()

    def new_emp():
        e_win.withdraw()

        def back_from_e_win3():
            e_win.deiconify()
            e_win3.destroy()


        e_win3 = Tk()
        e_win3.geometry("400x250")
        e_win3.title("New employee registration")

        new_username_label = Label(e_win3, text="Set Username: ")
        new_username_label.grid(row=1, column=1)
    
        new_username_entry = Entry(e_win3)
        new_username_entry.grid(row=1, column=2)
    
        new_pass_label = Label(e_win3, text="Set Password: ")
        new_pass_label.grid(row=2, column=1)
    
        new_pass_entry = Entry(e_win3)
        new_pass_entry.grid(row=2, column=2)

        full_name_label = Label(e_win3, text="Enter full name: ").grid(row=3, column=1)
        full_name_entry = Entry(e_win3).grid(row=3, column=2)

        dob_label = Label(e_win3, text="Enter date of birth: ").grid(row=4, column=1)
        dob_entry = Entry(e_win3).grid(row=4, column=2)

        mob_no_label = Label(e_win3, text="Enter mobile number: ").grid(row=5, column=1)
        mob_no_entry = Entry(e_win3).grid(row=5, column=2)

        back_button = Button(e_win3, text=" <-- ", padx=10, pady=10, command=back_from_e_win3)
        back_button.grid(row=0, column=0)


    # Employee window
    e_win = Tk()
    e_win.geometry("400x250")
    e_win.title("Employee Login")

    username_label = Label(e_win, text="Enter Username: ")
    username_label.grid(row=1, column=1)

    username_entry = Entry(e_win)
    username_entry.grid(row=1, column=2)

    pass_label = Label(e_win, text="Enter Password: ")
    pass_label.grid(row=2, column=1)

    pass_entry = Entry(e_win)
    pass_entry.grid(row=2, column=2)

    submit_button = Button(e_win, text="Submit")
    submit_button.grid(row=3, column=1)

    new_cust_button = Button(e_win, text="New employee?", command=new_emp)
    new_cust_button.grid(row=4, column=1)

    back_button = Button(e_win, text=" <-- ", padx=10, pady=10, command=back_from_e_win)
    back_button.grid(row=0, column=0)


#################################################################################################################


# Creating labels and buttons

frame = LabelFrame(root, padx=50, pady=50)
frame.pack()

space1 = Label(frame, text="  ")
heading = Label(frame, text="    Choose your role    ", bg="yellow", padx=40, pady=20, font=("TkDefaultFont", 15) )
customer = Button(frame, text="Customer", command=customer_section, padx=15, pady=9, font=("TkDefaultFont", 10))
employee = Button(frame, text="Employee", command=employee_section, padx=15, pady=9, font=("TkDefaultFont", 10) )

# Placing labels and buttons

space1.grid(row=0, column=0)
heading.grid(row=0, column=1)
customer.grid(row=1, column=1)
employee.grid(row=3, column=1)


root.mainloop()
