## b==1,b==2 ##
Test_Name=[]
Test_Price=[]
Test_Room=[]
Test_Conductor=[]

## b==3,b==4 ##
Doctor_Name=[]
Specialization=[]
Timing=[]
Venue=[]
Availability_Days=[]

## b==5 ##
Patient_Name=[]
Patient_Age=[]
patient_Gender=[]
Patient_Address=[]
Patient_Date=[]
Patient_Disease=[]


## b==7 ##
Appointments=[]
Appointments_Timings=[]


def menu():
    print("\t\t\t\t  Welcome")
    print("\t\t\tAK Hospital Management System\n\n")

    print("\t\tMenu\n")

    print("Press 1 to Add Test Information")
    print("Press 2 to Delete Test Information")
    print("Press 3 to Add Doctor Information")
    print("Press 4 to Delete Doctor Information")
    print("Press 5 to Add Patient Information")
    print("Press 6 to Add Test Record To Patient")
    print("Press 7 to Add Appointment")
    print("Press 8 to Exit")

    print("\n")

    print("Press 11 to Display Available Tests")
    print("Press 22 to Display Specific Test Details")
    print("Press 33 to Display Available Doctors")
    print("Press 44 to Display Specific Doctor Details")
    print("Press 55 to Display Patient LIST")
    print("Press 66 to Display Specific Patient Details")
    print("Press 77 to Display Appointments of a Doctors")
    print("Press 88 to Display Patient Test Record")

    print("\n")

    print("Press 10 to Save Whole Record")

    print("\n")
    
    print("Press 0 to Show Menu Again")


def Add_Test_Information():
    Test_Name.append(input("Enter Test Name = "))
    Test_Price.append(input("Enter Test Price = "))
    Test_Room.append(input("Enter Test Room No = "))
    Test_Conductor.append(input("Enter Test Conductor Name = "))


def Del_Test_Information():
    x = Test_Name.index(input("Enter Test Name That You Want To Delete = "))
        
    Test_Name.pop(x)
    Test_Price.pop(x)
    Test_Room.pop(x)
    Test_Conductor.pop(x)


def Add_Doc_Information():
    Doctor_Name.append(input("Enter Doctor Name = "))
    Specialization.append(input("Enter Dr. Specialization = "))
        
    Timing.append(input("Enter Doctor Timings = "))

    Venue.append(input("Enter Venue Of Sitting Of Doctor = "))
    Availability_Days.append(input("Enter Availability Days = "))


def Del_Doc_Information():
    x = Doctor_Name.index(input("Enter Doctor Name Whose Record u want to Change = "))
        
    Doctor_Name.pop(x)
    Specialization.pop(x)
    Timing.pop(x)
    Venue.pop(x)
    Availability_Days.pop(x)


def Add_Patient_Information():
    Patient_Name.append([input("Enter Patient Name = ")])
    Patient_Age.append(input("Enter Patient Age = "))
    patient_Gender.append(input("Enter Paient Gender = "))
    Patient_Address.append(input("Enter Patient Address = "))
    Patient_Date.append(input("Enter Patient Date = "))
    Patient_Disease.append(input("Enter Patient Disease = "))


def Add_Test_Record():
    
    n =(input("Enter Patient Name = "))
    x=0
    z = len(Patient_Name)
    while(x<z):
        if(Patient_Name[x][0]==n):
            y=x
            Patient_Name[y].append((input("Enter Test Name = ")))
            Patient_Name[y].append((input("Enter Test Price = ")))
        x=x+1


def Add_Appointment():
    Appointments.append([(input("Enter Doctor Name = ")),(input("Enter Patient Name = "))])
    z = len(Appointments)
    y = Doctor_Name.index(Appointments[z-1][0])
    print("Doctor Availability Days = ",Availability_Days[y])
    print("Doctor Sitting Timings = ",Timing[y])
    Appointments_Timings.append(input("Enter Appointments Timings = "))
        


def Display_Available_Tests():
    z = len(Test_Name)
    n=0
    while(n<z):
        print("Test Name = ",Test_Name[n])
        n=n+1


def Display_Specific_Test_Details():
    y = Test_Name.index(input("Enter Test Name = "))
    print("Test Name = ",Test_Name[y])
    print("Test Price = ",Test_Price[y])
    print("Test Room No = ",Test_Room[y])
    print("Test Conductor = ",Test_Conductor[y])
    print("\n")


def Display_Available_Doctors():
    z = len(Doctor_Name)
    n=0
    while(n<z):
        print("Doctor Name = ",Doctor_Name[n])
        print("Specialization In = ",Specialization[n])
        print("\n")
        n=n+1

def Display_Specific_Doctor_Details():
    y = Doctor_Name.index(input("Enter Doctor Name = "))
    print("Doctor Name = ",Doctor_Name[y])
    print("Specialization In = ",Specialization[y])
    print("Timings = ",Timing[y])
    print("Venue of Doctor = ",Venue[y])
    print("Availability Days = ",Availability_Days[y])
    print("\n")


