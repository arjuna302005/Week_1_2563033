import tkinter as tk
root=tk.Tk()
root.title("Calculater")
root.geometry("500x400")
def calculate_grade():
    try:
        m1 = float(sub1entry.get())
        m2 = float(sub2entry.get())
        m3 = float(sub3entry.get())

        if m1 < 0 or m2 < 0 or m3 < 0 or m1>=100 or m2>=100 or m3>=100:
            
            return

        total = m1 + m2 + m3
        average = total / 3

        if average >= 90:
            grade = "A"
        elif average >= 75:
            grade = "B"
        elif average >= 60:
            grade = "C"
        elif average >= 40:
            grade = "D"
        else:
            grade = "Fail"

        result_label.config(
            text=f"Total Marks: {total}\n\nAverage Marks: {average:.2f}\n\nGrade: {grade}"
        )

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")

        

sub1=tk.Label(root,text="Subject 1",font="arial 10")
sub1.grid(row=0,column=0,padx=10,pady=10)
sub1entry=tk.Entry(root,text="")
sub1entry.grid(row=0,column=1,padx=10,pady=10)

sub2=tk.Label(root,text="Subject 2",font="arial 10")
sub2.grid(row=1,column=0,padx=10,pady=10)
sub2entry=tk.Entry(root,text="")
sub2entry.grid(row=1,column=1,padx=10,pady=10)

sub3=tk.Label(root,text="Subject 3",font="arial 10")
sub3.grid(row=2,column=0,padx=10,pady=10)
sub3entry=tk.Entry(root,text="")
sub3entry.grid(row=2,column=1,padx=10,pady=10)

# Button
button=tk.Button(root, text="Calculate Grade", command=calculate_grade)
button.grid(row=3,column=0,padx=10,pady=10)
# Result Label
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.grid(row=4,column=0,padx=10,pady=10)



root.mainloop()

