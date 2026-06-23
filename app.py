from flask import Flask
app=Flask(__name__) #Python 內建變數 #__name__ 代表目前使用得模組
# Python 每個檔案在執行時，都會自動有一個內建變數
# 被 Python 直接執行的那個檔案，它的 __name__ 會是 __main__
@app.route("/") # 路由裝飾器（decorator）# 當使用者訪問網站根目錄 / 時，就執行下面這個函式
def home():
    return "Hello Flask" #Flask 會把這個字串當成 HTTP response 回傳出去

@app.route("/test")
def test():
    return "This is test"

if __name__=="__main__": # 如果以主程式執行
    app.run() # 立刻啟動伺服器