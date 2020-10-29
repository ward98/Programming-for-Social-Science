# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 13:05:25 2020

@author: Cameron
"""

#imports at the top 
import random
import operator
import tkinter
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot
import matplotlib.animation
import csv
import AF
import requests
import bs4

#Random seed will mean same numbers will be generated each time code is ran
#Good to identify errors as code is developed
random.seed(1)

#Creation of agents, iterations and neighbourhoods 
#Can alter if wanted to 
num_of_age = 20
num_of_it = 100
neighbourhood = 20

#Create empty list to store agents in 
agents = []

#Create an empty list to store envrionemnt in

environment = []

#reading in the the csv envrionment file 
f = open ('in.txt', newline = '') #Opening the file
reader = csv.reader(f, quoting = csv.QUOTE_NONNUMERIC)
for row in reader:
    rowlist = [] #Making a new list 
    for value in row:
        rowlist.append(value)
    environment.append(rowlist)
f.close() #Good practice to close something if you opened it 


#Scraping X and Y data
r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})
print(td_ys)
print(td_xs)

#Initialising the graph
#Stating the size of the figure 
fig = matplotlib.pyplot.figure(figsize=(7, 7))
#Allowing axis to be added to the figure 
ax = fig.add_axes([0, 0, 1, 1])

# Making of the agents.   
for i in range(num_of_age):
    y = int(td_ys[i].text)
    x = int(td_xs[i].text)
    agents.append(AF.Agent(environment, agents, y, x))

def update(frame_number):
    fig.clear()
    matplotlib.pyplot.imshow(environment)

# Move the agents.
    for i in range(num_of_age):
            agents[i].move()
            agents[i].eat()
            agents[i].share_with_neighbours(neighbourhood)
    for i in range(num_of_age):
                matplotlib.pyplot.scatter(agents[i].x,agents[i].y, color="White",
                                          edgecolor="black")
                
    #Setting axis to the total length of the envrionment 
    matplotlib.pyplot.ylim(0,len(environment) - 1)
    matplotlib.pyplot.xlim(0,len(environment[0]) - 1)
    
    #Adding a title to the model
    matplotlib.pyplot.title("ABM- Sheep in a field")
    
    #Adding a legend to the model and placing it to the right 
    matplotlib.pyplot.legend(["Sheep"], loc = "right")
    
    #Adding axis labels
    #Envrionment is a grid so axis labels can be the same
    matplotlib.pyplot.ylabel("Field")
    matplotlib.pyplot.xlabel("Field")
    
#Running the model 
def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, interval=1,repeat = False, frames = num_of_it)
    canvas.draw() 
    
#GUI- Building the main window 
root = tkinter.Tk()
root.wm_title("ABM")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

#GUI- Adding a menu to click and then option to run the model 
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run the ABM model", command=run) 

tkinter.mainloop()