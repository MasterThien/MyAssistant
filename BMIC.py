        #Import necessary library
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date, datetime
import PySimpleGUI as sg
import pyttsx3

        #Variable definition & Voice, datetime initialization
robot_mouth = pyttsx3.init()
robot_mouth.setProperty("rate", 160)
today = date.today()
d1 = today.strftime("%d/%m/%Y")# Move

name,continent = "",""
diagnosis,advice= "", ""
BMI,R_BMI,height,weight,age = 0,0,0,0,0

		#My Advice#
advice_ovw ="".join(["You should be careful because being overweight means you are very easy to get obesity by putting on weight.",
                                        "\n\nAlso, you should change your diet by reducing protein and lipids or fats in the food ",
                                        "\n\nAnd eat fresh food,fish or vegetables to balance your body.",
                                        "\n\nAnd please, eat fruits and do sports or exercising instead of being lazy."
                                        "\n\nNote: If your BMI is too high, you should firstly change your diet, then do easy exercises and improve it by the time "])

advice_fh      = "".join(["Just continue your living and eating habits to control your weight and height well.", 
                                 "\n\nDoing exercises more regularly if you feel weak and your belly is bigger than before ",
                                 "\n\nAnd if you want to have a balanced health and lot's of muscles,trying some new ",
                                 " exercises online and a healthy diet is also very important;) ",
                                 "\n\n(Exception with pregnant female or elder people with diseases) "
                                         ])
advice_obs = "".join(['You should completely change your lifestyle',
                            "\n\nFor example, have a better diet that your doctor will give you, with a balance of protein, fat, water and vegetables in each meal"
                            "\n\nAnd of course, doing enough exercises every day is one of the most important things to lower your BMI. Also, you can search for exercises online or join a gym or yoga class. ",
                            "\n\nAnd with all of my sincerity, go to bed before 10 pm and wake up at 6 am in the next morning and you will have a good day, also an enough sleep ",
                            "\n\n And if you have Take all the advice above, make it your habit. And if the result is still the same, this program is too stupid and you should go to the doctor, I suppose. "
                                    ])
advice_udw = "".join(["You should eat more healthy food like fresh meats,fish or vegetables and fruits.", 
                              "\n\nDoing more exercises isn't a bad idea,fruits are perfect for you after doing excercises ",
                              "\n\nAnd don't sleep late at night,please.If you are using drugs(like cigarette,beer,wine,.etc..),stop using them too",
                              "\n\nThen you will see your body better than before", 
                              "\n\nAlso,Going to the doctor if your status looks not good (Too high or too low).They will give you some vitamins or medicines then"
                                      ])

        # Status history definition (Special) 
def Status_History():    
    r_data = pd.read_csv('Body Mass Index.csv',encoding = "utf-8-sig")
    duplicated_values = r_data[r_data['Name'] == name]
    re_bmi = duplicated_values['Your BMI']
    dates = duplicated_values['Dates']
    headers = duplicated_values
    headings = list(headers)
    values = headers.values.tolist()

    layout1 = [[sg.Table(values = values, headings = headings,
        # Set column widths for empty record of table
        auto_size_columns=False,
        col_widths=list(map(lambda x:len(x)+ 10, headings)))]]

    window = sg.Window('Your Status History', layout1, modal = True)
    choice = None
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break    

			#Define function to speak and display your status
def Speak(diagnosis = "None",advice = "None",name = "None",R_BMI = "None",age = "None",continent = "None"):
	robot_mouth.say("".join(['You are', diagnosis, "And here is some of our advice for you "]))
	robot_mouth.runAndWait() 
	sg.PopupNonBlocking("".join(["Your name : ", name, "\nYour age: " ,str(age) ,"\nFrom / Nationality: " , continent, 
		"\n....................................." ,
		"\n\nYour BMI result: " , str(R_BMI) , (" kg/m2"),
		"\n\nYour body status: " , diagnosis , "\n\nOur advice for you:\n" , advice]))


    
        
			# Initialize layout for the main window
layout= [[sg.Text(d1,font = 'font')],
        [sg.Text("Enter your name :",font = 'font')],
        [sg.Input()],   
        [sg.Text("Enter your age :",font = 'font')],
        [sg.Input()],
        [sg.Text("What continent were you born in ?:",font = 'font')],
        [sg.Input()],
        [sg.Text("Enter your weight(kg) :",font = 'font')],
        [sg.Input()],
        [sg.Text("Enter your height(m) :",font = 'font')],
        [sg.Input()],
        [sg.Button('Enter'),sg.Button('Making Plot'),sg.Button('Status History'), sg.Exit()],
        ]        
