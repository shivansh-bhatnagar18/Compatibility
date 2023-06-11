import customtkinter

index_window=customtkinter.CTk()
index_window.geometry("900x600")
index_window.resizable(False,False)
index_window.title("Love Compatibility and Personality Calculator")
customtkinter.set_appearance_mode("Dark")

heading_frame=customtkinter.CTkFrame(index_window, width=900, height=100, fg_color="#ffe5ec")
heading_frame.place(x=0,y=0)

heading=customtkinter.CTkLabel(heading_frame, text="Compatibility Calculator", font=("SF Atarian System",60),
                               text_color="Black")
heading.place(x=200,y=20)

input_area=customtkinter.CTkFrame(index_window, width=600, height=400, fg_color="#ffe5ec")
input_area.place(x=150,y=150)

name1=customtkinter.CTkLabel(input_area, text="Name :", font=("SF Atarian System",30), text_color="Black")
name2=customtkinter.CTkLabel(input_area, text="Name :", font=("SF Atarian System",30), text_color="Black")
name1.place(x=50, y=75)
name2.place(x=325, y=75)

entry1=customtkinter.CTkEntry(input_area, width=200, height=30, corner_radius=10, fg_color="#f0d8d8",
                              text_color="Black", font=("SF Atarian System",25) )
entry2=customtkinter.CTkEntry(input_area, width=200, height=30, corner_radius=10, fg_color="#f0d8d8",
                              text_color="Black", font=("SF Atarian System",25))
entry1.place(x=50, y=125)
entry2.place(x=325, y=125)

traits={1:"Initiator of action\n pioneering, leading\n independent, attaining\n individualistic",
2:"Cooperation\n adaptability\n consideration of others\n partnering, mediating",
3:"Expression\n verbalization\n socialization the arts\n the joy of living",
4:"Values foundation\n order, service\n struggle against limits\n steady growth",
5:"Expansiveness\n visionary, adventure\n the constructive use of freedom",
6:"Responsibility\n protection, nurturing\n community, balance\n sympathy",
7:"Analysis\n understanding, knowledge\n awareness, studious\n meditating",
8:"Practical endeavors\n status-oriented\n power-seeking\n high-material goals",
9:"Humanitarian\n giving nature\n selflessness, obligations\n creative expression"}

planets={1:'Sun', 2:'Moon', 3:'Jupiter', 4:'Uranus', 5:'Mercury', 6:'Venus', 7:'Neptune', 8:'Saturn', 9:'Mars'}
comp={1:[1,2,3,4,5,7,9], 2:[1,3,4,7,8,9], 3:[1,2,3,5,6,8,9], 4:[1,2,5,6,7,9], 5:[1,3,4,5,6,7,8,9],
      6:[3,4,5,8,9], 7:[1,2,4,5], 8:[2,3,5,6], 9:[1,2,3,4,5,6,9]}

def submission():
    global firstname, secondname, sum1, sum2
    firstname = entry1.get()
    secondname = entry2.get()
    firstname=str(firstname).upper().strip()
    secondname=str(secondname).upper().strip()
    values={'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':1, 'K':2, 'L':3, 'M':4, 'N':5,
            'O':6, 'P':7, 'Q':8, 'R':9, 'S':1, 'T':1, 'U':2, 'V':3, 'W':4, 'X':5, 'Y':6, 'Z':7}
    sum1=0
    sum2=0
    for c in firstname:
        sum1=sum1+values[c]
        print(c)
    for c in secondname:
        sum2=sum2+values[c]
        print(c)
    while(sum1//10!=0):
        num=sum1
        sum1=0
        while(num>0):
            b=num%10
            sum1=sum1+b
            num=num//10
    while (sum2 // 10 != 0):
        num = sum2
        sum2 = 0
        while (num > 0):
            b = num % 10
            sum2 = sum2 + b
            num = num // 10
    name1_frame = customtkinter.CTkFrame(input_area, width=200, height=100, fg_color="#ffc2d1", corner_radius=5)
    name1_frame.place(x=50, y=175)
    name2_frame = customtkinter.CTkFrame(input_area, width=200, height=100, fg_color="#ffc2d1", corner_radius=5)
    name2_frame.place(x=320, y=175)
    traits1=customtkinter.CTkLabel(name1_frame, text=f"Traits : {traits[sum1]} \n Planet : {planets[sum1]}",font=("SF Atarian System",18), text_color="Black")
    traits2=customtkinter.CTkLabel(name2_frame,text=f"Traits : {traits[sum2]} \n Planet : {planets[sum2]}",font=("SF Atarian System",18), text_color="Black")
    compyes=customtkinter.CTkLabel(input_area,text="You'll have a Terrible Love Life",font=("SF Atarian System",30), text_color="Black")
    if(sum2 in comp[sum1]):
        compyes.configure(text="You will be Great Love Birds")
    traits1.place(x=10, y=10)
    traits2.place(x=10, y=10)
    compyes.place(x=150, y=290)



details_button=customtkinter.CTkButton(input_area, width=100, height=50, text="Submit", fg_color="#fb6f92",
                                       corner_radius=10,command=submission, font=("SF Atarian System",40))
details_button.place(x=250, y=320)

index_window.mainloop()