import os # operating system

products = []
if os.path.isfile('products.csv'): # 檢查檔案在不在
    print('yeah! 找到檔案了!')
    # 讀取檔案
    with open('products.csv', 'r') as f:
    # 在檔案寫入時若採用encoding='utf-8'，但讀取時未加encoding='utf-8'，仍可正常讀取無誤
    # with open('products.csv', 'r', encoding='utf-8') as f:#加了encoding='utf-8'反而只讀的到欄位名，讀取不到資料
        for line in f:
            if '商品,價格' in line:
                continue # 底下第9、10行不執行，直接跳到下一回會的for迴圈
            name, price = line.strip().split(',')
            products.append([name, price])
    print(products)
else:
    print('找不到檔案…')

# 讓使用者輸入
while True:
    name = input('請輸入商品名稱： ')
    if name == 'q':
        break
    price = input('請輸入商品價格： ')
    price = int(price)
    products.append([name , price])
print(products)

# 印出所有的購買紀錄
for p in products:
    print(p[0], "的價格是 ", p[1], '元')

# 寫入檔案
with open('products.csv', 'w') as f: 
# Microsoft 365 APP 商務版Excel 版本2105不需加寫encoding可直接正確顯示中文在excel.csv檔裡，採BIG5編碼
#with open('products.csv', 'w', encoding='utf-8') as f:#若加入utf-8反而會有錯誤，需要進excel-data內進行編碼調整    
    f.write('商品,價格\n')
    for p in products:
        f.write(p[0] + ',' + str(p[1]) +'\n')



