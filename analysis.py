import json
import numpy as np
import matplotlib.pyplot as plt
import plotly.plotly as py
data= open('D://mchine learning bvp//ina_singhal//titanic_data.json',"r")
mydata=json.loads(data.readline())
#print(mydata)
d=dict()
l=list()
l1=list()
l3=list()
for i in range(len(mydata)):
	try:
		b=mydata[i]['Age']
		s=int(mydata[i]['Survived'])
		if s==0 and b!='':

			
			l.append(int(b))
	except ValueError:
		continue
l.sort()
print(l)
plt.title('titanic data for survived')
plt.hist(l,bins=200)
plt.show()


#1. BOARDED

male_bd=list()
female_bd=list()
count1=0
count2=0
for i in range(len(mydata)):
	try:
		a=mydata[i]['Sex']
		if (a=="male"):
			count1+=1
			male_bd.append(a)
		else:
			count2+=1
			female_bd.append(a)
	except:
		continue
print(male_bd)
print('\n'female_bd)
plt.pie((count1,count2),labels=('male','female'),autopct='%1.1f%%')
plt.title('titanic_data for boarded')
plt.axis('equal')
plt.tight_layout()
plt.show()


#2.NOT SURVIVED
male_NS=list()
female_NS=list()
c1=0
c2=0
for i in range(len(mydata)):
	try:
		a=int(mydata[i]['Survived'])
		b=mydata[i]['Sex']
		if(a==0) and (b=="male"):
			male_NS.append(b)
			c1+=1
		elif (a==0) and (b=="female"):
			female_NS.append(b)
			c2+=1
	except:
		continue
print(male_NS)
print('\n')
print(female_NS)
plt.pie((c1,c2),labels=('male','female'),autopct='%1.1f%%')
plt.title('titanic_data for people who did not survived')
plt.axis('equal')
plt.tight_layout()
plt.show()
plt.hist(male_NS,bins=200)
plt.hist(female_NS,bins=200)
plt.show()



#3.
c1=0
c2=1
l=list()
l1=list()
male_fare=list()
female_fare=list()
male_age=list()
female_age=list()
for i in range(len(mydata)):
	try:
		a=mydata[i]['Fare']
		b=mydata[i]['Age']
		c=mydata[i]['Sex']
		l.append(a)
		l1.append(b)

		if(c=="male"):
			male_fare.append(a)
			male_age.append(b)
		else:
			female_fare.append(a)
			female_age.append(b)
	except:
		continue
print(male_fare,'\n')
print(female_fare,'\n')
print(male_age,'\n')
print(female_age,'\n')
for j in range(len(male_fare)):
	j=j+1
print(j)
for w in range(len(female_fare)):
	w=w+1
print(w)
for s in range(len(male_age)):
	s=s+1
print(s)
for k in range(len(female_age)):
	k=k+1
print(k)
plt.pie((j,w),labels=('male','female'),autopct='%1.1f%%')
plt.title('titanic_data for fare')
plt.axis('equal')
plt.tight_layout()
plt.show()

plt.pie((s,k),labels=('male','female'),autopct='%1.1f%%')
plt.title('titanic_data for Age')
plt.axis('equal')
plt.tight_layout()
plt.show()



#4.

l=list()
l1=list()
l3=list()
for i in range(len(mydata)):
	try:
		b=mydata[i]['Age']
		s=int(mydata[i]['Survived'])
		if s==0 and b!='':
			l.append(int(b))
	except ValueError:
		continue
l.sort()
print(l)
plt.hist(l,bins=200)
plt.show()


#5.

l4=list()
for i in range(len(mydata)):
	try:
		b=float(mydata[i]['Fare'])
		s=int(mydata[i]['Survived'])
		if s==0 :
			l4.append(b)
	except ValueError:
		continue
l4.sort()
print(l4)
plt.hist(l4,bins=10)
plt.show()


#6.
l5=list()
for i in range(len(mydata)):
	try:
		b=mydata[i]['Pclass']
		s=int(mydata[i]['Survived'])
		if s==0 :
			l5.append(b)
	except ValueError:
		continue
l5.sort()
print(l5)
plt.hist(l5,bins=10)
plt.show()



#7.

l6=list()
l7=list()
for i in range(len(mydata)):
	try:
		b=mydata[i]['Sex']
		s=int(mydata[i]['Survived'])
		if (s==0)  and (b=="male"):
			l6.append(b)
		elif (s==0) and (b=="female"):
			l7.append(b)
	except ValueError:
		continue
rint(l6)
print(l7)
plt.hist(l6,bins=10)
plt.hist(l7,bins=10)
plt.show()


#8.

l8=list()
for i in range(len(mydata)):
	try:
		b=mydata[i]['Cabin']
		s=int(mydata[i]['Survived'])
		if (s==0) and (b!=''):
			l8.append(b)
	except ValueError:
		continue
print(l8)
plt.hist(l8,bins=100)
plt.show()



#9.
l9=list()
for i in range(len(mydata)):
	try:
		b=float(mydata[i]['Fare'])
		l9.append(b)
	except:
		continue
print(l9)
plt.hist(l9,bins=10)
plt.show()