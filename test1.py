import pgzrun

城管_1 = Actor("城管_1")
城管_2 = Actor("城管_2")
城管_3 = Actor("城管_3")
张三 = Actor("张三_1")
顾客_1 = Actor("顾客_1")
顾客_2 = Actor("顾客_2")
顾客_3 = Actor("顾客_3")
顾客_4 = Actor("顾客_4")
标语 = Actor("标语")
广告牌 = Actor("广告牌")
商品_低1 = Actor("低_辣条")
商品_低2 = Actor("低_气球")
商品_中1 = Actor("中_魔方")
商品_中2 = Actor("中_雨伞")
商品_高1 = Actor("高_党章")
商品_高2 = Actor("高_飞机模型")
背景_1 = Actor("1_p大东门_1")
背景_2 = Actor("1_海淀区图书馆_1")
背景_3 = Actor("1_中关村地铁站_1")
背景_4 = Actor("2_工人体育馆_1")
背景_5 = Actor("2_三里屯_1")
背景_6 = Actor("2_广电总局_1")
背景_7 = Actor("3_北海公园门口_1")
背景_8 = Actor("3_胡同_1")
背景_9 = Actor("3_天安门_1")
背景1 = Actor("1_p大东门")
背景2 = Actor("1_海淀区图书馆")
背景3 = Actor("1_中关村地铁站")
背景4 = Actor("2_工人体育馆")
背景5 = Actor("2_三里屯")
背景6 = Actor("2_广电总局")
背景7 = Actor("3_北海公园门口")
背景8 = Actor("3_胡同")
背景9 = Actor("3_天安门")
button_1 = Actor("button_1")
button_2 = Actor("button_1")

WIDTH = 1000
HEIGHT = 1000

t = 0
s = 0
客流_概率 = 0.5
城管出现_概率 = 0.1
money = 0
级别 = 1
网红概率 = 0

def draw():
    global t
    global s
    global 级别,客流_概率,城管出现_概率,网红概率
    screen.fill((128, 128, 0))
    screen.draw.text(str(t / 60) + 's', (800, 0))
    screen.draw.text(str(s), (800, 20))
    screen.draw.text("level: "+str(级别), (800, 40))
    screen.draw.text("keliu： "+str(客流_概率), (800, 60))
    screen.draw.text("chenguan: "+str(城管出现_概率), (800, 80))
    screen.draw.text('money: '+str(money), (800, 100))
    screen.draw.text('wanghong: ' + str(网红概率), (800, 120))
    screen.draw.text(str(t), (800, 140))
    if t >=0 and t<= 120:
        screen.fill((0, 0, 0))
        标语.center = 500,500
        标语.draw()
    if t > 120 and t <= 240:

        张三.center = 500,500
        张三.draw()
        screen.draw.text('It has been one year since Zhang San graduated from school, but he still has not found a job',
                         (0, 0))
    if t > 240 and t <= 360:

        张三.center = 500, 500
        张三.draw()
        screen.draw.text('He heard that the policy encouraged stalls', (0, 20))
    if t > 360 and t <= 480:

        张三.center = 500, 500
        张三.draw()
        screen.draw.text('Zhang San was very excited and eager to try', (0, 40))
    if t > 480 and t <= 600:

        张三.center = 500, 500
        张三.draw()
        screen.draw.text('Let us see what zhang san can achieve ', (0, 60))
    if t > 600 and t <= 720:
        screen.draw.text('now you have'+str(money)+"RMB", (0, 0))

    if t >= 721:
        for i in range(0,7):

            if t > 720 and t <= 722 :
                t = 722
                if money >= 2000 and money <= 4000:
                    t = t - 1
                    screen.draw.text("if you want to get to a better place?", (0, 0))
                    button_1.center = 250,500
                    button_2.center = 750,500
                    button_1.draw()
                    button_2.draw()
            if t >= 723 and t <=843:
                screen.draw.text("you choose to stay here", (0, 0))
                级别 = 1
                客流_概率 = 0.5
                城管出现_概率 = 0.1
                if t == 843:
                    t = 1000
            if t >= 844 and t <= 964:
                screen.draw.text("you choose to leave here", (0, 0))
                级别 = 2
                客流_概率 = 0.7
                城管出现_概率 = 0.3


            if t >= 1000 and t <=1120:

                if 级别 == 1:
                    t = 1000
                    screen.draw.text("choose your position", (0, 0))
                    背景_1.center = 200,500
                    背景_2.center = 500, 500
                    背景_3.center = 800, 500
                    背景_1.draw()
                    背景_2.draw()
                    背景_3.draw()
                if 级别 == 2:
                    t = 1000
                    screen.draw.text("choose your position", (0, 0))
                    背景_4.center = 200, 500
                    背景_5.center = 500, 500
                    背景_6.center = 800, 500
                    背景_4.draw()
                    背景_5.draw()
                    背景_6.draw()
            if t >= 1121 and t <= 29921:
                if 级别 == 1:
                    背景1.center == 500, 500
                    背景1.draw()
                    screen.draw.text(str(t / 60) + 's', (800, 0))            #需补充主界面函数
                    screen.draw.text(str(s), (800, 20))
                    screen.draw.text("level: " + str(级别), (800, 40))
                    screen.draw.text("keliu： " + str(客流_概率), (800, 60))
                    screen.draw.text("chenguan: " + str(城管出现_概率), (800, 80))
                    screen.draw.text('money: ' + str(money), (800, 100))
                    screen.draw.text('wanghong: ' + str(网红概率), (800, 120))
                    screen.draw.text(str(t), (800, 140))
                if 级别 == 2:
                    背景4.center == 500, 500
                    背景4.draw()
            if t >= 30000 and t <= 58800 :
                if 级别 == 1:
                    背景2.center == 500, 500              #调用主界面函数
                    背景2.draw()

                if 级别 == 2:
                    背景5.center == 500, 500
                    背景5.draw()
            if t >= 60000 and t <= 88800:
                if 级别 == 1:                         #调用主界面函数
                    背景3.center == 500, 500
                    背景3.draw()
                if 级别 == 2:
                    背景6.center == 500, 500
                    背景6.draw()





