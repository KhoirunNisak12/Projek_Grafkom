from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import time
import random

w,h= 1200,600
xposition=150
yposition=50
pos_x_bintang = 10
pos_y_bintang = 10
pos_x_bintang1 = 10
pos_y_bintang1 = 10
bintang = False
xtikus = 0
# ytikus = random.randrange(10,400)
ytikus = 0
tikusbolean = False
opening_to_game_x = 1500
play = False
point = 0
health = 3
ringtangan_bool = False
ringtangan_bool1 = False
x_rintangan = 0
y_rintangan = 0
x_rintangan1 = 0
y_rintangan1= 0
run_game = False
speed = 10
speedRTG = [5,2.5]




class assets:
    def __init__(self,_color):
        self.color = _color if type(_color)==set or _color!='' else (255,255,255)

    def quads_1_color(self,_x_min,_x_max,_y_min,_y_max):
        glPushMatrix()
        glColor3ub(self.color[0],self.color[1],self.color[2])
        glBegin(GL_POLYGON)
        glVertex2f(_x_min,_y_min)
        glVertex2f(_x_max,_y_min)
        glVertex2f(_x_max,_y_max)
        glVertex2f(_x_min,_y_max)
        glEnd()
        glPopMatrix()

    def quads_2_color(self,_x_min,_x_max,_y_min,_y_max, warna_tambahan, arah):
        if arah == "kiri atas":
            glPushMatrix()
            glColor3ub(self.color[0],self.color[1],self.color[2])
            glBegin(GL_POLYGON)
            glVertex2f(_x_min,_y_min)
            glVertex2f(_x_max,_y_min)
            glVertex2f(_x_max,_y_max)
            glColor3ub(warna_tambahan[0],warna_tambahan[1],warna_tambahan[2])
            glVertex2f(_x_min,_y_max)
            glEnd()
            glPopMatrix()
        elif arah == "kanan atas":
            glPushMatrix()
            glColor3ub(self.color[0],self.color[1],self.color[2])
            glBegin(GL_POLYGON)
            glVertex2f(_x_min,_y_min)
            glVertex2f(_x_max,_y_min)
            glColor3ub(warna_tambahan[0],warna_tambahan[1],warna_tambahan[2])
            glVertex2f(_x_max,_y_max)
            glVertex2f(_x_min,_y_max)
            glEnd()
            glPopMatrix()
        elif arah == "kiri bawah":
            glPushMatrix()
            glColor3ub(self.color[0],self.color[1],self.color[2])
            glBegin(GL_POLYGON)
            glVertex2f(_x_min,_y_min)
            glColor3ub(warna_tambahan[0],warna_tambahan[1],warna_tambahan[2])
            glVertex2f(_x_max,_y_min)
            glVertex2f(_x_max,_y_max)
            glVertex2f(_x_min,_y_max)
            glEnd()
            glPopMatrix()
        elif arah == "kanan bawah" :
            glPushMatrix()
            glColor3ub(self.color[0],self.color[1],self.color[2])
            glBegin(GL_POLYGON)
            glColor3ub(warna_tambahan[0],warna_tambahan[1],warna_tambahan[2])
            glVertex2f(_x_min,_y_min)
            glVertex2f(_x_max,_y_min)
            glVertex2f(_x_max,_y_max)
            glVertex2f(_x_min,_y_max)
            glEnd()
            glPopMatrix()

    def circle(self,r,xR,yR):
        glColor3ub(self.color[0],self.color[1],self.color[2])
        glBegin(GL_POLYGON)
        for i in range(360):
            theta= 2 *3.1415926*i/360
            x = r * math.cos(theta)
            y = r * math.sin(theta)
            glVertex2f(x + xR, y + yR)
        glEnd()

    def create_line(self,x1,y1,x2,y2,z):
        glColor3ub(self.color[0],self.color[1],self.color[2])
        glLineWidth(z)
        glBegin(GL_LINE_STRIP)
        glVertex2f(x1,y1)
        glVertex2f(x2,y2)
        glEnd()
        
    def drawBitmapText(self,string,x,y,z) :
        glColor3ub(self.color[0],self.color[1],self.color[2])
        glRasterPos3f(x,y,z)
        for c in string :
            glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24,ord(c))
            
    def drawBitmapTextstart(self,string,x,y,z) :
        glColor3ub(self.color[0],self.color[1],self.color[2])
        glRasterPos3f(x,y,z)
        for c in string :
            glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24,ord(c))


