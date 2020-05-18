table =['0', '0', '0', '0', '0',
        '0', '0', '0', '0', '0',
        '0', '0', '0', '0', '0',
        '0', '0', '0', '0', '0',
        '0', '0', '0', '0', '0']

def insert():
    for x in range(1, 26):
        ngisi = False
        while ngisi == False :
            print("choose table :")
            inp = input()
            # print(int(inp))
            if table[int(inp)] == '0':
                 table[int(inp)] = str(x)
                #  print (x)
                 ngisi = True
            else :
                print ('Sudah Terisi')
    print(table)

def check():
    
    if table[0]=='x' and table[1]=='x' and table[2]=='x' and table[3]=='x' and table[4]=='x':
        kondisi = 'menang'
    elif table[5]=='x' and table[6]=='x' and table[7]=='x' and table[8]=='x' and table[9]=='x':
        kondisi = 'menang'
    elif table[10]=='x' and table[11]=='x' and table[12]=='x' and table[13]=='x' and table[14]=='x':
        kondisi = 'menang'
    elif table[15]=='x' and table[16]=='x' and table[17]=='x' and table[18]=='x' and table[19]=='x':
        kondisi = 'menang'
    elif table[20]=='x' and table[21]=='x' and table[22]=='x' and table[23]=='x' and table[24]=='x':
        kondisi = 'menang'
    elif table[0]=='x' and table[5]=='x' and table[10]=='x' and table[15]=='x' and table[20]=='x':
        kondisi = 'menang'
    elif table[1]=='x' and table[6]=='x' and table[11]=='x' and table[16]=='x' and table[21]=='x':
        kondisi = 'menang'
    elif table[2]=='x' and table[7]=='x' and table[12]=='x' and table[17]=='x' and table[22]=='x':
        kondisi = 'menang'
    elif table[3]=='x' and table[8]=='x' and table[13]=='x' and table[18]=='x' and table[23]=='x':
        kondisi = 'menang'
    elif table[4]=='x' and table[9]=='x' and table[14]=='x' and table[19]=='x' and table[24]=='x':
        kondisi = 'menang'
    elif table[0]=='x' and table[6]=='x' and table[12]=='x' and table[18]=='x' and table[24]=='x':
        kondisi = 'menang'
    elif table[4]=='x' and table[8]=='x' and table[12]=='x' and table[16]=='x' and table[20]=='x':
        kondisi = 'menang'
    else :
        kondisi = 'salah'
        
    return kondisi

def ngisi(): #milih tablenya bukan angka
    lanjut = True
    while lanjut == True:
        
        print('Choose Table to be Bingoed :')
        inp = input()
        if inp == 'bingo':
            kon = check()
            # print(kon)
            if kon == 'menang':
                print('Kamu Menang')
                lanjut = False
            else :
                print ('Kamu Belum Bingo')
        else :
            # print(int(inp))
            if table[int(inp)] != 'x':
                table[int(inp)] = 'x'
            else :
                print ('Sudah Dipilih')
                
# def ngisi(): #milih angka bukan tabel
#     lanjut = True
#     while lanjut == True:
        
#         print('Choose Angka to be Bingoed :')
#         inp = input()
#         if inp == 'bingo':
#             kon = check()
#             # print(kon)
#             if kon == 'menang':
#                 print('Kamu Menang')
#                 lanjut = False
#             else :
#                 print ('Kamu Belum Bingo')
#         else :
#             ke = table.index(inp)
#             if table[int(ke)] != 'x':
#                 table[int(ke)] = 'x'
#             else :
#                 print ('Sudah Dipilih')
   
def main():
    insert()
    ngisi()
    
main()

