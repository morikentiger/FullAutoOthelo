# -*- coding:utf-8 -*-
import pygame
from pygame.locals import *
import sys

clr_black = (0,0,0)
clr_white = (255,255,255)
clr_lightblue = (157,204,224)
clr_darkgreen = (0,100,0)

none = 0
black = 1
white = 2

size_square = 60
size_dir_othelo = 50
num_square = 8

board = [[0 for i in range(num_square)] for j in range(num_square)]
board[3][3] = white
board[3][4] = black
board[4][3] = black
board[4][4] = white


def square2coordinate(x,y):
	X = size_square + 0.5 * size_square + x*size_square
	Y = size_square + 0.5 * size_square + y*size_square
	return (X,Y)

def coordinate2ellipse(x,y):
	X1 = x - size_dir_othelo/2
	Y1 = y - size_dir_othelo/2
	return (X1,Y1,size_dir_othelo,size_dir_othelo)

def initboard(screen):
	#盤面の表示
	pygame.draw.rect(screen,clr_darkgreen,
Rect(0+size_square,0+size_square,
num_square*size_square,
num_square*size_square))	#四角形を描画塗りつぶし
	for i in range(0,num_square):
		for j in range(0,num_square):
			pygame.draw.line(screen,clr_black,
(size_square*1,size_square*(j+1)),
(size_square*9,size_square*(j+1)),5)	#直線の描画
			pygame.draw.line(screen,clr_black,
(size_square*(i+1),size_square*1),
(size_square*(i+1),size_square*9),5)	#直線の描画
	
	pygame.draw.line(screen,clr_black,
(size_square*1,size_square*(8+1)),
(size_square*9,size_square*(8+1)),5)	#直線の描画
	pygame.draw.line(screen,clr_black,
(size_square*(8+1),size_square*1),
(size_square*(8+1),size_square*9),5)	#直線の描画

#	drawPiece(screen,3,3,white)
#	drawPiece(screen,4,4,white)
#	drawPiece(screen,3,4,black)
#	drawPiece(screen,4,3,black)
	

def drawPiece(screen,x,y,piece):
	(X,Y) = square2coordinate(x,y)
	if piece == none:
		clr_piece = clr_darkgreen
	elif piece == black:
		clr_piece = clr_black
	elif piece == white:
		clr_piece = clr_white
	pygame.draw.ellipse(screen,clr_piece,coordinate2ellipse(X,Y))	#楕円を描画塗りつぶし

def main():
	pygame.init()				# Pygameの初期化
	screen = pygame.display.set_mode((600,600))	#大きさ600*500の画面を生成
	clock = pygame.time.Clock()
	pygame.display.set_caption("FullAutoOthelo")	#タイトルバーに表示する文字
	font = pygame.font.Font(None, 15)	#フォントの設定(55px)
	screen.fill(clr_lightblue)	#画面を黒色に塗りつぶし
	text = font.render("TEST", True, (255,255,255)) #描画する文字列の設定
	#screen.blit(text,[20,100])	#文字列の表示位置
	initboard(screen)
	
	cnt = 0
	clr = 2
	while(1):
		clock.tick(5)
		#drawPiece(screen,cnt,cnt,clr)
		board[cnt][cnt] = clr		
		cnt+=1
		if cnt>=num_square:
			cnt=0
			clr+=1
			if clr>white:
				clr=none
		for i in range(0,num_square):
			for j in range(0,num_square):
				(X_crd,Y_crd) = square2coordinate(i,j)
				drawPiece(screen,i,j,board[i][j])
				#pygame.draw.ellipse(screen,clr_white,coordinate2ellipse(X_crd,Y_crd))	#楕円を描画塗りつぶし
				#text_X = font.render(str(X_crd), True, clr_black)
				#text_Y = font.render(str(Y_crd), True, clr_black)
				#screen.blit(text_X,[X_crd,Y_crd-15])
				#screen.blit(text_Y,[X_crd,Y_crd])
				
		pygame.display.update()		#画面を更新

		#イベント処理
		for event in pygame.event.get():
			if event.type == QUIT:	#閉じるボタンが押されたら終了
				pygame.quit()		#Pygameの終了（画面閉じられる）
				sys.exit()

if __name__ == "__main__":
	main()