def Display_Patient_List():
    z = len(Patient_Name)
    n=0
    while(n<z):
        print("Patient Name = ",Patient_Name[n][0])
        n=n+1

def Display_Specific_Patient_Details():
    n =(input("Enter Patient Name = "))
    x=0
    z = len(Patient_Name)
    while(x<z):
        if(Patient_Name[x][0]==n):
            y=x
            print("Patient Name = ",Patient_Name[y][0])
            print("Patient Age = ",Patient_Age[y])
            print("patient Gender = ",patient_Gender[y])
            print("Patient Address = ",Patient_Address[y])
            print("Patient Date of Visit = ",Patient_Date[y])
            print("Patient Disease = ",Patient_Disease[y])
            print("\n")
        x=x+1


def Display_Appointments_of_Docter():
    x=input("Enter Doctor Name = ")
    y = Doctor_Name.index(x)  
    z = len(Appointments)
    n=0
    print("Patient Names \t Timing")
    while(n<z):
        if(Appointments[n][0]==x):
            print(Appointments[n][1],end="")
            print("\t\t",Appointments_Timings[n])
        n=n+1


def Display_Patient_Test_Record():
    n =(input("Enter Patient Name whose Test Records u Want to Display = "))
    x=0
    z = len(Patient_Name)
    while(x<z):
        if(Patient_Name[x][0]==n):
            y=x
            a=1
            b=2
            c= len(Patient_Name[y])
            while(b<c):
                print("Test Name = ",Patient_Name[y][a])
                print("Test Price = ",Patient_Name[y][b])
                a=a+2
                b=b+2
                
        x=x+1


#######################################################################################################################################################################

def write0():
    Test_Name1=open("Test_Name.txt","w+")
    n=0
    z=len(Test_Name)
    while(n<z):
        Test_Name1.write(Test_Name[n])
        Test_Name1.write("\n")
        n=n+1
    Test_Name1.close()

    Test_Price1=open("Test_Price.txt","w+")
    n=0
    z=len(Test_Price)
    while(n<z):
        Test_Price1.write(Test_Price[n])
        Test_Price1.write("\n")
        n=n+1
    Test_Price1.close()

    Test_Room1=open("Test_Room.txt","w+")
    n=0
    z=len(Test_Room)
    while(n<z):
        Test_Room1.write(Test_Room[n])
        Test_Room1.write("\n")
        n=n+1
    Test_Room1.close()

    Test_Conductor1=open("Test_Conductor.txt","w+")
    n=0
    z=len(Test_Conductor)
    while(n<z):
        Test_Conductor1.write(Test_Conductor[n])
        Test_Conductor1.write("\n")
        n=n+1
    Test_Conductor1.close()


    Doctor_Name1=open("Doctor_Name.txt","w+")
    n=0
    z=len(Doctor_Name)
    while(n<z):
        Doctor_Name1.write(Doctor_Name[n])
        Doctor_Name1.write("\n")
        n=n+1
    Doctor_Name1.close()

    Specialization1=open("Specialization.txt","w+")
    n=0
    z=len(Specialization)
    while(n<z):
        Specialization1.write(Specialization[n])
        Specialization1.write("\n")
        n=n+1
    Specialization1.close()

    Timing1=open("Timing.txt","w+")
    n=0
    z=len(Timing)
    while(n<z):
        Timing1.write(Timing[n])
        Timing1.write("\n")
        n=n+1
    Timing1.close()

    Venue1=open("Venue.txt","w+")
    n=0
    z=len(Venue)
    while(n<z):
        Venue1.write(Venue[n])
        Venue1.write("\n")
        n=n+1
    Venue1.close()

    Availability_Days1=open("Availability_Days.txt","w+")
    n=0
    z=len(Availability_Days)
    while(n<z):
        Availability_Days1.write(Availability_Days[n])
        Availability_Days1.write("\n")
        n=n+1
    Availability_Days1.close()


    Patient_Name1=open("Patient_Name.txt","w+")
    n=0
    z=len(Patient_Name)
    while(n<z):
        Patient_Name1.write(Patient_Name[n][0])
        Patient_Name1.write("\n")
        n=n+1
    Patient_Name1.close()

    Patient_Age1=open("Patient_Age.txt","w+")
    n=0
    z=len(Patient_Age)
    while(n<z):
        Patient_Age1.write(Patient_Age[n])
        Patient_Age1.write("\n")
        n=n+1
    Patient_Age1.close()

    patient_Gender1=open("patient_Gender.txt","w+")
    n=0
    z=len(patient_Gender)
    while(n<z):
        patient_Gender1.write(patient_Gender[n])
        patient_Gender1.write("\n")
        n=n+1
    patient_Gender1.close()

    Patient_Address1=open("Patient_Address.txt","w+")
    n=0
    z=len(Patient_Address)
    while(n<z):
        Patient_Address1.write(Patient_Address[n])
        Patient_Address1.write("\n")
        n=n+1
    Patient_Address1.close()

    Patient_Date1=open("Patient_Date.txt","w+")
    n=0
    z=len(Patient_Date)
    while(n<z):
        Patient_Date1.write(Patient_Date[n])
        Patient_Date1.write("\n")
        n=n+1
    Patient_Date1.close()

    Patient_Disease1=open("Patient_Disease.txt","w+")
    n=0
    z=len(Patient_Disease)
    while(n<z):
        Patient_Disease1.write(Patient_Disease[n])
        Patient_Disease1.write("\n")
        n=n+1
    Patient_Disease1.close()