class splashPage:
    def kurang(self, bg_dikurangi):

        bg_dikurangi -= 100
        return bg_dikurangi
    
    def opening_to_game(self):
        global opening_to_game_x,w,h
        glPushMatrix()
        glColor3ub(2, 5, 26)
        glBegin(GL_POLYGON)
        glVertex2f(opening_to_game_x,h)
        glVertex2f(opening_to_game_x,0)
        glColor3ub(65, 87, 224)
        glVertex2f(w,0)
        glVertex2f(w,h)
        glEnd()
        glPopMatrix()

        if opening_to_game_x > 0:
            time.sleep(0.05)
            proses = self.kurang(opening_to_game_x)
            opening_to_game_x = proses
            print(opening_to_game_x)
        if opening_to_game_x <= 0:
            opening_to_game_x = 0

    def bacgrond(self):
        # Bacgrond
        assets((65, 87, 224)).quads_2_color(0,1200,0,600, (2, 5, 26), "kanan atas")
        # assets((105,200,255)).quads_2_color(200,350,350,600, (255,0,255),"kiri bawah")
        # assets((220,220,220)).quads_2_color(0,1200,0,50, (0,255,255),"kanan atas")
        #assets((255,222,173)).quads_2_color(0,1200,50,100, (255,255,0),"kanan bawah")


        # Tanah
        assets((207, 63, 10)).quads_1_color(0,1200,0,50)
        # Rumput
        assets((0,255,0)).quads_1_color(0,1200,50,75)
        # Pohon                             x-, x+, y-, y+
        assets((207,63,10)).quads_1_color(120,170,75,300)
        assets((62, 181, 22)).circle(70,100,300)
        assets((62, 181, 22)).circle(64,65,350)
        assets((62, 181, 22)).circle(60,70,420)
        assets((62, 181, 22)).circle(79,140,450)
        assets((62, 181, 22)).circle(74,225,415)
        assets((62, 181, 22)).circle(75,255,350)
        assets((62, 181, 22)).circle(79,190,300)
        assets((207,63,10)).create_line(150,120,75,270,40)
        assets((207,63,10)).create_line(140,170,200,260,40)
        #buah
        assets((207, 2, 2)).circle(22,140,370)
        assets((207, 2, 2)).circle(18,100,300)
        assets((207, 2, 2)).circle(20,200,310)
        assets((207, 2, 2)).circle(20,70,425)
        assets((207, 2, 2)).circle(20,240,385)
        assets((207, 2, 2)).circle(20,150,470)

        # Rumah                            
        assets((0,205,205)).quads_2_color(350,550,75,210, (175,238,238), "kanan atas")
        # assets((175,238,238)).quads_1_color(350,550,75,210)
        glColor3ub(175,238,238)
        glBegin(GL_POLYGON)
        glVertex2f(350, 210)
        glVertex2f(450, 300)
        glVertex2f(550, 210)
        glEnd() 
        #atap kiri
        glBegin(GL_QUADS)
        glColor3ub(0,139,139)
        glVertex2f(320,200)
        glVertex2f(450,320)
        glVertex2f(450,280)
        glVertex2f(340,180)
        glEnd()
        # atap kanan
        glBegin(GL_QUADS)
        glColor3ub(0,139,139)
        glVertex2f(560,180)
        glVertex2f(580,200)
        glVertex2f(450,320)
        glVertex2f(450,280)
        glEnd()
        # Pintu
        # assets((72,209,204)).quads_2_color(410,490,75,160, (188,143,143), "kiri bawah")
        assets((150,205,205)).quads_1_color(410,490,75,160)
        assets((150,205,205)).circle(40,450,160)
    def bintang():
        global pos_x_bintang,pos_y_bintang,bintang
        glPushMatrix()
        glTranslated(pos_x_bintang,pos_y_bintang,0)
        pos_x_bintang -=2
        if pos_x_bintang <= 0:
                pos_x_bintang = 800
        glColor3ub(200,200,255)
        glPointSize(2)
        glBegin(GL_POINTS)
        glVertex2f(100, 550)
        glVertex2f(320, 400)
        glVertex2f(200, 560)
        glVertex2f(500, 500)
        glVertex2f(600, 550)
        glVertex2f(720, 420)
        glVertex2f(800, 530)
        glVertex2f(520, 440)
        glVertex2f(400, 550)
        glVertex2f(320, 540)
        glVertex2f(930, 550)
        glVertex2f(800, 600)
        glVertex2f(430, 550)
        glVertex2f(1180, 500)
        glVertex2f(1790, 450)
        glVertex2f(1170, 542)
        glVertex2f(1190, 351)
        glVertex2f(980, 490)
        glVertex2f(1060, 532)
        glVertex2f(890, 489)
        glVertex2f(1030, 590)
        glVertex2f(900, 559)
        glVertex2f(1020, 598)
        glVertex2f(1000, 389)
        glVertex2f(50, 500)
        glVertex2f(20, 510)
        glVertex2f(10, 570)
        glVertex2f(35, 560)
        glVertex2f(570, 504)
        glVertex2f(653, 582)
        glVertex2f(754, 556)
        glVertex2f(856, 594)
        glVertex2f(950, 542)
        glVertex2f(1005, 533)
        glEnd();
        glPopMatrix()
     
    def bintang1():
        global pos_x_bintang1,pos_y_bintang1,bintang
        glPushMatrix()
        glTranslated(pos_x_bintang1,pos_y_bintang1,0)

        pos_x_bintang1 +=2
        print(pos_x_bintang1)
        if pos_x_bintang1 >= 800:
                pos_x_bintang1 = 10
        glColor3ub(200,200,255)
        glPointSize(2)
        glBegin(GL_POINTS)
        glVertex2f(50, 500)
        glVertex2f(20, 510)
        glVertex2f(10, 570)
        glVertex2f(35, 560)
        glVertex2f(570, 504)
        glVertex2f(653, 582)
        glVertex2f(754, 556)
        glVertex2f(856, 594)
        glVertex2f(950, 542)
        glVertex2f(1005, 533)
        glVertex2f(800, 600)
        glVertex2f(430, 550)
        glVertex2f(1180, 500)
        glVertex2f(1790, 450)
        glVertex2f(1170, 542)
        glVertex2f(1190, 351)
        glVertex2f(980, 490)
        glVertex2f(1060, 532)
        glVertex2f(890, 489)
        glVertex2f(1030, 590)
        glVertex2f(900, 559)
        glVertex2f(1020, 598)
        glVertex2f(1000, 389)
        glVertex2f(100, 550)
        glVertex2f(320, 400)
        glVertex2f(200, 560)
        glVertex2f(500, 500)
        glVertex2f(600, 550)
        glVertex2f(720, 420)
        glVertex2f(800, 530)
        glVertex2f(520, 440)
        glVertex2f(400, 550)
        glVertex2f(320, 540)
        glVertex2f(930, 550)
        glEnd()
        glPopMatrix()

    def buttonSTR():
        glPushMatrix()
        assets((0,255,0)).quads_1_color(550,800,350,400)
        assets((255,255,255)).drawBitmapText("P L A Y  G A M E S",575,370,0)
        glPopMatrix()
    def run_splah():
        glPushMatrix()
        splashPage().bacgrond()
        splashPage.bintang()
        splashPage.bintang1()
        game.kucing()
        splashPage.buttonSTR()
        glPopMatrix()
