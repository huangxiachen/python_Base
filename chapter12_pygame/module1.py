import os
import sys
import pygame

# 设置工作路径
os.chdir(os.path.dirname(sys.argv[0]))
class Module1:
    '''管理module1的模块'''
    def __init__(self,ai_moudle1):
        #初始化图像1并设置初始值
        self.screen = ai_moudle1.screen
        self.screen_rect = ai_moudle1.screen.get_rect()

        # 加载图像1并获取其外接矩形
        self.image = pygame.image.load('./images/小熊.jpg')
        self.rect = self.image.get_rect()

        # 每个新图像都放在屏幕底部中央
        self.rect.midbottom = self.screen_rect.midbottom

    
    def blitme(self):
        # 在指定位置绘制图像1
        self.screen.blit(self.image,self.rect)