def update():
    global t,money,s
    global 级别, 客流_概率, 城管出现_概率,网红概率
    t = t + 1
    s = s + 1
    if t == 600:
        money = 2000
    if t == 964:
        t = 1001


def on_mouse_down(pos):
    global t
    global 级别, 客流_概率, 城管出现_概率,网红概率
    if t == 721:
        if button_1.collidepoint(pos):
            t = 723

        if button_2.collidepoint(pos):
            t = 844
    if t == 1000:
        if 级别 == 1:
            if 背景_1.collidepoint(pos):
                客流_概率 = 客流_概率 + 0.1
                城管出现_概率 = 城管出现_概率 + 0.1
                网红概率 = 网红概率 + 0.1
                t = 1121
            if 背景_2.collidepoint(pos):
                客流_概率 = 客流_概率 + 0.2
                城管出现_概率 = 城管出现_概率 + 0.2
                网红概率 = 网红概率 + 0.2
                t = 30000
            if 背景_3.collidepoint(pos):
                客流_概率 = 客流_概率 + 0.3
                城管出现_概率 = 城管出现_概率 + 0.3
                网红概率 = 网红概率 + 0.3
                t = 60000
        if 级别 == 2:
            if 背景_4.collidepoint(pos):
                客流_概率 = 客流_概率 + 0.4
                城管出现_概率 = 城管出现_概率 + 0.4
                网红概率 = 网红概率 + 0.4
                t = 1121
            if 背景_5.collidepoint(pos):
                客流_概率 = 客流_概率 + 0.5
                城管出现_概率 = 城管出现_概率 + 0.5
                网红概率 = 网红概率 + 0.5
                t = 30000
            if 背景_6.collidepoint(pos):
                客流_概率 = 客流_概率 + 0.6
                城管出现_概率 = 城管出现_概率 + 0.6
                网红概率 = 网红概率 + 0.6
                t = 60000


pgzrun.go()