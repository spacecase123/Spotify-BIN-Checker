from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import chromedriver_autoinstaller
from time import sleep
from subprocess import CREATE_NO_WINDOW

import SBCbackend

backend = SBCbackend
# chromedriver_autoinstaller.install()



def splash_screen():
    window_splash = Tk()

    window_splash.geometry("400x200")
    window_splash.configure(bg = "#ffffff")
    canvas_splash = Canvas(
        window_splash,
        bg = "#ffffff",
        height = 200,
        width = 400,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas_splash.place(x = 0, y = 0)

    background_img_splash = PhotoImage(file = f"imgs/splashbackground.png")
    background_splash = canvas_splash.create_image(
        195.0, 100.0,
        image=background_img_splash)
    # ---------CENTER--------
    window_height_splash = 200
    window_width_splash = 400

    screen_width_splash = window_splash.winfo_screenwidth()
    screen_height_splash = window_splash.winfo_screenheight()

    x_cordinate_splash = int((screen_width_splash/2) - (window_width_splash/2))
    y_cordinate_splash = int((screen_height_splash/2) - (window_height_splash/2))

    window_splash.geometry("{}x{}+{}+{}".format(window_width_splash, window_height_splash, x_cordinate_splash, y_cordinate_splash))
    # ---------CENTER END-----------
    window_splash.overrideredirect(True)

    window_splash.resizable(False, False)
    # ---------WEbDriverManager-------

    try:
        backend.driver = backend.webdriver.Chrome(options=backend.options)
        window_splash.after(3000, lambda: window_splash.destroy())

    except:
        msgval = messagebox.showerror("Chromedriver Error", 'Unable to find Chromedriver.exe')
        try:
            from webdriver_manager.chrome import ChromeDriverManager
            window_splash.after(3000, lambda: window_splash.destroy())
            backend.webdriver.Chrome(ChromeDriverManager().install(), options=backend.options)


        except:
            print("Unable to get latest chrome driver")

    window_splash.mainloop()



splash_screen()









def main_window():

    def btn_clicked():
        print("Button Clicked")


        backend.password = passwordField.get()
        backend.username = usernameField.get()
        backend.BIN = BINField.get()
        backend.fechaYY = yyField.get()

        if backend.fechaYY == "":
            backend.fechaYY = "RND"
        else:
            backend.fechaYY = backend.fechaYY

        backend.fechaMM = mmField.get()

        if backend.fechaMM == "":
            backend.fechaMM = "RND"
        else:
            backend.fechaMM = backend.fechaMM
        if backend.fechaMM > "9":
            backend.fechaMM = backend.fechaMM
        else:
            backend.fechaMM = "0" + backend.fechaMM

        backend.zipcode = zipcodeField.get()
        backend.country_code = countrycodeField.get()

        # ------CC DATA-------

        live_cc_db = {
            1: {"CC": '',
                "MM": '',
                "YY": '',
                "CVV": ''},
            2: {"CC": '',
                "MM": '',
                "YY": '',
                "CVV": ''},
            3: {"CC": '',
                "MM": '',
                "YY": '',
                "CVV": ''}
        }
        window.destroy()
        # -----MAIN WORKING-----





    window = Tk()

    icon = PhotoImage(file = 'imgs/sbc.png')
    window.iconphoto(False,icon)
    window.title("Spotify BIN Checker v1.0")
    window.geometry("900x500")
    window.configure(bg = "#ffffff")
    main_frame = Frame(window)
    canvas = Canvas(
        main_frame,
        bg = "#ffffff",
        height = 500,
        width = 900,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    main_frame.pack()
    canvas.pack()


    background_img = PhotoImage(file = f"imgs/background.png")
    background = canvas.create_image(
        450.5, 250.0,
        image=background_img)

    entry0_img = PhotoImage(file = f"imgs/img_textBox0.png")
    entry0_bg = canvas.create_image(
        171.5, 319.0,
        image = entry0_img)

    passwordField = Entry(main_frame,
        bd = 0,
        bg = "#f1f1f1",
        fg = '#555555',
        show='*',
        highlightthickness = 0)

    passwordField.place(
        x = 54.0, y = 296,
        width = 235.0,
        height = 44)

    entry1_img = PhotoImage(file = f"imgs/img_textBox1.png")
    entry1_bg = canvas.create_image(
        171.5, 212.0,
        image = entry1_img)

    usernameField = Entry(main_frame,
        bd = 0,
        bg = "#f1f1f1",
        fg = '#555555',
        highlightthickness = 0)

    usernameField.place(
        x = 54.0, y = 189,
        width = 235.0,
        height = 44)

    entry2_img = PhotoImage(file = f"imgs/img_textBox2.png")
    entry2_bg = canvas.create_image(
        624.5, 106.0,
        image = entry2_img)

    BINField = Entry(main_frame,
        bd = 0,
        bg = "#f1f1f1",
        fg = '#555555',
        highlightthickness = 0)

    BINField.place(
        x = 529.0, y = 84,
        width = 191.0,
        height = 42)

    entry3_img = PhotoImage(file = f"imgs/img_textBox3.png")
    entry3_bg = canvas.create_image(
        445.0, 200.0,
        image = entry3_img)

    mmField = Entry(main_frame,
        bd = 0,
        bg = "#f1f1f1",
        fg = '#555555',
        highlightthickness = 0)

    mmField.place(
        x = 394.0, y = 178,
        width = 102.0,
        height = 42)

    entry4_img = PhotoImage(file = f"imgs/img_textBox4.png")
    entry4_bg = canvas.create_image(
        628.0, 200.0,
        image = entry4_img)

    zipcodeField = Entry(main_frame,
        bd = 0,
        bg = "#f1f1f1",
        fg = '#555555',
        highlightthickness = 0)

    zipcodeField.place(
        x = 577.0, y = 178,
        width = 102.0,
        height = 42)

    entry5_img = PhotoImage(file = f"imgs/img_textBox5.png")
    entry5_bg = canvas.create_image(
        172.0, 424.0,
        image = entry5_img)

    countrycodeField = Entry(main_frame,
        bd = 0,
        bg = "#f1f1f1",
        fg = '#555555',
        highlightthickness = 0)

    countrycodeField.place(
        x = 121.0, y = 402,
        width = 102.0,
        height = 42)

    entry6_img = PhotoImage(file = f"imgs/img_textBox6.png")
    entry6_bg = canvas.create_image(
        810.0, 200.0,
        image = entry6_img)

    yyField = Entry(main_frame,
        bd = 0,
        bg = "#f1f1f1",
        fg = '#555555',
        highlightthickness = 0)

    yyField.place(
        x = 759.0, y = 178,
        width = 102.0,
        height = 42)

    img0 = PhotoImage(file = f"imgs/img0.png")
    b0 = Button(main_frame,
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda: [btn_clicked()],
        relief = "flat")

    b0.place(
        x = 530, y = 280,
        width = 189,
        height = 57)

    # CENTER THE WINDOW
    window_height = 500
    window_width = 900

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))

    window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
    window.resizable(False, False)

    window.mainloop()

