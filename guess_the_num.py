import random      #import�irandom�o�Ө禡�w
Randomnum=random.randint(1,100)    #�H�����ͤ@�Ӥ���1��100���ü�
firstnum=1      #�]�w�̤p��
count=0         #�]�w�p��q�����ƪ���l��
lastnum=100     #�]�w�̤j��
inputnum=input("�п�J�A�n�q���Ʀr: ")   #���o�ϥΪ̪���J
while True:       #���J�Ʀr�����{��
    if int(inputnum)>=int(firstnum) and int(inputnum)<=int(lastnum):    
    #�ˬd�q�����Ʀr�ϧ_����1��100����
        if int(inputnum)<int(Randomnum):   #�p�G�q�����Ʀr�p�󵪮�
            count+=1    #�q�����ƼW�[1
            print("�Ӥp�F !!!")   #�L�X���G
            firstnum=int(inputnum)+1   #�N�̤p�i�઺�ȳ]��(�q����+1)
            print("����:",firstnum,"��",lastnum,sep="")
            #�L�X�d��(�q����+1)��100������
            inputnum=input("�Э��s��J: ")   #���o�ϥΪ̤U�@������J
        elif int(inputnum)>int(Randomnum):   #�p�G�q�����Ʀr�j�󵪮�
            count+=1    #�q�����ƼW�[1
            print(("�Ӥj�F !!!"))   #�L�X���G
            lastnum=int(inputnum)-1   #�N�̤j�i�઺�ȳ]��(�q����-1)
            print("����:",firstnum,"��",lastnum,sep="")
            #�L�X�d��1��(�q����-1)������
            inputnum=input("�Э��s��J: ")   #���o�ϥΪ̤U�@������J
        elif int(inputnum)==int(Randomnum):   #�p�G�q�����Ʀr���󵪮�
            count+=1    #�q�����ƼW�[1
            print("yeah!!!�A�q��F!!!")     #�L�X���G
            print("�A�q�F",count,"��",sep="")   #�L�X�q������
            break   #���X�j��
    else:    #�Y�q�����Ʀr���b�d��
        count+=1   #�q�����ƼW�[1
        print("���A�d��!!!")  #�L�X���G
        print("����:",firstnum,"��",lastnum,sep="")
        #�L�X�d��1��100������
        inputnum=input("�Э��s��J: ")  #���o�ϥΪ̤U�@������J