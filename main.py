'''
Pi-Py-Pi: Cylon/Pepper's Ghost Edition
Calculating Pi in Python on Raspberry Pi 2040

Copyright (c) 2024:
Cristiano Monteiro - cristianomonteiro@gmail.com

MIT License

gospers_pi() function from:
https://www.gavalas.dev/blog/spigot-algorithms-for-pi-in-python/
by Konstantinos Gavalas

'''

from melopero_cookie import Cookie_RP2040
import time
import machine
import utime
import _thread

sLock = _thread.allocate_lock()

#create a new cookie_rp2040 object
cookie=Cookie_RP2040()
cookie.clear_screen()
cookie.led_init()
cylon = [1,0,0,0,0]

number_zero = [5,6,7,8,9,10,14,15,19,20,21,22,23,24]
number_one = [9,10,11,12,13,14,15,19,24]
number_two = [5,6,7,9,10,12,14,15,17,19,20,22,23,24]
number_three = [5,6,7,8,9,10,12,14,15,17,19,20,24]
number_four = [5,6,7,8,9,12,17,20,21,22]
number_five = [5,7,8,9,10,12,14,15,17,19,20,21,22,24]
number_six = [5,7,8,9,10,12,14,15,17,19,20,21,22,23,24]
number_seven = [5,6,7,8,9,10,15,20]
number_eight = [5,6,7,8,9,10,12,14,15,17,19,20,21,22,23,24]
number_nine = [5,6,7,8,9,10,12,14,15,17,19,20,21,22,24]
decimal_point = [8,9,13,14]

dir = 0

def draw_char(a):
    cookie.clear_screen()
    for y in range(len(a)):
        cookie.set_pixel(a[y],0,240,33,0.2)
        #utime.sleep(1)
    cookie.show_pixels()

def gospers_pi():
    q,r,t,n,i = 1,0,1,8,1
    while True:
        if n == (q*(675*i-216)+125*r)//(125*t):
            yield n
            q,r = 10*q,10*r-10*n*t
        else:
            q,r,t,i = i*(2*i-1)*q,3*(3*i+1)*(3*i+2)*((5*i-2)*q+r),3*(3*i+1)*(3*i+2)*t,i+1
        n = (q*(27*i-12)+5*r) // (5*t)

pi = gospers_pi()

def CoreTask():
    while True:
        #sLock.acquire()
        #for z in range (11):
        z = next(pi)
        time.sleep(0.5)
        if z == 0:
            draw_char(number_zero)
        elif z == 1:
            draw_char(number_one)
        elif z == 2:
            draw_char(number_two)
        elif z == 3:
            draw_char(number_three)
        elif z == 4:
            draw_char(number_four)
        elif z == 5:
            draw_char(number_five)
        elif z == 6:
            draw_char(number_six)
        elif z == 7:
            draw_char(number_seven)
        elif z == 8:
            draw_char(number_eight)
        elif z == 9:
            draw_char(number_nine)
        else:
            draw_char(decimal_point)
        #sLock.release()

_thread.start_new_thread(CoreTask, ())

while True:
    #sLock.acquire()
    cookie.led_toggle()
    for x in range(len(cylon)):
        if (cylon[x]==1):
            cookie.set_pixel(x,255,0,0,0.2)
            cookie.show_pixels()
            cylon[x] = 0
            if (dir==0):
                if (x<4):
                    cylon[x+1] = 1
                else:
                    dir=1
                    cylon[x] = 1
            else:
                if (x>0):
                    cylon[x-1] = 1
                else:
                    dir = 0
                    cylon[x] = 1
            time.sleep(0.15)
            cookie.set_pixel(x,0,0,0,0.2)
            cookie.show_pixels()
    #sLock.release()


