from tkinter import *
from tkinter import messagebox
import pymysql
from PIL import ImageTk, Image

my_pass = ""
my_database = "Public Library"

# ===Connecting to the MySql server===
con = pymysql.connect(host="localhost", user="root", password=my_pass, database=my_database)
cur = con.cursor()

# ===Creating Window===
root = Tk()
root.title("Library")
root.minsize(width=1000, height=800)
root.maxsize(width=1000, height=800)
root.geometry("0x0")
same = True
n = 0.25

# declaring string variable
# for storing name and password
# ===sign in error===
name_var = StringVar()
email_var = StringVar()
phone_var = StringVar()
password_var = StringVar()
address_var = StringVar()


def member_register():
    global name_var, email_var, phone_var, password_var, address_var
    name_var_ = name_var.get()
    email_var_ = email_var.get()
    phone_var_ = phone_var.get()
    password_var_ = password_var.get()
    address_var_ = address_var.get()

    if name_var_ == '' or email_var_ == '' or phone_var_ == '' or password_var_ == '' or address_var_ == '':
        messagebox.showerror("Error!", "Field cannot be empty")

    else:
        cur.execute("select * from members where email = %s", email_var_)
        row = cur.fetchone()
        if row is not None:
            messagebox.showerror("Error", "User already exist. Try with another email.")
        else:
            sql = "INSERT INTO `members` (`member-name`,`email`, `password`, `phone-no`,`address`) VALUES (%s, %s, %s, %s, %s)"
            val = (name_var_, email_var_, password_var_, phone_var_, address_var_)
            cur.execute(sql, val)
            con.commit()
            print(cur.rowcount, "record inserted.")
            name_var.set("")
            email_var.set("")
            phone_var.set("")
            password_var.set("")
            address_var.set("")


# ===login error===
sign_in_var = StringVar()
sign_in_P_var = StringVar()


def login():
    global sign_in_P_var, sign_in_var
    temp1_var = sign_in_P_var.get()
    temp2_var = sign_in_var.get()
    if temp1_var == '' or temp2_var == '':
        messagebox.showerror("Error!", "Field cannot be empty")
    else:
        cur.execute("select * from members where email=%s and password=%s", (temp2_var, temp1_var))
        row = cur.fetchone()
        if row is None:
            messagebox.showerror("Error", "Invalid Email or Password")
        else:
            root.destroy()
            con.close()
            exec(open("./member.py").read())


# Adding a background image
# newImageHeight and newImageWidth contains the adjusted image dimensions.
background_image = Image.open("lib.jpg")
[imageSizeWidth, imageSizeHeight] = background_image.size
newImageSizeWidth = int(imageSizeWidth*n)
if same:
    newImageSizeHeight = int(imageSizeHeight*n)
else:
    newImageSizeHeight = int(imageSizeHeight/n)
background_image = background_image.resize((newImageSizeWidth, newImageSizeHeight), Image.ANTIALIAS)
img = ImageTk.PhotoImage(background_image)
Canvas1 = Canvas(root)

# We create the image on the canvas1 using .create_image() method.
# We use .pack() method to organize widgets in blocks before placing them in the parent widget.
Canvas1.create_image(400, 400, image=img)
Canvas1.config(bg="#3e271e", width=newImageSizeWidth, heigh=newImageSizeHeight)
Canvas1.pack(expand=True, fill=BOTH)

# Showing txt
headingFrame1 = Frame(root, bg="#9d8764")
headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.8)

# ====== Sign Up ========
headingLabel = Label(headingFrame1, text="Welcome to Public Library", bg='#9d8764', fg='light gray', font=('Bahnschrift SemiBold Condensed', 24))
headingLabel.place(relx=0.225, y=20)

userName = Label(headingFrame1, text="Name", bg='#9d8764', fg="light gray", font=('Calibri bold', 12)).place(relx=0.2, y=90)
txt_userName = Entry(headingFrame1, textvariable=name_var, font=('Calibri', 12)).place(relx=0.2, y=120, width=300)

email = Label(headingFrame1, text="Email", bg='#9d8764', fg="light gray", font=('Calibri bold', 12)).place(relx=0.2, y=150)
txt_email = Entry(headingFrame1, textvariable=email_var, font=('Calibri', 12)).place(relx=0.2, y=180, width=300)

phone = Label(headingFrame1, text="Phone", bg='#9d8764', fg="light gray", font=('Calibri bold', 12)).place(relx=0.2, y=210)
txt_phone = Entry(headingFrame1, textvariable=phone_var, font=('Calibri', 12)).place(relx=0.2, y=240, width=300)

password = Label(headingFrame1, text="Password", bg='#9d8764', fg="light gray", font=('Calibri bold', 12)).place(relx=0.2, y=270)
txt_password = Entry(headingFrame1, textvariable=password_var, font=('Calibri', 12)).place(relx=0.2, y=300, width=300)

address = Label(headingFrame1, text="Address", bg='#9d8764', fg="light gray", font=('Calibri bold', 12)).place(relx=0.2, y=330)
txt_address = Entry(headingFrame1, textvariable=address_var, font=('Calibri', 12)).place(relx=0.2, y=360, width=300)

register = Button(headingFrame1,
                  command=member_register,
                  text="Register",
                  bg='dark green',
                  fg='light gray').place(relx=0.2, y=400, width=300)

# ====== Sign In ========
sign_in_email = Label(headingFrame1, text="Email", bg='#9d8764', fg="light gray", font=('Calibri bold', 12)).place(relx=0.2, y=440)
sign_in_e = Entry(headingFrame1, textvariable=sign_in_var, font=('Calibri', 12)).place(relx=0.2, y=470, width=300)

sign_in_password = Label(headingFrame1, text="Password", bg='#9d8764', fg="light gray", font=('Calibri bold', 12)).place(relx=0.2, y=500)
sign_in_pass = Entry(headingFrame1, textvariable=sign_in_P_var, font=('Calibri', 12)).place(relx=0.2, y=530, width=300)

sign_in = Button(headingFrame1,
                 command=login,
                 text="Sign In",
                 bg='dark green',
                 fg='light gray').place(relx=0.2, y=570, width=300)

# ==== root.mainloop ====
root.mainloop()
