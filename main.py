import pygame
import time
from pygame import mixer

#cores
preto = (0, 0, 0)
branco = (255, 255, 255)
vermelho = (255, 0, 0)
cinza = (220, 220, 220)
a = (177, 156, 217)
#inicializando a biblioteca e a janela
pygame.init()

largura = 1200
altura = 485
tela_tamanho = (largura, altura)
tela = pygame.display.set_mode(tela_tamanho)

pygame.display.set_caption('Matrix')

pausa = 60
relogio = pygame.time.Clock()
def menu():
  telainicial = pygame.image.load("tela inicial.png")
  tela.blit(telainicial, (0, 0))
  pygame.display.update()
#ajustando a posição dos fundos

running = False

#loop principal do jogo
running = False
acaboupoha = False
fimdojogo = False
while acaboupoha == False:
    while running == False:
        menu()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                mouse_x = mouse_pos[0]
                mouse_y = mouse_pos[1]
                if 330.2811 < mouse_x < 874.6011 and 296.0989 < mouse_y < 380.3489:
                    running = True
                    runni = False
                    runnin = False
                    valor_fase = 1



                    pos_fundo1_x = 130
                    pos_fundo1_y = altura
                    
                    pos_fundo2_x = 1040
                    pos_fundo2_y = altura
                    
                    #ajustando fonte e posiçaõ do contador das fases
                    pos_fase_x = 20
                    pos_fase_y = 440
                    fonte = pygame.font.Font('timesnewroman.ttf', 30)
                    fa = pygame.font.Font('timesnewroman.ttf', 10)
                    fontemenu = pygame.font.Font('timesnewroman.ttf', 100)
                    valor_fase = 1
                    
                    
                    
                    
                    
                    #fundo verde da esquerda
                    def planodefundo1():
                        fundo = pygame.image.load("Fundo Verde.jpg")
                        fundo1 = pygame.transform.scale(fundo, (130, altura))
                        tela.blit(fundo1, (0, 0))
                    
                    
                    #fundo verde da direita
                    def planodefundo2():
                        fundo = pygame.image.load("Fundo Verde.jpg")
                        fundo2 = pygame.transform.scale(fundo, (1040, altura))
                    
                        tela.blit(fundo2, (1040, 0))
                    
                    
                    #contador de fase
                    def mostrarfase(x, y):
                        fase = fonte.render('Fase ' + str(valor_fase), True, (0, 0, 0))
                        tela.blit(fase, (x, y))
                    
                    
                    #tela de fim de jogo
                    def fimdejogo(x, y):
                        gameover = pygame.image.load("Game Over.png")
                        gameover_ = pygame.transform.scale(gameover, (largura, altura))
                        tela.blit(gameover_, (0, 0))
                        pygame.display.update()
                    
                    
                    def level1():
                        level = pygame.image.load("levels/1x/level1.png")
                        tela.blit(level, (0, 0))
                        pygame.display.update()
                    
                    
                    def level2():
                        level2 = pygame.image.load("levels/1x/level2.png")
                        tela.blit(level2, (0, 0))
                        pygame.display.update()
                    
                    
                    def level3():
                        level3 = pygame.image.load("levels/1x/level3.png")
                        tela.blit(level3, (0, 0))
                        pygame.display.update()
                    
                    
                    def level4():
                        level4 = pygame.image.load("levels/1x/level4.png")
                        tela.blit(level4, (0, 0))
                        pygame.display.update()
                    
                    
                    def level5():
                        level5 = pygame.image.load("levels/1x/level5.png")
                        tela.blit(level5, (0, 0))
                        pygame.display.update()
                    
                    
                    def level6():
                        level6 = pygame.image.load("levels/1x/level6.png")
                        tela.blit(level6, (0, 0))
                        pygame.display.update()
                    
                    
                    #tela de vitoria
                    def win(x, y):
                        youwin = pygame.image.load("Fundo Youwin.jpg")
                        youwin_ = pygame.transform.scale(youwin, (largura, altura))
                        tela.blit(youwin_, (0, 0))
                        pygame.display.update()
                    
                    
                    #musica de fundo
                    
                    
                    #musica de colisao
                    barulho_colisao = mixer.Sound("audiocolisao.mpeg")
                    barulho_colisao.set_volume(0.1)
                    
                    #musica de vitoria
                    barulho_vitoria = mixer.Sound("audiovitoria.mpeg")
                    barulho_vitoria.set_volume(0.1)
                    
                    #criando as dimensões do boneco e dos misseis
                    boneco = pygame.Rect(80, 242, 30, 30)
                    
                    rect_0 = pygame.Rect(-85, -90, 20, 20)
                    rect_1 = pygame.Rect(150, -20, 20, 20)
                    rect_2 = pygame.Rect(350, -20, 20, 20)
                    rect_3 = pygame.Rect(550, -20, 20, 20)
                    rect_4 = pygame.Rect(750, -20, 20, 20)
                    rect_5 = pygame.Rect(950, -20, 20, 20)
                    rect_6 = pygame.Rect(215, 505, 20, 20)
                    rect_7 = pygame.Rect(415, 505, 20, 20)
                    rect_8 = pygame.Rect(615, 505, 20, 20)
                    rect_9 = pygame.Rect(815, 505, 20, 20)
                    rect_10 = pygame.Rect(1015, 505, 20, 20)
                    #viloes da fase 2
                    rect_falso = pygame.Rect(-200000, -2000000, 1, 1)
                    rect_11 = pygame.Rect(1010, 30, 20, 20)
                    rect_12 = pygame.Rect(1010, 110, 20, 20)
                    rect_13 = pygame.Rect(1010, 190, 20, 20)
                    rect_14 = pygame.Rect(1010, 270, 20, 20)
                    rect_15 = pygame.Rect(1010, 350, 20, 20)
                    rect_16 = pygame.Rect(1010, 430, 20, 20)
                    
                    rect_17 = pygame.Rect(140, 60, 20, 20)
                    rect_18 = pygame.Rect(140, 140, 20, 20)
                    rect_19 = pygame.Rect(140, 220, 20, 20)
                    rect_20 = pygame.Rect(140, 300, 20, 20)
                    rect_21 = pygame.Rect(140, 380, 20, 20)
                    rect_22 = pygame.Rect(140, 460, 20, 20)
                    
                    rect_falso = pygame.Rect(-1010191920, -19299210100, 1, 1)
                    rect_23_2 = pygame.Rect(200, 20, 20, 20)
                    rect_23 = pygame.Rect(300, 20, 20, 20)
                    rect_24 = pygame.Rect(400, 20, 20, 20)
                    rect_25 = pygame.Rect(500, 20, 20, 20)
                    rect_26 = pygame.Rect(600, 20, 20, 20)
                    rect_27 = pygame.Rect(700, 20, 20, 20)
                    rect_28 = pygame.Rect(800, 20, 20, 20)
                    rect_29 = pygame.Rect(900, 20, 20, 20)
                    rect_30 = pygame.Rect(1000, 20, 20, 20)
                    
                    rect_31_1 = pygame.Rect(140, 465, 20, 20)
                    rect_31 = pygame.Rect(240, 465, 20, 20)
                    rect_32 = pygame.Rect(340, 465, 20, 20)
                    rect_33 = pygame.Rect(440, 465, 20, 20)
                    rect_34 = pygame.Rect(540, 465, 20, 20)
                    rect_35 = pygame.Rect(640, 465, 20, 20)
                    rect_36 = pygame.Rect(740, 465, 20, 20)
                    rect_37 = pygame.Rect(840, 465, 20, 20)
                    rect_38 = pygame.Rect(940, 465, 20, 20)
                    rect_39 = pygame.Rect(1030, 465, 20, 20)
                    
                    rect_40 = pygame.Rect(1020, 20, 20, 20)
                    rect_41 = pygame.Rect(1020, 100,20, 20)
                    rect_42_2 = pygame.Rect(1020, 180, 20, 20)
                    rect_42_3= pygame.Rect(1020, 260 ,20, 20)
                    rect_42 = pygame.Rect(1020, 340, 20, 20)
                    rect_43 = pygame.Rect(1020, 420, 20, 20)
                    
                    rect_44 = pygame.Rect(130, 20, 20, 20)
                    rect_45= pygame.Rect(230,20 ,20, 20)
                    rect_46 = pygame.Rect(330, 20, 20, 20)
                    rect_47 = pygame.Rect(430, 20, 20, 20)
                    rect_48 = pygame.Rect(530, 20, 20, 20)
                    rect_49 = pygame.Rect(630, 20, 20, 20)
                    rect_50= pygame.Rect(730,20 ,20, 20)
                    rect_51 = pygame.Rect(830, 20, 20, 20)
                    rect_52 = pygame.Rect(930, 20, 20, 20)
                    rect_53= pygame.Rect(1000, 20, 20, 20)
                    
                    
                    rect_54= pygame.Rect(130, 0, 70, 242.5)
                    rect_55= pygame.Rect(970,0,70, 242.5)
                    rect_56= pygame.Rect(565, 242.5, 70,242.5)
                    rect_57= pygame.Rect(250,0,265,70)
                    rect_58= pygame.Rect(685, 415, 235,70)
                    
                    
                    vel_54=+0.15
                    vel_55=+0.15
                    vel_56=-0.15
                    vel_57=+0.13
                    vel_58=+0.13
                    
                    
                    rect_59= pygame.Rect(130, 0, 70, 242.5)
                    rect_60= pygame.Rect(970,0,70, 242.5)
                    rect_61= pygame.Rect(565, 242.5, 70,242.5)
                    rect_62= pygame.Rect(250,0,100, 70)
                    rect_63= pygame.Rect(400,415,100, 70)
                    rect_64= pygame.Rect(680,0,100, 70)
                    rect_65= pygame.Rect(820,415,100, 70)
                    
                    
                    
                    
                    
                    
                    
                    vel_59=0.15
                    vel_60=0.15
                    vel_61=-0.15
                    vel_62=0.13
                    vel_63=-0.16
                    vel_64=0.13
                    vel_65=-0.16
                    
                    
                    misseis6=[rect_falso,rect_59,rect_60,rect_61,rect_62,rect_63,rect_64,rect_65]
                    
                    
                    
                    misseis4=[rect_falso,rect_40,rect_41,rect_42,rect_42_2,rect_42_3,rect_43,rect_44,rect_45,rect_46,rect_47,rect_48,rect_49,rect_50,rect_51,rect_52,rect_53]
                    
                    vel_fase3=0.25
                    vel_fase3_2=-0.25
                    
                    misseis5=[rect_falso,rect_54,rect_55,rect_56,rect_57,rect_58]
                    
                    
                    
                    misseis1 = [
                        rect_0, rect_1, rect_2, rect_3, rect_4, rect_5, rect_6, rect_7, rect_8,
                        rect_9, rect_10
                    ]
                    misseis2 = [
                        rect_falso, rect_11, rect_12, rect_13, rect_14, rect_15, rect_16, rect_17,
                        rect_18, rect_19, rect_20, rect_21, rect_22
                    ]
                    
                    misseis3 = [
                        rect_falso, rect_23, rect_23_2, rect_31_1, rect_24, rect_25, rect_26,
                        rect_27, rect_28, rect_29, rect_30, rect_31, rect_32, rect_33, rect_34,
                        rect_35, rect_36, rect_37, rect_38
                    ]
                    
                    q_flaso_fase2 = pygame.Rect(-10001991, -1991020992, 1, 1)
                    
                    vel_1 = -0.10
                    #velocidade inicial do boneco e retângulos
                    velocidade_boneco_y = 0
                    velocidade_boneco_x = 0
                    
                    vel_rect_fase21 = -0.30
                    vel_rect_fase22 = 0.30
                    
                    vel_rect_cima_1 = 0.15
                    
                    vel_rect_baixo_1 = -0.15
                    
                    vel_rect_cima_3 = 0.15
                    
                    vel_rect_baixo_3 = -0.15
                    
                    vel_rect_baixo_2 = -0.30
                    
                    vel_rect_baixo_3 = -0.20
                    
                    vel_rect_cima_3 = 0.20
                    
                    vel_rect5=0.20
                    vel_rect5_2=-0.20
                    
                    fimdojogo = False
                    while not fimdojogo:

                        delta = relogio.tick(60)
                      

                        #fazendo os bonecos e misseis se moverem para uma direção infinitamente

                        boneco.move_ip(velocidade_boneco_x * delta,
                                       velocidade_boneco_y * delta)
                        if valor_fase == 1:
                            rect_1.move_ip(0, vel_rect_cima_1 * delta)
                            rect_2.move_ip(0, vel_rect_cima_1 * delta)
                            rect_3.move_ip(0, vel_rect_cima_1 * delta)
                            rect_4.move_ip(0, vel_rect_cima_1 * delta)
                            rect_5.move_ip(0, vel_rect_cima_1 * delta)
                            rect_6.move_ip(0, delta * vel_rect_baixo_1)
                            rect_7.move_ip(0, delta * vel_rect_baixo_1)
                            rect_8.move_ip(0, delta * vel_rect_baixo_1)
                            rect_9.move_ip(0, delta * vel_rect_baixo_1)
                            rect_10.move_ip(0, delta * vel_rect_baixo_1)
                        if valor_fase == 2:
                            rect_11.move_ip(delta * vel_rect_fase21, 0)
                            rect_12.move_ip(delta * vel_rect_fase21, 0)
                            rect_13.move_ip(delta * vel_rect_fase21, 0)
                            rect_14.move_ip(delta * vel_rect_fase21, 0)
                            rect_15.move_ip(delta * vel_rect_fase21, 0)
                            rect_16.move_ip(delta * vel_rect_fase21, 0)

                            rect_17.move_ip(delta * vel_rect_fase22, 0)
                            rect_18.move_ip(delta * vel_rect_fase22, 0)
                            rect_19.move_ip(delta * vel_rect_fase22, 0)
                            rect_20.move_ip(delta * vel_rect_fase22, 0)
                            rect_21.move_ip(delta * vel_rect_fase22, 0)
                            rect_22.move_ip(delta * vel_rect_fase22, 0)

                            if rect_11.left <140:
                                vel_rect_fase21 = 0.30
                            elif rect_11.left > 1010:
                                vel_rect_fase21 = -0.30
                            if rect_22.left > 1010:
                                vel_rect_fase22 = -0.30
                            elif rect_22.left < 140:
                                vel_rect_fase22 = 0.30
                        elif valor_fase == 3:
                            rect_23_2.move_ip(0, vel_rect_cima_3 * delta)
                            rect_23.move_ip(0, vel_rect_cima_3 * delta)
                            rect_24.move_ip(0, vel_rect_cima_3 * delta)
                            rect_25.move_ip(0, vel_rect_cima_3 * delta)
                            rect_26.move_ip(0, vel_rect_cima_3 * delta)
                            rect_27.move_ip(0, vel_rect_cima_3 * delta)
                            rect_28.move_ip(0, vel_rect_cima_3 * delta)
                            rect_29.move_ip(0, vel_rect_cima_3 * delta)
                            rect_30.move_ip(0, vel_rect_cima_3 * delta)

                            if rect_30.top > 465:
                                vel_rect_cima_3 = -0.20
                            elif rect_30.top < 0:
                                vel_rect_cima_3 = 0.20
                            rect_31_1.move_ip(0, vel_rect_baixo_3 * delta)
                            rect_31.move_ip(0, vel_rect_baixo_3 * delta)
                            rect_32.move_ip(0, vel_rect_baixo_3 * delta)
                            rect_33.move_ip(0, vel_rect_baixo_3 * delta)
                            rect_34.move_ip(0, vel_rect_baixo_3 * delta)
                            rect_35.move_ip(0, vel_rect_baixo_3 * delta)
                            rect_36.move_ip(0, vel_rect_baixo_3 * delta)
                            rect_37.move_ip(0, vel_rect_baixo_3 * delta)
                            rect_38.move_ip(0, vel_rect_baixo_3 * delta)
                            rect_39.move_ip(0, vel_rect_baixo_3 * delta)

                            if rect_38.top < 0:
                                vel_rect_baixo_3 = 0.20
                            elif rect_38.top > 465:
                                vel_rect_baixo_3 = -0.20

                     
                        if valor_fase==4:
                            rect_40.move_ip(vel_fase3_2* delta,0)
                            rect_41.move_ip(vel_fase3_2 * delta,0)
                            rect_42.move_ip(vel_fase3_2 * delta,0)
                            rect_42_2.move_ip(vel_fase3_2 * delta,0)
                            rect_42_3.move_ip(vel_fase3_2 * delta,0)
                            rect_43.move_ip( vel_fase3_2* delta,0)
                            if rect_40.left<130:
                              vel_fase3_2=0.25
                            elif rect_40.left>1020:
                               vel_fase3_2=-0.25
                              

                            rect_44.move_ip(0, vel_fase3* delta)
                            rect_45.move_ip(0, vel_fase3 * delta)
                            rect_46.move_ip(0, vel_fase3* delta)
                            rect_47.move_ip(0, vel_fase3* delta)
                            rect_48.move_ip(0, vel_fase3* delta)
                            rect_49.move_ip(0, vel_fase3 * delta)
                            rect_50.move_ip(0, vel_fase3* delta)
                            rect_51.move_ip(0, vel_fase3* delta)
                            rect_52.move_ip(0, vel_fase3* delta)
                            rect_53.move_ip(0, vel_fase3* delta) 
                            if rect_45.top>465:
                              vel_fase3=-0.25
                            elif rect_45.top<20:
                              vel_fase3=0.25
                        elif valor_fase==5:
                          
                          rect_54.move_ip(0,vel_54*delta)
                          rect_55.move_ip(0,vel_55*delta)
                          rect_56.move_ip(0,vel_56*delta)
                          rect_57.move_ip(0,vel_57*delta)
                          rect_58.move_ip(0,vel_58*delta)
                          
                              
                          if rect_54.top<0:
                            vel_54= +0.15
                          elif rect_54.top>242.5:
                            vel_54= -0.15
                          if rect_55.top<0:
                            vel_55= +0.15
                          elif rect_55.top>242.5:
                            vel_55= -0.15
                          if rect_56.top<0:
                            vel_56= +0.15
                          elif rect_56.top>242.5:
                            vel_56= -0.15
                          if rect_57.top<0:
                            vel_57= +0.13
                          elif rect_57.top>415:
                            vel_57= -0.13
                          if rect_58.top<0:
                            vel_58= +0.13
                          elif rect_58.top>415:
                            vel_58= -0.13
  
                        elif valor_fase==6:
                          rect_59.move_ip(0,vel_59*delta)
                          rect_60.move_ip(0,vel_60*delta)
                          rect_61.move_ip(0,vel_61*delta)
                          rect_62.move_ip(0,vel_62*delta)
                          rect_63.move_ip(0,vel_63*delta)
                          rect_64.move_ip(0,vel_64*delta)
                          rect_65.move_ip(0,vel_65*delta)
                         
                          if rect_59.top<0:
                            vel_59= +0.15
                          elif rect_59.top>250:
                            vel_59= -0.15
                          if rect_60.top<0:
                            vel_60= +0.15
                          elif rect_60.top>250:
                            vel_60= -0.15
                          if rect_61.top<0:
                            vel_61= +0.15
                          elif rect_61.top>250:
                            vel_61= -0.15
                          if rect_62.top<0:
                            vel_62= +0.13
                          elif rect_62.top>415:
                            vel_62= -0.13
                          if rect_63.top<0:
                            vel_63= +0.16
                          elif rect_63.top>415:
                            vel_63= -0.16
                          if rect_64.top<0:
                            vel_64= +0.13
                          elif rect_64.top>415:
                            vel_64= -0.13
                          if rect_65.top<0:
                            vel_65= +0.16
                          elif rect_65.top>415:
                            vel_65= -0.16
            

                            
                       
                          
                                            

                      
                          
                          
                            
                        if boneco.top > 505 or boneco.top < -20 or boneco.left < -20:
                            while runni == False:
                                fimdejogo(largura, altura)
                                for event in pygame.event.get():
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        mouse_posiI = pygame.mouse.get_pos()
                                        mouse_x = mouse_posiI[0]
                                        mouse_y = mouse_posiI[1]
                                        if 415.4 < mouse_x < 771.08 and 172.6 < mouse_y < 264.76:
                                            runni = True
                                            running = False
                                            runnin = False
                                            valor_fase = 0
                                            fimdojogo = True
                                            boneco.left = 80
                                            boneco.top = 242.5
                                            velocidade_boneco_x = 0
                                            velocidade_boneco_y = 0
                                        elif 415.4 < mouse_x < 771.08 and 307.6 < mouse_y < 399.32:
                                            time.sleep(1)
                                            runni = True
                                            fimdojogo = True
                                            acaboupoha = True

                        if rect_1.top > 505:
                            rect_1.top = -22
                            rect_2.top = -22
                            rect_3.top = -22
                            rect_4.top = -22
                            rect_5.top = -22

                        if rect_6.top < -22:
                            rect_6.top = 505
                            rect_7.top = 505
                            rect_8.top = 505
                            rect_9.top = 505
                            rect_10.top = 505

                        #verificando se está tocando nos cantos da janela
                        

                        if valor_fase == 1:

                            while runnin == False:
                                level1()
                                for event in pygame.event.get():
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        mouse_posi = pygame.mouse.get_pos()
                                        mouse_x = mouse_posi[0]
                                        mouse_y = mouse_posi[1]
                                        if 308.5072 < mouse_x < 503.6879 and 115.241 < mouse_y < 285.1205:
                                            runnin = True

                                    elif event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_SPACE:
                                            runnin = True

                            tela.fill(cinza)
                            planodefundo1()
                            planodefundo2()
                            mostrarfase(pos_fase_x, pos_fase_y)
                            colisao1 = boneco.collidelist(misseis1)

                            #desenhando o boneco

                            pygame.draw.rect(tela, preto, boneco)

                            #desenhando os retângulos
                            for ret in misseis1:
                                pygame.draw.rect(tela, vermelho, ret)
                            if colisao1 > 0:
                                barulho_colisao.play()
                                print(colisao1)
                                time.sleep(1)

                                while runni == False:
                                    fimdejogo(largura, altura)
                                    for event in pygame.event.get():
                                        if event.type == pygame.MOUSEBUTTONDOWN:
                                            mouse_posiI = pygame.mouse.get_pos(
                                            )
                                            mouse_x = mouse_posiI[0]
                                            mouse_y = mouse_posiI[1]
                                            if 415.4 < mouse_x < 771.08 and 172.6 < mouse_y < 264.76:
                                                runni = True
                                                running = False
                                                runnin = False
                                                valor_fase = 0
                                                fimdojogo = True
                                                boneco.left = 80
                                                boneco.top = 242.5
                                                velocidade_boneco_x = 0
                                                velocidade_boneco_y = 0
                                            elif 415.4 < mouse_x < 771.08 and 307.6 < mouse_y < 399.32:
                                                time.sleep(1)
                                                runni = True
                                                fimdojogo = True
                                                acaboupoha = True

                            elif boneco.left >= 1040:

                                boneco.left = 80
                                boneco.top = 230
                                velocidade_boneco_x = 0
                                velocidade_boneco_y = 0
                                valor_fase += 1
                                runnin = False
                                runni = False

                            pygame.display.update()
                        elif valor_fase == 2:
                            while runnin == False:
                                level2()
                                for event in pygame.event.get():
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        mouse_posi = pygame.mouse.get_pos()
                                        mouse_x = mouse_posi[0]
                                        mouse_y = mouse_posi[1]
                                        if 528.2418 < mouse_x < 723.4225 and 115.241 < mouse_y < 285.2501:
                                            runnin = True

                                    elif event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_SPACE:
                                            runnin = True

                            tela.fill(cinza)

                            x2 = 1050
                            y2 = 242.5
                            for ret in misseis2:
                                pygame.draw.rect(tela, vermelho, ret)

                            planodefundo1()
                            planodefundo2()

                            mostrarfase(pos_fase_x, pos_fase_y)

                            #desenhando o boneco

                            pygame.draw.rect(tela, preto, boneco)
                            colisao2 = boneco.collidelist(misseis2)
                            if colisao2 > 0:
                                mixer.music.set_volume(0)
                                barulho_colisao.play()
                                print(colisao2)
                                time.sleep(1)

                                while runni == False:
                                    fimdejogo(largura, altura)
                                    for event in pygame.event.get():
                                        if event.type == pygame.MOUSEBUTTONDOWN:
                                            mouse_posiI = pygame.mouse.get_pos(
                                            )
                                            mouse_x = mouse_posiI[0]
                                            mouse_y = mouse_posiI[1]
                                            if 415.4 < mouse_x < 771.08 and 172.6 < mouse_y < 264.76:
                                                runni = True
                                                running = False
                                                runnin = False
                                                valor_fase = 0
                                                fimdojogo = True
                                                boneco.left = 80
                                                boneco.top = 242.5
                                                velocidade_boneco_x = 0
                                                velocidade_boneco_y = 0
                                            elif 415.4 < mouse_x < 771.08 and 307.6 < mouse_y < 399.32:
                                                time.sleep(1)
                                                runni = True
                                                fimdojogo = True
                                                acaboupoha = True

                            elif boneco.left >= 1040:
                                boneco.left = 80
                                boneco.top = 230
                                velocidade_boneco_x = 0
                                velocidade_boneco_y = 0

                                valor_fase += 1
                                runnin = False
                                runni = False

                                #desenhando os retângulos

                            pygame.display.update()
                        elif valor_fase == 3:
                            while runnin == False:
                                level3()
                                for event in pygame.event.get():
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        mouse_posii = pygame.mouse.get_pos()
                                        mouse_x3 = mouse_posii[0]
                                        mouse_y3 = mouse_posii[1]
                                        if 723.4225 < mouse_x3 < 918.6032 and 115.241 < mouse_y3 < 285.2501:
                                            runnin = True

                                    elif event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_SPACE:
                                            runnin = True

                            tela.fill(cinza)

                            for ret in misseis3:
                                pygame.draw.rect(tela, vermelho, ret)
                            planodefundo1()
                            planodefundo2()
                            mostrarfase(pos_fase_x, pos_fase_y)

                            pygame.draw.rect(tela, preto, boneco)

                            colisao3 = boneco.collidelist(misseis3)
                            if colisao3 > 0:
                                
                                barulho_colisao.play()
                                print(colisao2)
                                while runni == False:
                                    fimdejogo(largura, altura)
                                    for event in pygame.event.get():
                                        if event.type == pygame.MOUSEBUTTONDOWN:
                                            mouse_posiI = pygame.mouse.get_pos(
                                            )
                                            mouse_x = mouse_posiI[0]
                                            mouse_y = mouse_posiI[1]
                                            if 415.4 < mouse_x < 771.08 and 172.6 < mouse_y < 264.76:
                                                runni = True
                                                running = False
                                                runnin = False
                                                valor_fase = 0
                                                fimdojogo = True
                                                boneco.left = 80
                                                boneco.top = 242.5
                                                velocidade_boneco_x = 0
                                                velocidade_boneco_y = 0
                                            elif 415.4 < mouse_x < 771.08 and 307.6 < mouse_y < 399.32:
                                                time.sleep(1)
                                                runni = True
                                                fimdojogo = True
                                                acaboupoha = True

                            elif valor_fase == 3:
                                if boneco.left >= 1040:
                                    boneco.left = 80
                                    boneco.top = 230
                                    velocidade_boneco_x = 0
                                    velocidade_boneco_y = 0

                                    valor_fase += 1
                                    runnin = False
                                    runni = False

                            pygame.display.update()
                        elif valor_fase == 4:
                            while runnin == False:
                                level4()
                                for event in pygame.event.get():
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        mouse_posi = pygame.mouse.get_pos()
                                        mouse_x = mouse_posi[0]
                                        mouse_y = mouse_posi[1]
                                        if 307.8862  < mouse_x < 503.0669  and 307.8862  < mouse_y <475.4911  :
                                            runnin = True

                                    elif event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_SPACE:
                                            runnin = True

                            tela.fill(cinza)
                           
                            planodefundo1()
                            planodefundo2()
                            mostrarfase(pos_fase_x, pos_fase_y)
                            pygame.draw.rect(tela, preto, boneco)
                            for ret in misseis4:
                              pygame.draw.rect(tela, vermelho, ret)
                            
                            mostrarfase(pos_fase_x, pos_fase_y)
                            colisao_4=boneco.collidelist(misseis4)
                            if colisao_4>0:
                              
                             
                              barulho_colisao.play()
                              print(colisao2)
                              while runni == False:
                                  fimdejogo(largura, altura)
                                  for event in pygame.event.get():
                                      if event.type == pygame.MOUSEBUTTONDOWN:
                                          mouse_posiI = pygame.mouse.get_pos(
                                          )
                                          mouse_x = mouse_posiI[0]
                                          mouse_y = mouse_posiI[1]
                                          if 415.4 < mouse_x < 771.08 and 172.6 < mouse_y < 264.76:
                                              runni = True
                                              running = False
                                              runnin = False
                                              valor_fase = 0
                                              fimdojogo = True
                                              boneco.left = 80
                                              boneco.top = 242.5
                                              velocidade_boneco_x = 0
                                              velocidade_boneco_y = 0
                                          elif 415.4 < mouse_x < 771.08 and 307.6 < mouse_y < 399.32:
                                              time.sleep(1)
                                              runni = True
                                              fimdojogo = True
                                              acaboupoha = True
                                          
                            elif boneco.left>1040:
                              
                                boneco.left = 80
                                boneco.top = 230
                                velocidade_boneco_x = 0
                                velocidade_boneco_y = 0

                                valor_fase += 1
                                runnin = False
                                runni = False
                    
                            pygame.display.update()
                        elif valor_fase==5:
                            while runnin == False:
                              level5()
                              for event in pygame.event.get():
                                  if event.type == pygame.MOUSEBUTTONDOWN:
                                      mouse_posi = pygame.mouse.get_pos()
                                      mouse_x = mouse_posi[0]
                                      mouse_ = mouse_posi[1]
                                      if 527.8741  < mouse_x < 723.0548 and 307.8862  < mouse_y <475.4911  :
                                          runnin = True

                                  elif event.type == pygame.KEYDOWN:
                                      if event.key == pygame.K_SPACE:
                                          runnin = True

                            tela.fill(cinza)
                           
                            planodefundo1()
                            planodefundo2()
                            mostrarfase(pos_fase_x, pos_fase_y)
                            pygame.draw.rect(tela, preto, boneco)
                            for ret in misseis5:
                              pygame.draw.rect(tela, vermelho, ret)
                            
                            mostrarfase(pos_fase_x, pos_fase_y)
                            colisao_5=boneco.collidelist(misseis5
                                                        )
                            if colisao_5>0:
                              
                              
                              barulho_colisao.play()
                              print(colisao2)
                              while runni == False:
                                  fimdejogo(largura, altura)
                                  for event in pygame.event.get():
                                      if event.type == pygame.MOUSEBUTTONDOWN:
                                          mouse_posiI = pygame.mouse.get_pos(
                                          )
                                          mouse_x = mouse_posiI[0]
                                          mouse_y = mouse_posiI[1]
                                          if 415.4 < mouse_x < 771.08 and 172.6 < mouse_y < 264.76:
                                              runni = True
                                              running = False
                                              runnin = False
                                              valor_fase = 0
                                              fimdojogo = True
                                              boneco.left = 80
                                              boneco.top = 242.5
                                              velocidade_boneco_x = 0
                                              velocidade_boneco_y = 0
                                          elif 415.4 < mouse_x < 771.08 and 307.6 < mouse_y < 399.32:
                                              time.sleep(1)
                                              runni = True
                                              fimdojogo = True
                                              acaboupoha = True
                                          
                            elif boneco.left>1040:
                              
                                boneco.left = 80
                                boneco.top = 230
                                velocidade_boneco_x = 0
                                velocidade_boneco_y = 0

                                valor_fase += 1
                                runnin = False
                                runni = False
                              
                    
                            pygame.display.update()
                        elif valor_fase==6:
                            while runnin == False:
                                level6()
                                for event in pygame.event.get():
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        mouse_posi = pygame.mouse.get_pos()
                                        mouse_x = mouse_posi[0]
                                        mouse_ = mouse_posi[1]
                                        if 723.4225 < mouse_x3 < 918.6032 and 307.8862  < mouse_y <475.4911  :
                                            runnin = True
  
                                    elif event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_SPACE:
                                            runnin = True

                            tela.fill(cinza)
                           
                            planodefundo1()
                            planodefundo2()
                            mostrarfase(pos_fase_x, pos_fase_y)
                            pygame.draw.rect(tela, preto, boneco)
                            for ret in misseis6:
                              pygame.draw.rect(tela, vermelho, ret)
                            
                            mostrarfase(pos_fase_x, pos_fase_y)
                            colisao_6=boneco.collidelist(misseis6)
                            if colisao_6>0:
                              
                              
                              barulho_colisao.play()
                              print(colisao2)
                              while runni == False:
                                  fimdejogo(largura, altura)
                                  for event in pygame.event.get():
                                      if event.type == pygame.MOUSEBUTTONDOWN:
                                          mouse_posiI = pygame.mouse.get_pos(
                                          )
                                          mouse_x = mouse_posiI[0]
                                          mouse_y = mouse_posiI[1]
                                          if 415.4 < mouse_x < 771.08 and 172.6 < mouse_y < 264.76:
                                              runni = True
                                              running = False
                                              runnin = False
                                              valor_fase = 0
                                              fimdojogo = True
                                              boneco.left = 80
                                              boneco.top = 242.5
                                              velocidade_boneco_x = 0
                                              velocidade_boneco_y = 0
                                          elif 415.4 < mouse_x < 771.08 and 307.6 < mouse_y < 399.32:
                                              time.sleep(1)
                                              runni = True
                                              fimdojogo = True
                                              acaboupoha = True
                                          
                            elif boneco.left>1040:
                              
                               
                                velocidade_boneco_x = 0
                                velocidade_boneco_y = 0

                                valor_fase += 1
                    
                            pygame.display.update()
                          
                        elif valor_fase == 7:
                            barulho_vitoria.play()
                            win(largura, altura)
                            time.sleep(3)
                            fimdojogo = True
                            acaboupoha=True

                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                acaboupoha = True
                            if event.type == pygame.KEYDOWN:

                                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                                    velocidade_boneco_y = +0.2
                                    velocidade_boneco_x = 0
                                if event.key == pygame.K_w or event.key == pygame.K_UP:
                                    velocidade_boneco_y = -0.2
                                    velocidade_boneco_x = 0
                                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                                    velocidade_boneco_x = -0.2
                                    velocidade_boneco_y = 0

                                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                                    velocidade_boneco_x = +0.2
                                    velocidade_boneco_y = 0
