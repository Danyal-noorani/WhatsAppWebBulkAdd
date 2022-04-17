import webbrowser
from colored import fg

Amount = int(input("How many entries are there? --> "))

lst = []
if Amount > 1:

    fileadd = input("Enter File Address -->")
    file = open(fileadd, "r")
    with file as f:
        lst = [int(x) for x in f.read().split()]
    for i in range(len(lst)):
        print(f"http://api.whatsapp.com/send?phone={lst[i]}")
        webbrowser.open(f"http://api.whatsapp.com/send?phone={lst[i]}")
        i = i + 1


elif Amount == 1:
    Number = input("Enter the number with country code --> ")
    print(f"http://web.whatsapp.com/send?phone={Number}")
    webbrowser.open(f"http://web.whatsapp.com/send?phone={Number}")


else:
    color = fg('red')
    print("An Error Has occurred")
