import os

hero = {
    "name": "",
    "health": 100,
    "attack": 15,
    "armor": 5,
    "experience": 0,
}

current_level = 1

while True:
    print("Добро пожаловать в игру!")

    while not hero["name"]:
        hero["name"] = input("Введите имя вашего героя: ")

    while current_level <= 3:  # Теперь есть 3 уровня
        print(f"\nВы находитесь на уровне {current_level}.")

        monster = {
            "name": "Гоблин",
            "health": 40,
            "attack": 10,
            "armor": 2,
        }

        print(f"Вы встречаете монстра - {monster['name']}.")
        print(f"{monster['name']} имеет {monster['health']} здоровья, {monster['attack']} силы атаки и {monster['armor']} брони.")

        while hero['health'] > 0 and monster['health'] > 0:
            print("\nБой начинается!")
            print("Ваш ход: (1) Атаковать (2) Использовать способность (3) Сохранить и выйти")
            action = input("Выберите действие: ")

            if action == '1':
                monster['health'] -= hero['attack']
                print(f"Вы атакуете {monster['name']} и наносите {hero['attack']} урона. У {monster['name']} осталось {monster['health']} здоровья.")

                if monster['health'] > 0:
                    hero['health'] -= max(0, monster['attack'] - hero['armor'])
                    print(f"{monster['name']} атакует вас и наносит {max(0, monster['attack'] - hero['armor'])} урона. У вас осталось {hero['health']} здоровья.")
            elif action == '2':
                print("Вы используете способность, но на этом уровне у вас нет способности.")
            elif action == '3':
                with open("game_save.txt", "w", encoding="utf-8") as save_file:
                    save_file.write(f"{hero['name']},{hero['health']},{hero['attack']},{hero['armor']},{hero['experience']},{current_level}")
                print("Игра сохранена.")
                break
            else:
                print("Неправильный выбор. Попробуйте снова.")

        if monster['health'] <= 0:
            print(f"\nВы победили {monster['name']}!")
            hero['experience'] += 20
            print(f"Вы получаете 20 опыта. Ваш опыт: {hero['experience']}")
            current_level += 1
        else:
            print("Вы проиграли. Игра завершена.")
            break

    print("\nВыберите действие: (1) Новая игра (2) Загрузить игру (3) Выйти")
    choice = input()

    if choice == '1':
        hero = {
            "name": "",
            "health": 100,
            "attack": 15,
            "armor": 5,
            "experience": 0,
        }
        current_level = 1
    elif choice == '2':
        try:
            with open("game_save.txt", "r", encoding="utf-8") as save_file:
                data = save_file.read()
                parts = data.split(",")
                if len(parts) == 6:
                    hero["name"] = parts[0]
                    hero["health"] = int(parts[1])
                    hero["attack"] = int(parts[2])
                    hero["armor"] = int(parts[3])
                    hero["experience"] = int(parts[4])
                    current_level = int(parts[5])
        except FileNotFoundError:
            print("Файл сохранения не найден.")
    elif choice == '3':
        break
    else:
        print("Неправильный выбор. Попробуйте снова.")
