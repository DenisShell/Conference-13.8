tickets  = int(input('Количество билетов:'))
result = 0

for person in range(tickets):
    age = int(input('Возраст участникa:'))
    if age < 18:
        result += 0
    elif 18 <= age < 25:
        result += 990
    elif age >= 25:
        result += 1390
if tickets >= 3:
    result = result - (result * 0.1)
print('Полная стоимость билетов на конференцию с учетом скидок:', result)