main_window()

loading_window = Tk()
icon = PhotoImage(file = 'imgs/sbc.png')
loading_window.iconphoto(False, icon)
loading_window.title("Spotify BIN Checker v1.0")
loading_window.geometry("900x500")
loading_window.configure(bg = "#ffffff")
loading_canvas = Canvas(
    loading_window,
    bg = "#ffffff",
    height = 500,
    width = 900,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
loading_canvas.place(x = 0, y = 0)


loading_background_img = PhotoImage(file = f"imgs/loadingbackground.png")
loading_background = loading_canvas.create_image(
    450.0, 249.0,
    image=loading_background_img)

# ------------- CENTER -------------

window_height_loading = 500
window_width_loading = 900

screen_width_loading = loading_window.winfo_screenwidth()
screen_height_loading = loading_window.winfo_screenheight()

x_cordinate_loading = int((screen_width_loading/2) - (window_width_loading/2))
y_cordinate_loading = int((screen_height_loading/2) - (window_height_loading/2))

loading_window.geometry("{}x{}+{}+{}".format(window_width_loading, window_height_loading, x_cordinate_loading, y_cordinate_loading))

# ---------- CENTER END ------------


# ---------- LOADING BAR -----------

mpb = ttk.Progressbar(loading_window,orient ="horizontal",length = 600, mode ="determinate")

mpb.pack(ipady = 7, pady = 130, side = BOTTOM)




def progress_main(start_value,times,speed_value,multi_value):
    mpb["maximum"] = 600
    mpb["value"] = start_value

    for i in range(times):
        mpb["value"] += 1
        floatval = str(float(i/6)*multi_value)
        percent.config(text = floatval.split('.')[0]+"%")
        loading_window.update_idletasks()
        loading_window.after(speed_value)





# ------- LOADING BAR END ----------
def main_work():

    try:
        login_status = backend.LoginSpotify()

        if login_status == 'OK':
            progress_main(0, 151, 1, 1)

            try:
                backend.GenerateCC()
                progress_main(151, 151, 1, 2)
            except:
                msgval = messagebox.showerror("Unable to Generate CC", 'Please check the BIN')
                if msgval == "ok":
                    loading_window.destroy()
                    backend.driver.quit()

            try:
                backend.CheckCC()
                progress_main(301, 151, 1, 3)
            except:
                msgval = messagebox.showerror("Unable to Check CC", 'CC Checking Unsuccessful')
                if msgval == "ok":
                    loading_window.destroy()
                    backend.driver.quit()

            try:
                try_status = backend.TryCC()
                if try_status == 'OK':
                    progress_main(451, 151, 1, 4)
                    msgval = messagebox.showinfo("BIN STATUS", 'The BIN is Working!')
                else:
                    progress_main(451, 151, 1, 4)
                    msgval = messagebox.showerror("BIN STATUS", 'BIN Not Working!')
                    if msgval == "ok":
                        loading_window.destroy()
                        backend.driver.quit()
            except:
                msgval = messagebox.showerror("Unable to Try CC", 'CC Trying Unsuccessful')
                if msgval == "ok":
                    loading_window.destroy()
                    backend.driver.quit()

        else:
            msgval = messagebox.showerror("Unable to Login", 'Please check the Email and Password!')

            if msgval == "ok":
                loading_window.destroy()
                backend.driver.quit()
    except:
        msgval = messagebox.showerror("Failed", 'Something went wrong!')
        if msgval == "ok":
            loading_window.destroy()
            backend.driver.quit()


percent = Label(
    font = ("Roberto",16,"bold"),
    fg = "#00D084",
    bg = "white"
)
percent.place(x = 710, y = 290)

# b0 = Button(command = starting,)
# b0.pack()
img0 = PhotoImage(file = f"imgs/img0.png")
b1 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda: [main_work()],
    relief = "flat")
b1.place(
    x = 360, y = 400,
    width = 189,
    height = 57)
# b0.pack()


loading_window.resizable(False, False)

loading_window.mainloop()