class game:
    def kurang(self, bg_dikurangi):
        bg_dikurangi -= 100
        return bg_dikurangi
    def opening_to_game(self):
        global opening_to_game_x,w,h
        glPushMatrix()
        glColor3ub(2, 5, 26)
        glBegin(GL_POLYGON)
        glVertex2f(opening_to_game_x,h)
        glVertex2f(opening_to_game_x,0)
        glColor3ub(65, 87, 224)
        glVertex2f(w,0)
        glVertex2f(w,h)
        glEnd()
        glPopMatrix()

        if opening_to_game_x > 0:
            time.sleep(0.05)
            proses = self.kurang(opening_to_game_x)
            opening_to_game_x = proses
            print(opening_to_game_x)
        if opening_to_game_x <= 0:
            opening_to_game_x = 0
    def bacgrond():
        global point,health
        assets((2, 5, 26)).quads_2_color(0,1200,0,600,(65, 87, 224),"kanan atas")
        assets((1,1,1)).quads_2_color(0,1200,550,600,(65, 87, 224),"kanan atas")
        assets((1,1,1)).quads_2_color(-20,1200,-20,50,(65, 87, 224),"kanan atas")
        assets((255,255,255)).drawBitmapText(f"Score : {point}",800,570,0)
        assets((255,255,255)).drawBitmapText(f"Healt : {health}",950,570,0)
    def actions():
        global  xposition,yposition,health,play,point,health,speedRTG
        if xposition <= -40 and 50<=yposition<=550:
            xposition+=5
        if point %  1000 == 0:
            if health < 3:
                health = 3
            elif health > 3:
                health +=1
                speedRTG[0] +=1
                speedRTG[1] +=1
        if health == 0:
            assets((245, 25, 10)).drawBitmapText(" G A M E  O V E R",500,300,0)
            assets((255,255,255)).drawBitmapText(f"Score Akhir: {point}",520,250,0)
            assets((255,255,255)).drawBitmapText(f"Please Your Enter To Play Again",443,200,0)
            # run_game == False
    def kucing():
        global xposition,yposition,xtikus,ytikus,point,tikusbolean,ringtangan_bool,x_rintangan,y_rintangan,health,point,play,ringtangan_bool1,x_rintangan1,y_rintangan1,run_game
        glPushMatrix()
        glTranslated(xposition,yposition,0)
        glScaled(0.3,0.3,0)
        if run_game == True:  #colision untuk tikus
            if xposition-10 <= xtikus <= xposition+130 and yposition-35 <= ytikus <= yposition+70:
                point+=100
                tikusbolean = True
                if tikusbolean == True:
                    ytikus = random.randrange(50,450,25)
                    xtikus= 1200
                if xtikus == 1200:
                    tikusbolean = False
                print('kena makan')
            if xposition -10 <=x_rintangan <=xposition+130 and yposition-30 <=y_rintangan <=yposition+50:
                ringtangan_bool = True
                if ringtangan_bool == True:
                    health -=1
                    x_rintangan = 1200
                    y_rintangan = random.randrange(50,450,25)
                if x_rintangan == 1200:
                    ringtangan_bool = False
            if xposition -10 <=x_rintangan1 <=xposition+130 and yposition-30 <=y_rintangan1 <=yposition+50:
                ringtangan_bool1 = True
                if ringtangan_bool1 == True:
                    health -=1
                    x_rintangan1 = 1200
                    y_rintangan1 = random.randrange(50,450,50)
                if x_rintangan1 == 1200:
                    ringtangan_bool1 = False
            if health < 1:
                run_game = False
                print('kapok kena batunya')
         # ekor
        glBegin(GL_POLYGON)
        glColor3ub(1,1,1)
        glVertex2f(248.5381470326646, 225.8743228793545)
        glVertex2f(256.325724704732, 244.0453374475175)
        glColor3ub(240, 116, 7)
        glVertex2f(266.7091616008217, 256.5054617228292)
        glVertex2f(255.8065528599275, 276.2339918254062)
        glVertex2f(236.0780227573569, 320.8827704786066)
        glVertex2f(219.4645237236132, 362.9356899077838)
        glVertex2f(206.485227603501, 397.2010316648911)
        glVertex2f(184.1608382769079, 444.4456695421149)
        glVertex2f(157.1141584400838, 468.7984511926027)
        glVertex2f(139.1155572194571, 468.7984511926027)
        glVertex2f(126.9022206768889, 454.013885904226)
        glVertex2f(125.616606303987, 439.8721278023005)
        glVertex2f(137.8299428465551, 422.5163337681192)
        glColor3ub(240, 116, 7)
        glVertex2f(159.0425799994366, 399.3752750558774)
        glVertex2f(174.4699524742596, 368.5205301062217)
        glVertex2f(191.1829393219844, 328.0236773597986)
        glVertex2f(205.9675046103563, 289.455246172729)
        glVertex2f(221.3948770851793, 252.1724293585617)
        glColor3ub(240, 116, 7)
        glVertex2f(232.9894452983404, 237.7857300298651)
        glVertex2f(248.5381470326646, 225.8743228793545)
        glEnd()
        # Badan
        glBegin(GL_POLYGON)
        glColor3ub(240, 116, 7)
        glVertex2f(404.837455964905, 276.2560146441095)
        glVertex2f(363.4116434958999, 277.166472061011)
        glVertex2f(323.3515171522465, 276.7112433525603)
        glVertex2f(287.8436778930993, 269.882812725799)
        glVertex2f(266.7091616008217, 256.5054617228292)
        glVertex2f(256.325724704732, 244.0453374475175)
        glVertex2f(248.5381470326646, 225.8743228793545)
        glVertex2f(247.4119057600651, 192.0663642884108)
        glVertex2f(250.0397738301183, 169.729485692952)
        glVertex2f(259.8942790928176, 143.4508049924122)
        glVertex2f(259.8942790928176, 117.1721242918725)
        glVertex2f(259.8942790928176, 98.1200807839811)
        glVertex2f(265.8069822504372, 79.7250042936033)
        glVertex2f(276.3184545306498, 73.8123011359818)
        glVertex2f(294.7135310210218, 76.4401692060358)
        glVertex2f(305.2493182735089, 81.924589649048)
        glVertex2f(306.2712412581901, 106.7913822762991)
        glVertex2f(306.2712412581901, 130.2956109239748)
        glVertex2f(312.4027791662775, 140.8554817656842)
        glVertex2f(330.894497399685, 141.0890063991688)
        glVertex2f(331.4786748803271, 129.6143289341871)
        glVertex2f(330.4567518956459, 113.2635611792823)
        glVertex2f(332.1599568701146, 98.9566393937406)
        glVertex2f(346.126237660758, 91.4625375060759)
        glVertex2f(361.1144414360828, 91.121896511182)
        glVertex2f(375.7620042165137, 99.6379213835283)
        glVertex2f(376.4432862063012, 119.0544580924777)
        glVertex2f(374.3994402369387, 134.383302862701)
        glVertex2f(400.3951111207507, 133.0806941759182)
        glVertex2f(430.8504165655212, 128.9651123590561)
        glVertex2f(458.8363729201752, 128.9651123590561)
        glVertex2f(478.9356651342682, 131.6270097078514)
        glVertex2f(480.6489565495379, 117.4414832718419)
        glVertex2f(480, 100)
        glVertex2f(480, 80)
        glVertex2f(492.1725856367484, 70.9354087412991)
        glVertex2f(505.7540056323892, 68.877617832868)
        glVertex2f(518.512309264658, 73.4047578314164)
        glVertex2f(527.2309880441118, 81.2513521400592)
        glVertex2f(538.2218171128628, 152.366781383405)
        glVertex2f(552.7374238814507, 96.2606278906918)
        glVertex2f(563.9090460909522, 87.2075566478043)
        glVertex2f(581.4685036316547, 87.2075566478043)
        glVertex2f(590.7857668165174, 96.1664635563289)
        glVertex2f(591.1441230928582, 114.80098992606)
        glColor3ub(138, 74, 18)
        glVertex2f(591.8098499935546, 229.1624113912076)
        glVertex2f(404.837455964905, 276.2560146441095)
        glEnd()
        # Kepala
        glBegin(GL_POLYGON)
        glColor3ub(230, 136, 69)
        glVertex2f(404.8347126832238, 276.988717885963)
        glVertex2f(416.9727413861352, 260.6793230714568)
        glVertex2f(429.166633248886, 246.8035150897015)
        glVertex2f(442.6219622008868, 237.5529764351979)
        glVertex2f(442.6219622008868, 237.5529764351979)
        glVertex2f(457.7592072718877, 228.7229168104446)
        glVertex2f(476.2602845808889, 222.4157313641921)
        glVertex2f(494.34088286014, 217.7904620369404)
        glVertex2f(517.0467504666414, 214.4266297989391)
        glVertex2f(540.1730971028927, 216.1085459179397)
        glVertex2f(560, 220)
        glVertex2f(579.6981258993951, 225.7795636021934)
        glVertex2f(591.8098499935546, 229.1624113912076)
        glVertex2f(607.8702208926469, 241.7577667326996)
        glVertex2f(624.2689030528978, 258.576927922706)
        glVertex2f(641.8501063936102, 286.5962526268445)
        glVertex2f(651.4385582605202, 317.7587211943119)
        glVertex2f(650, 350)
        glVertex2f(633.460211010064, 381.282214812611)
        glVertex2f(641.0438150300592, 403.6314883322661)
        glVertex2f(643.7010806306308, 430.190302492164)
        glVertex2f(640.5561154725197, 448.9875471834599)
        glVertex2f(636.2808730936458, 458.6274846952714)
        glVertex2f(628.0776305135344, 460.763275249518)
        glVertex2f(607.1611792179243, 456.0570737080042)
        glVertex2f(587.8134617694851, 444.553025495415)
        glVertex2f(569.9046184506126, 430.9998680241636)
        glVertex2f(547.5492930254358, 439.3239126715108)
        glVertex2f(526.1099304474357, 439.3239126715108)
        glVertex2f(504.0560992545389, 438.9672437993908)
        glVertex2f(483.3927877819403, 433.099883751614)
        glVertex2f(463.749886752433, 425.9570106499726)
        glVertex2f(449.2090379383822, 436.4162176916618)
        glVertex2f(438.4947282859237, 442.5386803502115)
        glVertex2f(425.229392525737, 447.6407325656696)
        glVertex2f(414.2599802625056, 450.1917586733986)
        glVertex2f(402.2701575561829, 446.6203221225779)
        glVertex2f(397.6783105622722, 435.9060124701159)
        glVertex2f(396.1476948976352, 421.1100610452875)
        glVertex2f(396.9130027299537, 406.314109620459)
        glVertex2f(399.2089262269091, 389.4773373094473)
        glVertex2f(406.9296844985526, 378.134965786151)
        glVertex2f(397.4232079514994, 359.8854344597903)
        glVertex2f(392.0151233369628, 336.4837125748053)
        glVertex2f(391.0075278981944, 320.234706411955)
        glVertex2f(394.2668737796338, 298.9429147787215)
        glVertex2f(404.8347126832238, 276.988717885963)
        glEnd()
        #telinga dalam
        glBegin(GL_POLYGON) #1
        glColor3ub(102, 49, 2)
        glVertex2f(606.9458400978685, 405.3197365631428)
        glVertex2f(619.7517681084512, 402.1210865385868)
        glVertex2f(628.3951115356411, 415.4135113573921)
        glVertex2f(630.6954042800227, 435.573310065762)
        glVertex2f(626.769987563937, 446.9144786949161)
        glVertex2f(611.8898182057849, 445.4973197084249)
        glVertex2f(600, 440)
        glVertex2f(591.5181577749815, 433.0971785766276)
        glVertex2f(588.0200123586574, 424.2455643023601)
        glVertex2f(594.6440520673813, 413.8363590457906)
        glVertex2f(606.9458400978685, 405.3197365631428)
        glEnd()
        glBegin(GL_POLYGON) #2
        glColor3ub(102, 49, 2)
        glVertex2f(416.8325827457516, 396.0250731068243)
        glVertex2f(430.1304280132349, 399.3454942719764)
        glVertex2f(440.689287285385, 408.5844961351107)
        glVertex2f(447.2885743304789, 417.4935336459903)
        glVertex2f(435.40985764931, 429.372250327163)
        glVertex2f(423.3045350103578, 435.2612837110117)
        glVertex2f(411.6524242869722, 435.971537372259)
        glVertex2f(408.3527807644253, 424.0928206910862)
        glVertex2f(409.9561334646075, 408.5644806195028)
        glVertex2f(416.8325827457516, 396.0250731068243)
        glEnd()
        glBegin(GL_POLYGON) # Hidung
        glColor3ub(102, 49, 2)
        glVertex2f(518.9853467597952, 321.8414225320357)
        glVertex2f(527.2686055916901, 323.2513389289543)
        glVertex2f(531.2339954580227, 326.2474112724066)
        glVertex2f(531.0577559084079, 331.0058791120073)
        glVertex2f(524.1844134734313, 333.8257119058447)
        glVertex2f(516.0773941911513, 334.5306701043041)
        glVertex2f(508.9396924317525, 332.1514361845037)
        glVertex2f(505.5030212142643, 328.2741660929773)
        glVertex2f(510.1216610801684, 323.6038180281843)
        glVertex2f(518.9853467597952, 321.8414225320357)
        glEnd()
         # Bola Mata
        assets((2, 194, 212)).circle(20,482, 355)
        assets((0, 3, 46)).circle(15,482, 355)
        assets((255,255,255)).circle(7,485, 360)
        assets((2, 194, 212)).circle(20,553, 355)
        assets((0, 3, 46)).circle(15,553, 355)
        assets((255,255,255)).circle(7,558, 360)
        # Kumis
        assets((1,1,1)).create_line(548.3965966111367, 326.2053953474911, 610.0376783878472, 346.4275684204901,1) # Kanan
        assets((1,1,1)).create_line(548.1529559717031, 318.8961761644795, 593.538516976132, 330.4133492976663,1)
        assets((1,1,1)).create_line(546.9880996044008, 311.4131789418511, 608.7386532607788, 323.075693847985,1)
        assets((1,1,1)).create_line(487.1687612961308, 324.7432837010833, 425.6601852446667, 344.5346867208042,1) #Kiri
        assets((1,1,1)).create_line(487.7508613849459, 317.5640492723611, 441.3768876426749, 328.4299175969137,1)
        assets((1,1,1)).create_line(486.9747279331924, 310.5788482065772, 426.8243854222969, 320.5788482065772,1)

        assets((1,1,1)).create_line(518.4587512892717, 321.8895390929896, 518.8471119319009, 301.4728653090471,1)
        assets((1,1,1)).create_line(552.7318397496078, 310.0407650243402, 539.0623521776037, 294.4405588687142,1)
        assets((1,1,1)).create_line(539.0623521776037, 294.4405588687142, 518.8471119319009, 301.4728653090471,1)
        assets((1,1,1)).create_line(502.5930407061666, 294.328980004843, 518.8471119319009, 301.4728653090471,1)
        assets((1,1,1)).create_line(486.0096490279609, 311.6927665855582,502.5930407061666, 294.328980004843 ,1)
        glPopMatrix()

    def rintangan():
        global x_rintangan,y_rintangan,speedRTG,run_game
        glPushMatrix()
        glTranslated(x_rintangan,y_rintangan,0)
        if run_game == True:    
            x_rintangan -=speedRTG[0]
            if x_rintangan < -100:

                y_rintangan = random.randrange(50,500,50)
                x_rintangan = 1200
            assets((1,1,1)).circle(20,100,100)
            assets((255,255,255)).circle(10,100,100)
        glPopMatrix()
    def rintangan1():
        global x_rintangan1,y_rintangan1,speedRTG,run_game
        glPushMatrix()
        # time.sleep(0)
        glTranslated(x_rintangan1,y_rintangan1,0)
        if run_game == True:
            x_rintangan1 -=speedRTG[1]
            if x_rintangan1 < -100:
                x_rintangan1 = 1200
                y_rintangan1 = random.randrange(50,250,25)
            assets((1,1,1)).circle(20,100,100)
            assets((255,255,255)).circle(10,100,100)
        glPopMatrix()
    def tikus():
        global xtikus,ytikus,tikusbolean,play,run_game
        glPushMatrix()
        glTranslated(xtikus,ytikus,0)
        glScaled(0.5,0.5,0)
        if run_game == True:
            xtikus -=5
            if xtikus < -100 or tikusbolean == True :
                ytikus = random.randrange(50,500,25)
                xtikus=1200
            # print(xtikus,' ',ytikus)
        glBegin(GL_POLYGON) #Badan Tikus
        glColor3ub(131, 139, 131) 
        glVertex2f(18.2309773145172, 54.1606186425384)
        glVertex2f(24.013329419721, 54.4234528291386)
        glVertex2f(29.4452359427912, 56.788960508541)
        glVertex2f(34.3514740926612, 60.4686391209447)
        glVertex2f(39.0508057657112, 64.8223666462086)
        glVertex2f(43.1198195241634, 69.1986645884173)
        glVertex2f(47.8109159137314, 74.0442440563389)
        glVertex2f(52.8525817759823, 79.9391150207098)
        glVertex2f(57.00062065093, 83.3091418057783)
        glVertex2f(61.0491154431295, 85.7449930349409)
        glVertex2f(68.1952984112422, 89.1681407480453)
        glVertex2f(73.02746794767, 89.9189961759516)
        glVertex2f(77.7299289342714, 90.483262199498)
        glVertex2f(112.9730088027043, 101.2874175806672)
        glVertex2f(115.5396706635254, 102.3193552625726)
        glVertex2f(125.6101962216785, 106.338881584941)
        glVertex2f(132.2563403157912, 107.7072053690234)
        glVertex2f(137.5679549753515, 107.5798410683836)
        glVertex2f(148.08892658697, 108.2374017941099)
        glVertex2f(158.6098981985883, 105.6071588912045)
        glVertex2f(165.8430661815762, 102.6481356254358)
        glVertex2f(172.7474538017007, 98.3739909082144)
        glVertex2f(179.6518414218253, 90.483262199498)
        glVertex2f(184.2547665019085, 79.9622905878762)
        glVertex2f(185.5698879533609, 66.8110760733489)
        glVertex2f(181.515996542742, 59.4249232735426)
        glVertex2f(175.4562769275215, 53.5606784846178)
        glVertex2f(177.6065000167932, 42.2231385593632)
        glVertex2f(178.248771831533, 37.2152646132813)
        glVertex2f(177.0215985189207, 32.6179183355778)
        glVertex2f(169.45965017307, 28.0149932554933)
        glVertex2f(159.2674589243145, 26.6998718040405)
        glVertex2f(150.7191694898745, 25.0559699897246)
        glVertex2f(143.4860015068869, 19.1379234581873)
        glVertex2f(141.9848398008646, 22.5047347444137)
        glVertex2f(135.4160214592443, 22.051712789819)
        glVertex2f(139.5992297532898, 26.8324073023021)
        glVertex2f(134.1702110841095, 27.0349542903604)
        glVertex2f(142.8255136598032, 29.3855157938854)
        glVertex2f(147.9815394542618, 29.3855157938854)
        glVertex2f(157.2910304720347, 31.032579589338)
        glVertex2f(157.2910304720347, 31.032579589338)
        glVertex2f(155.7871896153174, 40.1988476683788)
        glVertex2f(150.527941309486, 45.274608053389)
        glVertex2f(137.0378129823064, 44.9330858172578)
        glVertex2f(122.0108345925366, 46.9822192340452)
        glVertex2f(123.03540130093, 44.5915635811265)
        glVertex2f(117.1904376716868, 30.6139375904249)
        glVertex2f(106.2949130908687, 28.2180630752703)
        glVertex2f(96.4383711753665, 26.467181167228)
        glVertex2f(88.5416554516855, 22.9049015867928)
        glVertex2f(88.382898858529, 25.7651439288025)
        glVertex2f(88.382898858529, 25.7651439288025)
        glVertex2f(84.6141497361775, 26.8324073023021)
        glVertex2f(85.9870243433752, 30.100535908606)
        glVertex2f(90.6365377264103, 28.3466483408342)
        glVertex2f(84.6141497361775, 26.8324073023021)
        glVertex2f(85.9870243433752, 30.100535908606)
        glVertex2f(89.492514229433, 32.1055826880465)
        glVertex2f(87.9744209360085, 32.7586338379806)
        glVertex2f(94.071266957967, 33.0823601754299)
        glVertex2f(97.416439111608, 32.7046794484058)
        glVertex2f(101.731342585814, 33.8084369439643)
        glVertex2f(100.665694834341, 43.908519108864)
        glVertex2f(88.37089433362, 42.0301468101422)
        glVertex2f(78.8082717219484, 43.0547135185359)
        glVertex2f(68.3568372101279, 44.6812984107546)
        glVertex2f(72.319349235457, 50.0559193592264)
        glVertex2f(72.1485881173912, 55.3495140192606)
        glVertex2f(70.4409769367355, 57.5694085541136)
        glVertex2f(62.6499548499464, 51.0942197988686)
        glVertex2f(58.7649015298257, 47.4850949942286)
        glVertex2f(48.432913556053, 44.1208106068465)
        glVertex2f(44.7937641230033, 47.0451271155483)
        glVertex2f(37.580450068208, 47.5650056059842)
        glVertex2f(25.8723251216227, 46.640696997914)
        glVertex2f(37.580450068208, 47.5650056059842)
        glVertex2f(45.446867758329, 44.1648095664304)
        glVertex2f(39.5810301692213, 44.2385936870482)
        glVertex2f(25.8723251216227, 46.640696997914)
        glVertex2f(20.7494915796558, 48.3483081785702)
        glVertex2f(16.953320851663, 49.5729076763323)
        glVertex2f(18.2309773145172, 54.1606186425384)
        glEnd()

        glBegin(GL_POLYGON) # Telinga Kiri
        glColor3ub(71, 41, 1)
        glVertex2f(52.8424599760667, 79.5161156524092)
        glVertex2f(48.5247772338294, 80.7942332570112)
        glVertex2f(44.6049881300712, 83.9847592716993)
        glVertex2f(42.4171988628573, 89.1807587813344)
        glVertex2f(43.8022425185072, 96.1614212369437)
        glVertex2f(48.583553824343, 102.308821487306)
        glVertex2f(56.2731975552124, 105.3157046270431)
        glVertex2f(61.219876561195, 104.6994771402247)
        glVertex2f(65.2978282824702, 103.4013890182302)
        glVertex2f(69.1264595000946, 100.2108630035421)
        glVertex2f(70.9140421732484, 95.128744755221)
        glVertex2f(70.9140421732484, 89.9657702148054)
        glVertex2f(66.843235324076, 89.2707544112879)
        glVertex2f(61.4128153239628, 86.4707482707862)
        glVertex2f(56.7061447640526, 82.4665658541449)
        glVertex2f(52.8424599760667, 79.5161156524092)
        glEnd()

        glBegin(GL_POLYGON) # Telinga kiri 1
        glColor3ub(212, 188, 174)
        glVertex2f(52.8424599760667, 79.5161156524092)
        glVertex2f(49.049024002408, 82.536814668472)
        glVertex2f(46.6605643152893, 85.6980113131888)
        glVertex2f(45.9580761720192, 91.0369212020439)
        glVertex2f(47.7142965301946, 96.5865775338801)
        glVertex2f(52.2102206471236, 100.3097646932132)
        glVertex2f(58.040872236266, 101.3634969081189)
        glVertex2f(63.2688683345589, 99.6917192956366)
        glVertex2f(65.9496435766966, 97.0152162219113)
        glVertex2f(66.6842323392932, 93.2584822298282)
        glVertex2f(66.843235324076, 89.2707544112879)
        glVertex2f(61.4128153239628, 86.4707482707862)
        glVertex2f(56.7061447640526, 82.4665658541449)
        glVertex2f(52.8424599760667, 79.5161156524092)
        glEnd()
        
        glBegin(GL_POLYGON) #Telinga Kanan
        glColor3ub(71, 41, 1)
        glVertex2f(78.7577919558, 86.7885551130112)
        glVertex2f(79.055655871593, 90.3629221025297)
        glVertex2f(81.5404496109975, 98.722838007928)
        glVertex2f(85, 105)
        glVertex2f(98.9350882658891, 109.2354937308029)
        glVertex2f(98.9350882658891, 109.2354937308029)
        glVertex2f(104.7691929784598, 107.230020235856)
        glVertex2f(109.3323550070595, 104.9280713763132)
        glVertex2f(112.9730088027043, 101.2874175806672)
        glVertex2f(116.1387947119608, 95.9055815349296)
        glVertex2f(116.1387947119608, 90.9986133755806)
        glVertex2f(114.8877183393245, 86.9929695141196)
        glVertex2f(112.1815623253901, 82.2927021251228)
        glVertex2f(108.5409085297454, 78.4937590340139)
        glVertex2f(102.9460352557815, 74.8689706583046)
        glVertex2f(96.5649832264073, 73.8662339108311)
        glVertex2f(92.736352008783, 74.6866548860367)
        glVertex2f(91.27782583064, 78.2418124452606)
        glVertex2f(88.5416554516855, 81.646726201366)
        glVertex2f(85.1264330903743, 84.2081429723503)
        glVertex2f(80.6866440206695, 86.598798625269)
        glVertex2f(78.7577919558, 86.7885551130112)
        glEnd()
        
        glBegin(GL_POLYGON) #Telinga Kanan 1
        glColor3ub(212, 188, 174)
        glVertex2f(80.6866440206695, 86.598798625269)
        glVertex2f(82.9065385555218, 93.9415267020906)
        glVertex2f(86.8340442710298, 100.2596880705186)
        glVertex2f(92.6399222852592, 103.5041493137654)
        glVertex2f(100.153411480144, 102.6503437234373)
        glVertex2f(106.8130950847012, 97.8690324175999)
        glVertex2f(109.5094030574235, 92.4624426821565)
        glVertex2f(108.0508768792808, 85.3521275637086)
        glVertex2f(104.678035092326, 81.5234963460828)
        glVertex2f(99.508978089386, 78.9448053304568)
        glVertex2f(94.4683518453273, 77.8771809007248)
        glVertex2f(91.27782583064, 78.2418124452606)
        glVertex2f(88.5416554516855, 81.646726201366)
        glVertex2f(85.1264330903743, 84.2081429723503)
        glVertex2f(80.6866440206695, 86.598798625269)
        glEnd()

        # bawahan
        #Sblm_Ekor
        glBegin(GL_POLYGON)
        glColor3ub(91, 91, 92)
        glVertex2f(177.469119467042, 42.37403845087)
        glVertex2f(176.0352574303315, 48.3993757530106)
        glVertex2f(175.239069077308, 53.7472954385178)
        glVertex2f(181.4832101685636, 59.4339239323416)
        glVertex2f(185.162793311625, 64.897547387192)
        glVertex2f(182.3752303244573, 52.6322702436503)
        glVertex2f(177.469119467042, 42.37403845087)
        glEnd()
        #bawah1
        glBegin(GL_POLYGON)
        glColor3ub(91, 91, 92)
        glVertex2f(122.0108345925366, 46.9822192340452)
        glVertex2f(129.406276942566, 45.90068221576)
        glVertex2f(138.9614555853111, 45.2478439233983)
        glVertex2f(150.527941309486, 45.274608053389)
        glVertex2f(154.1468817304446, 42.2256816998223)
        glVertex2f(158.2121916224366, 36.5657910320424)
        glVertex2f(159.5555362625325, 33.734150403565)
        glVertex2f(157.1815788357635, 32.8439163685264)
        glVertex2f(157.1815788357635, 30.9447504271106)
        glVertex2f(151.9588724968717, 29.9951674564027)
        glVertex2f(147.4483533860105, 29.2829802283718)
        glVertex2f(143.2939278891647, 29.104933421364)
        glVertex2f(139.7753305588046, 29.1778260308288)
        glVertex2f(137.0029407082268, 28.3927461933331)
        glVertex2f(127.1510173871352, 29.7577717137257)
        glVertex2f(118.5784923297522, 32.1563152295852)
        glVertex2f(121.4535195628896, 38.7194609997815)
        glVertex2f(122.9965918902894, 43.942167338675)
        glVertex2f(122.0108345925366, 46.9822192340452)
        glEnd()
        # bawah2
        glBegin(GL_POLYGON)
        glColor3ub(91, 91, 92)
        glVertex2f(13.9982096661213, 46.3178083092116)
        glVertex2f(21.859640403103, 43.1933013353322)
        glVertex2f(30.4762348189906, 40.8697253130697)
        glVertex2f(38.0278568913416, 39.5143059667499)
        glVertex2f(47.4189766479833, 39.4174902991556)
        glVertex2f(57.197359075002, 41.2569879834468)
        glVertex2f(64.9426124825413, 39.3206746315613)
        glVertex2f(79.4649626216778, 36.5130202713274)
        glVertex2f(91.857368073741, 35.5448635953847)
        glVertex2f(102.3134601739193, 36.0289419333561)
        glVertex2f(99.6026214812805, 43.8710110084922)
        glVertex2f(88.37089433362, 42.0301468101422)
        glVertex2f(79.077699951301, 42.7092229973609)
        glVertex2f(71.284149855515, 43.8971135706084)
        glVertex2f(68.5991021325965, 44.8200987253619)
        glVertex2f(63.2290066867602, 45.1557296907268)
        glVertex2f(58.5301731716531, 47.5890541896226)
        glVertex2f(54.0024420443917, 45.8073243603776)
        glVertex2f(48.7743959943027, 44.161458011275)
        glVertex2f(44.656048108835, 44.4208024630609)
        glVertex2f(39.8673545756324, 44.2582736788692)
        glVertex2f(33.8980976707044, 44.5915635811265)
        glVertex2f(25.8723251216227, 46.640696997914)
        glVertex2f(20.7494915796558, 48.3483081785702)
        glVertex2f(16.8219858641478, 49.5436360050295)
        glVertex2f(13.9982096661213, 46.3178083092116)
        glEnd()

        #gigi
        glBegin(GL_POLYGON)
        glColor3ub(255,255,255)
        glVertex2f(62.5776073799386, 51.1159299877339)
        glVertex2f(64.7924520664105, 48.2970367504046)
        glVertex2f(68.4167433715468, 52.0220028140183)
        glVertex2f(66.1044004936723, 53.8430247707022)
        glVertex2f(62.5776073799386, 51.1159299877339)
        glEnd()

        #Mulut
        glBegin(GL_POLYGON)
        glColor3ub(171, 36, 45)
        glVertex2f(58.5301731716531, 47.5890541896226)
        glVertex2f(63.2290066867602, 45.1557296907268)
        glVertex2f(68.5991021325965, 44.8200987253619)
        glVertex2f(71.0419995409786, 46.1945870307547)
        glVertex2f(73.0751285604579, 50.4544764049027)
        glVertex2f(72.2300582547805, 55.136069443959)
        glVertex2f(70.4409769367355, 57.5694085541136)
        glVertex2f(58.5301731716531, 47.5890541896226)
        glEnd()
        #kumis1
        glBegin(GL_POLYGON)
        glColor3ub(0,0,0)
        glVertex2f(47.2253453127948, 54.3271031086736)
        glVertex2f(41.2227739219518, 55.4888911198049)
        glVertex2f(36.188359207051, 55.4888911198049)
        glVertex2f(31.83165416531, 54.2302874410793)
        glVertex2f(27.2813177883806, 51.7130800836282)
        glVertex2f(31.9942688046947, 52.7892682024076)
        glVertex2f(36.4788062098337, 53.2621307651366)
        glVertex2f(41.1221132560654, 53.9126952118076)
        glVertex2f(47.2253453127948, 54.3271031086736)
        glEnd()
        # kumis2
        glBegin(GL_POLYGON)
        glColor3ub(0,0,0)
        glVertex2f(27.7814175194467, 48.7870594814203)
        glVertex2f(31.713412052345, 48.2253459767203)
        glVertex2f(36.9794761589048, 47.3827757196704)
        glVertex2f(41.8242551369399, 46.3295628983579)
        glVertex2f(48.5648171933367, 43.942280503383)
        glVertex2f(44.901769290533, 47.1627437066974)
        glVertex2f(41.8036679275172, 48.2277160502344)
        glVertex2f(38.0326889802168, 48.9274878575953)
        glVertex2f(33.679409318794, 49.2785587980328)
        glVertex2f(27.7814175194467, 48.7870594814203)
        glEnd()  
        assets((165,42,42)).circle(10,20,50) # Bola Mata
        assets((0,0,0)).circle(5,55,70)
        assets((255,255,255)).circle(2,55,70)
        assets((0,0,0)).circle(5,70,70)
        assets((255,255,255)).circle(2,70,70)
        assets((1,1,1)).create_line(273.17481134881, 74.2510975614262, 183.5860601525576, 64.147733790161,4)
        glPopMatrix()

    def run_game():
        # game.opening_to_game()
        game.bacgrond()
        game.actions()
        game.rintangan()
        game.rintangan1()
        # game.tikus()
        game.tikus()
        game.kucing()

