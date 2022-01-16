from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import pymysql

# Enter Table
issueTable = "issued"
bookTable = "books"


def delete_book():

    title = title_var.get().lower()
    delete_sql = "DElETE FROM books WHERE title = %s"
    try:
        cur.execute(delete_sql, (title,))
        con.commit()
        messagebox.showinfo('Success', "Book Record Deleted Successfully")
    except (pymysql.Error, pymysql.Warning):
        messagebox.showerror("Error", "Please check Book ISBN")
    title_var.set("")
    root.destroy()


def delete():
    global title_var, con, cur, root

    root = Toplevel()
    root.title("Library_Delete Book")
    root.minsize(width=1000, height=800)
    root.geometry("0x0")
    same = True
    n = 0.25

    title_var = StringVar()

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

    canvas1 = Canvas(root)
    canvas1.create_image(400, 400, image=img)
    canvas1.config(bg="#3e271e", width=new_image_size_width, heigh=new_image_size_height)
    canvas1.pack(expand=True, fill=BOTH)

    # ===Heading===
    heading_frame1 = Frame(root, bg='#9d8764')
    heading_frame1.place(relx=0.25, rely=0.25, relwidth=0.5, relheight=0.4)

    heading_label = Label(heading_frame1, text="Delete Books", bg='#9d8764', fg='light gray', font=('Calibri bold', 24))
    heading_label.place(relx=0.35, y=40)

    # ===Book Title===
    lb2 = Label(heading_frame1, text="Title : ", bg='#9d8764', fg='light gray', font=('Calibri bold', 15))
    lb2.place(relx=0.1, rely=0.35, relheight=0.08)

    book_info2 = Entry(heading_frame1, textvariable=title_var, font=('Calibri bold', 12))
    book_info2.place(relx=0.25, rely=0.35, relwidth=0.62, relheight=0.08)

    # ===Submit Button===
    submit_btn = Button(root,
                        text="SUBMIT",
                        bg='#9d8764',
                        fg='light gray',
                        font=('Calibri bold', 12),
                        command=delete_book
                        )
    submit_btn.place(
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
