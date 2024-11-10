import tkinter as tk
import calendar

class calendarApp:
    def __init__(self, window):
        self.window = window
        self.window.title("calendar")
        self.window.geometry("800x600")
        self.window.configure(bg="blue")
        
        self.create_widget()
    
    def create_widget(self):
        calendar_label = tk.Label(self.window, text="Calendar", font=("Arial", 20), bg="gray")
        enter_label = tk.Label(self.window, text="Enter Year:", font=("Arial", 15), bg="green")
        self.year_entry = tk.Entry(self.window, font=("Arial", 15), width=10, bg="gray", fg="black")
        show_calendar_button = tk.Button(self.window, text="Show calendar", font=("Arial", 15), bg="yellow", command=self.show_calendar)
        exit_button = tk.Button(self.window, text="Exit", font=("Arial", 15), bg="red", command=window.destroy)
        self.calendar_data_label = tk.Label(self.window, text="", font=("Arial", 15), bg="white", fg="black")

        calendar_label.pack(pady=20)
        enter_label.pack(pady=10)
        self.year_entry.pack(pady=10)
        show_calendar_button.pack(pady=10)
        exit_button.pack(pady=10)
        self.calendar_data_label.pack(pady=10)
    
    def show_calendar(self):
        #Creating a new window. This is part of the base window.
        calendar_window = tk.Toplevel(self.window)
        calendar_window.title("calendar of the year.")
        calendar_window.geometry("300x500")
        
        try:
            year = int(self.year_entry.get())
        except:
            self.calendar_data_label.config(text="You have entered an invalid year.")
            return
        
        calendar_content = calendar.calendar(year)
        calender_text = calendar.TextCalendar(calendar.SUNDAY)
        #calender_text.insert(tk.END, calendar_content)
        #calender_text.pack(expand=True, fill=tk.BOTH)
        cal_data = calender_text.formatyear(year)
        cal_text = tk.Text(calendar_window, font=("Arial", 15))
        cal_text.insert(tk.END, cal_data)
        cal_text.pack(expand=True, fill=tk.BOTH)
        
        
        
    

window = tk.Tk()
calendar1 = calendarApp(window)

window.mainloop()