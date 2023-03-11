# 服學-A時段-第2組
## import
### 基本介紹
隨著程式越變越長，如果沒有適當的組織程式碼，除了會降低開發的效率外，也不易於維護，因此會想要分開成幾個檔案，好好分類，讓程式比較好維護。可能也會想用一個之前已經在其他程式寫好的函式，但不想要複製該函式的原始定義到所有使用他的程式裡。所以模組(Module)化就顯得相當的重要，讓程式碼能夠透過引用的方式來重複使用，提升重用性(Reusable)。

為了支援這一點， Python 有一種方法可以將定義放入檔案中，之後只要在程式中引用這個檔案就可以使用定義在這個檔案裡的函式了。這種檔案稱為模組 (module)，其中包含了相關性較高的程式碼，模組中的定義可以被 `import` 到其他模組中。

但是隨著專案模組(Module)的增加，將難以管理及問題的追蹤，這時候就能將模組(Module)打包成套件(Package)，套件(Package)就是一個容器(資料夾)，包含了一個或多個的模組(Module)，並且擁有__init__.py檔案，其中可以撰寫套件(Package)初始化的程式碼，利用其階層式的結構來彈性規劃模組(Module)。

`import` 很大的好處就是可以在自己的程式中使用別人寫在別的檔案的函式，這樣就不用自己花時間花心力寫，可以把心力花在其他地方創造出更多樣的程式。

### import 用法
```python
# 引用 numpy 並用 np 稱呼使用他
import numpy as np
# 使用 numpy 的 array 函式
np.array([1, 2, 3])
# 從 matplotlib 引用 pyplot 以 plt 稱呼
from matplotlib import pyplot as plt
```

**題外話**

呼叫函式的語法
```python
function(parameter)
# parameter 可能有可能沒有
```
把函式賦值給某個變數
```python
a = function
a() # 呼叫 a 相當於呼叫函式 function 
# a() 和 function() 執行結果一樣
```

* 引用模組中的所有名稱
   ```python
   from module import *  
   ```
   這個寫法會 import 模組中所有的名稱（包含變數和函式），除了使用底線（_）開頭的名稱。這個功能最好不要用，因為會引入未知的名稱可能會覆蓋某些已經命名的物件，而且可讀性較差。

* 引用模組或套件中的變數
   ```python
   from module import var1, var2
   sum = var1 + var2
   ```
   之後直接像是平常一樣使用引用來的變數就好

* 引用模組
   ```python
   # 引用模組 module2
   import module2
   # 使用 function2
   module2.function2()
   ```
   
   ```python
   # 從模組 module2 中引用函式 function2 和 function3
   from module2 import function2, function3
   # 使用 function2
   function2()
   ```
   
* 引用套件
   ```python
   # 引用套件 package2
   import package2
   ```
   
   ```python
   # 從套件 package2 中引用模組 module2
   from package2 import module2
   # 使用 module2 裡的 function2
   module2.function2()
   ```
   
   ```python
   # 從套件 package2 中引用模組 module2
   import package2.module2
   # 使用 module2 裡的 function2
   package2.module2.function2()
   ```


   
### 常用函式庫

pandas：用於資料分析、資料建模、資料視覺化的第三方庫。
numpy:開源的Python機器學習庫。
Tkinter:提供圖形化介面。
math: 數學相關數值或函數。
turtle:繪製影像的函式庫，
### 實例
**1. 算圓的周長、面積(利用math函式庫)**
```python=
import math # pi值定義在math函式庫
Radius = 10
Circle_Perimeter = 10*2*math.pi
Circle_Area = 10*10*math.pi
print(math.pi)
print(Circle_perimeter,Circle_Area)
```

![](https://i.imgur.com/chm72rU.png)


錯誤示範:
```python=
Radius = 10
Circle_Perimeter = 10*2*math.pi
Circle_Area = 10* 10*math.pi
print(math.pi)
print(Circle_perimeter,Circle_Area)
```

![](https://i.imgur.com/qNfVT8s.png)


---

**2. 畫奧林匹克會旗(利用turtle函式庫)**
```python=
import turtle
turtle.pensize(10)  #調整畫筆大小

turtle.color("blue") #將畫筆顏色改成藍色
turtle.penup()  #將畫筆筆頭提起來
                #避免移動時，畫到不必要的部分
turtle.goto(-110,-25) #將畫筆筆頭移動到此點
turtle.pendown() #將畫筆筆頭抵住此點，
turtle.circle(45) #以此點為中心畫出半徑
                  #45pixel的圓。
turtle.color("black") #換顏色
turtle.penup()
turtle.goto(0,-25) #換到適當位置
turtle.pendown()
turtle.circle(45)
                    #以下依照會旗改變顏色。
turtle.color("red")
turtle.penup()
turtle.goto(110,-25)
turtle.pendown()
turtle.circle(45)

turtle.color("yellow")
turtle.penup()
turtle.goto(-55,-75)
turtle.pendown()
turtle.circle(45)

turtle.color("green")
turtle.penup()
turtle.goto(55,-75)
turtle.pendown()
turtle.circle(45)

turtle.done() #讓程式執行完，不要自動關掉。
```
完成品:
![](https://i.imgur.com/79vaw9e.png)


---







## 猜數字
```python=
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
```
