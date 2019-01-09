# coding:utf-8
import datetime
import jpholiday
import pyperclip

def youbi(date):
	delta = date - datetime.date(1900,1,1) # 1900/1/1 は月曜日
	dict = {0: "月", 1: "火", 2: "水", 3: "木", 4: "金", 5: "土", 6: "日"}
	return dict[delta.days % 7]

def isHoliday(date):
	pass

while True: # 開始日と終了日の指定
	try:
		print("開始日を入力してください (ex. 20180101): ", end='')
		start_str = input()
		start_year = int(start_str[:4])
		start_month = int(start_str[4:6])
		start_day = int(start_str[6:])
		start_date = datetime.date(start_year, start_month, start_day)

		print("終了日を入力してください (ex. 20180912): ", end='')
		end_str = input()
		end_year = int(end_str[:4])
		end_month = int(end_str[4:6])
		end_day = int(end_str[6:])
		end_date = datetime.date(end_year, end_month, end_day)

		break

	except IndexError:
		print("日程の入力が間違っています")
		print()
	except ValueError:
		print("日程の入力が間違っています")
		print()

delta = end_date - start_date + datetime.timedelta(1)

while True: # 休日の分割数を指定
	print("休日の分割数を指定してください (デフォルト値 = 4): ", end='')
	try:
		holidayStr = input()
		if holidayStr == "":
			holidayCnt = 4
		else:
			holidayCnt = int(holidayStr)
		break
	except ValueError:
		print("入力が不正です")
		print()

text = ""
for i in range(int(delta.days)):
	date = start_date + datetime.timedelta(i)
	if youbi(date) == "土" or youbi(date) == "日" or jpholiday.is_holiday(date):
		for j in range(holidayCnt):
			text += str(date.month) + "/" + str(date.day) + "(" + youbi(date) + ")[" + str(j+1) + "]\n"
	else:
		text += str(date.month) + "/" + str(date.day) + "(" + youbi(date) + ")\n"

pyperclip.copy(text)
print("コピーしました。伝助に貼り付けてください。")