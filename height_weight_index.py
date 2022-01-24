from datetime import date
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

class person:
    def __init__(self,name,surname,birthDay,height,weight,gender):
        self.name = name
        self.surname = surname
        self.birthDay = birthDay
        self.height = height
        self.weight = weight
        self.gender = gender
        Birthdate = birthDay.split("/")
        today = date.today()
        self.age = today.year - int(Birthdate[0]) - ((today.month,today.day)< (int(Birthdate[1]),int(Birthdate[2])))

        if gender == "e":
            self.gender_name = "Mr"

        else:
            self.gender_name = "Lady"

    def calculate_height_weight_index(self):
        self.square_height = self.height**2
        self.height_weight_index = round((self.weight / self.square_height),2)

    def show_body_index(self):
        print(f"{self.name}  {self.surname}, {self.age} age old {self.gender_name}, your body weight index: {self.height_weight_index}")

    
    def monthly_weiht_index(self,month_weight):
        self.weight = month_weight
        self.calculate_height_weight_index()

    def general_information(self):
        weekly_info = []
        weekly_index=[]
        daily_weight_index = []
        while True:
            counter = int(input("How many weeks of weight information do you want to enter?(min 8 weeks):"))
            if counter >= 8 :
                break

        weekly_info.append(self.weight)    
        i = 1
        while i<= counter:
            weekly_info.append(int(input(f"{i}. week weight information: ")))
            i+=1

        for j in weekly_info:
            weekly_index.append(round((j/self.square_height),2))
        

        week_counter =[]
        k = 1
        while k <=len(weekly_index):
            week_counter.append(f"{k}. week")
            k +=1
        
        index_array = np.array(weekly_index)
        week_array = np.array(week_counter)
        week_array_weightss = np.array(weekly_info[1:])
        week_array_weig = np.array(week_counter[:(len(week_counter)-1)])



                # all information entered week by week
        weightgraphdatas = {"Kilo" : week_array_weightss , "week":week_array_weig}
        pdgraph = pd.DataFrame(weightgraphdatas)
        sns.set(style="darkgrid")
        sns.lineplot(y="Kilo",x="week",data=pdgraph)
        plt.show()


                # weekly index information
        d = {"height weight index" : index_array , "week":week_array}
        pdgraph = pd.DataFrame(d)
        sns.set(style="darkgrid")
        sns.lineplot(y="height weight index",x="week",data=pdgraph)
        plt.show()

        m = 0
        while m+1 < len(weekly_info):
            gap = weekly_info[m+1]-weekly_info[m]
            n=1
            while n<=7:
                daily_weight_index.append(round((gap/7),2))
                n+=1
            m+=1

        day_counter = []

        g = 1
        while g<= len(daily_weight_index):
            day_counter.append(f"{g}.")
            g+=1

        index_array_weight = np.array(daily_weight_index)
        day_array = np.array(day_counter)
                
                # daily weight gain/loss information
        xdxd = {"weightGap" : index_array_weight , "day":day_array}
        pdgraphwght = pd.DataFrame(xdxd)
        sns.set(style="darkgrid")
        sns.lineplot(y="weightGap",x="day",data=pdgraphwght)
        plt.show()


#please enter your information before use
p1 = person("Adem","Koçdoğan","2002/10/15",1.65,57,"e")                 #please enter your information before use
p1.calculate_height_weight_index()
p1.show_body_index()
p1.monthly_weiht_index(50)
p1.show_body_index()
p1.general_information()
