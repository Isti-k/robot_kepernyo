#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import random


class Darts():

    def __init__(self):
        # tégla
        self.ev3 = EV3Brick()
        # motorok
        self.jm = Motor(Port.B)
        self.bm = Motor(Port.C)
        self.km = Motor(Port.A)
        # szenzorok
        self.cs = ColorSensor(Port.S3)
        self.ts = TouchSensor(Port.S1)
        self.gs = GyroSensor(Port.S2)
        self.us = UltrasonicSensor(Port.S4)
        #self.ir = InfraredSensor(Port.S4)

        # dupla motorkezelő
        self.robot = DriveBase(self.jm, self.bm, 55, 115)

        #stopper óra
        self.ido = StopWatch()

    def csipog(self):
        self.ev3.speaker.set_volume(100)
        self.ev3.speaker.play_file("boo.wav")


    def darts1(self):
        #képernyő törlése
        self.ev3.screen.clear()
        # kör rajzolása
        self.ev3.screen.draw_circle(90, 60, 50, fill=True, color=Color.BLACK)

        # 10 véletlen lövés
        db=0
        for loves in range(0,10,1):
            x= random.randint(0,177)
            y= random.randint(0,127)

            if(90-x)**2+(60-y)**2<=50**2:
                #talált
                self.ev3.screen.draw_circle(x,y,2, fill=True, color=Color.WHITE)
                db+=1
            else:
                #nem talált
                self.ev3.screen.draw_circle(x,y,2, fill=True, color=Color.BLACK)
                self.csipog()
            wait(100)
        # Találatok számának kiírása
        szoveg = "Találat: " + str(db)+"."
        self.ev3.screen.draw_text(80,100, szoveg, text_color=Color.WHITE, background_color=Color.BLACK)
        wait(5000)


        def darts2a(self):
            #tábla kirajzolása
            self.ev3.screen.draw_circle(172,40,177,80, fill=True, color=Color.BLACK)
            #bal szélére véletlenszerűen megjelenik a golyó
            #r=5
            #y= random.randint(0+r,127+r)
            #self.ev3.screen.draw_circle(0+r,y,r, fill=True, color=Color.BLACK)
            #mozog a golyó
            r=5
            y= random.randint(0+r,127+r)
            for x in range(177+r+1):
                #kirajzolom a kört
                self.ev3.screen.draw_circle(x,y,r, fill=True, color=Color.BLACK)
                wait(30)
                #letörlöm
                self.ev3.screen.clear()


            wait(5000)

        def darts2b(self):
            #tábla kirajzolása
            self.ev3.screen.draw_circle(172,40,177,80, fill=True, color=Color.BLACK)
            #bal szélére véletlenszerűen megjelenik a golyó
            #r=5
            #y= random.randint(0+r,127+r)
            #self.ev3.screen.draw_circle(0+r,y,r, fill=True, color=Color.BLACK)
            #mozog a golyó
            r=5
            y= random.randint(0+r,127+r)
            for x in range(177+r+1,1):
                #kirajzolom a kört
                self.ev3.screen.draw_circle(x,y,r, fill=True, color=Color.BLACK)
                wait(30)
                #eltakarom egy másik körrel
                self.ev3.screen.draw_circle(x,y,r, fill=True, color=Color.WHITE)

            wait(5000)
        
        def darts3(self):
            #tábla kirajzolása
            self.ev3.screen.draw_circle(172,40,177,80, fill=True, color=Color.BLACK)
            #bal szélére véletlenszerűen megjelenik a golyó
            #r=5
            #y= random.randint(0+r,127+r)
            #self.ev3.screen.draw_circle(0+r,y,r, fill=True, color=Color.BLACK)
            #mozog a golyó
            r=5
            y= random.randint(0+r,127+r)
            yiránya = random.randint(-1,1)
            for x in range(177+r+1,1)
                # minden 8. lépésben változzon y kordináta
                if x%8==0:
                    # y kordináta változási iránya
                    x+=yiránya
                #kirajzolom a kört
                self.ev3.screen.draw_circle(x,y,r, fill=True, color=Color.BLACK)
                wait(30)
                #eltakarom egy másik körrel
                self.ev3.screen.draw_circle(x,y,r, fill=True, color=Color.WHITE)

            wait(5000)