#######################################################################################################################################################################


Test_Name1=open("Test_Name.txt","r")
Test_Name=Test_Name1.readlines()
n=0
while(n<len(Test_Name)):
    if("\n" in Test_Name[n]):
        Test_Name[n]=Test_Name[n].replace("\n","")
        n=n+1
Test_Name1.close()


Test_Price1=open("Test_Price.txt","r")
Test_Price=Test_Price1.readlines()
n=0
while(n<len(Test_Price)):
    if("\n" in Test_Price[n]):
        Test_Price[n]=Test_Price[n].replace("\n","")
        n=n+1
Test_Price1.close()

Test_Room1=open("Test_Room.txt","r")
Test_Room=Test_Room1.readlines()
n=0
while(n<len(Test_Room)):
    if("\n" in Test_Room[n]):
        Test_Room[n]=Test_Room[n].replace("\n","")
        n=n+1
Test_Room1.close()

Test_Conductor1=open("Test_Conductor.txt","r")
Test_Conductor=Test_Conductor1.readlines()
n=0
while(n<len(Test_Conductor)):
    if("\n" in Test_Conductor[n]):
        Test_Conductor[n]=Test_Conductor[n].replace("\n","")
        n=n+1
Test_Conductor1.close()


Doctor_Name1=open("Doctor_Name.txt","r")
Doctor_Name=Doctor_Name1.readlines()
n=0
while(n<len(Doctor_Name)):
    if("\n" in Doctor_Name[n]):
        Doctor_Name[n]=Doctor_Name[n].replace("\n","")
        n=n+1
Doctor_Name1.close()

Specialization1=open("Specialization.txt","r")
Specialization=Specialization1.readlines()
n=0
while(n<len(Specialization)):
    if("\n" in Specialization[n]):
        Specialization[n]=Specialization[n].replace("\n","")
        n=n+1
Specialization1.close()

Timing1=open("Timing.txt","r")
Timing=Timing1.readlines()
n=0
while(n<len(Timing)):
    if("\n" in Timing[n]):
        Timing[n]=Timing[n].replace("\n","")
        n=n+1
Timing1.close()

Venue1=open("Venue.txt","r")
Venue=Venue1.readlines()
n=0
while(n<len(Venue)):
    if("\n" in Venue[n]):
        Venue[n]=Venue[n].replace("\n","")
        n=n+1
Venue1.close()

Availability_Days1=open("Availability_Days.txt","r")
Availability_Days=Availability_Days1.readlines()
n=0
while(n<len(Availability_Days)):
    if("\n" in Availability_Days[n]):
        Availability_Days[n]=Availability_Days[n].replace("\n","")
        n=n+1
Availability_Days1.close()


######################################################################################################################################################################

        

menu()

b=input("\nEnter Your Option = ")
print("\n")

while(b!="8"):

    if(b=="0"):
        menu()
    
    elif(b=="1"):
        Add_Test_Information()      

    elif(b=="2"):
        Del_Test_Information()

    elif(b=="3"):
        Add_Doc_Information()

    elif(b=="4"):
        Del_Doc_Information()
       
    elif(b=="5"):
        Add_Patient_Information()
        
    elif(b=="6"):
        Add_Test_Record()

    elif(b=="7"):
        Add_Appointment()

    elif(b=="11"):
        Display_Available_Tests()

    elif(b=="22"):
        Display_Specific_Test_Details()

    elif(b=="33"):
        Display_Available_Doctors()
        
    elif(b=="44"):
        Display_Specific_Doctor_Details()

    elif(b=="55"):
        Display_Patient_List()
        
    elif(b=="66"):
        Display_Specific_Patient_Details()
        
    elif(b=="77"):
        Display_Appointments_of_Docter()
        
    elif(b=="88"):
        Display_Patient_Test_Record()

    elif(b=="10"):
        write0()

    else:
        print("Wrong Option")
        print("Enter Correct Option")
        
           
    b=input("\nEnter Your Option = " )
    print("\n")

write0()


#######################################################################################################################################################################






    


















    
