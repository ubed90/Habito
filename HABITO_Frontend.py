'''
    AUTHOR :: UBED SHAIKH
    GITHUB :: www.github.com/ubed90
'''

from tkinter import *
import tkinter
from tkinter.ttk import *
from tkinter import ttk
from tkinter import messagebox
import habito_backend
import datetime

selected_row = None


'''
        CALL BACK FUNCTION'S FOR THE PROGRAM
'''

def iexit():
    iexit = messagebox.askyesno("Habito" , "Confirm if you want to exit ?")
    if iexit > 0:
        root.destroy()
    else:
        pass

def get_selected_row(event):
    global selected_row
    try:
        index = display_box.curselection()[0]
        selected_row = display_box.get(index).split("==>")
        selected_row = habito_backend.get_habit_data(selected_row[0].strip())
        if selected_row is not None:
            streak_name_label.configure(state=ACTIVE , text="      HABIT NAME       :- {:>35}".format(selected_row[1]) , background="black" , foreground="cyan")
            streak_counter_label.configure(state=ACTIVE , text="STREAK COUNTER :- {:>40}".format(selected_row[2]) , background="black" , foreground="cyan")
            longest_streal_label.configure(state=ACTIVE , text="LONGEST STREAK :- {:>40}".format(selected_row[3]) , background="black" , foreground="cyan")
        else:
            pass

    except IndexError or tkinter.TclError:
        pass

def sort_habits_accordin_len(habit):
    return len(habit[0])

def add_habit_command():
    if habito_backend.chech_habit_if_present(title=habit_entry_text.get()):
        messagebox.showinfo("Error" , "Habit Already Added !")
    elif len(habit_entry_text.get()) >= 2: 
        todays_date = datetime.datetime.now().date()
        todays_date = todays_date.strftime("%Y-%m-%d")
        tommorrows_date = (datetime.datetime.now() + datetime.timedelta(days=1)).date()
        tommorrows_date = tommorrows_date.strftime("%Y-%m-%d")
        
        habito_backend.add_habit(title=habit_entry_text.get() , updation_date=todays_date , tomorrows_date=tommorrows_date)
        messagebox.showinfo("SUCCESS" , "HABIT SUCCESSFULLY ADDED !")
        add_window.destroy()
    else:
        messagebox.showerror("ERROR" , "HABIT NAME SHOULD BE ATLEAST 2 CHARACTERS")


def add_habit():
    global add_window
    add_window = tkinter.Tk()
    add_window.wm_title("Add Habit")
    add_window.iconbitmap("Habito.ico")
    add_window.configure(background="rosy brown")
    add_window.resizable(width=False , height=False)
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (320 / 2)
    y = (screen_height / 2) - (230 / 2)
    add_window.geometry(f"320x230+{int(x)}+{int(y)}")

    add_habit_label = tkinter.Label(add_window , text="ENTER THE NAME OF HABIT" , font=('Times new roman' , 15 , 'bold') , justify=CENTER)
    add_habit_label.grid(row=0 , column=0 , padx=20 , ipady=10 , columnspan=3)

    global habit_entry_text
    habit_entry_text = tkinter.StringVar(add_window)
    habit_entry = tkinter.Entry(add_window , textvariable=habit_entry_text , font=('Times new roman' , 13 , 'bold') , width=28 , bd=15 , justify=LEFT)
    habit_entry.grid(row=1 , column=0 , columnspan=3 , pady=30)

    add_button = tkinter.Button(add_window , text="ADD" , font=('Times new roman' , 10 , 'bold') , width=10 , height=2 , bd=2 , background="green" , foreground="snow3" , command=add_habit_command)
    add_button.grid(row=2 , column=0)

    cancel_button = tkinter.Button(add_window , text="CANCEL" , font=('Times new roman' , 10 , 'bold') , width=10 , height=2 , bd=2 , background="red" , foreground="snow3" , command=add_window.destroy)
    cancel_button.grid(row=2 , column=2)

    add_window.mainloop()

def edit_habit_command():
    global selected_row
    if selected_row is not None:
        habito_backend.update_habit(selected_row[0] , edit_entry_text.get())
        messagebox.showinfo("SUCCESS" , "HABIT NAME SAVED SUCCESSFULLY")
        edit_window.destroy()
    else:
        messagebox.showerror("ERROR" , "PLEASE SELECT A HABIT FIRST")
        edit_window.destroy()

