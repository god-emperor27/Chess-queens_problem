import numpy as np
from datetime import datetime
starttime=datetime.now()

def horizref(origmat):
    #creates a retun list or array which is a horizontal reflection of the original
    #
    #input: original matrix: origmat
    #output: return matrix: retmat
    #working copy of original matrix: tempmat
    #n: index counter
    #
    tempmat=np.array(origmat)
    retmat=tempmat.copy()
    n=1
    for i in tempmat:
        retmat[-n]=i
        n+=1
    if type(origmat)==list: #check original type for list to return same
        retmat=np.ndarray.tolist(retmat)
    return retmat

def rot90cw(origmat):
    #creates a retun list or array which is a 90 degree clockwise rotation of the original
    #
    #input: original matrix: origmat
    #output: return matrix: retmat
    #working copy of original matrix: tempmat
    #m,n: index counters
    #
    tempmat=np.array(origmat)
    retmat=tempmat.copy()
    m=0
    for i in tempmat:
        n=0
        for j in i:
            retmat[n,-m-1]=j
            n+=1
        m+=1
    if type(origmat)==list: #check original type for list to return same
        retmat=np.ndarray.tolist(retmat)
    return retmat

BOARD = np.zeros((8,8),dtype=int)
SOLUTIONS = []
UNIQUESOL = []

