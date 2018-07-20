#Variable Length Arguments Functions

def Register(name,gender,age,*qual):
        print("Name : " + name)
        print("Gender : " + gender)
        print("Age : " + str(age))
        print("Qualification : ")
        print(qual)

Register("Ankit","Male",23,"10th","12th","BCA")
