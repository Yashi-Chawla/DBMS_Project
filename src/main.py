import db_utils
import datetime
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


CACHE = {
    "user_id": None,
    "role": None
}

def createTkinterTable(column_names, values, master):
    table = ttk.Treeview(master, height=10, show="headings", columns=column_names)
    for column in column_names:
        table.column(column, anchor=CENTER)
        table.heading(column, text=column)
    for index, row in enumerate(values):
        row = list(map(str, row))
        table.insert("", values=row, index=index)
    return table


class Home():
    def __init__(self, CACHE):

        self.USER_ID = CACHE["user_id"]
        self.ROLE = CACHE["role"]

        self.root = Tk()
        self.root.title("Shopper")
        self.root.configure(background="#d2d2c9")
        self.root.geometry("480x480")

        self.blank = Label(self.root, bg="#d2d2c9")
        self.blank.pack()

        self.welcome = Label(
            self.root, text="Shopper", background="#d2d2c9")
        self.welcome.config(fg="#6d031c", font=("Comfortaa", 40))
        self.welcome.pack()
        self.blank = Label(self.root, bg="#d2d2c9")
        self.blank.pack()

        self.welcome = Label(
            self.root, text="Please choose your role to proceed", background="#d2d2c9")
        self.welcome.config(fg="#6d031c", font=("Comfortaa", 15))
        self.welcome.pack()
        self.blank = Label(self.root, bg="#d2d2c9")
        self.blank.pack()

        self.admin_button_choice = Button(
            self.root,
            text="ADMIN",
            command=lambda: self.role_selection("admin"),
            bg="#4759b8",
            fg="white",
            font=("Comfortaa", 15),
        )
        self.admin_button_choice.config(height=2, width=30, borderwidth=0)
        self.admin_button_choice.pack(side=TOP, expand=1)
        self.blank = Label(self.root, bg="#d2d2c9")
        self.blank.pack()

        self.user_button_choice = Button(
            self.root,
            text="USER",
            command=lambda: self.role_selection("user"),
            bg="#4759b8",
            fg="white",
            font=("Comfortaa", 15),
        )
        self.user_button_choice.config(height=2, width=30, borderwidth=0)
        self.user_button_choice.pack(side=TOP, expand=1)
        self.blank = Label(self.root, bg="#d2d2c9")
        self.blank.pack()

        self.exit_button_choice = Button(
            self.root,
            text="EXIT",
            command=self.on_close_root,
            bg="#4759b8",
            fg="white",
            font=("Comfortaa", 15),
        )
        self.exit_button_choice.config(height=2, width=30, borderwidth=0)
        self.exit_button_choice.pack(side=TOP, expand=1)
        self.blank = Label(self.root, bg="#d2d2c9")
        self.blank.pack()

        self.root.protocol("WM_DELETE_WINDOW", self.on_close_root)
        self.root.mainloop()


    def role_selection(self, role):
        self.on_close_root()
        self.root = Tk()
        self.root.title("Shopper")
        self.root.configure(background="#d2d2c9")
        self.ROLE = role

        self.blank = Label(self.root, bg="#d2d2c9")
        self.blank.pack()
        self.welcome = Label(self.root, text="Shopper", background="#d2d2c9")
        self.welcome.config(fg="#6d031c", font=("Comfortaa", 40))
        self.welcome.pack()
        self.blank = Label(self.root, bg="#d2d2c9")
        self.blank.pack()
        self.blank = Label(self.root, bg="#d2d2c9")
        self.blank.pack()

        self.welcome = Label(
            self.root, text="Please enter your credentials to continue", background="#d2d2c9")
        self.welcome.config(fg="#6d031c", font=("Comfortaa", 15))
        self.welcome.pack()
        self.blank = Label(self.root, bg="#d2d2c9")
        self.blank.pack()

        self.email = StringVar()
        self.password = StringVar()

        if self.ROLE == "admin":
            self.email.set("admin")
        else:
            self.welcome = Label(self.root, text="Email Address",
                             background="#d2d2c9")
            self.welcome.config(fg="#6d031c", font=("Comfortaa", 15))
            self.welcome.pack()
            self.blank = Label(self.root, bg="#d2d2c9")
            self.blank.pack()

            self.email_entry = Entry(self.root, textvariable=self.email)
            self.email_entry.pack()

        self.welcome = Label(self.root, text="Password",
                             background="#d2d2c9")
        self.welcome.config(fg="#6d031c", font=("Comfortaa", 15))
        self.welcome.pack()
        self.blank = Label(self.root, bg="#d2d2c9")
        self.blank.pack()

        self.password = StringVar()
        self.password_entry = Entry(
            self.root, textvariable=self.password, show="*")
        self.password_entry.pack()

        self.blank = Label(self.root, bg="#d2d2c9")
        self.blank.pack()

        self.blank = Label(self.root, bg="#d2d2c9")
        self.blank.pack()

        self.login_button = Button(
            self.root,
            text="LOGIN",
            command=self.verify_credentials,
            bg="#4759b8",
            fg="white",
            font=("Comfortaa", 15),
        )
        self.login_button.config(height=2, width=30, borderwidth=0)
        self.login_button.pack(side=TOP, expand=1)
        self.blank = Label(self.root, bg="#d2d2c9")
        self.blank.pack()

        self.exit_button_choice = Button(
            self.root,
            text="BACK",
            command=self.load_home,
            bg="#4759b8",
            fg="white",
            font=("Comfortaa", 15),
        )
        self.exit_button_choice.config(height=2, width=30, borderwidth=0)
        self.exit_button_choice.pack(side=TOP, expand=1)
        self.blank = Label(self.root, bg="#d2d2c9")
        self.blank.pack()

        self.root.protocol("WM_DELETE_root", self.on_close_root)
        self.root.mainloop()


    def verify_credentials(self):
        email = self.email.get()
        password = self.password.get()

        if self.ROLE == 'admin':
            if email == 'admin' and password == 'admin':
                CACHE["user_id"] = 'admin'
                CACHE["role"] = 'admin'
                self.USER_ID = 'admin'
                self.load_role_home()
            else:
                messagebox.showerror("Error", "Invalid credentials")
        else:
            status, user_id = db_utils.verify_credentials(email, password)
            if status:
                CACHE["user_id"] = user_id
                CACHE["role"] = 'user'
                self.USER_ID = user_id
                self.load_role_home()
            else:
                messagebox.showerror("Error", "Invalid credentials")


    def load_role_home(self):
        if CACHE["role"] == 'admin':
            self.on_close_root()
            Admin(CACHE)
        else:
            self.on_close_root()
            User(CACHE)

    def on_close_window(self):
        self.window.destroy()

    def on_close_root(self):
        self.root.destroy()

    def load_home(self):
        self.on_close_root()
        CACHE["user_id"] = None
        CACHE["role"] = None
        Home(CACHE)