def edit_habit_name():
    global edit_window
    edit_window = tkinter.Tk()
    edit_window.wm_title("EDIT HABIT NAME")
    edit_window.iconbitmap("Habito.ico")
    edit_window.configure(background="rosy brown")
    edit_window.resizable(width=False , height=False)
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (320 / 2)
    y = (screen_height / 2) - (230 / 2)
    edit_window.geometry(f"320x230+{int(x)}+{int(y)}")

    edit_habit_label = tkinter.Label(edit_window , text="ENTER THE NAME" , font=('Times new roman' , 15 , 'bold') , justify=CENTER)
    edit_habit_label.grid(row=0 , column=0 , padx=30 , ipadx=40 , ipady=10 , columnspan=3)

    global edit_entry_text
    edit_entry_text = tkinter.StringVar(edit_window)
    edit_entry_text = tkinter.Entry(edit_window , textvariable=edit_entry_text , font=('Times new roman' , 13 , 'bold') , width=28 , bd=15 , justify=LEFT)
    edit_entry_text.grid(row=1 , column=0 , columnspan=3 , pady=30)

    add_button = tkinter.Button(edit_window , text="CONFIRM" , font=('Times new roman' , 10 , 'bold') , width=10 , height=2 , bd=2 , background="green" , foreground="snow3" , command=edit_habit_command)
    add_button.grid(row=2 , column=0)

    cancel_button = tkinter.Button(edit_window , text="CANCEL" , font=('Times new roman' , 10 , 'bold') , width=10 , height=2 , bd=2 , background="red" , foreground="snow3" , command=edit_window.destroy)
    cancel_button.grid(row=2 , column=2)

    edit_window.mainloop()


def view_all_command():
    if len(habito_backend.view_all()) > 0:
        rows = habito_backend.view_all()
        rows.sort(key=sort_habits_accordin_len , reverse = True)
        display_box.delete(0 , END)
        # column_head = f'{"HABITS":<24}==>{"STREAK":>20}'
        display_box.insert(END , f'{"HABITS":30}{"==>"}{"STREAK":>15}')
        display_box.insert(END , "-"*42)
        for habit , streak in rows:
            display_box.insert(END , f"{habit}  ==>  {streak}")

    else:
        messagebox.showerror("Error" , "No Habits to TRACK!!")

def update_streak_command():
    global selected_row
    if selected_row is not None:
        todays_date = datetime.datetime.now().date()
        todays_date = todays_date.strftime("%Y-%m-%d")
        tommorrows_date = (datetime.datetime.now() + datetime.timedelta(days=1)).date()
        tommorrows_date = tommorrows_date.strftime("%Y-%m-%d")
        updation_date = datetime.datetime.strptime(selected_row[4] , "%Y-%m-%d").date()
        tommorrows_date_1 = datetime.datetime.strptime(selected_row[5] , "%Y-%m-%d").date()

        if int(selected_row[2]) == 1:
            habito_backend.update_streak(selected_row[1] , updation_date=todays_date , tomorrows_date=tommorrows_date)
            data = habito_backend.get_habit_data(title=selected_row[1])
            if data[2] > data[3]:
                habito_backend.update_longest_streak(selected_row[0] , streak=data[2])
            messagebox.showinfo("SUCCESS" , "STREAK UPDATED SUCCESSFULLY !")
            view_all_command()

        elif todays_date == str(updation_date):
            messagebox.showinfo("ERROR" , "STREAK UPDATION ALLOWED ONLY ONCE A DAY !")
        
        elif todays_date == str(tommorrows_date_1):
            habito_backend.update_streak(selected_row[1] , updation_date=todays_date , tomorrows_date=tommorrows_date)
            data = habito_backend.get_habit_data(title=selected_row[1])
            if data[2] > data[3]:
                habito_backend.update_longest_streak(selected_row[0] , streak=data[2])
            messagebox.showinfo("SUCCESS" , "STREAK UPDATED SUCCESSFULLY !")
            view_all_command()

        else:
            habito_backend.reset_streak(selected_row[0] , updation_date=todays_date , tomorrows_date=tommorrows_date)
            messagebox.showinfo("SORRY" , "BE PUNCTUAL YOUR STREAK GOT RESET !")
            view_all_command()
    
    else:
        pass


def delete_habit_command():
    global selected_row
    if selected_row is not None:
        ans = messagebox.askyesno("CONFIRM" , "ARE YOU SURE ?")
        if ans > 0:
            habito_backend.delete_habit(selected_row[0])
            messagebox.showinfo("SUCCESS" , "HABIT DELETED SUCCESSFULLY")
            view_all_command()
    else:
        messagebox.showerror("ERROR" , "PLEASE SELECT HABIT FIRST !")


def about_command():
    about_me = '''I am a Final year Computer Engineering\nstudent and an Enthusiastic programmer\naiming to be the best. I am a keen and highly\nmotivated learner and would like to utilize my skills and knowledge to provide optimal\nsolutions.\n\n\twww.github.com/ubed90'''
    about_window = tkinter.Tk()
    about_window.title("ABOUT ME")
    about_window.iconbitmap("Habito.ico")
    about_window.resizable(width=False , height=False)
    about_window.configure(background="rosy brown")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (320 / 2)
    y = (screen_height / 2) - (230 / 2)
    about_window.geometry(f"320x230+{int(x)}+{int(y)}")

    about_me_label = tkinter.Label(about_window , text="ABOUT THE DEVELOPER" , font = ("Times new roman" , 13 , 'bold') , width=25 , height=3 , bd=3 , foreground="cyan" , background="black")
    about_me_label.grid(row=0 , column=0 , columnspan=2 , padx=30 , pady=2)

    about_me_text = tkinter.Text(about_window , font=("Times new roman" , 10 , 'bold') , bg="black" , fg="cyan" , width=36 , height=8 , bd=3)
    about_me_text.grid(row=1 , column=0 , columnspan=2 , pady=7)

    about_me_text.insert(END , about_me)
    about_me_text.configure(state=DISABLED)


