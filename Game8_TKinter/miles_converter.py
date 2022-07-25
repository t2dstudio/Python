import tkinter


window = tkinter.Tk()
window.title("Miles To Kilometer Converter")
window.config(padx=20 ,pady=20)
window.minsize(width=500, height=300)

def convert_miles_to_kilo():
    miles = float(miles_input.get())
    km =round(miles * 1.689)
    kilometer_result_label.config(text=f"{km}")

miles_input = tkinter.Entry(width=20)
miles_input.grid(column=1 , row=0)

miles_label = tkinter.Label(text="Miles")
miles_label.grid(column=2, row=0)

result = tkinter.Label(text="result")
result.grid(column=0, row=1)

kilometer_result_label = tkinter.Label(text="0")
kilometer_result_label.grid(column=1, row=1)

kilometer_label = tkinter.Label(text="Km")
kilometer_label.grid(column=2, row=1)

calculate_button = tkinter.Button(text="Calculate", command=convert_miles_to_kilo)
calculate_button.grid(column=1, row=2)




window.mainloop()