x0=0
while x0<8:
    BOARD[x0,0]=1

    x1=0
    while x1<8:
        #check previous rows
        for j in range(0,8):

                
            #check horizontals on column 0
            for i in range(0,1):
                if x1<8:
                    if BOARD[x1,i]==1:
                        x1+=1
            #check diagonals on column 0
            for i in range(1,2):
                if x1-i>=0 and x1-i<=7:
                    if BOARD[x1-i,1-i]==1:
                        x1+=1
            for i in range(1,2):
                if x1+i>=0 and x1+i<=7:
                    if BOARD[x1+i,1-i]==1:
                        x1+=1
               
        if x1<8:
            BOARD[x1,1]=1

            x2=0
            while x2<8:
                #check previous rows
                for j in range(0,8):
                    if x2<8:
                        
                        #check horizontals on column 0-1
                        for i in range(0,2):
                            if x2<8:
                                if BOARD[x2,i]==1:
                                    x2+=1
                        #check diagonals on column 0-1
                        for i in range(1,3):
                            if x2-i>=0 and x2-i<=7:
                                if BOARD[x2-i,2-i]==1:
                                    x2+=1
                        for i in range(1,3):
                            if x2+i>=0 and x2+i<=7:
                                if BOARD[x2+i,2-i]==1:
                                    x2+=1

                if x2<8:
                    BOARD[x2,2]=1

                    x3=0
                    while x3<8:
                        #check previous rows
                        for j in range(0,8):
                            if x3<8:
                                
                                #check horizontals on column 0-2
                                for i in range(0,3):
                                    if x3<8:
                                        if BOARD[x3,i]==1:
                                            x3+=1
                                #check diagonals on column 0-2
                                for i in range(1,4):
                                    if x3-i>=0 and x3-i<=7:
                                        if BOARD[x3-i,3-i]==1:
                                            x3+=1
                                for i in range(1,4):
                                    if x3+i>=0 and x3+i<=7:
                                        if BOARD[x3+i,3-i]==1:
                                            x3+=1

                        if x3<8:
                            BOARD[x3,3]=1

                            x4=0
                            while x4<8:
                                #check previous rows
                                for j in range(0,8):
                                    if x4<8:
                                        
                                        #check horizontals on column 0-3
                                        for i in range(0,4):
                                            if x4<8:
                                                if BOARD[x4,i]==1:
                                                    x4+=1
                                        #check diagonals on column 0-3
                                        for i in range(1,5):
                                            if x4-i>=0 and x4-i<=7:
                                                if BOARD[x4-i,4-i]==1:
                                                    x4+=1
                                        for i in range(1,5):
                                            if x4+i>=0 and x4+i<=7:
                                                if BOARD[x4+i,4-i]==1:
                                                    x4+=1
                                if x4<8:
                                    BOARD[x4,4]=1
                                    
                                    x5=0
                                    while x5<8:
                                        #check previous rows
                                        for j in range(0,8):
                                            if x5<8:
                                                
                                                #check horizontals on column 0-4
                                                for i in range(0,5):
                                                    if x5<8:
                                                        if BOARD[x5,i]==1:
                                                            x5+=1
                                                #check diagonals on column 0-4
                                                for i in range(1,6):
                                                    if x5-i>=0 and x5-i<=7:
                                                        if BOARD[x5-i,5-i]==1:
                                                            x5+=1
                                                for i in range(1,6):
                                                    if x5+i>=0 and x5+i<=7:
                                                        if BOARD[x5+i,5-i]==1:
                                                            x5+=1
                                        if x5<8:
                                            BOARD[x5,5]=1
                                            
                                            x6=0
                                            while x6<8:
                                                #check previous rows
                                                for j in range(0,8):
                                                    if x6<8:
                                                        
                                                        #check horizontals on column 0-5
                                                        for i in range(0,6):
                                                            if x6<8:
                                                                if BOARD[x6,i]==1:
                                                                    x6+=1
                                                        #check diagonals on column 0-5
                                                        for i in range(1,7):
                                                            if x6-i>=0 and x6-i<=7:
                                                                if BOARD[x6-i,6-i]==1:
                                                                    x6+=1
                                                        for i in range(1,7):
                                                            if x6+i>=0 and x6+i<=7:
                                                                if BOARD[x6+i,6-i]==1:
                                                                    x6+=1
                                                if x6<8:
                                                    BOARD[x6,6]=1

                                                    x7=0
                                                    while x7<8:
                                                        #check previous rows
                                                        for j in range(0,8):
                                                            if x7<8:
                                                                
                                                                #check horizontals on column 0-6
                                                                for i in range(0,7):
                                                                    if x7<8:
                                                                        if BOARD[x7,i]==1:
                                                                            x7+=1
                                                                #check diagonals on column 0-6
                                                                for i in range(1,8):
                                                                    if x7-i>=0 and x7-i<=7:
                                                                        if BOARD[x7-i,7-i]==1:
                                                                            x7+=1
                                                                for i in range(1,8):
                                                                    if x7+i>=0 and x7+i<=7:
                                                                        if BOARD[x7+i,7-i]==1:
                                                                            x7+=1
                                                        if x7<8:
                                                            BOARD[x7,7]=1

                                                            SOLUTIONS.append(np.ndarray.tolist(BOARD))

                                                            #D4 permutations test
                                                            VIABLE=1
                                                            #print(BOARD) #show options as they occur, test for running
                                                            for sollist in SOLUTIONS:
                                                                if VIABLE==1: #stop checking once a repetition is found
                                                                    if rot90cw(np.ndarray.tolist(BOARD))==sollist:
                                                                        VIABLE=0
                                                                    if rot90cw(rot90cw(np.ndarray.tolist(BOARD)))==sollist:
                                                                        VIABLE=0
                                                                    if rot90cw(rot90cw(rot90cw(np.ndarray.tolist(BOARD))))==sollist:
                                                                        VIABLE=0
                                                                    if horizref(np.ndarray.tolist(BOARD))==sollist:
                                                                        VIABLE=0
                                                                    if rot90cw(horizref(np.ndarray.tolist(BOARD)))==sollist:
                                                                        VIABLE=0
                                                                    if rot90cw(rot90cw(horizref(np.ndarray.tolist(BOARD))))==sollist:
                                                                        VIABLE=0
                                                                    if rot90cw(rot90cw(rot90cw(horizref(np.ndarray.tolist(BOARD)))))==sollist:
                                                                        VIABLE=0
                                                                                                                                                                                                                                                                                        
                                                            if VIABLE==1:
                                                                UNIQUESOL.append(np.ndarray.tolist(BOARD))
                                                                #print(BOARD)
                                                            BOARD[x7,7]=0
                                                        x7+=1
                                                    BOARD[x6,6]=0
                                                x6+=1
                                            BOARD[x5,5]=0
                                        x5+=1
                                    BOARD[x4,4]=0
                                x4+=1
                            BOARD[x3,3]=0
                        x3+=1
                    BOARD[x2,2]=0
                x2+=1
            BOARD[x1,1]=0
        x1+=1
    BOARD[x0,0]=0
    x0+=1
endtime=datetime.now()                                

f=open("solution2.py","w")
f.write("import numpy as np\n")
f.write("\n")
f.write("# start time "+str(starttime)+"\n")
f.write("# end time "+str(endtime)+"\n")
f.write("sol2="+str(SOLUTIONS)+"\n")
f.write("sol2=np.array(sol2)\n")
f.write("print(sol2)\n")
f.write("uni2="+str(UNIQUESOL)+"\n")
f.write("uni2=np.array(uni2)\n")
f.write("print(uni2)\n")
f.close()