sg.theme('LightBlue4')# background color & If the GUI doesn't respose, change the theme color as this color sometimes sucks 
sg.set_options(font=("Maven Pro", 14))
window = sg.Window('Your Body Status', layout,size = (445,430))# Display command

				#Main Program
while True:
    event, values = window.Read()
    if event is None or event == 'Exit':# Shut down condition
        break
    if event == 'Enter':# Main part display
        try :
            name = values[0]#Move
            age = values[1]#Move
            continent = values[2]
            weight = values[3]
            height = values[4]                       
            BMI = float(weight)/(float(height)*float(height))  #BMI calculation 
            R_BMI = round(BMI,2)# Move

            #Diagnosis 
            if "Asia" in continent:# Asian's BMI
                if BMI < 18.5 :
                    diagnosis = "Underweight"
                    Speak(diagnosis,advice_udw,name,str(R_BMI) ,str(age) ,continent )

                if BMI < 22.9:
                    if BMI >= 18.5:
                        diagnosis = "Fit health"                        
                        Speak(diagnosis,advice_fh,name,str(R_BMI) ,str(age) ,continent )

                elif BMI <= 24.9:
                    if BMI >= 23:                   
                        diagnosis = "Overweight"
                        Speak(diagnosis,advice_ovw,name,str(R_BMI) ,str(age) ,continent )

                elif BMI <= 29.9:
                    if BMI >=25:
                        diagnosis = "Obesity first degree" 
                        Speak(diagnosis,advice_obs,name,str(R_BMI) ,str(age) ,continent )

                elif BMI <= 34.9:
                    if BMI >= 30:
                        diagnosis = "Obesity second degree"
                        Speak(diagnosis,advice_obs,name,str(R_BMI) ,str(age) ,continent )

                elif BMI >= 35:
                    diagnosis = "Obesity third degree"
                    Speak(diagnosis,advice_obs,name,str(R_BMI) ,str(age) ,continent )

            else:  # Foreigner 's BMI
                if BMI < 18.5 :
                    diagnosis = "Underweight"
                    Speak(diagnosis,advice_udw,name,str(R_BMI) ,str(age) ,continent )

                if BMI <= 24.9 :
                    if BMI >= 18.5:
                        diagnosis = "Fit health"
                        Speak(diagnosis,advice_fh ,name,str(R_BMI) ,str(age) ,continent ) 

                elif BMI <= 29.9:
                    if BMI >= 25 :                   
                        diagnosis = "Overweight"
                        Speak(diagnosis,advice_ovw,name,str(R_BMI) ,str(age) ,continent )

                elif BMI <= 34.9:
                    if BMI >= 30:
                        diagnosis = "Obesity first degree" 
                        Speak(diagnosis,advice_obs,name,str(R_BMI) ,str(age) ,continent )

                elif BMI <= 39.9:
                    if BMI >= 35:
                        diagnosis = "Obesity second degree"
                        Speak(diagnosis,advice_obs,name,str(R_BMI) ,str(age) ,continent )

                elif BMI >= 40:
                    diagnosis = "Obesity third degree"
                    Speak(diagnosis,advice_obs,name,str(R_BMI) ,str(age) ,continent )


            df = pd.DataFrame([[name,age,R_BMI,diagnosis,d1]])
            df.to_csv('Body Mass Index.csv',mode = 'a',index = False,
                        encoding = "utf-8-sig",header = ['Name','Age','Your BMI','Status','Dates'])        
        except:
            pass
        # Making plot process   
    elif event == 'Making Plot':    
        name = values[0]
        r_data = pd.read_csv('Body Mass Index.csv',encoding = "utf-8-sig")
        duplicated_values = r_data[r_data['Name'] == name]
        re_bmi = duplicated_values['Your BMI']
        dates = duplicated_values['Dates']
        x = dates
        y = re_bmi
        plt.plot(x,y)
        plt.title('Your BMI plot') 
        plt.xlabel('Dates')
        plt.ylabel('Your BMI values')
        plt.grid(axis = 'y')
        plt.show()
    elif event == 'Status History':  # Status History display 
        name = values[0]       
        Status_History()

                    #End of Programme    
window.close()
