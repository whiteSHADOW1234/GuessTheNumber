import random      #import進random這個函式庫
Randomnum=random.randint(1,100)    #隨機產生一個介於1到100的亂數
firstnum=1      #設定最小值
count=0         #設定計算猜測次數的初始值
lastnum=100     #設定最大值
inputnum=input("請輸入你要猜的數字: ")   #取得使用者的輸入
while True:       #當輸入數字後執行程式
    if int(inputnum)>=int(firstnum) and int(inputnum)<=int(lastnum):    
    #檢查猜測的數字使否介於1到100之間
        if int(inputnum)<int(Randomnum):   #如果猜測的數字小於答案
            count+=1    #猜測次數增加1
            print("太小了 !!!")   #印出結果
            firstnum=int(inputnum)+1   #將最小可能的值設為(猜測值+1)
            print("提示:",firstnum,"到",lastnum,sep="")
            #印出範圍為(猜測值+1)到100的提示
            inputnum=input("請重新輸入: ")   #取得使用者下一次的輸入
        elif int(inputnum)>int(Randomnum):   #如果猜測的數字大於答案
            count+=1    #猜測次數增加1
            print(("太大了 !!!"))   #印出結果
            lastnum=int(inputnum)-1   #將最大可能的值設為(猜測值-1)
            print("提示:",firstnum,"到",lastnum,sep="")
            #印出範圍為1到(猜測值-1)的提示
            inputnum=input("請重新輸入: ")   #取得使用者下一次的輸入
        elif int(inputnum)==int(Randomnum):   #如果猜測的數字等於答案
            count+=1    #猜測次數增加1
            print("yeah!!!你猜到了!!!")     #印出結果
            print("你猜了",count,"次",sep="")   #印出猜測次數
            break   #跳出迴圈
    else:    #若猜測的數字不在範圍內
        count+=1   #猜測次數增加1
        print("不再範圍內!!!")  #印出結果
        print("提示:",firstnum,"到",lastnum,sep="")
        #印出範圍為1到100的提示
        inputnum=input("請重新輸入: ")  #取得使用者下一次的輸入