'''
        GUI IMPLEMENTATION STARTS HERE
'''

root = tkinter.Tk()
root.title("Habito")
root.iconbitmap("Habito.ico")
root.resizable(width=False , height=False)
root.configure(background="rosy brown")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 2) - (480 / 2)
y = (screen_height / 2) - (790 / 2)

root.geometry(f"480x790+{int(x)}+{int(y)}")

menubar = Menu(root , background="gainsboro")
root.config(menu=menubar)

filemenu = Menu(menubar , tearoff=0)
menubar.add_cascade(label="File" , menu=filemenu)
filemenu.add_command(label="Access Hidden Habits" , state=DISABLED)
filemenu.add_separator()
filemenu.add_command(label="Exit" , command=iexit)

editmenu = Menu(menubar , tearoff=0)
menubar.add_cascade(label="Edit" , menu=editmenu)
editmenu.add_command(label="Add Habit" , command=add_habit)

helpmenu = Menu(menubar , tearoff=0)
menubar.add_cascade(label="Help" , menu=helpmenu)
helpmenu.add_command(label="About" , command=about_command)
helpmenu.add_separator()
helpmenu.add_command(label="Exit" , command=iexit)


habito_label = Label(root , text="H  A  B  I  T  O\n-----------------------------------\nA Personalized Habit Manager." , font=('Times new roman' , 20 , 'bold') , justify=CENTER , background="black" , foreground="snow" , anchor=CENTER)
habito_label.grid(row=0 , column=0 , sticky=tkinter.W , ipadx=55)

def on_enter(event):
    event.widget['background'] = 'grey75'
    event.widget['foreground'] = 'black'

def on_leave(event):
    event.widget['background'] = 'black'
    event.widget['foreground'] = 'grey75'

streak_name_label = ttk.Label(root , text="      HABIT NAME       :- {}".format("_"*33) ,font=('Times new roman' , 10 , 'bold') , padding=5 , justify=LEFT , width="51" , state='disabled')
streak_name_label.grid(row=1 , column=0 , sticky=tkinter.W , padx=50 , pady=10)


streak_counter_label = ttk.Label(root , text="STREAK COUNTER :- {}".format("_"*40) ,font=('Times new roman' , 10 , 'bold') , padding=5 , justify=LEFT , width="51" , state='disabled')
streak_counter_label.grid(row=2 , column=0 , sticky=tkinter.W , padx=50 , pady=10)

longest_streal_label = ttk.Label(root , text="LONGEST STREAK :- {}".format("_"*40) ,font=('Times new roman' , 10 , 'bold') , padding=5 , justify=LEFT , width="51" , state='disabled')
longest_streal_label.grid(row=3 , column=0 , sticky=tkinter.W , padx=50 , pady=10)


display_box = Listbox(root , height=25 , width=35 , background="snow3" , selectbackground="black" , selectforeground = "cyan" , borderwidth=5 , relief=RAISED , cursor="plus")
display_box.grid(row=4 , column=0 , rowspan=6 , columnspan=2 , sticky=tkinter.W , padx=47 , pady=10)

display_box_scroolbar = tkinter.Scrollbar(root , width=20)
display_box_scroolbar.place(x=280 , y=400, height="100")

display_box.configure(yscrollcommand=display_box_scroolbar.set)
display_box_scroolbar.configure(command=display_box.yview)

display_box.bind("<<ListboxSelect>>" , get_selected_row)

style = ttk.Style()
style.theme_use("default")

style.map("C.TButton",
   foreground=[('!active', 'white'), ('active', 'black')],
    background=[ ('!active','black'), ('active', 'grey75')]
    )


view_all_habits = ttk.Button(root , text="VIEW ALL" , style="C.TButton" , command=view_all_command)
view_all_habits.place(x=310 , y=246 , width="110")


update_selected_streak = ttk.Button(root , text="UPDATE STREAK" , style="C.TButton" , command=update_streak_command)
update_selected_streak.place(x=310 , y=336 , width="110")

edit_selected_habit = ttk.Button(root , text="EDIT HABIT NAME" , style="C.TButton" , command=edit_habit_name)
edit_selected_habit.place(x=310 , y=444 , width="110")

delete_streak = ttk.Button(root , text="DELETE" , style="C.TButton" , command=delete_habit_command)
delete_streak.place(x=310 , y=544 , width="110")

close = ttk.Button(root , text="EXIT" , style="C.TButton" , command=iexit)
close.place(x=310 , y=630 , width="110")


habito_footer = Label(root , text="AUTHOR - UBED SHAIKH\n{}\nwww.github.com/ubed90".format("-"*41) , font=('Times new roman' , 20 , 'bold') , justify=CENTER , background="grey75" , foreground="black" , anchor=CENTER)
habito_footer.grid(row=10 , column=0 , sticky=tkinter.W , ipadx=55 , ipady=5)

habito_footer.bind("<Enter>" , on_leave)
habito_footer.bind("<Leave>" , on_enter)

root.mainloop()

