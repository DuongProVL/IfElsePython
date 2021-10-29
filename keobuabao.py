from random import randint

player = input("Vui lòng nhập Keo, Bua, Bao: ")
computer = randint(0,2)

if computer == 0:
	computer = "Bua"
elif computer == 1:
	computer = "Keo"
else:
	computer = "Bao"
if player == "Bao":
	if computer == "Bao":
		print("-----")
		print("Bạn đã chọn: " + player)
		print("VS")
		print("Máy tính đã chọn: " + computer)
		print("-----")
		print("Hoà")
	if computer == "Bua":
		print("-----")
		print("Bạn đã chọn: " + player)
		print("VS")
		print("Máy tính đã chọn: " + computer)
		print("-----")
		print("Bạn đã thắng")
	if computer == "Keo":
		print("-----")
		print("Bạn đã chọn: " + player)
		print("VS")
		print("Máy tính đã chọn: " + computer)
		print("-----")
		print("Bạn đã thua")
if player == "Bua":
	if computer == "Bua":
		print("-----")
		print("Bạn đã chọn: " + player)
		print("VS")
		print("Máy tính đã chọn: " + computer)
		print("-----")
		print("Hoà")
	if computer == "Keo":
		print("-----")
		print("Bạn đã chọn: " + player)
		print("VS")
		print("Máy tính đã chọn: " + computer)
		print("-----")
		print("Bạn đã thắng")
	if computer == "Bao":
		print("-----")
		print("Bạn đã chọn: " + player)
		print("VS")
		print("Máy tính đã chọn: " + computer)
		print("-----")
		print("Bạn đã thua")
if player == "Keo":
	if computer == "Keo":
		print("-----")
		print("Bạn đã chọn: " + player)
		print("VS")
		print("Máy tính đã chọn: " + computer)
		print("-----")
		print("Hoà")
	if computer == "Bao":
		print("-----")
		print("Bạn đã chọn: " + player)
		print("VS")
		print("Máy tính đã chọn: " + computer)
		print("-----")
		print("Bạn đã thắng")
	if computer == "Bua":
		print("-----")
		print("Bạn đã chọn: " + player)
		print("VS")
		print("Máy tính đã chọn: " + computer)
		print("-----")
		print("Bạn đã thua")