class User():
    
    def __init__(self, CACHE):
        self.CACHE = CACHE
        self.USER_ID = CACHE["user_id"]
        self.ROLE = CACHE["role"]
        self.username = db_utils.get_username(self.USER_ID)

        self.root = Tk()
        self.root.title("Shopper")
        self.root.configure(background="#d2d2c9")
        self.root.geometry("480x480")

        self.blank = Label(self.root, bg="#d2d2c9")
        self.blank.pack()

        self.welcome = Label(
            self.root, text="Shopper", background="#d2d2c9")
        self.welcome.config(fg="#6d031c", font=("Comfortaa", 40))
        self.welcome.pack()
        self.blank = Label(self.root, bg="#d2d2c9")
        self.blank.pack()

        self.welcome = Label(
            self.root, text=f"Welcome {self.username}", background="#d2d2c9")
        self.welcome.config(fg="#6d031c", font=("Comfortaa", 15))
        self.welcome.pack()
        self.blank = Label(self.root, bg="#d2d2c9")
        self.blank.pack()

        self.buy_button = Button(
            self.root,
            text="BUY A PRODUCT",
            command=self.buy_product,
            bg="#4759b8",
            fg="white",
            font=("Comfortaa", 15),
        )
        self.buy_button.config(height=2, width=30, borderwidth=0)
        self.buy_button.pack(side=TOP, expand=1)
        self.blank = Label(self.root, bg="#d2d2c9")
        self.blank.pack()

        self.review_button = Button(
            self.root,
            text="ADD REVIEW",
            command=self.review,
            bg="#4759b8",
            fg="white",
            font=("Comfortaa", 15),
        )
        self.review_button.config(height=2, width=30, borderwidth=0)
        self.review_button.pack(side=TOP, expand=1)
        self.blank = Label(self.root, bg="#d2d2c9")
        self.blank.pack()

        self.cart_button = Button(
            self.root,
            text="VIEW YOUR CART",
            command=self.cart,
            bg="#4759b8",
            fg="white",
            font=("Comfortaa", 15),
        )
        self.cart_button.config(height=2, width=30, borderwidth=0)
        self.cart_button.pack(side=TOP, expand=1)
        self.blank = Label(self.root, bg="#d2d2c9")
        self.blank.pack()

        self.logout_button = Button(
            self.root,
            text="LOGOUT",
            command=self.load_main,
            bg="#4759b8",
            fg="white",
            font=("Comfortaa", 15),
        )
        self.logout_button.config(height=2, width=30, borderwidth=0)
        self.logout_button.pack(side=TOP, expand=1)
        self.blank = Label(self.root, bg="#d2d2c9")
        self.blank.pack()

        self.root.protocol("WM_DELETE_root", self.on_close_root)
        self.root.mainloop()

    def buy_product(self):
        all_products = db_utils.get_all_products()
        if all_products:
            self.window = Tk()
            self.window.title("Shopper")
            self.window.configure(background="#d2d2c9")

            self.welcome = Label(
            self.window, text=f"Select to add to cart", background="#d2d2c9")
            self.welcome.config(fg="#6d031c", font=("Comfortaa", 15))
            self.welcome.pack()
            self.blank = Label(self.window, bg="#d2d2c9")
            self.blank.pack()

            self.table = createTkinterTable(["Product ID", "Product Name", "Description", "Price", "Brand ID"], all_products, self.window)
            self.table.pack(side=TOP, expand=1)
            self.blank = Label(self.window, bg="#d2d2c9")
            self.blank.pack()
            self.blank = Label(self.window, bg="#d2d2c9")
            self.blank.pack()

            self.add_button = Button(
            self.window,
            text="ADD TO ORDER",
            command=lambda : self.add_product_selection_to_order(self.table.selection(), all_products),
            bg="#4759b8",
            fg="white",
            font=("Comfortaa", 15),
            )
            self.add_button.config(height=2, width=30, borderwidth=0)
            self.add_button.pack(side=TOP, expand=1)
            self.blank = Label(self.window, bg="#d2d2c9")
            self.blank.pack()

            self.review_button = Button(
            self.window,
            text="VIEW REVIEWS",
            command=lambda : self.view_reviews_for_products(self.table.selection(), all_products),
            bg="#4759b8",
            fg="white",
            font=("Comfortaa", 15),
            )
            self.review_button.config(height=2, width=30, borderwidth=0)
            self.review_button.pack(side=TOP, expand=1)
            self.blank = Label(self.window, bg="#d2d2c9")
            self.blank.pack()

        else:
            messagebox.showerror("Error", "No products available")

    def review(self):
        self.window = Tk()
        self.window.title("Shopper")
        self.window.configure(background="#d2d2c9")

        self.welcome = Label(
            self.window, text=f"Add a review", background="#d2d2c9")
        self.welcome.config(fg="#6d031c", font=("Comfortaa", 30))
        self.welcome.pack()
        self.blank = Label(self.window, bg="#d2d2c9")
        self.blank.pack()

        current_date = datetime.datetime.now().date()

        self.product_id_text = Label(self.window, text="Product ID", background="#d2d2c9")
        self.product_id_text.config(fg="#6d031c", font=("Comfortaa", 15))
        self.product_id_text.pack()
        self.product_entry = Entry(self.window)
        self.product_entry.pack(side=TOP, expand=1)
        self.blank = Label(self.window, bg="#d2d2c9")
        self.blank.pack()

        self.rating_text = Label(self.window, text="Rating", background="#d2d2c9")
        self.rating_text.config(fg="#6d031c", font=("Comfortaa", 15))
        self.rating_text.pack()
        self.rating_entry = Entry(self.window)
        self.rating_entry.pack(side=TOP, expand=1)
        self.blank = Label(self.window, bg="#d2d2c9")
        self.blank.pack()

        self.review_text = Label(self.window, text="Review", background="#d2d2c9")
        self.review_text.config(fg="#6d031c", font=("Comfortaa", 15))
        self.review_text.pack()
        self.review_entry = Text(self.window, height=5, width=30)
        self.review_entry.pack(side=TOP, expand=1)
        self.blank = Label(self.window, bg="#d2d2c9")
        self.blank.pack()

        self.submit_button = Button(
            self.window,
            text="SUBMIT",
            command=lambda : self.add_review(self.product_entry.get(), self.rating_entry.get(), self.review_entry.get("1.0", END), current_date),
            bg="#4759b8",
            fg="white",
            font=("Comfortaa", 15),
        )
        self.submit_button.config(height=2, width=30, borderwidth=0)
        self.submit_button.pack(side=TOP, expand=1)
        self.blank = Label(self.window, bg="#d2d2c9")
        self.blank.pack()   

    def cart(self):
        cart_details, total_amount, num_products = db_utils.get_cart_for_user(self.USER_ID)
        if len(cart_details):
            column_names = ["Product Name", "Description", "Price"]
            cart_details = [x[1:4] for x in cart_details]

            self.window = Tk()
            self.window.title("Shopper")
            self.window.configure(background="#d2d2c9")

            self.table = createTkinterTable(["Product Name", "Description", "Price"], cart_details, self.window)
            self.table.pack(side=TOP, expand=1)

            self.welcome = Label(
            self.window, text=f"Total Price: {total_amount}", background="#d2d2c9")
            self.welcome.config(fg="#6d031c", font=("Comfortaa", 20))
            self.welcome.pack()

            self.blank = Label(self.window, bg="#d2d2c9")
            self.blank.pack()

        else:
            messagebox.showinfo("Cart", "Your cart is empty!")


    def add_product_selection_to_order(self, indices, products):
        indices = list(map(lambda x: int(x[1:], 16) -1, indices))
        for index, product in enumerate(products):
            if index in indices:
                status = db_utils.add_product_to_order(self.USER_ID, product[0])
                if not status:
                    messagebox.showerror("Error", f"Error adding product {product[0]} to order")
        self.on_close_window()


    def view_reviews_for_products(self, indices, products):
        indices = list(map(lambda x: int(x[1:], 16) -1, indices))[:1]
        for index, product in enumerate(products):
            if index in indices:
                product_reviews = db_utils.get_reviews_for_product(product[0])
                if product_reviews:
                    self.sub_window = Tk()
                    self.sub_window.title("Shopper")
                    self.sub_window.configure(background="#d2d2c9")

                    self.welcome = Label(
                    self.sub_window, text=f"Reviews for {product[1]}", background="#d2d2c9")
                    self.welcome.config(fg="#6d031c", font=("Comfortaa", 15))
                    self.welcome.pack()
                    self.blank = Label(self.sub_window, bg="#d2d2c9")
                    self.blank.pack()

                    self.review_table = createTkinterTable(["Date", "Rating", "Description"], product_reviews, self.sub_window)
                    self.review_table.pack(side=TOP, expand=1)
                    self.blank = Label(self.sub_window, bg="#d2d2c9")
                    self.blank.pack()
                    self.blank = Label(self.sub_window, bg="#d2d2c9")
                    self.blank.pack()

                    self.close_button = Button(
                    self.sub_window,
                    text="BACK",
                    command=self.sub_window.destroy,
                    bg="#4759b8",
                    fg="white",
                    font=("Comfortaa", 15),
                    )
                    self.close_button.config(height=2, width=30, borderwidth=0)
                    self.close_button.pack(side=TOP, expand=1)
                    self.blank = Label(self.sub_window, bg="#d2d2c9")
                    self.blank.pack()
                else:
                    messagebox.showinfo("Reviews", "No reviews for this product")


    def add_review(self, product_id, rating, review, date):
        user_id = self.USER_ID
        status = db_utils.add_review(product_id, user_id, rating, review, date)
        if not status:
            messagebox.showerror("Error", "Error adding review")
        self.on_close_window()


    def load_main(self):
        self.on_close_root()
        self.CACHE["user_id"] = None
        self.CACHE["role"] = None
        Home(self.CACHE)

    def on_close_window(self):
        self.window.destroy()

    def on_close_root(self):
        self.root.destroy()


