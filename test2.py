#coding:utf-8

while True:
    N = raw_input('N入力:')
    if len(N) == 0:
        break
    else:
        N = int(N)
        x = float(input('x入力:'))
        tem_list = [str(N)+"\n",str(x)+"\n"]
        shisuu_file = open('shisuu.txt','w')
        shisuu_file.writelines(tem_list)
        shisuu_file.flush()
        shisuu_file.close()
        print(tem_list)
