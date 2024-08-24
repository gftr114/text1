with open ('quotes.txt', "r", encoding="UTF-8") as file:
    for line in file:
        print(line)

author = input("Хто це пише?")
with open ('quotes.txt', "a", encoding="UTF-8") as file:
    file.write(f"({author})\n")

while True:
    answer = input("Бажаєте додати ще одну цитату? (так/ні)")

    if answer =="так":
        quote = input("Введіть цитату")
        file = open('quotes.txt', "a", encoding="UTF-8")
        file.write(quote)
        file.close()
    else:
        break

with open ('quotes.txt', "r", encoding="UTF-8") as file:
    for line in file:
        print(line)        