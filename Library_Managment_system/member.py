from ReturnBook import return_book
from IssueBook import issue_book
from ViewBook import view
from AddBook import add_book
from DeleteBook import delete
from tkinter import *
from PIL import ImageTk, Image
import pymysql

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

# Adding a background image
# newImageHeight and newImageWidth contains the adjusted image dimensions.
background_image = Image.open("lib.jpg")
[imageSizeWidth, imageSizeHeight] = background_image.size
newImageSizeWidth = int(imageSizeWidth * n)
if same:
    newImageSizeHeight = int(imageSizeHeight * n)
else:
    newImageSizeHeight = int(imageSizeHeight / n)
background_image = background_image.resize((newImageSizeWidth, newImageSizeHeight), Image.ANTIALIAS)
img = ImageTk.PhotoImage(background_image)
Canvas1 = Canvas(root)

# We create the image on the canvas1 using .create_image() method.
# We use .pack() method to organize widgets in blocks before placing them in the parent widget.
Canvas1.create_image(400, 400, image=img)
Canvas1.config(bg="#3e271e", width=newImageSizeWidth, heigh=newImageSizeHeight)
Canvas1.pack(expand=True, fill=BOTH)

# ===Showing Headings===
headingFrame1 = Frame(root, bg="#9d8764")
headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.8)

headingLabel = Label(headingFrame1, text="Welcome to Public Library", bg='#9d8764', fg='light gray',
                     font=('Bahnschrift SemiBold Condensed', 24))
headingLabel.place(relx=0.225, y=20)

# member functions
# ===Button 1===
btn1 = Button(root,
              text="Add Book Details",
              bg='#9d8764',
              fg="light gray",
              font=('Calibri bold', 12),
              command=add_book
              )
btn1.place(
    relx=0.28,
    rely=0.3,
    relwidth=0.45,
    relheight=0.1
)

# ===Button 2===
btn2 = Button(root,
              text="Delete Book",
              bg='#9d8764',
              fg="light gray",
              font=('Calibri bold', 12),
              command=delete
              )
btn2.place(
    relx=0.28,
    rely=0.4,
    relwidth=0.45,
    relheight=0.1
)

# ===Button 3===
btn3 = Button(root,
              text="View Book List",
              bg='#9d8764',
              fg="light gray",
              font=('Calibri bold', 12),
              command=view
              )
btn3.place(
    relx=0.28,
    rely=0.5,
    relwidth=0.45,
    relheight=0.1
)

# ===Button 4===
btn4 = Button(root,
              text="Issue Book to Student",
              bg='#9d8764',
              fg="light gray",
              font=('Calibri bold', 12),
              command=issue_book
              )
btn4.place(
    relx=0.28,
    rely=0.6,
    relwidth=0.45,
    relheight=0.1
)

# ===Button 5===
btn5 = Button(root,
              text="Return Book",
              bg='#9d8764',
              fg="light gray",
              font=('Calibri bold', 12),
              command=return_book
              )
btn5.place(
    relx=0.28,
    rely=0.7,
    relwidth=0.45,
    relheight=0.1
)

root.mainloop()
