# Calculate the mean and standard deviation of the following list:
# Numbers = [1,2,3,5,88,99,55,33,41,52]
import math
Numbers = [1, 2, 3, 5, 88, 99, 55, 33, 41, 52]
total=sum(Numbers)
mean=total/len(Numbers)         #for mean
print('The mean is %.2f'%mean)
#  for standard deviation
count=0
for a in Numbers:
        a=pow(a,2)
        Numbers.insert(count,a)    
        Numbers.pop(count+1)
        count+=1
total1=(sum(Numbers)/10)-pow(mean,2)
standard_deviation=math.sqrt(total1) 
print('The standard deviation is:{:.2f}'.format(standard_deviation))
