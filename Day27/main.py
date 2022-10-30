from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=100)
window.config(padx=20, pady=20)

equals = Label(text="Is equal to", font=("Arial", 10, "bold"))
equals.grid(column=0, row=1)
equals.config(padx=10, pady=10)

converted = Label(text="0", font=("Arial", 10, "bold"))
converted.grid(column=1, row=1)
converted.config(padx=10, pady=10)

miles = Label(text="Miles", font=("Arial", 10, "bold"))
miles.grid(column=2, row=0)
miles.config(padx=10, pady=10)

kilometers = Label(text="Km", font=("Arial", 10, "bold"))
kilometers.grid(column=2, row=1)
kilometers.config(padx=10, pady=10)


def button_clicked():
    miles_to_convert = input.get()
    converted_km = int(miles_to_convert) * 1.609344
    converted["text"] = converted_km


input = Entry(width=10)
input.grid(column=1, row=0)

calculate_button = Button(text="Calculate", command=button_clicked)
calculate_button.grid(column=1, row=2)



window.mainloop()
