from tkinter import *
from tkinter.ttk import *
from ball import Ball
import variable
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)
import ppmodel

HEIGHT = variable.Y_LIMIT/10
WIDTH = variable.X_LIMIT/10
fig = Figure()
plot1 = fig.add_subplot()
window = Tk()
frame = Frame(window)
canvas = Canvas(window, width = WIDTH, height = HEIGHT, bg = "white")
graph = FigureCanvasTkAgg(fig, master = window)
window.title("Virus Simulation")
toolbar = NavigationToolbar2Tk(graph,frame)

def start_ui():
    window.geometry(str(int(WIDTH)*2)+"x"+str(int(HEIGHT)+50))
    frame.pack(side=BOTTOM)
    graph.get_tk_widget().pack(side='right',anchor='nw',expand=True,fill='both')
    canvas.pack(side='left',anchor='nw', expand = True, fill = 'both')
    toolbar.update()
    
def ui_redraw(person,day):
    if(person.status==variable.disease_status.VULNERABLE):
        if(person.masked and person.vaccinated):
            color="#00008b"
        elif(person.masked):
            color="#ADD8E6"
        elif(person.vaccinated):
            color="#4d4dff"
        else:
            color="white"
    if(person.status==variable.disease_status.INCUBATION):
        color="yellow"
    if(person.status==variable.disease_status.ASYMPTOMATIC):
        color="orange"
    if(person.status==variable.disease_status.SYMPTOMATIC):
        color="red"
    if(person.status==variable.disease_status.IMMUNE):
        color="green"
    if(person.status==variable.disease_status.DEAD):
        color="black"
    Ball(canvas,person.location.getX()/10,person.location.getY()/10,5,color)
    canvas.create_text(55, 20, text="Day "+str(day), fill="black", font=('Helvetica 24'))
    
def draw_popularPlace():
    for place in ppmodel.popularPlaces:
        Ball(canvas, place.getX()/10, place.getY()/10, 10, 'pink')

def ui_refresh():
    window.update()

def ui_delete():
    canvas.delete("all")
    
def print_graph(hours_past,max_infected_at_once,vulnerable_history,incubation_history,asymptomatic_history,symptomatic_history,infected_history,immune_history,dead_history):
    plot1.clear()
    plot1.set_xlim([0,hours_past])
    plot1.set_ylim([0,1000])
    plot1.set_xlabel("Hours #")
    plot1.set_ylabel("Population #")
    plot1.axhline(y=max_infected_at_once,color="red",linestyle="--",label="Max Infection")
    plot1.plot(vulnerable_history,label="Vulnerable #",lw=3,color='blue')
    plot1.plot(incubation_history,label="Incubation #",color="yellow")
    plot1.plot(asymptomatic_history,label="Asymptomatic #",color="orange")
    plot1.plot(symptomatic_history,label="Sysptomatic #",color="red")
    plot1.plot(infected_history,label="Total Infected #",lw=3,color="purple")
    plot1.plot(immune_history,label="Immune #",lw=3,color="green")
    plot1.plot(dead_history,label="Dead #",color="black")
    plot1.legend(loc='lower center', bbox_to_anchor=(0.5, 1), ncol=3, fancybox=True, shadow=True)
    graph.draw()
    
def end():
    window.mainloop()