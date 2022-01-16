from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import pymysql


def book_register():

    title = title_var.get().lower()
    author = author_var.get().lower()
    quantity = int(quantity_var.get())
    # ===Insert Book===
    insert_books = "INSERT INTO `books`(`title`,`author`,`quantity`) Values (%s, %s, %s)"
    data_books = (title, author, quantity)
    try:
        cur.execute(insert_books, data_books)
        con.commit()
        messagebox.showinfo('Success', "Book added successfully")
    except (pymysql.Error, pymysql.Warning):
        messagebox.showerror("Error", "Can't add data into Database")

    root.destroy()


def add_book():
    global cur, con, root, title_var, author_var, quantity_var

    # ===Open Window===
    root = Toplevel()
    root.title("Library_Add Book")
    root.minsize(width=1000, height=800)
    root.geometry("0x0")
    same = True
    n = 0.25

    title_var = StringVar()
    author_var = StringVar()
    quantity_var = StringVar()

    my_pass = ""
    my_database = "Public Library"
    # ===Connecting to the MySql server===
    con = pymysql.connect(host="localhost", user="root", password=my_pass, database=my_database)
    cur = con.cursor()

    # Adding a background image
    # newImageHeight and newImageWidth contains the adjusted image dimensions.
    background_image = Image.open("lib.jpg")
    [image_size_width, image_size_height] = background_image.size
    new_image_size_width = int(image_size_width*n)
    if same:
        new_image_size_height = int(image_size_height*n)
    else:
        new_image_size_height = int(image_size_height/n)
    background_image = background_image.resize((new_image_size_width, new_image_size_height), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(background_image)
    
    # We create the image on the canvas1 using .create_image() method.
    # We use .pack() method to organize widgets in blocks before placing them in the parent widget.
    canvas1 = Canvas(root)
    canvas1.create_image(400, 400, image=img)
    canvas1.config(bg="#3e271e", width=new_image_size_width, heigh=new_image_size_height)
    canvas1.pack(expand=True, fill=BOTH)

    # ===Heading===
    heading_frame1 = Frame(root, bg='#9d8764')
    heading_frame1.place(relx=0.25, rely=0.15, relwidth=0.5, relheight=0.6)

    heading_label = Label(heading_frame1, text="Add Books", bg='#9d8764', fg='light gray', font=('Calibri bold', 24))
    heading_label.place(relx=0.4, y=30)

    label_frame = Frame(root, bg='#9d8764')
    label_frame.place(relx=0.25, rely=0.25, relwidth=0.5, relheight=0.4)

    # ===Book Title===
    lb2 = Label(label_frame, text="Title : ", bg='#9d8764', fg='light gray', font=('Calibri bold', 15))
    lb2.place(relx=0.05, rely=0.35, relheight=0.08)
        
    book_info2 = Entry(label_frame,  textvariable=title_var, font=('Calibri bold', 12))
    book_info2.place(relx=0.3, rely=0.35, relwidth=0.62, relheight=0.08)
        
    # ===Book Author===
    lb3 = Label(label_frame, text="Author : ", bg='#9d8764', fg='light gray', font=('Calibri bold', 15))
    lb3.place(relx=0.05, rely=0.50, relheight=0.08)
        
    book_info3 = Entry(label_frame,  textvariable=author_var, font=('Calibri bold', 12))
    book_info3.place(relx=0.3, rely=0.50, relwidth=0.62, relheight=0.08)
        
    # ===Book Quantity===
    lb4 = Label(label_frame, text="Quantity : ", bg='#9d8764', fg='light gray', font=('Calibri bold', 15))
    lb4.place(relx=0.05, rely=0.65, relheight=0.08)
        
    book_info4 = Entry(label_frame,  textvariable=quantity_var, font=('Calibri bold', 12))
    book_info4.place(relx=0.3, rely=0.65, relwidth=0.62, relheight=0.08)
        
    # ===Submit Button===
    submit_btn = Button(root,
                        text="SUBMIT",
                        bg='#9d8764',
                        fg='light gray',
                        font=('Calibri bold', 12),
                        command=book_register
                        )
    submit_btn.place(
        relx=0.28,
        rely=0.65,
        relwidth=0.18,
        relheight=0.08
        )
    # ===Quit Button===
    quit_btn = Button(root,
                      text="Quit",
                      bg='#9d8764',
                      fg='light gray',
                      font=('Calibri bold', 12),
                      command=root.destroy
                      )
    quit_btn.place(
        relx=0.53,
        rely=0.65,
        relwidth=0.18,
        relheight=0.08
        )

    root.mainloop()
