from collections import deque
import curses
from curses import wrapper
import time

maze = [    
    [' ', ' ', ' ', '#', '#', ' ', '#', '#', '#', '#'],
    ['#', '#', ' ', '#', '#', ' ', ' ', ' ', ' ', '#'],
    ['#', '#', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#'],
    ['#', '#', '#', ' ', '#', '#', '#', '#', ' ', '#'],
    ['#', '#', '#', ' ', '#', ' ', ' ', '#', ' ', '#'],
    ['#', ' ', ' ', ' ', '#', ' ', '#', '#', ' ', '#'],
    ['#', ' ', '#', '#', '#', ' ', ' ', ' ', '#', '#'],
    ['#', ' ', '#', ' ', '#', ' ', '#', ' ', ' ', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#'],
    ['#', '#', '#', ' ', ' ', '#', ' ', '#', ' ', ' '],
]

r=len(maze)
c=len(maze[0])
def print_maze(maze,stdscr,path):
    G = curses.color_pair(1) 
    R   = curses.color_pair(2)
    for i in range(r): 
        for j in range(c):
            if (i,j) in path:
                stdscr.addstr(i,j*2,'*',R)
            else:
                stdscr.addstr(i,j*2,maze[i][j],G)

def find_path(maze,stdscr):
    r=len(maze[0])
    c=len(maze)
    directions = [(0,1),(1,0),(-1,0),(0,-1)]
    visited = set()

    q=deque()
    q.append((0,0,[(0,0)]))
    visited.add((0,0))
    while q:
        x,y,path = q.popleft()

        stdscr.clear()
        print_maze(maze,stdscr,path)
        time.sleep(0.15)
        stdscr.refresh()
        if x==r-1 and y==c-1:
            return path
        

        for i,j in directions:
            nx,ny=x+i,y+j
            if r>nx>=0 and c>ny>=0 and maze[nx][ny]==' ' and (nx,ny) not in visited:
                visited.add((nx,ny))
                
                q.append((nx,ny,path+[(nx,ny)]))
    print("Path Does Not Exist")

def centre(stdscr):
    curses.init_pair(1,curses.COLOR_GREEN,curses.COLOR_BLACK)
    curses.init_pair(2,curses.COLOR_RED,curses.COLOR_BLACK)
    # stdscr.addstr(4,2,"hello world!")
    find_path(maze,stdscr)
    stdscr.getch()
wrapper(centre)