OUt = /usr/bin/fileexplorer

install:
	sudo cp FileExlorer.py $(OUT)
	suod chmod 777 $(OUT)

uninstsall:
	sudo rm $(OUT)
	
