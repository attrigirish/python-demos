from tkinter import *

root=Tk()

#Tkinter Customization

#Setting Window State
root.state('zoomed')
#Setting Font Seetings
root.option_add("*Foreground","blue")
root.option_add("*Label.Font", ("Calibri", "16", "bold"))


#Name
lblName=Label(root,text="Name",width=40)
txtName=Entry(root,width=40)
#
lblName.grid(row=0,column=0)
txtName.grid(row=0,column=1)


#Gender
lblGender=Label(root,text="Gender",width=40)
frameGender=Frame(root)
rbnMale=Radiobutton(frameGender, text="Male",variable="gender",value="Male")
rbnFemale=Radiobutton(frameGender, text="Female",variable="gender",value="Female")
#
rbnMale.grid(row=0,column=0)
rbnFemale.grid(row=0,column=1)
#
lblGender.grid(row=1,column=0)
frameGender.grid(row=1,column=1)

#City
lblCity=Label(root,text="City",width=40)
cv=StringVar(root)
cities=("New Delhi","Chennai","Kolkata") 
opCities=OptionMenu(root,cv,*cities)
#
lblCity.grid(row=2,column=0)
opCities.grid(row=2,column=1)

#Pref
lblPref=Label(root,text="Preference",width=40)
framePref=Frame(root)
cbxEnglish=Checkbutton(framePref, text="Hindi")
cbxHindi=Checkbutton(framePref, text="English")
#
cbxEnglish.grid(row=0,column=0)
cbxHindi.grid(row=0,column=1)
#
lblPref.grid(row=3,column=0)
framePref.grid(row=3,column=1)


#Bio
lblBio=Label(root,text="Bio",width=40)
txtBio=Text(root,height=5,width=30)
#
lblBio.grid(row=4,column=0)
txtBio.grid(row=4,column=1)










