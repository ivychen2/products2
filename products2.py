
products = []
while True:
    name = input('請輸入商品名稱： ')
    if name == 'q':
        break
    price = input('請輸入商品價格： ')
    price = int(price)
    products.append([name , price])
print(products)

for p in products:
    print(p[0], "的價格是 ", p[1], '元')

#with open('products.csv', 'w') as f: 
# Microsoft 365 APP 商務版Excel 版本2105不需加寫encoding可直接正確顯示中文在excel.csv檔裡，採BIG5編碼
with open('products.csv', 'w', encoding='utf-8') as f:#若加入utf-8反而會有錯誤，需要進excel-data內進行編碼調整    
    f.write('商品,價格\n')
    for p in products:
        f.write(p[0] + ',' + str(p[1]) +'\n')

