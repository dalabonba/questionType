import random as rd
import sys
from time import sleep

row=0
col=0
while row<5:
   row=eval(input("row(must>4):"))

while col<5:
   col=eval(input("col(must>4):"))


maze=[] #迷宮本身
path=[(1,1)] #迷宮開路路徑，起點座標(1,1)
popList=[] #沒地方開路時的後退紀錄


#printMaze:印出迷宮並在最後加上分隔線
def printMaze():
    for i in maze:
        for j in i:
            print(j,end=" ")
        print()
    print("-------------------------------------------------------")
#-----------------------------


#產生row列col行的二維陣列maze(迷宮)，值都是I(代表都是牆)
for i in range(row):
    a=[]
    for j in range(col):
        a.append("I")
    maze.append(a)
#-----------------------------


maze[1][1]="O" #迷宮起點座標(1,1)設為O(路)

direction=[("x",-2),("x",2),("y",-2),("y",2)] #上 下 左 右
while 1:
    
    rd.shuffle(direction)#將上下左右順序隨機
    rd.shuffle(direction)#再打亂一次，感覺更隨機
    
    for xory,pors in direction: # xory:x or y    pors:plus 2 or subtract 2  四方向嘗試移動
    
        flag=0 #用來判斷有沒有找到路
        beAdded=path[-1]#path的最後一個數組(be added 被加的)
        
        if xory=="x":
            x=beAdded[0]+pors
            y=beAdded[1]
            if (x)<1 or (x)>row-2: # x 若不在邊界內
                continue
            elif (x,y) in path or (x,y) in popList: #若隨機出來的目的地座標已經走過了
                continue
            else:
                path.append((x,y)) #將座標加入迷宮開路路徑，代表開路一步
                
                #-----將開路的地方從牆壁(I)變成開路標記(O)-----
                maze[x][y]="O"
                if pors==2:
                    print("往下開路")
                    maze[x-1][y]="O"
                else:#pors==-2
                    print("往上開路")
                    maze[x+1][y]="O"
                #--------------------------------------------
                flag=1
                printMaze()
                sleep(0.5)
                break
                
                
        else: # xory = y
            x=beAdded[0]
            y=beAdded[1]+pors
            if (y)<1 or (y)>col-2: # y 若不在邊界內
                continue
            elif (x,y) in path or (x,y) in popList: #若隨機出來的目的地座標已經走過了
                continue
            else:
                path.append((x,y)) #將座標加入迷宮開路路徑，代表開路一步
                
                #-----將開路的地方從牆壁(I)變成開路標記(O)-----
                maze[x][y]="O"
                if pors==2:
                    print("往右開路")
                    maze[x][y-1]="O"
                else:#pors==-2
                    print("往左開路")
                    maze[x][y+1]="O"
                #--------------------------------------------
                    
                flag=1
                printMaze()
                sleep(0.5)
                break
            
    #---------------------END for 四方向嘗試移動-----------------------
    
    
    if not flag: #走了四個方向沒有找到路，而不是找到路後break出來的
    
        pathPop=path.pop()  #將最後一個 迷宮開路路徑 的座標 移除，代表後退一步
        
        if pathPop==(1,1): #若pop出來的已經是最後一個
            maze[1][1]=" "
            printMaze()
            
            sys.exit("結束")#----------------------------!!!!!!!!!!!!!!!!!!!!!!!!!程式結束點
            
        else:#pop出來的不是最後一個
            print("找不到路",end="，")
            x,y=pathPop #將pathPop數組拆開放進x,y
            lx,ly=path[-1] #last x,last y，pop之後path裡剩下的最後一個座標
        
        popList.append(pathPop) #將 開路路徑 pop出來的座標 加入 後退紀錄
        
        #-----將開路標記(O)變成路( )------
        maze[x][y]=" "
        if x<lx: #往下退回
            print(f"往下退回，x:{x}<lx:{lx}  y:{y}=ly:{ly}")
            maze[x+1][y]=" "
        elif x>lx: #往上退回
            print(f"往上退回，x:{x}>lx:{lx}  y:{y}=ly:{ly}")
            maze[x-1][y]=" "
        elif y<ly: #往右退回
            print(f"往右退回，x:{x}=lx:{lx}  y:{y}<ly:{ly}")
            maze[x][y+1]=" "
        else: #y>ly 往左退回
            print(f"往左退回，x:{x}=lx:{lx}  y:{y}>ly:{ly}")
            maze[x][y-1]=" "
        #-------------------------------
        
        printMaze()
        sleep(0.5)