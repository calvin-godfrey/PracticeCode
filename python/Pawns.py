safe_pawns=lambda p:sum([chr(ord(i[0])+1)+str(int(i[1])-1)in p or chr(ord(i[0])-1)+str(int(i[1])-1)in p for i in p])
#So p is an array of the locations of pawns, and this program is supposed to return how many are sasfe
#An example of p would b e["A3", "B3", "C6", "H4"], where the letter is column, number is row
#This checks if there is a pawn above and to the right/left by using ord/chr to get the char before/after it
#And checks if the new chess position has a pawn (is in p)