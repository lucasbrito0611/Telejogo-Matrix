import pygame
import time

#cores
preto = (0, 0, 0)
branco = (255, 255, 255)
vermelho = (255, 0, 0)
cinza = (220, 220, 220)

#inicializando a biblioteca e a janela
pygame.init()
largura = 1200
altura = 485
tela_tamanho = (largura, altura)
tela = pygame.display.set_mode(tela_tamanho)

pygame.display.set_caption('Matrix')

pausa = 60
relogio = pygame.time.Clock()



#ajustando a posição dos fundos 
pos_fundo1_x = 130
pos_fundo1_y = altura

pos_fundo2_x = 1040
pos_fundo2_y = altura

#ajustando fonte e posiçaõ do contador das fases
pos_fase_x = 20
pos_fase_y = 440
fonte = pygame.font.Font('timesnewroman.ttf', 30)
valor_fase = 1



#fundo verde da esquerda
def planodefundo1(x,y):
    fundo = pygame.image.load("Fundo Verde.jpg")
    fundo1 = pygame.transform.scale(fundo, (130, altura))
    tela.blit(fundo1, (0, 0))

#fundo verde da direita
def planodefundo2(x,y):
    fundo = pygame.image.load("Fundo Verde.jpg")
    fundo2 = pygame.transform.scale(fundo, (1040, altura))
    tela.blit(fundo2, (1040, 0))

#contador de fase
def mostrarfase(x,y):
    fase = fonte.render('Fase ' + str(valor_fase), True, (0,0,0))
    tela.blit(fase, (x,y))

#tela de vitoria
def win(x,y):
    youwin = pygame.image.load("Fundo Youwin.jpg")
    youwin_ = pygame.transform.scale(youwin, (largura, altura))
    tela.blit(youwin_, (0,0))
    pygame.display.update()

#tela de inicio
def menu():
    telainicial = pygame.image.load("tela inicial.png")
    tela.blit(telainicial,(0,0))
    pygame.display.update()

#tela de game over
def fimdejogo(x, y):
    gameover = pygame.image.load("Game Over.png")
    gameover_ = pygame.transform.scale(gameover, (largura, altura))
    tela.blit(gameover_, (0, 0))
    pygame.display.update()

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

misseis = [rect_0, rect_1, rect_2, rect_3, rect_4, rect_5, rect_6, rect_7, rect_8,
    rect_9, rect_10]

#velocidade inicial do boneco e retângulos
velocidade_boneco_y = 0
velocidade_boneco_x = 0

vel_rect_cima_1 = 0.15
vel_rect_baixo_1 = -0.15

def menu():
    telainicial = pygame.image.load("tela inicial.png")
    tela.blit(telainicial,(0,0))
    pygame.display.update()
def fimdejogo(x, y):
    gameover = pygame.image.load("Game Over.png")
    gameover_ = pygame.transform.scale(gameover, (largura, altura))
    tela.blit(gameover_, (0, 0))
    pygame.display.update()

#loop prncipal do jogo
running = False
endgame = False
while endgame == False:
  while running == False:
      menu()
      for event in pygame.event.get():
          if event.type == pygame.MOUSEBUTTONDOWN:
              mouse_pos = pygame.mouse.get_pos()
              mouse_x = mouse_pos[0]
              mouse_y = mouse_pos[1]
              if 330.2811  < mouse_x < 874.6011 and 296.0989  < mouse_y < 380.3489:
                  running = True
                  runni = False
                  valor_fase = 1
                  fimdojogo = False
                
                  while not fimdojogo:
                      
                      delta = relogio.tick(60)
                  
                      #fazendo os bonecos e misseis se moverem para uma direção infinitamente
                      boneco.move_ip(velocidade_boneco_x * delta, velocidade_boneco_y * delta)
                  
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
                  
                      #fazendo com que os retângulos sempre voltem de onde saíram, com velocidade maior
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
                      if boneco.top < 0 or boneco.bottom > altura or boneco.left < 0:
                          fimdejogo(largura, altura)
                          time.sleep(1)
                          
                          while runni == False:
                            fimdejogo(largura, altura)
                            for event in pygame.event.get():
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    mouse_posiI = pygame.mouse.get_pos()
                                    mouse_x = mouse_posiI[0]
                                    mouse_y = mouse_posiI[1]
                                    if 415.4 < mouse_x < 771.08 and 172.6< mouse_y < 264.76 :
                                        runni = True
                                        running = False
                                        valor_fase = 0
                                        fimdojogo = True
                                        boneco.left = 80
                                        boneco.top = 242.5
                                        velocidade_boneco_x = 0
                                        velocidade_boneco_y = 0
                                    elif 415.4<mouse_x <771.08 and 307.6 < mouse_y <399.32 :
                                          time.sleep(1)
                                          runni = True
                                          fimdojogo = True
                                          endgame = True
                            
                      if boneco.right >= 1070:
                          boneco.left = 80
                          boneco.top = 242.5
                          velocidade_boneco_x = 0
                          velocidade_boneco_y = 0
                          vel_rect_cima_1 *= 1.15
                          vel_rect_baixo_1 *= 1.15
                          valor_fase += 1
                    
                  
                      if valor_fase == 11:
                          win(largura, altura)  
                          time.sleep(3)
                          fimdojogo = True
                          endgame = True  
                  
                      for event in pygame.event.get():
                          if event.type == pygame.KEYDOWN:
                              if event.key == pygame.K_w or event.key == pygame.K_UP:
                                  velocidade_boneco_y = -0.2
                                  velocidade_boneco_x = 0
                              if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                                  velocidade_boneco_y = +0.2
                                  velocidade_boneco_x = 0
                              if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                                  velocidade_boneco_x = -0.2
                                  velocidade_boneco_y = 0
                              if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                                  velocidade_boneco_x = +0.2
                                  velocidade_boneco_y = 0
                  
                      #verificando se existe colisão do boneco com os retângulos
                      colisao = boneco.collidelist(misseis)
                      if colisao > 0:
                          print(colisao)
                        
                          while runni == False:
                            fimdejogo(largura, altura)
                            for event in pygame.event.get():
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    mouse_posiI = pygame.mouse.get_pos()
                                    mouse_x = mouse_posiI[0]
                                    mouse_y = mouse_posiI[1]
                                    if 415.4 < mouse_x < 771.08 and 172.6< mouse_y < 264.76 :
                                        
                                        runni = True
                                        running = False
                                        valor_fase = 0
                                        fimdojogo = True
                                        boneco.left = 80
                                        boneco.top = 242.5
                                        velocidade_boneco_x = 0
                                        velocidade_boneco_y = 0
                                    elif 415.4<mouse_x <771.08 and 307.6 < mouse_y <399.32 :
                                          time.sleep(1)
                                          runni = True
                                          fimdojogo = True
                                          endgame = True
                            
                  
                      tela.fill(cinza)
                  
                      planodefundo1(pos_fundo1_x, pos_fundo1_y)
                      planodefundo2(pos_fundo2_x, pos_fundo2_y)
                      mostrarfase(pos_fase_x, pos_fase_y)
                      
                      #desenhando o boneco
                      pygame.draw.rect(tela, preto, boneco)
                  
                      #desenhando os retângulos
                      for ret in misseis:
                          pygame.draw.rect(tela, vermelho, ret)
                      
                      pygame.display.update()                                      
                  
                