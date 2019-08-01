
# coding: utf-8

# # Exoplanets

# # The first submission had some errors regarding x and y axis.

# My final project is all about exoplanets. I will be analysing the relationship between the semi-major axis and period of orbit of exoplanets.
# 
# I used the public data of exoplanets from NASA.
# 
# What exactly are exoplanets? In our solar system, the planets orbit around the sun. The planets that orbit OTHER stars are called exoplanets. Some exoplanets may be qualifying cadidates for HZ (habitable zones).
# 
# What is the semimajor axis? Planets and stars actually orbit around their common center of mass. This common center of mass is called the barycenter. The distance from the star to the barycenter plus the distance from the barycenter to the planet makes up the semimajor axis. Our intuition tells that the longer the semimajor axis, the greater the orbit period. I will analyse it in greater details.
# 
# Below is a small animation showing the above described objects.
# 

# In[1]:


'''Importing some important libraries we will use'''
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation, rc, axes
from IPython.display import HTML
import pandas as pd


# In[2]:


'''Doing some animation of exoplanets'''
fig, ax = plt.subplots()   # plt.subplots returns two objects(both are instances of a class, in fact)
                           # The object "ax" keeps track of the axes of the plot.
                           # The object "fig" keeps track of everything else.
ax.set_xlim(( 0, 2)) # Setting the x limits
ax.set_ylim((0, 2)) # setting the y limits
ax.plot(1,1, '.') #this plots a dot at 1,1
ax.plot(1,0.75, 'go')  #go makes a green filled circle at 1,0.75
ax.plot(1,1.8, 'ro') #ro makes a red filled circle at 1,1.3
circle=plt.Circle((1, 1), 0.8, color='b', fill=False) #defining a circle with origin at 1,1 and radius 0.8 and it is not filled and is blue
circle2=plt.Circle((1, 1), 0.25, color='r', fill=False) #defining circle2 with origin at 1,1 and radius 0.25, it is also not filled and is red
ax.add_artist(circle) #plotting the circle
ax.add_artist(circle2) #plotting the smaller circle
plt.plot([1, 1], [0.8, 1.8], '--c', lw=2) #plots a dotted line from 1,0.8 to 1,1.8


# Okay so the small dot at the center is the barycenter of this system. The blue small filled circle represents the star and the red one is exoplanet. The blue big circle represents the orbit pathway of exoplanet around its star and the red small circle is the orbit of star around barycenter. And the dotted line presents the semimajor axis.

# In[3]:


exop=pd.read_csv("planetss.csv") #reading in the data from the csv file and naming it exop


# In[4]:


exo=exop.loc[0:2000,'pl_hostname':'pl_rade'] #since the data is huge, we will get a limited number of data using loc


# In[5]:


exo.columns=['HostName', 'Discovery_Method', 'No.planets', 'Period', 'Semimajor_axis', 'eccentricity', 'density',            'ra', 'dec', 'temperature', 'solar_mass', 'solar_radii', 'Earth_mass', 'earth_radius']  #renaming the columns so that it easier to understand
exo #printing the renamed table


# In[6]:


'''Plotting period vs semi-major axis for period less than 10,000 days'''
y=np.array(exo.Period) #defining the array for period values
x=np.array(exo.Semimajor_axis) #defining the array for semi-major axis
xx=x[np.where(y<10000)] #defining the period values less than 10000
yy=y[np.where(y<10000)] #defining the semimajor axis values for period less than 10000
#we would get alot of values including 'nan' values meaning they are 'not a number' or infinity 
goodind=np.where((np.isnan(xx)==False)&(np.isnan(yy)==False)) #now we are removing all the nan values from our data, we don't need them
xx=xx[goodind] #redefining xx as an array with no nan
yy=yy[goodind] #redefining yy as an array with no nan
plt.plot(xx,yy, '.') #plotting xx vs yy
plt.ylabel("Peiod(days)") #labelling the y axis
plt.xlabel("Semi-major axis(AU)") #labelling x axis


# In[7]:


