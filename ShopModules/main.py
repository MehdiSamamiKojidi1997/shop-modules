import re


class user_management:
    def __init__(self):
        pass#این قسمت را برای تشخیص کلید گذاشتم. اگر از قبل کلید داشته باشد نیازی
         #  به login یا signup نیست.
    def read_database(self,user_name):
        pass# این قسمت به database متصل است. خروجی در اینجا اطلاعات کاربر است.
    def login(self,user_name,password):#خروجی این متد یک پیام و یک true یا false است.
        if len(self.read_database(user_name))==0 or (self.read_database(user_name))[1]!=password:
            return "Wrong Username or Password!\nDon't have an Account? Signup first!",False
        else:          #پیام برای نمایش مشکل و true یا false برای عملیات بعدی(ورود به پنجره ی جدید و...) است.
            return f"Wellcome {user_name}!",True
    def signup(self,user_name,password,password_confirmation):
        if len(self.read_database(user_name))!=0:
            a="Username has been used before!"
            b=False
        else:
            a="Username is Ok!"
            b=True
        if not re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$",password):
            c="Password must have at least one uppercase letter, one lowercase letter, and one number!"
            d=False
        else:
            c="Password is Ok!"
            d=True
        if d and password!=password_confirmation:
            e="Password confirmation doesn't match!"
            f=False
        else:
            e=""
            f=True
        if b and d and f:
            return f"You have signed up!",True#خروجی یک پیام همراه با true یا false است.
        else: # باز هم مثل قبل true یا false برای عملیات بعدی است.
            return f"{a}\n{c}\n{e}",False


    def read_user_settings(self):
        pass
