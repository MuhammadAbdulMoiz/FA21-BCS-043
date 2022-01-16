from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import pymysql

my_pass = ""
my_database = "Public Library"

# ===Connecting to the MySql server===
con = pymysql.connect(host="localhost", user="root", password=my_pass, database=my_database)
cur = con.cursor()

# Enter Table
issueTable = "issued"
bookTable = "books"


def issue():
    book = book_issued.get().lower()
    person = issued_to.get()
    select = "Select quantity from books where title = %s"
    cur.execute(select, (book,))
    got = cur.fetchone()
    got = eval(got[0]) - 1

    # ===Insert Book===
    insert_books = "INSERT INTO `issued`(`book_issued`,`issued_to`) Values (%s, %s)"
    data_books = (book, person,)
    # ===Update Quantity===
    update_quantity = "UPDATE books SET quantity = %s where title = %s"
    d_b = (got, book,)
    try:
        cur.execute(insert_books, data_books)
        con.commit()
        cur.execute(update_quantity, d_b)
        con.commit()
        messagebox.showinfo('Success', "Book issued successfully")
    except (pymysql.Error, pymysql.Warning):
        messagebox.showerror("Error", "Can't add data into Database")

    root.destroy()


def issue_book():
    global root, book_issued, issued_to

    root = Toplevel()
    root.title("Library_Issue Book")
    root.minsize(width=1000, height=800)
    root.geometry("0x0")
    same = True
    n = 0.25

    book_issued = StringVar()
    issued_to = StringVar()

    # Adding a background image
    # newImageHeight and newImageWidth contains the adjusted image dimensions.
    background_image = Image.open("lib.jpg")
    [image_size_width, image_size_height] = background_image.size
    new_image_size_width = int(image_size_width * n)
    if same:
        new_image_size_height = int(image_size_height * n)
    else:
        new_image_size_height = int(image_size_height / n)
    background_image = background_image.resize((new_image_size_width, new_image_size_height), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(background_image)

    canvas1 = Canvas(root)
    canvas1.create_image(400, 400, image=img)
    canvas1.config(bg="#3e271e", width=new_image_size_width, heigh=new_image_size_height)
    canvas1.pack(expand=True, fill=BOTH)

    # ===Heading===
    heading_frame1 = Frame(root, bg='#9d8764')
    heading_frame1.place(relx=0.25, rely=0.25, relwidth=0.5, relheight=0.4)

    heading_label = Label(heading_frame1, text="Issue Book", bg='#9d8764', fg='light gray', font=('Calibri bold', 24))
    heading_label.place(relx=0.32, y=35)

    # Book ID
    lb1 = Label(heading_frame1, text="Book Title : ", bg='#9d8764', fg='light Gray', font=('Calibri', 14))
    lb1.place(relx=0.1, rely=0.3)

    inf1 = Entry(heading_frame1, textvariable=book_issued, font=('Calibri', 14))
    inf1.place(relx=0.3, rely=0.3, relwidth=0.60)

    # Issued To Student name
    lb2 = Label(heading_frame1, text="Issued To : ", bg='#9d8764', fg='light Gray', font=('Calibri', 14))
    lb2.place(relx=0.1, rely=0.4)

    inf2 = Entry(heading_frame1, textvariable=issued_to, font=('Calibri', 14))
    inf2.place(relx=0.3, rely=0.4, relwidth=0.60)

    # ===Issue Button===
    issue_btn = Button(root,
                       text="SUBMIT",
                       bg='#9d8764',
                       fg='light gray',
                       font=('Calibri bold', 12),
                       command=issue
                       )
    issue_btn.place(
        relx=0.28,
        rely=0.5,
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
        rely=0.5,
        relwidth=0.18,
        relheight=0.08
    )

    root.mainloop()