'''Analyzing using first degree polynomial'''
p=np.polyfit(xx,yy,1) #defining the parameters for first degree poly
f=p[0]*xx+p[1] #fitting the parameters to data
plt.plot(xx,yy,'.') #plotting xx vs yy
plt.plot(xx,f) #plotting xx vs f on the same graph
plt.ylabel("Peiod(days)") #labelling the y axis
plt.xlabel("Semi-major axis(AU)") #labelling x axis


# * We see that this is not a very accurate fit, because there is alot of scatter above and below the line, also the linearity changes after y almost equal to thousand. I will analyze values above and below 1000 separately now.

# In[8]:


'''Plotting period vs semi-major axis for period less than 1000 days'''
y=np.array(exo.Period) #defining the array for period values
x=np.array(exo.Semimajor_axis) #defining the array for semi-major axis
xx=x[np.where(y<1000)] #defining the period values less than 1000
yy=y[np.where(y<1000)] #defining the semimajor axis values for period less than 1000
#we would get alot of values including 'nan' values meaning they are 'not a number' or infinity 
goodind=np.where((np.isnan(xx)==False)&(np.isnan(yy)==False)) #now we are removing all the nan values from our data, we don't need them
xx=xx[goodind] #redefining xx as an array with no nan
yy=yy[goodind] #redefining yy as an array with no nan
plt.plot(xx,yy, '.') #plotting xx vs yy
plt.ylabel("Peiod(days)") #labelling the y axis
plt.xlabel("Semi-major axis(AU)") #labelling x axis


# In[9]:


'''Analyzing using first degree polynomial'''
p=np.polyfit(xx,yy,1) #defining the parameters for first degree poly
f=p[0]*xx+p[1] #fitting the parameters to data
plt.plot(xx,yy,'.') #plotting xx vs yy
plt.plot(xx,f) #plotting xx vs f on the same graph
plt.ylabel("Peiod(days)") #labelling the y axis
plt.xlabel("Semi-major axis(AU)") #labelling x axis
p #it will print out the gradient and y-intercept


# * This isnt a very accurate fit because there still is a lot of scattering around the line, so i will see the residuals of this.

# In[10]:


'''Plotting residuals'''
residuals=yy-f #residuals are seimajor axis values minus fitted line values
plt.plot(xx,residuals, '.') #plotting xx against the residuals
plt.ylabel("Peiod(days)") #labelling the y axis
plt.xlabel("Semi-major axis(AU)") #labelling x axis


# * No there are alot of residuals for first degree fit, i will try 2nd degree poly fit to this data now.

# In[11]:


'''Fitting a 2nd order polynomial to our data'''
p=np.polyfit(xx,yy,2) #defining the 2nd degree polynomial parameters
f=p[0]*xx**2+p[1]*xx+p[2] #fitting the data to 2nd degree poly
plt.plot(xx,yy,'.') #plotting xx vs yy
plt.plot(xx,f,'.') #plotting xx vs f on the same graph
plt.ylabel("Peiod(days)") #labelling the y axis
plt.xlabel("Semi-major axis(AU)") #labelling x axis


# * Looks like a better fit as compared to first degree fit, let's check residuals.

# In[12]:


'''Plotting residuals'''
residuals=yy-f #residuals are seimajor axis values minus fitted line values
plt.plot(xx,residuals, '.') #plotting xx against the residuals
plt.ylabel("Peiod(days)") #labelling the y axis
plt.xlabel("Semi-major axis(AU)") #labelling x axis


# * Residuals are not as spread as before which indicates 2nd order fit is better. But lets check third degree fit, is that even better?

# In[13]:


'''Fitting a 3rd degree polynomial to the data'''
p=np.polyfit(xx,yy,3) #parameters of 3rd degree poly
f=p[0]*xx**3+p[1]*xx**2+p[2]*xx+p[3] #fitting the data 
plt.plot(xx,yy,'.') #plotting xx vs yy
plt.plot(xx,f,'.') #plotting xx vs f on the same graph
plt.ylabel("Peiod(days)") #labelling the y axis
plt.xlabel("Semi-major axis(AU)") #labelling x axis


