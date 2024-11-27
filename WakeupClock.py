import winsound
import time

def wakeupTimer(t):
    while t > 0:# حلقه وایل تا وقتی عددی که کاربر داده صفر نشده، تکرار میشه
        min , sec = divmod(t,60) #  این تابع عدد سمت راست رو تقسیم بر سمت چپی میکنه و یک تاپل دو جزئی میده که جز اول عدد صحیح تقسیم شده و جزو راستی باقیمانده تقسیمه. بعد این تاپل رو میریزه تو متغیر هایی که بش دادیم
        timer = str(min) + ":" + str(sec) #متغیر های بالا رو در قالب یک تایمر به نمایش میذاریم
        print(timer, end="\r ") # گزینه اند و بعدش اسلش آر میان یه کاری میکنن که نره خط بعد و همونجا کد پاکمیشه باز اجرا میشه
        time.sleep(1) #یک ثانیه توقف کد با این تابع اجرا میشه
        t -= 1

def wakeup(): 
    for i in range(5): # با این کد میگیم 5 بار عملیات درونشو اجرا کنه
        for j in range(2):# با این کد میگیم 2 بار عملیات درونشو اجرا کنه
            winsound.Beep(400,200) # این تابع صدای بوق با فرکانس 400 و طول 200 میلی ثانیه اجرا میکنه
        time.sleep(1)    # تایمو یک ثانیه نگه میداره
t = int(input("Enter the time in seconds: ")) # گرفتن یک عدد در از کاربر
wakeupTimer(t) # تابع wakeupTimer رو اجرا میکنه
wakeup()# تابعو فراخوانی میکنه
    
