from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import pymysql

my_pass = ""
my_database = "Public Library"

# ===Connecting to the MySql server===
con = pymysql.connect(host="localhost", user="root", password=my_pass, database=my_database)
cur = con.cursor()

# Enter Table Names here
bookTable = "books"


def view():
    root = Toplevel()
    root.title("Library_View Books")
    root.minsize(width=1000, height=800)
    root.geometry("0x0")
    same = True
    n = 0.25

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

    canvas1 = Canvas(root)
    canvas1.create_image(400, 400, image=img)
    canvas1.config(bg="#3e271e", width=new_image_size_width, heigh=new_image_size_height)
    canvas1.pack(expand=True, fill=BOTH)

    # ===Heading===
    heading_frame1 = Frame(root, bg='#9d8764')
    heading_frame1.place(relx=0.25, rely=0.15, relwidth=0.5, relheight=0.6)

    heading_label = Label(heading_frame1, text="View Books", bg='#9d8764', fg='light gray', font=('Calibri bold', 24))
    heading_label.place(relx=0.32, y=25)

    y = 0.3

    Label(heading_frame1, text="%-15s%-40s%-20s%-20s" % ('Title', 'Author', 'Quantity', 'ISBN'), font=('Calibri bold', 14), bg='#9d8764', fg='light Gray').place(
        relx=0.07, rely=0.15)
    Label(heading_frame1, text="-----------------------------------------------------------------------------------------", bg='#9d8764',
          fg='light Gray').place(relx=0.05, rely=0.2)
    get_books = "select * from " + bookTable
    try:
        cur.execute(get_books)
        con.commit()
        for i in cur:
            Label(heading_frame1, text="%-15s%-40s%-20s%-20s" % (i[0], i[1], i[2], i[3]), font=('Calibri', 14), bg='#9d8764', fg='light Gray').place(
                relx=0.07, rely=y)
            y += 0.1
    except (pymysql.Error, pymysql.Warning):
        messagebox.showinfo("Failed to fetch files from database")

    # ===Quit Button===
    quit_btn = Button(root,
                      text="Quit",
                      bg='#9d8764',
                      fg='light gray',
                      font=('Calibri bold', 12),
                      command=root.destroy
                      )
    quit_btn.place(
        relx=0.4,
        rely=0.9,
        relwidth=0.18,
        relheight=0.08
        )

    root.mainloop()
