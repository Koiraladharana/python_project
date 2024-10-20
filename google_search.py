from googlesearch import search

print("WelCome to google search tool!")

query= input("What do you want to search ? :")

for i in search(query, start=1 ,stop=10):
    print(i)
