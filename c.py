import select 
import socket 
import sys 
import threading 

class Checkers():
    def __init__(self):
        #connection stuff
        self.host = 'localhost'
        self.port = 9000
        self.size = 1024
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((self.host,self.port))

    self.width = 9
    self.height = 9
    self.board = [[0 for x in range(self.width)] for y in range(self.height)]
    self.didiwin = False
    self.didilose = False
    self.x = ''
    self.y = ''

    #setting pawns
    for i in range(0,3,2):
        for j in xrange( 0,self.height,2):
            self.board[i][j] = str(1) 
    for i in range(1,3,2):
        for j in xrange( 1,self.height,2):
            self.board[i][j] = str(1) 
    for i in range(5,8,2):
        for j in xrange( 1,self.height,2):
            self.board[i][j] = str(2) 
    for i in range(6,8,2):
        for j in xrange( 0,self.height,2):
            self.board[i][j] =  str(2)
    self.turn = None

def drawBoard(self):
    for i in range(self.width):
        self.board[i][0] = str(i+1)
    self.board[8][0] = ' '
    self.board[8][1] = 'a'
    self.board[8][2] = 'b'
    self.board[8][3] = 'c'
    self.board[8][4] = 'd'
    self.board[8][5] = 'e'
    self.board[8][6] = 'f'
    self.board[8][7] = 'g'
    self.board[8][8] = 'h'
    for i in range(self.width):
        for j in range( self.height):
            print " {0}".format(self.board[i][j]),
        print "\n"
def drawHud(self):
    if self.turn == True:
        print "Your move \n"
    else:
        print "Opponent moving"
def update(self):
    #draw board
    self.drawBoard()
    #draw hud
    self.drawHud()

def finished(self):
    if self.didiwin == True:
        print 'u won'
        exit()
    if self.didilose == True:
        print 'u lost' 
        exit()
    self.s.close()
def who_starts(self, doistart):
    if doistart == "t":
        self.turn = True
    elif doistart == "f":
        self.turn = False
def is_it_my_turn(self, turn):
    if turn == "t":
        self.turn = True
    elif turn == "f":
        self.turn = False

def run(self):
    running = True

    try:
        self.s.sendto("c", (self.host, self.port))
        while running:
            msg, addr = self.s.recvfrom(32)
            self.who_starts(msg)
            print '\nReceived message: ',msg
            if len(msg) >=3 and (msg != 'f' or msg != 't'):
                self.x = msg[0]
                self.y = msg[1]
                turn = msg[2]
                self.x = int(self.x)
                self.y = int(self.y)
                self.is_it_my_turn(turn)
                print '\nx:',self.x
                print 'y:',self.y
                print "turn: ",turn
                try:
                    if self.x != 0 and self.y != 0:
                        self.board[self.x][self.y] = 'test'
                except:
                    pass  # If something goes wrong, don't draw anything.
            if self.x != 0 and self.y != 0:
                self.update()
            if self.turn == True:
                self.move = raw_input('Make a move i.e, A1 B3 etc.(only test, test2, quit and show players available)')
                if self.move == 'show players':
                    self.s.sendto("s",(self.host, self.port))
                if self.move == 'quit':
                    running = False
                if self.move == 'test':
                    self.s.sendto("uu", (self.host, self.port))
                if self.move == 'test2':
                    self.s.sendto("uw", (self.host, self.port))
    finally:
        self.s.sendto("d", (self.host, self.port))

if __name__ == "__main__": 
    c = Checkers()
    c.run()
