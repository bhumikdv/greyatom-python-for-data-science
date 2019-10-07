# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Code starts here
data = np.genfromtxt(path, delimiter = ',', skip_header=1)
print(data)
census = np.concatenate((data, new_record), axis=0)
print(census)


# --------------
#Code starts here
age = census[:,[0]]
max_age = age.max() 
min_age = age.min()
age_mean = round(age.mean(),2)
age_std = round(np.std(age),2)

print(age,max_age,min_age,age_mean,age_std)


# --------------
#Code starts here
race_0 = census[census[:,2]==0]
race_1 = census[census[:,2]==1]
race_2 = census[census[:,2]==2]
race_3 = census[census[:,2]==3]
race_4 = census[census[:,2]==4]
#print(race_0,race_1,race_2,race_3,race_4)

len_0 = len(race_0)
len_1 = len(race_1)
len_2 = len(race_2)
len_3 = len(race_3)
len_4 = len(race_4)
print(len_0,len_1,len_2,len_3,len_4)

minority_race = [len_0,len_1,len_2,len_3,len_4].index(min([len_0,len_1,len_2,len_3,len_4]))
print(minority_race)


# --------------
#Code starts here
senior_citizens = census[census[:,0]>60]
working_hours_sum = senior_citizens[:,6].sum()
senior_citizens_len = len(senior_citizens)
avg_working_hours = working_hours_sum/senior_citizens_len
print(avg_working_hours)


# --------------
#Code starts here
high = census[census[:,1]>10]
low = census[census[:,1]<=10]

avg_pay_high = high[:,7].mean()
avg_pay_low = low[:,7].mean()

if avg_pay_high>avg_pay_low:
    print("better education leads to better pay")
else:
    print("better education doesn't leads to better pay")


