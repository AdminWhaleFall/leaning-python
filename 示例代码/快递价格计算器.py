
while 1==1:
	zhongliang=int(input("请输入重量（不满一公斤的按1公斤计算）："))
	didian=input("请输入地点编号（1.其他  2.新疆/西藏:20元  3.港澳台/国外  4.东三省/宁夏/青海/海南）：")
	kauidifei=0

	if zhongliang<=3:
		if didian=="1":
			kauidifei=10
		elif didian=="2":
			kauidifei=20
		elif didian=="3":
		    kauidifei=10000
		elif didian=="4":
			kauidifei=12
		else:
			kauidifei=30000

	elif zhongliang>3:
		if didian=="1":
			kauidifei=10+(zhongliang-3)*5
		elif didian=="2":
			kauidifei=20+(zhongliang-3)*20
		elif didian=="3":
		    kauidifei=20000
		elif didian=="4":
			kauidifei=12+(zhongliang-3)*10
		else:
			kauidifei=30000
	else:
		print("输入错误！")

	if kauidifei==10000:
		print("不接受寄件！")
	elif kauidifei==20000:
		print("联系总公司！")
	elif kauidifei==30000:
		print("请重新输入地点编号！")
	else:
		print("您好！本次快递重量为:",zhongliang,"公斤，金额为：",kauidifei,"元")