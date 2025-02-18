import flet as ft
import sympy
from sympy import *


def main(page: ft.Page):

   #imagen de la unam 
   unamImg = ft.Image(
      src=f"src/icon.png",
      width=100,
      height=100,
      fit= ft.ImageFit.FILL
   )
   #define la variable que guardara el resultado en todo el programa 
   r = "not a number"
   def divisionSintetica(x0,forma):
      x,y,z = symbols("x y z")

      dxdy = diff(forma)
      r = x0 - (forma.subs(x,x0)/dxdy.subs(x,x0))
      if(int(forma.subs(x,r) != 0)):
         divisionSintetica(r,forma)
      else:
         page.add(ft.Text(str(r)))

   
   #funcion para calcular la ecuacion dentro de los rangos establecidos
   def calculate(e):
      x,y,z = symbols("x y z")
      form =  formula.value
      form = sympify(form)
      #inicia el buble con el cual se sustituiran las incognitas en rango de valores dado
      primerVal = form.subs(x, int(de1.value))

      for i in range(int(de1.value),int(del2.value)):
         if(primerVal == 0):
            divisionSintetica(primerVal,form)
         if(int(form.subs(x,i)) == 0):
            page.add(ft.Text(str(i)))
         if((primerVal < 0) and int(form.subs(x,i)) > 0 ):
            #code here
            x= ((i-1) + i)/2
            divisionSintetica(x,form)
         if((primerVal > 0) and int(form.subs(x,i)) < 0 ):
            #codehere
             x= ((i-1) + i)/2
             divisionSintetica(x,form)



   page.add(unamImg)
   formula = ft.TextField(label="formula")
   de = ft.Text("de")
   de1 = ft.TextField(label="primer rango")#entrada primer rango 
   del2 = ft.TextField(label="segundo rango")#entrada segundo rango 
   a = ft.Text("a")
   button = ft.ElevatedButton(text="calcular",on_click=calculate)
   anim = ft.AnimatedSwitcher
   row = ft.Row([formula,de,de1,a,del2,button])
   
   page.add(row)
   page.add(
        ft.Container(
            image_src='https://images.pexels.com/photos/259915/pexels-photo-259915.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1',
            image_fit=ft.ImageFit.COVER,
            expand=True,
        )
    )
   
   page.update()


ft.app(main)
