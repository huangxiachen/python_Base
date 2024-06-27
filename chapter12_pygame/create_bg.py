import sys
import pygame

from module1 import Module1

class Create_bg:

    #初始化窗口
    def __init__(self):
        pygame.init()
        '''
        我们将创建一个时钟(clock)，并确保它在主循环每次通过后都进
        行计时(tick)。当这个循环的通过速度超过我们定义的帧率时，Pygame 会计算需要
        暂停多长时间，以便游戏的运行速度保持一致。
        '''
        self.clock = pygame.time.Clock()
        #设置窗口尺寸其他参数默认
        self.screen = pygame.display.set_mode((1200,800))
        # 设置窗口标题
        pygame.display.set_caption('Hello')
        # 设置背景颜色
        self.bg_color = (0, 0, 255, 255)
        # 加载组件类
        self.module1 = Module1(self)
    
    # 运行窗口后发生的事件
    def run(self):
        while True:
            # 侦听键盘和鼠标事件
            self.__check_events()
            # 每次循环多重绘屏幕
            self.___update_screen()
            '''
            初始化 pygame 后，创建 pygame.time 模块中的 Clock 类的一个实例，然后在
            run_game() 的 while 循环末尾让这个时钟进行计时
            (帧率)
            '''
            self.clock.tick(60)
     
    def __check_events(self):
        # 响应按键鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    '''
    为了进一步简化 run_game()，我们把更新屏幕的代码移到一个名为
    __update_screen() 的方法中
    '''
    def ___update_screen(self):
        # 每次循环多重绘屏幕
        self.screen.fill(self.bg_color)
        # 在指定位置绘制图像
        self.module1.blitme()
        # 让最近绘制的屏幕可见
        pygame.display.flip()




if __name__ == '__main__':
    # 创建游戏实例并运行游戏
    create_bg = Create_bg()
    create_bg.run()