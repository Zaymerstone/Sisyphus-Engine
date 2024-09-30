import customtkinter
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as font
import subprocess
from datetime import date, timedelta
from interface_backtest import interface_backtest
from tkinter import messagebox

# function for running python script
def run_script():
    subprocess.run(["python", "C:\\Users\\HP\\OneDrive\\Рабочий стол\\PythonProjects\\backtest.py"])



customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("750x750")

# -------------

# ------------------






my_font = font.Font(size=12) # for button font

label = customtkinter.CTkLabel(master=root, text="Select strategy:", font=("Arial", 14)) # text for strategy saying that user has to select strategy
label.grid(row=0, column=0, padx=10, pady=10) # Positioning of the text label

label_start_year = customtkinter.CTkLabel(master=root, text="Start year:", font=("Arial", 14)) # Text saying that user has to select start year for analysing 
label_start_year.grid(row=15, column=3, padx=10, pady=10) # Positioning of the start year text label

label_end_year = customtkinter.CTkLabel(master=root, text="End year:", font=("Arial", 14)) # Text saying thhat user has to select end year for analysing
label_end_year.grid(row=17, column=3, padx=10, pady=10) # Positioning of the end year text label

label_start_month = customtkinter.CTkLabel(master=root, text="Start month:", font=("Arial", 14)) # Text saying that user has to select starting month for analysis
label_start_month.grid(row=16, column=3, padx=10, pady=10) # Positioning of the start month text label

label_end_month = customtkinter.CTkLabel(master=root,text="End month:", font=("Arial", 14)) # Text saying that user has to select ending month for analysis
label_end_month.grid(row=18, column=3, padx=10, pady=10) # Positioning of the ending month text label

label1 = customtkinter.CTkLabel(master=root, text="Select ticker:", font=("Arial", 14)) # text that says user to select the ticker he wants to analyze
label1.grid(row = 13, column=0, padx=10, pady=10) # positioning of the text ticker label





def strategy_selected(): # when user selects radiobutton strategy, dopolnitelnie polya visvechivaetsya
    widget=[]
    strategy_radio_button = selected_value.get()
    strategy2_radio_button = selected_value.get()
    if selected_value.get() == "SmaCross":
        label2 = customtkinter.CTkLabel(master=root, text="Enter the first length:", font=("Arial", 12))
        label2.grid(row=4, column=0,padx=10,pady=10)
        length1_entry = customtkinter.CTkEntry(master=root, font=("Arial", 12))
        length1_entry.grid(row=4, column=1,padx=10,pady=10)
        label3 = customtkinter.CTkLabel(master=root,text="Enter the second length:", font=("Arial", 12))
        label3.grid(row=5, column=0, padx=10, pady=10)

        length2_entry = customtkinter.CTkEntry(master=root, font=("Arial", 12))
        length2_entry.grid(row=5, column=1,padx=10,pady=10)
    elif selected_value.get() == "RSI0scillator":
        label4 = customtkinter.CTkLabel(master=root, text="Enter the upperbound:", font=("Arial", 12))
        label4.grid(row=4, column=0,padx=10,pady=10)
        upperbound_entry = customtkinter.CTkEntry(master=root, font=("Arial", 12))
        upperbound_entry.grid(row=4,column=1, padx=10,pady=10)
        label5 = customtkinter.CTkLabel(master=root, text="Enter the lowerbound:", font=("Arial", 12))
        label5.grid(row=5, column=0,padx=10,pady=10)
        lowerbound_entry = customtkinter.CTkEntry(master=root, font=("Arial", 12))
        lowerbound_entry.grid(row=5, column=1,padx=10,pady=10)
        label6 = customtkinter.CTkLabel(master=root, text="Enter the rsi window:", font=("Arial", 12))
        label6.grid(row=6, column=0,padx=10,pady=10)
        rsi_entry = customtkinter.CTkEntry(master=root, font=("Arial", 12))
        rsi_entry.grid(row=6, column=1, padx=10,pady=10)