def btnklik(button,state,x,y):
    global play,run_game
    if button == GLUT_LEFT_BUTTON:
        if 550<=x<=800 and 200<=y<=250:
            play=True
            run_game = True
        print( x, ' ',y)
   
def mySpecialKeyboard(key,x,y):
    global xposition,yposition,xtikus,ytikus,run_game,speed
    if run_game == True:
        if key == GLUT_KEY_LEFT and xposition >=-20:
            xposition -= speed
        if key == GLUT_KEY_RIGHT and xposition <=810:
            xposition +=speed
        if key == GLUT_KEY_UP and yposition <= 450:
            yposition +=speed
        if key == GLUT_KEY_DOWN and  yposition >= 40: 
            yposition -=speed
        print('xkucing |',xposition, '|  ykucing ', yposition, '| xtikus :',xtikus,' | ytikus :',ytikus)
def mykeyboradSpeed(key,x,y):
    global speed,health,point,play,xposition,yposition,x_rintangan,x_rintangan1,xtikus,ytikus,run_game
    if key == b'1':
        speed+=5
    if key == b'2':
        speed-=5
    if speed >= 20:
        speed +=0
    if speed <=5:
        speed-=0
        speed = 5
    if health == 0 and ord(key) == ord(b'\r'):
            point = 0
            play = False
            xposition=150
            yposition=50

    print('kalah')
            
def page ():
    if play == False:
        splashPage.run_splah()
    else:
        game().opening_to_game()
        game.run_game()

def iterate():
    glViewport(0, 0, 1200, 600)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 1200, 0.0, 600, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(255,255,255,1)
    glLoadIdentity()
    iterate()
    page()
    glutSwapBuffers()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(w,h)
    glutInitWindowPosition(0, 0)
    wind = glutCreateWindow("Projek Grafkom")
    glutDisplayFunc(showScreen)
    glutIdleFunc(showScreen)
    glutSpecialFunc(mySpecialKeyboard)
    glutKeyboardFunc(mykeyboradSpeed)
    glutMouseFunc(btnklik)
    glutMainLoop()

main()