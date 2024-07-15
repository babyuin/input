pelmen_shlepa = 0
bulmen = 0
bolshoy_bulmen = 0


print('Это тест "Какой ты пельмень"! Отвечай на вопросы и узнаешь, какой именно ТЫ пельмень!!!!!???')

question1 = 'Ты пельмень?'
question2 = 'Чего в тебе больше? мяса или теста?'
question3 = 'В тебе много бульёна?'
question4 = 'Ты большой пельмень, или маленький?'
question5 = 'Ты любишь сметану?'





print(question1)
print("1.да 2.нет")
answer1 =input("Введи ответ цифрой")
if answer1 == "1":
  pelmen_shlepa +=  1
else:
  bulmen += 1
  bolshoy_bulmen += 1
 
print(question2)
print("1.Мяса 2.Теста")
answer2 =input("Введи ответ цифрой")
if answer2 == "1":
  pelmen_shlepa +=1
  bolshoy_bulmen += 1
else:
  bulmen += 1

print(question3)
print("1.да 2.нет")
answer3 =input("Введи ответ цифрой")
if answer3 == "1":
  bulmen +=1
  bolshoy_bulmen +=1
else:
  pelmen_shlepa +=1

print(question4)
print("1.Большой 2.Маленький")
answer4 =input("Введи ответ цифрой")
if answer4 == "1":
  bolshoy_bulmen +=1
else:
  bulmen +=1
  pelmen_shlepa +=1

print(question5)
print("1 Да,люблю 2.Нет, не люблю")
answer5 =input("Введи ответ цифрой")
if answer5 =="1":
  pelmen_shlepa +=1
else:
  bulmen +=1
  bolshoy_bulmen +=1
  
if pelmen_shlepa >= 3:
  print("Поздравляем!! Вы ПЕЛЬМЕН ШЛЁПАААААА")
elif bulmen >= 3:
  print("Поздровляем!!!!! Вы БУЛЬМЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕНЬ")
elif bolshoy_bulmen >=3:
  print("Поздровляем!! ВЫ БОЛЬШОООЙ БУЛЬМЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕНЬ")
else:
  print("ТЫ НЕ ДОСТОИН БЫТЬ ПЕЛЬМЕНЬ, ПОПЛАЧЬ, иди играй в свою доту и кс2, ты реал овощь чел.")
print("Спасибо, за прохождение данного шедевротеста!")

  
  

  