selected_value = tk.StringVar(value="st") # value has a random string, so both of the radiobuttons will be deselected
strategy_radio_button = tk.Radiobutton(root, text="SmaCross", value = "SmaCross", variable=selected_value, indicatoron=True, width=20, height=2, font=("Arial", 12), command=strategy_selected) # Radio button for the 1st strategy
strategy_radio_button.grid(row=0, column=1, padx=10, pady=10) # Positioning of the first radio button
#strategy_radio_button.deselect() # dont work idk why

strategy2_radio_button = tk.Radiobutton(root, text="RSI0scillator", value = "RSI0scillator", variable=selected_value, indicatoron=True, width=20, height=2, font=("Arial", 12), command=strategy_selected) # Radio button for the 2nd strategy
strategy2_radio_button.grid(row=1, column=1, padx=10, pady=10) # Positioning of the second radio button
#strategy2_radio_button.deselect() # dont work idk why

choice_box1 = ttk.Combobox(root, values=["GOOG", "TSLA", "MSFT"], state= "readonly", font=("Arial", 14)) # list box for tickers
choice_box1.grid(row=13, column=1, padx=10, pady=10) # positioning of the ticker list box

start_year_combobox = ttk.Combobox(root, values=["2010","2011","2012","2013","2014","2015","2016","2017","2018","2019", "2020", "2021","2022"], font=("Arial", 14), state= "readonly") # creating list box for the starting year
start_year_combobox.grid(row=15, column=4, padx=10, pady=10) # Positioning of the starting year list box
end_year_combobox = ttk.Combobox(root, values=["2010","2011","2012","2013","2014","2015","2016","2017","2018","2019", "2020", "2021","2022"], font=("Arial", 14), state= "readonly") # creating list box for ending years
end_year_combobox.grid(row=17, column=4, padx=10, pady=10) # Positioning of the end years list box
start_month_combobox = ttk.Combobox(root, values=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"], font=("Arial", 14), state= "readonly") # creating starting month list box
start_month_combobox.grid(row=16, column=4, padx=10, pady=10) # Positioning of the start month list box
end_month_combobox = ttk.Combobox(root, values=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"], font=("Arial", 14), state= "readonly") # creating end month list box
end_month_combobox.grid(row=18, column=4, padx=10, pady=10) # positioning of the ending month list box








# gets the user choices from comboboxes
def run_backtest():
    strategy = selected_value.get()
    ticker = choice_box1.get() # ticker chosen by the user
    start_year = int(start_year_combobox.get()) # start year chosen by the user сделать ошибки для месяцев и годов
    end_year = int(end_year_combobox.get()) # end year by user
    start_month = int(start_month_combobox.get()) # start month by user
    end_month = int(end_month_combobox.get()) # end month by user
    #if ticker !="GOOG" or "TSLA" or "MSFT": # if the ticker is not selected by the user raise an error with the following message
        #raise ValueError("You didn't select the ticker!")
    ticker = choice_box1.current()
    if ticker == -1: # check if user has selected a ticker
    # show error message and return
        return messagebox.showerror("Error", "Please select a ticker")




    # if strategy != "SmaCross" or "RSI0scillator": # if the strategy is not selected by the user raise an error with the following message
        # raise ValueError("You didn't select the strategy!")
    try:
        if selected_value.get() not in ["SmaCross", "RSI0scillator"]:
            return messagebox.showerror("Error", "Please select the strategy")
        else:
            run_script()
    except ValueError as e:
        print(e)



    if start_year > end_year: # check if start year is less than end year 
        raise ValueError("Start year cant be greater than end year!") # Если начальный год меньше конечного
    interface_backtest(uc_strategy=strategy, uc_ticker=ticker, uc_start_year=start_year, uc_start_month= start_month, uc_end_year=end_year,uc_end_month=end_month) #run the programme with user choices


button = tk.Button(root, text="Start testing", command=run_backtest, width=15, height=5, font=("Arial", 14)) # button for executing script
button.grid(row = 12, column=3, padx=10, pady=10)

# set default value
# choice_box1.current(0)







root.mainloop() # run the programme