class Admin():

    def __init__(self, CACHE):
        self.CACHE = CACHE
        self.USER_ID = self.CACHE["user_id"]
        self.ROLE = self.CACHE["role"]

        self.root = Tk()
        self.root.title("Shopper")
        self.root.configure(background="#d2d2c9")
        self.root.geometry("480x480")


        self.welcome = Label(
            self.root, text="Shopper Admin Portal", background="#d2d2c9")
        self.welcome.config(fg="#6d031c", font=("Comfortaa", 30))
        self.welcome.pack()
        self.blank = Label(self.root, bg="#d2d2c9")
        self.blank.pack()

        self.cart_details_button = Button(
            self.root,
            text="CUSTOMER CART DETAILS",
            command=self.customer_cart_details,
            bg="#4759b8",
            fg="white",
            font=("Comfortaa", 15),
        )
        self.cart_details_button.config(height=2, width=30, borderwidth=0)
        self.cart_details_button.pack(side=TOP, expand=1)
        self.blank = Label(self.root, bg="#d2d2c9")
        self.blank.pack()

        self.product_reviews_button = Button(
            self.root,
            text="PRODUCT RATING DETAILS",
            command=self.product_rating,
            bg="#4759b8",
            fg="white",
            font=("Comfortaa", 15),
        )
        self.product_reviews_button.config(height=2, width=30, borderwidth=0)
        self.product_reviews_button.pack(side=TOP, expand=1)
        self.blank = Label(self.root, bg="#d2d2c9")
        self.blank.pack()

        self.product_details_button = Button(
            self.root,
            text="PRODUCT DETAILS",
            command=self.product_details,
            bg="#4759b8",
            fg="white",
            font=("Comfortaa", 15),
        )
        self.product_details_button.config(height=2, width=30, borderwidth=0)
        self.product_details_button.pack(side=TOP, expand=1)
        self.blank = Label(self.root, bg="#d2d2c9")
        self.blank.pack()

        self.logout_button = Button(
            self.root,
            text="LOGOUT",
            command=self.load_main,
            bg="#4759b8",
            fg="white",
            font=("Comfortaa", 15),
        )
        self.logout_button.config(height=2, width=30, borderwidth=0)
        self.logout_button.pack(side=TOP, expand=1)
        self.blank = Label(self.root, bg="#d2d2c9")
        self.blank.pack()

        self.root.protocol("WM_DELETE_root", self.on_close_root)
        self.root.mainloop()

    def load_main(self):
        self.on_close_root()
        self.CACHE["user_id"] = None
        self.CACHE["role"] = None
        Home(self.CACHE)

    def on_close_root(self):
        self.root.destroy()

    def customer_cart_details(self):
        details = db_utils.get_customer_and_cart_details()
        if details:
            self.window = Tk()
            self.window.title("Shopper")
            self.window.configure(background="#d2d2c9")
            # self.window.geometry("480x480")

            self.welcome = Label(
                self.window, text="Customer Cart Details", background="#d2d2c9")
            self.welcome.config(fg="#6d031c", font=("Comfortaa", 30))
            self.welcome.pack()
            self.blank = Label(self.window, bg="#d2d2c9")
            self.blank.pack()

            self.table = createTkinterTable(["Customer Name", "Cart Email Address", "Number of Products", "Total Price"], details, self.window)
            self.table.pack(side=TOP, expand=1)
            self.blank = Label(self.window, bg="#d2d2c9")
            self.blank.pack()

            self.close_button = Button(
                self.window,
                text="BACK",
                command=self.window.destroy,
                bg="#4759b8",
                fg="white",
                font=("Comfortaa", 15),
            )
            self.close_button.config(height=2, width=30, borderwidth=0)
            self.close_button.pack(side=TOP, expand=1)
            self.blank = Label(self.window, bg="#d2d2c9")
            self.blank.pack()

        else:
            messagebox.showinfo("Customer Cart Details", "No customer cart details")

    def product_rating(self):
        product_ratings = db_utils.get_product_review_details()
        if product_ratings:
            self.window = Tk()
            self.window.title("Shopper")
            self.window.configure(background="#d2d2c9")
            # self.window.geometry("480x480")

            self.welcome = Label(
                self.window, text="Product Rating Details", background="#d2d2c9")
            self.welcome.config(fg="#6d031c", font=("Comfortaa", 30))
            self.welcome.pack()
            self.blank = Label(self.window, bg="#d2d2c9")
            self.blank.pack()

            self.table = createTkinterTable(["Product ID", "Product Name", "Number of Ratings", "Average Rating"], product_ratings, self.window)
            self.table.pack(side=TOP, expand=1)
            self.blank = Label(self.window, bg="#d2d2c9")
            self.blank.pack()

            self.review_button = Button(
                self.window,
                text="VIEW REVIEWS",
                command=lambda: self.view_reviews_for_products(self.table.selection(), product_ratings),
                bg="#4759b8",
                fg="white",
                font=("Comfortaa", 15),
            )
            self.review_button.config(height=2, width=30, borderwidth=0)
            self.review_button.pack(side=TOP, expand=1)
            self.blank = Label(self.window, bg="#d2d2c9")
            self.blank.pack()

            self.close_button = Button(
                self.window,
                text="BACK",
                command=self.window.destroy,
                bg="#4759b8",
                fg="white",
                font=("Comfortaa", 15),
            )
            self.close_button.config(height=2, width=30, borderwidth=0)
            self.close_button.pack(side=TOP, expand=1)
            self.blank = Label(self.window, bg="#d2d2c9")
            self.blank.pack()

        else:
            messagebox.showinfo("Product Rating Details", "No product rating details")


    def product_details(self):
        all_products = db_utils.get_product_details()
        if all_products:
            self.window = Tk()
            self.window.title("Shopper")
            self.window.configure(background="#d2d2c9")
            # self.window.geometry("480x480")

            self.welcome = Label(
                self.window, text="Product Details", background="#d2d2c9")
            self.welcome.config(fg="#6d031c", font=("Comfortaa", 30))
            self.welcome.pack()
            self.blank = Label(self.window, bg="#d2d2c9")
            self.blank.pack()

            self.table = createTkinterTable(["Product Name", "Brand Name", "Supplier Name", "Price"], all_products, self.window)
            self.table.pack(side=TOP, expand=1)
            self.blank = Label(self.window, bg="#d2d2c9")
            self.blank.pack()

            self.close_button = Button(
                self.window,
                text="BACK",
                command=self.window.destroy,
                bg="#4759b8",
                fg="white",
                font=("Comfortaa", 15),
            )
            self.close_button.config(height=2, width=30, borderwidth=0)
            self.close_button.pack(side=TOP, expand=1)
            self.blank = Label(self.window, bg="#d2d2c9")
            self.blank.pack()
        else:
            messagebox.showinfo("Product Details", "No product details")


    def view_reviews_for_products(self, indices, product_ratings):
        indices = list(map(lambda x: int(x[1:], 16) -1, indices))[:1]
        for index, product in enumerate(product_ratings):
            if index in indices:
                product_reviews = db_utils.get_reviews_for_product(product[0])
                if product_reviews:
                    self.sub_window = Tk()
                    self.sub_window.title("Shopper")
                    self.sub_window.configure(background="#d2d2c9")

                    self.welcome = Label(
                    self.sub_window, text=f"Reviews for {product[1]}", background="#d2d2c9")
                    self.welcome.config(fg="#6d031c", font=("Comfortaa", 15))
                    self.welcome.pack()
                    self.blank = Label(self.sub_window, bg="#d2d2c9")
                    self.blank.pack()

                    self.review_table = createTkinterTable(["Date", "Rating", "Description"], product_reviews, self.sub_window)
                    self.review_table.pack(side=TOP, expand=1)
                    self.blank = Label(self.sub_window, bg="#d2d2c9")
                    self.blank.pack()
                    self.blank = Label(self.sub_window, bg="#d2d2c9")
                    self.blank.pack()

                    self.close_button = Button(
                    self.sub_window,
                    text="BACK",
                    command=self.sub_window.destroy,
                    bg="#4759b8",
                    fg="white",
                    font=("Comfortaa", 15),
                    )
                    self.close_button.config(height=2, width=30, borderwidth=0)
                    self.close_button.pack(side=TOP, expand=1)
                    self.blank = Label(self.sub_window, bg="#d2d2c9")
                    self.blank.pack()
                else:
                    messagebox.showinfo("Reviews", "No reviews for this product")


if __name__ == "__main__":
    # Home(CACHE)
    # User({
    #     "user_id": 2,
    #     "role": "user"
    # })
    Admin({
        "user_id": "admin",
        "role": "admin"
    })