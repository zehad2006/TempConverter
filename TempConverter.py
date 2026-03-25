import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror

#root
root=tk.Tk()
root.geometry("400x400")
root.title("Temperature Calculator")
root.resizable(width=False, height=False)
root.configure(background="grey22")

#menu
menu=tk.Frame(root, bg="grey22")
menu.place(relwidth=1, relheight=1)

celsius=tk.Button(menu,text="Celsius to Fahrenheit",bg="grey22", fg="grey70", font=("Arial",12,))
celsius.config(command=lambda: c_to_f.tkraise())


fahrenheit=tk.Button(menu,text="Fahrenheit to Celsius",bg="grey22", fg="grey70",font=("Arial",12))
fahrenheit.config(command=lambda: f_to_c.tkraise())

kelvin=tk.Button(menu, text="Kelvin to Celsius", bg="grey22", fg="grey70", font=("Arial",12))
kelvin.config(command=lambda: k_to_c.tkraise())

kelvin_2=tk.Button(menu, text="Celsius to Kelvin", bg="grey22", fg="grey70", font=("Arial",12))
kelvin_2.config(command=lambda: c_to_k.tkraise())

info=tk.Label(menu, text="Welcome.",bg="grey22", fg="grey80", font=("Arial",10))


exit_button=tk.Button(menu, text="Exit", command=root.destroy,bg="grey70", fg="grey20")

celsius.pack(pady=20)
fahrenheit.pack(pady=20)
kelvin.pack(pady=20)
kelvin_2.pack(pady=20)
info.place(x=10, y=10)
exit_button.pack(pady=20)


#displlay screen1
f_to_c=tk.Frame(root, bg="grey22")
#display screen2
c_to_f=tk.Frame(root, bg="grey22")
#display screen3
k_to_c=tk.Frame(root, bg="grey22")
#display screen4
c_to_k=tk.Frame(root, bg="grey22")

#placing frames
for frame in (menu,f_to_c, c_to_f, k_to_c, c_to_k):
    frame.place(relwidth=1, relheight=1)
menu.tkraise()

#conversions
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def kelvin_to_celsius(kelvin):
    celsius = (kelvin-273.15)
    return celsius

def celsius_to_kelvin(celsius):
    kelvin = (celsius + 273.15)
    return kelvin

#button click
def click_for_f():
    try:
        f = float(temperature1.get())
        c = fahrenheit_to_celsius(f)
        result = f'{f}  Fahrenheit is:  {round(c, 2)}  Celsius'
        result_label.config(text=result)
    except:
        showerror("Error", "Please Try again.")


def click_for_c():
    try:
        c = float(temperature2.get())
        f = celsius_to_fahrenheit(c)
        result = f'{c}  Celsius is:  {round(f, 2)}  Fahrenheit'
        result_label2.config(text=result)
    except:
        showerror("Error", "Please Try again.")


def click_for_k():
    try:
        k = float(temperature3.get())
        c = kelvin_to_celsius(k)
        result = f'{k}  Kelvin is:  {round(c, 2)}  Celsius'
        result_label3.config(text=result)
    except:
        showerror("Error", "Please Try again.")

def click_for_k2():
    try:
        c = float(temperature4.get())
        k = celsius_to_kelvin(c)
        result = f'{c}  Celsius is:  {round(k, 2)}  Kelvin'
        result_label4.config(text=result)
    except:
        showerror("Error", "Please Try again.")


####F to C page####
#page
fahrenheit_conversion=tk.Frame(f_to_c, bg="grey22")
fahrenheit_conversion.pack(pady=100)
#label
tk.Label(fahrenheit_conversion, text="Fahrenheit", bg="grey22", fg="grey70").grid(row=0, column=0)
temperature1=tk.StringVar()
#entry
tk.Entry(fahrenheit_conversion, textvariable=temperature1, bg="grey20", fg="grey70").grid(row=0, column=1)
#buttons
tk.Button(fahrenheit_conversion, text="Convert",bg="grey22",fg="grey70",command=click_for_f).grid(row=0, column=2)
tk.Button(fahrenheit_conversion,text="Go Back", bg="grey22", fg="grey70",command=lambda:menu.tkraise()).grid(row=2, column=0,columnspan=3)


#result
result_label=tk.Label(fahrenheit_conversion, bg="grey22", fg="grey70")
result_label.grid(row=1, column=0, columnspan=2, pady=10)


####C to F page####
#page
celsius_conversion=tk.Frame(c_to_f, bg="grey22")
celsius_conversion.pack(pady=100)
#label
tk.Label(celsius_conversion, text="Celsius", bg="grey22", fg="grey70").grid(row=0, column=0)
temperature2=tk.StringVar()
#entry
tk.Entry(celsius_conversion, textvariable=temperature2, bg="grey20", fg="grey70").grid(row=0, column=1)
#buttons
tk.Button(celsius_conversion, text="Convert",bg="grey22",fg="grey70",command=click_for_c).grid(row=0, column=2)
tk.Button(celsius_conversion,text="Go Back", bg="grey22", fg="grey70",command=lambda:menu.tkraise()).grid(row=2, column=0,columnspan=3)
#result
result_label2=tk.Label(celsius_conversion, bg="grey22", fg="grey70")
result_label2.grid(row=1, column=0, columnspan=2, pady=10)

####K to C page####
#page
kelvin_conversion=tk.Frame(k_to_c, bg="grey22")
kelvin_conversion.pack(pady=100)
#label
tk.Label(kelvin_conversion, text="Kelvin", bg="grey22", fg="grey70").grid(row=0, column=0)
temperature3=tk.StringVar()
#entry
tk.Entry(kelvin_conversion, textvariable=temperature3, bg="grey20", fg="grey70").grid(row=0, column=1)
#buttons
tk.Button(kelvin_conversion, text="Convert",bg="grey22",fg="grey70",command=click_for_k).grid(row=0, column=2)
tk.Button(kelvin_conversion,text="Go Back", bg="grey22", fg="grey70",command=lambda:menu.tkraise()).grid(row=2, column=0,columnspan=3)
#result
result_label3=tk.Label(kelvin_conversion, bg="grey22", fg="grey70")
result_label3.grid(row=1, column=0, columnspan=2, pady=10)

####C to K page####
#page
celsius2_conversion=tk.Frame(c_to_k, bg="grey22")
celsius2_conversion.pack(pady=100)
#label
tk.Label(celsius2_conversion, text="Celsius", bg="grey22", fg="grey70").grid(row=0, column=0)
temperature4=tk.StringVar()
#entry
tk.Entry(celsius2_conversion, textvariable=temperature4, bg="grey20", fg="grey70").grid(row=0, column=1)
#buttons
tk.Button(celsius2_conversion, text="Convert",bg="grey22",fg="grey70",command=click_for_k2).grid(row=0, column=2)
tk.Button(celsius2_conversion,text="Go Back", bg="grey22", fg="grey70",command=lambda:menu.tkraise()).grid(row=2, column=0,columnspan=3)
#result
result_label4=tk.Label(celsius2_conversion, bg="grey22", fg="grey70")
result_label4.grid(row=1, column=0, columnspan=2, pady=10)

#start
root.mainloop()










