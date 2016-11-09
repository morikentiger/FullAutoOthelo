# -*- coding:utf-8 -*-
import pygame
from pygame.locals import *
import sys

import numpy as np

clr_black = np.array([0,0,0])
clr_white = np.array([255,255,255])
clr_lightblue = np.array([157,204,224])
clr_darkgreen = np.array([0,100,0])
clr_darkred = np.array([100,0,0])

none = 0
black = 1
white = 2
mouse = 3


size_square = 60
size_dir_othelo = 50
num_square = 8

board = [[[0 for k in range(2)] for i in range(num_square)] for j in range(num_square)]

print(board)
board[3][3][0] = white
board[3][4][0] = black
board[4][3][0] = black
board[4][4][0] = white
print(board)

def coordinate2square(X,Y):
	x = int(X/size_square -1 )#-0.5
	y = int(Y/size_square -1 )#-0.5
	#x = (X - size_square - 0.5 * size_square)/size_square
	#y = (Y - size_square - 0.5 * size_square)/size_square
	return (x,y)

def square2coordinate(x,y):
	X = size_square + 0.5 * size_square + x*size_square
	Y = size_square + 0.5 * size_square + y*size_square
	return (X,Y)

def coordinate2ellipse(x,y):
	X1 = x - size_dir_othelo/2
	Y1 = y - size_dir_othelo/2
	return (X1,Y1,size_dir_othelo,size_dir_othelo)

def drawboard(screen):
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
			drawPiece(screen,i,j,board[i][j][0])
			if board[i][j][0]==none:
				drawPiece(screen,i,j,board[i][j][1])
	
	pygame.draw.line(screen,clr_black,
	(size_square*1,size_square*(8+1)),
	(size_square*9,size_square*(8+1)),5)	#直線の描画
	pygame.draw.line(screen,clr_black,
	(size_square*(8+1),size_square*1),
	(size_square*(8+1),size_square*9),5)	#直線の描画

def drawPiece(screen,x,y,piece):
	(X,Y) = square2coordinate(x,y)
	if piece == none:
		clr_piece = clr_darkgreen
	elif piece == black:
		clr_piece = clr_black
	elif piece == white:
		clr_piece = clr_white
	elif piece == mouse:
		clr_piece = clr_darkred
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
	
	
	cnt = 0
	clr = 2
	X_mouse_past = -100
	Y_mouse_past = -100
	x_mouse_past = 0
	y_mouse_past = 0
	while(1):
		clock.tick(30)
		drawboard(screen)
		#board[cnt][cnt] = clr		
		#cnt+=1
		#if cnt>=num_square:
		#	cnt=0
		#	clr+=1
		#	if clr>white:
		#		clr=none

		for i in range(0,num_square):
			for j in range(0,num_square):
				(X_crd,Y_crd) = square2coordinate(i,j)
				
				
		pygame.display.update()		#画面を更新

		#イベント処理
		for event in pygame.event.get():
			if event.type == MOUSEMOTION:
				X_mouse,Y_mouse = event.pos
				x_mouse,y_mouse = coordinate2square(X_mouse,Y_mouse)
				print(x_mouse,y_mouse)
				X_mouse,Y_mouse = square2coordinate(x_mouse,y_mouse)
				
				pygame.draw.rect(screen,clr_darkgreen,
				Rect(X_mouse_past - size_square/2,
				Y_mouse_past - size_square/2,
				size_square,
				size_square))
				if (x_mouse_past>=0 and x_mouse_past<num_square and y_mouse_past>=0 and y_mouse_past<num_square):
					board[x_mouse_past][y_mouse_past][1]=none
				pygame.draw.rect(screen,clr_darkred,
				Rect(X_mouse - size_square/2,
				Y_mouse - size_square/2,
				size_square,
				size_square))
				if (x_mouse>=0 and x_mouse<num_square and y_mouse>=0 and y_mouse<num_square):
					board[x_mouse][y_mouse][1]=mouse
				x_mouse_past = x_mouse
				y_mouse_past = y_mouse
				X_mouse_past = X_mouse
				Y_mouse_past = Y_mouse
			if event.type == QUIT:	#閉じるボタンが押されたら終了
				pygame.quit()		#Pygameの終了（画面閉じられる）
				sys.exit()
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					pygame.quit()
					sys.exit()
			if event.type == MOUSEBUTTONDOWN and event.button==1:
				drawPiece(screen,x_mouse,y_mouse,white)

if __name__ == "__main__":
	main()
