import flet as ft
import sympy
from sympy import *


def main(page: ft.Page):
   unamImg = ft.Image(
      src=f"src/icon.png",
      width=100,
      height=100,
      fit= ft.ImageFit.FILL
   )
   
   #funcion para calcular la ecuacion dentro de los rangos establecidos
   def calculate(e):
      x,y,z = symbols("x y z")
      form =  formula.value
      form = sympify(form)
      #inicia el buble con el cual se sustituiran las incognitas en rango de valores dado
      for i in range(int(de1.value),int(del2.value)):
         page.add(ft.Text(str(form.subs(x,i))))


   page.add(unamImg)
   formula = ft.TextField(label="formula")
   de = ft.Text("de")
   de1 = ft.TextField(label="primer rango")#entrada primer rango 
   del2 = ft.TextField(label="segundo rango")#entrada segundo rango 
   a = ft.Text("a")
   button = ft.ElevatedButton(text="calcular",on_click=calculate)
   row = ft.Row([formula,de,de1,a,del2,button])
   
   page.add(row)
   page.update()


ft.app(main)