# * This one is an even better fit because it covers most of the scatters. Lets check residuals for this one as well.

# In[14]:


'''Plotting residuals'''
residuals=yy-f #residuals are seimajor axis values minus fitted line values
plt.plot(xx,residuals, '.') #plotting xx against the residuals
plt.ylabel("Peiod(days)") #labelling the y axis
plt.xlabel("Semi-major axis(AU)") #labelling x axis


# * These residuals are less spread as before but there isn't a HUGE difference. We can still believe that 3rd fit is better than 2nd.

# So, for period less than 1000 days we see that semimajor axis and period are directly proportional. The relationship is not very linear because the gradient of the fitted lines fluctuate a little.
# 
# Now i will analyze the relationship for period more than 1000 days and less than 10000 days.

# In[15]:


'''Plotting period vs semi-major axis for period less than 10,000 days'''
y=np.array(exo.Period) #defining the array for period values
x=np.array(exo.Semimajor_axis) #defining the array for semi-major axis
xx=x[np.where((y>1000) & (y<10000))] #defining the period values less than 10000 but more than 1000
yy=y[np.where((y>1000) & (y<10000))] #defining the semimajor axis values for period less than 10000 but more than 1000
#we would get alot of values including 'nan' values meaning they are 'not a number' or infinity 
goodind=np.where((np.isnan(xx)==False)&(np.isnan(yy)==False)) #now we are removing all the nan values from our data, we don't need them
xx=xx[goodind] #redefining xx as an array with no nan
yy=yy[goodind] #redefining yy as an array with no nan
plt.plot(xx,yy, '.') #plotting xx vs yy
plt.ylabel("Peiod(days)") #labelling the y axis
plt.xlabel("Semi-major axis(AU)") #labelling x axis


# * I will first check the gradient for 1 degree polyfit to compare with the previous data, then i will just fit a 3rd degree polynomial because as we've seen it is the most accurate.

# In[16]:


p=np.polyfit(xx,yy,1) #defining the parameters for first degree poly
p #printing the gradient and y-intercept


# In[17]:


'''Fitting a 3rd degree polynomial to the data'''
p=np.polyfit(xx,yy,3) #parameters of 3rd degree poly
f=p[0]*xx**3+p[1]*xx**2+p[2]*xx+p[3] #fitting the data 
plt.plot(xx,yy,'.') #plotting xx vs yy
plt.plot(xx,f,'.') #plotting xx vs f on the same graph
plt.ylabel("Peiod(days)") #labelling the y axis
plt.xlabel("Semi-major axis(AU)") #labelling x axis


# * Wow! it looks very accurate and a nice fit. Let's check residuals for this.

# In[18]:


'''Plotting residuals'''
residuals=yy-f #residuals are seimajor axis values minus fitted line values
plt.plot(xx,residuals, '.') #plotting xx against the residuals
plt.ylabel("Peiod(days)") #labelling the y axis
plt.xlabel("Semi-major axis(AU)") #labelling x axis


# * The residuals are much less spread and are less in number indicating 3rd degree fit was a good choice.

# So the analysis of the public data of exoplanets tell us some important things to notice. The gradient for values after 1000 to 10000 is much more than values before 1000 (1083 vs 421). This means that as the semi-major axisi increases, period also increases or vice versa but after a certain period value, period increases at a greater rate as compared to before. This is interesting because it is not exactly according to my intuition, and this is a topic of curiosity as to why is the proportionality not constant.

# Referances: 
# https://exoplanetarchive.ipac.caltech.edu/exoplanetplots/#confirmed
# 
# https://exoplanetarchive.ipac.caltech.edu/docs/API_exoplanet_columns.html
# 
# https://spaceplace.nasa.gov/barycenter/en/
# 
# https://stackoverflow.com/questions/12864294/adding-an-arbitrary-line-to-a-matplotlib-plot-in-ipython-notebook
# 
# https://stackoverflow.com/questions/9215658/plot-a-circle-with-pyplot?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
# 
