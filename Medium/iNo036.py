def haveRepeat(nineList):
    if nineList.count("1") > 1:
        return True
    if nineList.count("2") > 1:
        return True
    if nineList.count("3") > 1:
        return True
    if nineList.count("4") > 1:
        return True
    if nineList.count("5") > 1:
        return True
    if nineList.count("6") > 1:
        return True
    if nineList.count("7") > 1:
        return True
    if nineList.count("8") > 1:
        return True
    if nineList.count("9") > 1:
        return True
    return False

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            if haveRepeat(board[i]) == True:
                return False
            if haveRepeat([ board[1][i], board[2][i], board[3][i], board[0][i], board[4][i], board[5][i], board[6][i], board[7][i], board[8][i]]) == True: 
                return False
        
        if haveRepeat([ board[0][0], board[0][1], board[0][2], board[1][0], board[1][1], board[1][2], board[2][0], board[2][1], board[2][2]]) == True: 
            return False
        if haveRepeat([ board[0][3], board[0][4], board[0][5], board[1][3], board[1][4], board[1][5], board[2][3], board[2][4], board[2][5]]) == True: 
            return False
        if haveRepeat([ board[0][6], board[0][7], board[0][8], board[1][6], board[1][7], board[1][8], board[2][6], board[2][7], board[2][8]]) == True: 
            return False
        if haveRepeat([ board[3][0], board[3][1], board[3][2], board[4][0], board[4][1], board[4][2], board[5][0], board[5][1], board[5][2]]) == True: 
            return False
        if haveRepeat([ board[3][3], board[3][4], board[3][5], board[4][3], board[4][4], board[4][5], board[5][3], board[5][4], board[5][5]]) == True: 
            return False
        if haveRepeat([ board[3][6], board[3][7], board[3][8], board[4][6], board[4][7], board[4][8], board[5][6], board[5][7], board[5][8]]) == True:  
            return False
        if haveRepeat([ board[6][0], board[6][1], board[6][2], board[7][0], board[7][1], board[7][2], board[8][0], board[8][1], board[8][2]]) == True: 
            return False
        if haveRepeat([ board[6][3], board[6][4], board[6][5], board[7][3], board[7][4], board[7][5], board[8][3], board[8][4], board[8][5]]) == True: 
            return False
        if haveRepeat([ board[6][6], board[6][7], board[6][8], board[7][6], board[7][7], board[7][8], board[8][6], board[8][7], board[8][8]]) == True:  
            return False

        return True
