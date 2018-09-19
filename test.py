#coding:utf-8

while True:
       N = raw_input('Nを入力してください。：')
       if len(N) == 0:
               break   #Enterでストップ
       else:
               N = int(N)
               x = float(input('xを入力してください。：'))
               tem_list = [str(N)+'\n',str(x)+'\n']
               shisuu_file = open('shisuu.txt','a')
               shisuu_file.writelines(tem_list)
               shisuu_file.flush()
               shisuu_file.close()
               print(tem_list)
