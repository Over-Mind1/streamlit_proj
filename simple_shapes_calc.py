#import needed lib
import streamlit as st
st.title('shapes calc')
#needed fun    
def calc_circle(r):
    area=r*r*3.14
    perimeter=2*3.14*r
    return f'Area:{area},Perimeter:{perimeter}'

def calc_rectangle(width,hight):
    area=width*hight
    perimeter=2*(width+hight)
    return f'Area:{area},Perimeter:{perimeter}'
#boooody
option=st.selectbox('chosse shape',('circle','Rectangle'))
if option=='circle':
    r=st.number_input('Enter R of circle',min_value=0,max_value=100)
    calc_circle_btn=st.button('calc circle')
    if calc_circle_btn:
        if r <= 0:
            st.error('Please enter a positive value for the radius.')
        else:
            st.write(calc_circle(r).split(','))

elif option=='Rectangle':
    width=st.number_input('Enter width of Rectangle',min_value=0,max_value=100)
    hight=st.number_input('Enter hight of Rectangle',min_value=0,max_value=100)
    calc_rectangle_btn=st.button('calc rectangle')
    if calc_rectangle_btn:
        if width <= 0 or hight<=0:
            st.error('Please enter a positive value.')
        else:
            st.write(calc_rectangle(width,hight).split(','))            
