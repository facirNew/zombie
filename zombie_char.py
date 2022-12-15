from tkinter import *
from tkinter import messagebox
import json


class Ben:
    def __init__(self, win):
        # TODO: separate window class
        self.win = win
        self.win.title('Ben')
        self.win.geometry('500x840+200+100')
        self.win.resizable(False, False)
        self.hp = None
        self.ip = None
        self.bonus = None
        self.weapon = {'Руки': {'ammo': 'нет', 'damage': 1, 'intelegent': 0}}
        self.weapon1 = 'Руки'
        self.weapon2 = 'Руки'
        self.heart = None
        self.brain = None
        self.muscle = None
        self.current_panel = None
        self.bonus_dmg = None
        self.weapon_var = BooleanVar()
        self.style_pink_12 = {'bg': 'pink', 'font': ("Helvetica", "12")}
        self.style_pink_14 = {'bg': 'pink', 'font': ("Helvetica", "14")}
        self.style_brown_12 = {'bg': 'brown', 'font': ("Helvetica", "12")}

    def define_new_game_params(self):
        self.hp = 70
        self.ip = 0
        self.bonus = 0
        self.weapon = {'Руки': {'ammo': 'нет', 'damage': 1, 'intelegent': 0}}
        self.weapon1 = 'Руки'
        self.weapon2 = 'Руки'

    def char_config(self):
        """main list"""
        main_menu = Menu(self.win)
        self.win.config(menu=main_menu)
        file_menu = Menu(main_menu, tearoff=0)
        file_menu.add_command(label='Новая игра', command=self.new_game)
        file_menu.add_command(label='Сохранить', command=self.save)
        file_menu.add_command(label='Загрузить', command=self.load)
        main_menu.add_cascade(label='Файл', menu=file_menu)
        frame = Frame(self.win, padx=10, pady=5, bg='pink')
        frame.pack()

        header = Label(frame, text='Путевой лист Бена', bg='pink', font=("Helvetica", "16"))
        header.grid(row=1, column=1, columnspan=3, rowspan=2)

        self.hit_points = Label(frame, text=f'Очки здоровья: {self.hp}', **self.style_pink_14)
        self.hit_points.grid(row=3, column=1, columnspan=2)

        self.int_points = Label(frame, text=f'Очки интеллекта: {self.ip}', **self.style_pink_14)
        self.int_points.grid(row=5, column=1, columnspan=2)

        self.bonus_points = Label(frame, text=f'Бонусные очки: {self.bonus}', **self.style_pink_14)
        self.bonus_points.grid(row=6, column=1, columnspan=2)

        self.weapon_left = Label(frame, text=f'Оружие 1: {self.weapon1}', **self.style_pink_14, anchor=W, width=16 )
        self.weapon_left.grid(row=8, column=1, sticky=W)

        self.ammo_left = Label(frame, text=f'Патроны: {self.weapon[self.weapon1]["ammo"]}', **self.style_pink_12)
        self.ammo_left.grid(row=9, column=1, sticky=W)

        self.damage_left = Label(frame, text=f'Урон: {self.weapon[self.weapon1]["damage"]}', **self.style_pink_12)
        self.damage_left.grid(row=10, column=1, sticky=W)

        self.int_left = Label(frame, text=f'Очки интеллекта: {self.weapon[self.weapon1]["intelegent"]}',
                              **self.style_pink_12
                              )
        self.int_left.grid(row=11, column=1, sticky=W)

        self.weapon_right = Label(frame, text=f'Оружие 2: {self.weapon2}', **self.style_pink_14, anchor=W, width=16)
        self.weapon_right.grid(row=8, column=2, sticky=W)

        self.ammo_right = Label(frame, text=f'Патроны: {self.weapon[self.weapon2]["ammo"]}', **self.style_pink_12)
        self.ammo_right.grid(row=9, column=2, sticky=W)

        self.damage_right = Label(frame, text=f'Урон: {self.weapon[self.weapon2]["damage"]}', **self.style_pink_12)
        self.damage_right.grid(row=10, column=2, sticky=W)

        self.int_right = Label(frame, text=f'Очки интеллекта: {self.weapon[self.weapon2]["intelegent"]}',
                               **self.style_pink_12
                               )
        self.int_right.grid(row=11, column=2, sticky=W)

        inv_label = Label(frame, text='Снаряжение:', **self.style_pink_14)
        inv_label.grid(row=12, column=1)

        self.inventory = Listbox(frame, activestyle='underline', borderwidth=2, width=40, **self.style_pink_12)
        self.inventory.grid(row=13, column=1, columnspan=2, rowspan=10)

        stock = Label(frame, text='Запас:', **self.style_pink_14)
        stock.grid(row=13, column=3, sticky=W)

        self.heart_stock = Label(frame, text=f'Сердце: {self.heart}', **self.style_pink_12, width=12)
        self.heart_stock.grid(row=14, column=3, sticky=W)

        self.brain_stock = Label(frame, text=f'Мозги: {self.brain}', **self.style_pink_12, width=12)
        self.brain_stock.grid(row=15, column=3, sticky=W)

        self.muscles_stock = Label(frame, text=f'Мышцы: {self.muscle}', **self.style_pink_12, width=12)
        self.muscles_stock.grid(row=16, column=3, sticky=W)

        self.notes = Text(frame, width=53, height=4, wrap=WORD, **self.style_pink_12)
        self.notes.insert(INSERT, "Заметки:\n")
        self.notes.grid(row=24, column=1, columnspan=6)

        self.current_panel_lbl = Label(frame, text=f'Продолжить с панели: {self.current_panel}', **self.style_pink_12)
        self.current_panel_lbl.grid(row=25, column=2, columnspan=2)

        user_frame = Frame(self.win, bg='brown', padx=13, pady=13)
        user_frame.pack(side='bottom')

        enemy_hp_lbl = Label(user_frame, text='Здоровье врага', **self.style_brown_12)
        enemy_hp_lbl.grid(row=1, column=1, columnspan=2, sticky=W)

        enemy_dmg_lbl = Label(user_frame, text='Урон врага', **self.style_brown_12)
        enemy_dmg_lbl.grid(row=2, column=1, columnspan=2, sticky=W)

        self.enemy_hp_ent = Entry(user_frame, bg='brown')
        self.enemy_hp_ent.grid(row=1, column=3, columnspan=2)

        self.enemy_dmg_ent = Entry(user_frame, bg='brown')
        self.enemy_dmg_ent.grid(row=2, column=3, columnspan=2)

        fight_btn = Button(user_frame, text='В бой', command=self.who_first, **self.style_brown_12)
        fight_btn.grid(row=3, column=2, columnspan=2)

        eat_btn = Button(user_frame, text='Съесть труп', command=self.eat_corpse, **self.style_brown_12, width=20)
        eat_btn.grid(row=1, column=6, columnspan=2)

        Label(user_frame, bg='brown', text='          ').grid(row=4, column=5)

        add_item_btn = Button(user_frame, text='Взять вещь', **self.style_brown_12, width=16,
                              command=self.take_item_window
                              )
        add_item_btn.grid(row=5, column=1, columnspan=3, sticky=W)

        dlt_item_btn = Button(user_frame, text='Выбросить вещь', **self.style_brown_12, width=16,
                              command=self.delete_item
                              )
        dlt_item_btn.grid(row=6, column=1, columnspan=3, sticky=W)

        add_weapon_btn = Button(user_frame, text='Взять оружие', **self.style_brown_12, width=16,
                                command=self.take_weapon_win
                                )
        add_weapon_btn.grid(row=7, column=1, columnspan=3, sticky=W)

        dlt_weapon_btn = Button(user_frame, text='Выбросить оружие', **self.style_brown_12, width=16,
                                command=self.throw_away_win
                                )
        dlt_weapon_btn.grid(row=8, column=1, columnspan=3, sticky=W)

        change_weapon_btn = Button(user_frame, text='Поменять оружие', **self.style_brown_12, width=16,
                                   command=self.change_weapon
                                   )
        change_weapon_btn.grid(row=9, column=1, columnspan=3, sticky=W)

        use_stock = Button(user_frame, text='Использовать запасы', **self.style_brown_12, width=20,
                           command=self.use_stock
                           )
        use_stock.grid(row=5, column=6, columnspan=2, sticky=W)

        go_to = Button(user_frame, text='Перейти на страницу:', **self.style_brown_12, width=20,
                       command=self.jump
                       )
        go_to.grid(row=8, column=6, columnspan=2, sticky=W)

        self.go_to_ent = Entry(user_frame, bg='brown', width=5)
        self.go_to_ent.grid(row=9, column=6, columnspan=2)
        self.new_game()

    def jump(self):
        """panel change"""
        try:  # check null
            go_to = int(self.go_to_ent.get())
            self.current_panel = go_to
            self.rewrite('p')
        except ValueError:
            self.error_message()

    def who_first(self):
        """choice first turn in battle"""
        if self.hp < 1:  # death check
            messagebox.showinfo('Вы мертвы', 'Вы мертвы. Начните игру с начала.')
            return
        try:  # check null
            self.enemy_hp = int(self.enemy_hp_ent.get())
            self.enemy_dmg = int(self.enemy_dmg_ent.get())
            self.who = Toplevel(bg='pink', bd=2, height=300, width=300)
            frame = Frame(self.who, bg='pink')
            frame.pack()
            Label(frame, text='Кто нападает?', **self.style_pink_12).grid(row=0, column=0, columnspan=3)
            Button(frame, text='Вы', command=self.fight_you, **self.style_pink_12, width=6).grid(row=1, column=0)
            Button(frame, text='Враг', command=self.fight_enemy, **self.style_pink_12, width=6).grid(row=1, column=2)
            Label(frame, text='<==>', **self.style_pink_12).grid(row=1, column=1)
        except ValueError:
            self.error_message()

    @staticmethod
    def error_message():
        messagebox.showerror('Ошибка!', 'Вы ввели неверные данные.')

    def fight_you(self):
        """if first turn gamer"""
        self.who.destroy()
        while self.hp > 0:
            self.bullets()
            self.enemy_hp -= self.weapon[self.weapon1]['damage'] + self.bonus_dmg
            self.bonus_dmg = 0
            if self.enemy_hp < 1:
                self.win_message()
                return
            self.hp -= self.enemy_dmg
        self.lose_message()

    def fight_enemy(self):
        """fight if first turn enemy"""
        self.who.destroy()
        while self.enemy_hp > 0:
            self.hp -= self.enemy_dmg
            if self.hp < 1:
                self.lose_message()
                return
            self.bullets()
            self.enemy_hp -= self.weapon[self.weapon1]['damage'] + self.bonus_dmg
            self.bonus_dmg = 0
        self.win_message()

    def win_message(self):
        """fight win message"""
        self.rewrite('p')
        messagebox.showinfo('Победа!', f'Вы победили, у вас осталось {self.hp} очков здоровья')

    def lose_message(self):
        """fight lose message. game over"""
        messagebox.showinfo('Поражение', 'У вас не осталось здоровья. Вы умерли. Еще раз.')
        self.rewrite('p')

    def bullets(self):
        """change number of ammo and weapon if out of ammo"""
        if self.weapon[self.weapon1]['ammo'] == 'нет':  # check existence of ammo
            return
        if self.weapon[self.weapon1]['ammo'] > 0:
            self.weapon[self.weapon1]['ammo'] -= 1
            self.rewrite('w')
            if self.weapon[self.weapon1]['ammo'] < 1:  # delete main weapon and get second weapon at main
                messagebox.showinfo('Патроны', f'В оружии 1 ({self.weapon1}) закончились патроны')
                self.weapon1 = self.weapon2
                self.weapon2 = 'Руки'
                self.rewrite('w')

    def eat_corpse(self):
        """window of eat corpse"""
        self.eat = Toplevel(bg='pink', bd=2)
        eat_frame = Frame(self.eat, bg='pink')
        eat_frame.pack(padx=25, pady=25)

        Label(eat_frame,
              text='Введите количество:',
              **self.style_pink_12
              ).grid(row=0, column=1)

        self.eat_number_ent = Entry(eat_frame, bg='pink')
        self.eat_number_ent.grid(row=1, column=1, pady=10)
        Button(eat_frame, text='Съесть сердце', command=self.eat_heart, **self.style_pink_12, width=20
               ).grid(row=2, columnspan=3)

        Button(eat_frame, text='Съесть мозги', command=self.eat_brain, **self.style_pink_12, width=20
               ).grid(row=3, columnspan=3)

        Button(eat_frame, text='Съесть мышцы', command=self.eat_muscles, **self.style_pink_12, width=20
               ).grid(row=4, columnspan=3)

    def eat_brain(self):
        """add brain"""
        try:
            eat_number = int(self.eat_number_ent.get())
            self.eat.destroy()
            self.brain += eat_number
            self.rewrite('p')
        except ValueError:
            self.error_message()

    def eat_heart(self):
        """add heart"""
        try:
            eat_number = int(self.eat_number_ent.get())
            self.eat.destroy()
            self.heart += eat_number
            self.rewrite('p')
        except ValueError:
            self.error_message()

    def eat_muscles(self):
        """add muscle"""
        try:
            eat_number = int(self.eat_number_ent.get())
            self.eat.destroy()
            self.muscle += eat_number
            self.rewrite('p')
        except ValueError:
            self.error_message()

    def use_stock(self):
        """use stock window"""
        self.use = Toplevel(bg='pink', bd=2)
        use_frame = Frame(self.use, bg='pink')
        use_frame.pack(padx=25, pady=25)

        Label(use_frame,
              text='Использовать одну порцию из запаса',
              **self.style_pink_12
              ).grid(row=0, column=1, pady=10)

        Button(use_frame, text='Сердце: 100г = 1 Оз', command=self.use_heart, **self.style_pink_12, width=20
               ).grid(row=2, columnspan=3)

        Button(use_frame, text='Мозги: 200г = 1 Ои', command=self.use_brain, **self.style_pink_12, width=20
               ).grid(row=3, columnspan=3)

        Button(use_frame, text='Мышцы: 100г = +2 урона\n на первый выстрел/удар',
               bg='pink', font=("Helvetica", "8"), width=30,
               command=self.use_muscles
               ).grid(row=4, columnspan=3)

        Button(use_frame, text='Выход', command=self.use.destroy, **self.style_pink_12, width=20
               ).grid(row=5, columnspan=3)

    def use_heart(self):
        """convert heart of stock at hp"""
        if self.hp >= 70:
            messagebox.showerror('Ошибка!', 'Вы полностью здоровы. Здоровье не может быть больше 70.')
            return
        if self.heart < 100:
            messagebox.showerror('Ошибка!', 'Вы съели недостаточно сердец. Необходимо не менее 100г.')
            return
        self.heart -= 100
        self.hp += 1
        self.rewrite()

    def use_brain(self):
        """convert brain at intellect"""
        if self.brain < 200:
            messagebox.showerror('Ошибка!', 'Нужно больше мозгов. Хотя бы 200г')
            return
        self.brain -= 200
        self.ip += 1
        self.rewrite()

    def use_muscles(self):
        """convert muscles at bonus damage"""
        if self.muscle < 100:
            messagebox.showerror('Ошибка!', 'Недостаточно мышц. Найдите хотя бы 100г')
            return
        self.muscle -= 200
        self.bonus_dmg += 2
        self.rewrite()

    def take_item_window(self):
        """take item window, insert name of item"""
        if len(self.inventory.get(0, END)) == 10:
            messagebox.showerror('Ошибка!', 'У вас может быть не более 10 предметов')
            return
        self.take = Toplevel(bg='pink', bd=2)
        take_frame = Frame(self.take, bg='pink')
        take_frame.pack(padx=25, pady=25)
        Label(take_frame, text='Какую вещь вы хотите взять?\nПомните, у вас может быть не больше 10 вещей',
              **self.style_pink_12
              ).grid(row=0, rowspan=2, column=0, columnspan=5)
        self.take_ent = Entry(take_frame, bg='pink', width=20)
        self.take_ent.grid(row=2, column=1, columnspan=3)
        Button(take_frame, text='Взять', **self.style_pink_12, width=20, command=self.take_item
               ).grid(row=3, column=1, columnspan=3)

    def take_item(self):
        """add insert item at listbox"""
        if self.take_ent.get() == "":
            messagebox.showerror('Ошибка!', 'Введите название вещи')
        else:
            self.inventory.insert(END, self.take_ent.get())
            self.take.destroy()
            return

    def delete_item(self):
        """delete item at listbox"""
        select = list(self.inventory.curselection())
        select.reverse()
        for i in select:
            self.inventory.delete(i)

    def take_weapon_win(self):
        """window take weapon, insert weapon name and his attribute"""
        self.weapon_win = Toplevel(bg='pink', bd=2)
        weapon_frame = Frame(self.weapon_win, bg='pink')
        weapon_frame.grid(padx=25, pady=25)

        Label(weapon_frame, text='Название оружия', **self.style_pink_12).grid(row=0, column=0, columnspan=2)

        self.w_name_ent = Entry(weapon_frame, bg='pink')
        self.w_name_ent.grid(row=0, column=2, columnspan=2)

        Label(weapon_frame, text='Урон', **self.style_pink_12).grid(row=1, column=0, columnspan=2)

        self.w_damage_ent = Entry(weapon_frame, bg='pink')
        self.w_damage_ent.grid(row=1, columnspan=2, column=2)

        Label(weapon_frame, text='Очки интеллекта', **self.style_pink_12).grid(row=2, column=0, columnspan=2)

        self.w_int_ent = Entry(weapon_frame, bg='pink')
        self.w_int_ent.grid(row=2, column=2, columnspan=2)

        Label(weapon_frame, text='Патроны', **self.style_pink_12).grid(row=3, column=0, columnspan=2)

        self.w_ammo_ent = Entry(weapon_frame, bg='pink')
        self.w_ammo_ent.grid(row=3, column=2, columnspan=2)

        self.rbutton(weapon_frame, 4, 0, 4,2)

        Button(weapon_frame, text='Взять', **self.style_pink_12, command=self.take_weapon
               ).grid(row=5, column=1, columnspan=2)

    def take_weapon(self):
        """take weapon on first or second slot"""
        try:
            name = self.w_name_ent.get().capitalize()
            dmg = int(self.w_damage_ent.get())
            ammo = self.w_ammo_ent.get()
            intelegent = int(self.w_int_ent.get())
        except ValueError:
            self.error_message()
            return
        if not name.isalnum():
            self.error_message()
            return
        try:
            ammo = int(ammo)
            if ammo == 0:
                ammo = 'нет'
        except ValueError:
            ammo = 'нет'
        if intelegent > self.ip:
            messagebox.showerror('Ошибка!', 'Вы не можете использовать это оружие.\nНе хватает интеллекта')
            return
        self.weapon[name] = {"ammo": ammo, "damage": dmg, "intelegent": intelegent}
        if self.weapon_var.get() == False:
            self.weapon1 = name
            self.rewrite()
        if self.weapon_var.get() == True:
            self.weapon2 = name
            self.rewrite()
        self.weapon_win.destroy()

    def throw_away_win(self):
        """delete weapon from first or second slot window"""
        self.discard = Toplevel(bg='pink', bd=2)
        discard_frame = Frame(self.discard, bg='pink', padx=25, pady=25)
        discard_frame.pack()

        Label(discard_frame, text='Какое оружие вы хотите выбросить?', **self.style_pink_12
              ).grid(row=0, column=1, columnspan=2)

        self.rbutton(discard_frame, 2, 0, 2, 2)

        Button(discard_frame, text='Выбросить', **self.style_pink_12, command=self.discard_weapon
               ).grid(row=3, column=1, columnspan=2)

    def rbutton(self, frame, row1, column1, row2, column2):
        """delete weapon from first or second slot"""
        self.weapon_var.set(False)
        Radiobutton(frame, text='Оружие 1', variable=self.weapon_var, value=False, **self.style_pink_12
                    ).grid(row=row1, column=column1, columnspan=2)
        Radiobutton(frame, text='Оружие 2', variable=self.weapon_var, value=True, **self.style_pink_12
                    ).grid(row=row2, column=column2, columnspan=2)

    def discard_weapon(self):
        """check slot to delete weapon"""
        if not self.weapon_var.get():
            self.weapon1 = 'Руки'
            self.rewrite()
        else:
            self.weapon2 = 'Руки'
            self.rewrite()
        self.discard.destroy()

    def change_weapon(self):
        """swap weapon slot"""
        self.weapon1, self.weapon2 = self.weapon2, self.weapon1
        self.rewrite('w')

    def rewrite(self, arg="a"):
        """rewrite label at main page. 'a' = all, 'w' = weapon only, 'p' = parameters only"""
        if arg == 'w':
            self.weapon_left.config(text=f'Оружие 1: {self.weapon1}')
            self.ammo_left.config(text=f'Патроны: {self.weapon[self.weapon1]["ammo"]}')
            self.damage_left.config(text=f'Урон: {self.weapon[self.weapon1]["damage"]}')
            self.int_left.config(text=f'Очки интеллекта: {self.weapon[self.weapon1]["intelegent"]}')
            self.weapon_right.config(text=f'Оружие 2: {self.weapon2}')
            self.ammo_right.config(text=f'Патроны: {self.weapon[self.weapon2]["ammo"]}')
            self.damage_right.config(text=f'Урон: {self.weapon[self.weapon2]["damage"]}')
            self.int_right.config(text=f'Очки интеллекта: {self.weapon[self.weapon2]["intelegent"]}')
        if arg == 'p':
            self.hit_points.config(text=f'Очки здоровья: {self.hp}')
            self.int_points.config(text=f'Очки интеллекта: {self.ip}')
            self.bonus_points.config(text=f'Бонусные очки: {self.bonus}')
            self.current_panel_lbl.config(text=f'Продолжить с панели: {self.current_panel}')
            self.brain_stock.config(text=f'Мозги: {self.brain}')
            self.heart_stock.config(text=f'Сердце: {self.heart}')
            self.muscles_stock.config(text=f'Мышцы: {self.muscle}')
        if arg == 'a':
            self.rewrite('p')
            self.rewrite('w')

    def save(self):
        """save variables at file"""
        data = {}
        data['inventory'] = self.inventory.get(0, END)
        data['notes'] = self.notes.get(1.0, END)
        data['hp'] = self.hp
        data['ip'] = self.ip
        data['bonus'] = self.bonus
        data['weapon'] = self.weapon
        data['weapon1'] = self.weapon1
        data['weapon2'] = self.weapon2
        data['heart'] = self.heart
        data['brain'] = self.brain
        data['muscle'] = self.muscle
        data['current_panel'] = self.current_panel
        data['bonus_dmg'] = self.bonus_dmg
        # TODO: create global variable with filepath
        with open(FILE_PATH, 'w') as save_file:
            json.dump(data, save_file)

    def load(self):
        """load variables from file"""
        with open(FILE_PATH) as load_file:
            data = json.load(load_file)
            self.hp = data['hp']
            self.ip = data['ip']
            self.bonus = data['bonus']
            self.weapon = data['weapon']
            self.weapon1 = data['weapon1']
            self.weapon2 = data['weapon2']
            self.heart = data['heart']
            self.brain = data['brain']
            self.muscle = data['muscle']
            self.current_panel = data['current_panel']
            self.bonus_dmg = data['bonus_dmg']
            self.inventory.delete(0, END)
            for i in data['inventory']:
                self.inventory.insert(END, i)
            self.notes.delete(1.0, END)
            self.notes.insert(1.0, data['notes'])
            self.rewrite()

    def new_game(self):
        """change variables at start parameters"""
        self.inventory.delete(0, END)
        self.notes.delete(1.0, END)
        self.notes.insert(1.0, "Заметки:\n")
        self.hp = 70
        self.ip = 0
        self.bonus = 0
        self.weapon = {'Руки': {'ammo': 'нет', 'damage': 1, 'intelegent': 0}}
        self.weapon1 = 'Руки'
        self.weapon2 = 'Руки'
        self.heart = 0
        self.brain = 0
        self.muscle = 0
        self.current_panel = 1
        self.bonus_dmg = 0
        self.rewrite()

# class Judi:
#     def __init__(self, win):
#         self.win = win
#         self.win.title('Judi')
#         self.win.geometry('200x200')

if __name__ == "__main__":
    FILE_PATH = 'save_game.json'
    window = Tk()
    Ben(window).char_config()
    # Judi(window)
    window.mainloop()
