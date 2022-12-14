from tkinter import *
from tkinter import messagebox
import json

class Ben:
    def __init__(self, win):
        self.win = win
        self.win.title('Ben')
        self.win.geometry('500x840+200+100')
        self.win.resizable(False, False)
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
        self.weapon_var = BooleanVar()

    # main list
    def char_config(self):
        mainmenu = Menu(self.win)
        self.win.config(menu=mainmenu)
        filemenu = Menu(mainmenu, tearoff=0)
        filemenu.add_command(label='Новая игра')
        filemenu.add_command(label='Сохранить', command=self.save)
        filemenu.add_command(label='Загрузить', command=self.load)
        mainmenu.add_cascade(label='Файл', menu=filemenu)
        frame = Frame(self.win, padx=10, pady=5, bg='pink')
        frame.pack()

        header = Label(frame,
                       text='Путевой лист Бена',
                       bg='pink', font=("Helvetica", "16")
                       )
        header.grid(row=1, column=1, columnspan=3, rowspan=2)

        self.hit_points = Label(
            frame,
            text=f'Очки здоровья: {self.hp}',
            bg='pink', font=("Helvetica", "14")
        )
        self.hit_points.grid(row=3, column=1, columnspan=2)

        self.int_points = Label(frame,
                                text=f'Очки интеллекта: {self.ip}',
                                bg='pink', font=("Helvetica", "14")
                                )
        self.int_points.grid(row=5, column=1, columnspan=2)

        self.bonus_points = Label(frame,
                                  text=f'Бонусные очки: {self.bonus}',
                                  bg='pink', font=("Helvetica", "14")
                                  )
        self.bonus_points.grid(row=6, column=1, columnspan=2)

        self.weapon_left = Label(frame,
                                 text=f'Оружие 1: {self.weapon1}',
                                 bg='pink', font=("Helvetica", "14"), anchor=W, width=16
                                 )
        self.weapon_left.grid(row=8, column=1, sticky=W)

        self.ammo_left = Label(frame,
                               text=f'Патроны: {self.weapon[self.weapon1]["ammo"]}',
                               bg='pink', font=("Helvetica", "12")
                               )
        self.ammo_left.grid(row=9, column=1, sticky=W)

        self.damage_left = Label(frame,
                                 text=f'Урон: {self.weapon[self.weapon1]["damage"]}',
                                 bg='pink', font=("Helvetica", "12")
                                 )
        self.damage_left.grid(row=10, column=1, sticky=W)

        self.int_left = Label(frame,
                              text=f'Очки интеллекта: {self.weapon[self.weapon1]["intelegent"]}',
                              bg='pink', font=("Helvetica", "12")
                              )
        self.int_left.grid(row=11, column=1, sticky=W)

        self.weapon_right = Label(frame,
                                  text=f'Оружие 2: {self.weapon2}',
                                  bg='pink', font=("Helvetica", "14"),anchor=W, width=16
                                  )
        self.weapon_right.grid(row=8, column=2, sticky=W)

        self.ammo_right = Label(frame,
                                text=f'Патроны: {self.weapon[self.weapon2]["ammo"]}',
                                bg='pink', font=("Helvetica", "12")
                                )
        self.ammo_right.grid(row=9, column=2, sticky=W)

        self.damage_right = Label(frame,
                                  text=f'Урон: {self.weapon[self.weapon2]["damage"]}',
                                  bg='pink', font=("Helvetica", "12")
                                  )
        self.damage_right.grid(row=10, column=2, sticky=W)

        self.int_right = Label(frame,
                               text=f'Очки интеллекта: {self.weapon[self.weapon2]["intelegent"]}',
                               bg='pink', font=("Helvetica", "12")
                               )
        self.int_right.grid(row=11, column=2, sticky=W)

        inv_label = Label(frame,
                          text='Снаряжение:',
                          bg='pink', font=("Helvetica", "14")
                          )
        inv_label.grid(row=12, column=1)

        self.inventory = Listbox(frame,
                                 activestyle='underline', borderwidth=2, width=40,
                                 bg='pink', font=("Helvetica", "12")
                                 )
        self.inventory.grid(row=13, column=1, columnspan=2, rowspan=10)

        stock = Label(frame,
                      text='Запас:',
                      bg='pink', font=("Helvetica", "14")
                      )
        stock.grid(row=13, column=3, sticky=W)

        self.heart_stock = Label(frame,
                                 text=f'Сердце: {self.heart}',
                                 bg='pink', font=("Helvetica", "12"), width=12
                                 )
        self.heart_stock.grid(row=14, column=3, sticky=W)

        self.brain_stock = Label(frame,
                                 text=f'Мозги: {self.brain}',
                                 bg='pink', font=("Helvetica", "12"), width=12
                                 )
        self.brain_stock.grid(row=15, column=3, sticky=W)

        self.muscles_stock = Label(frame,
                                   text=f'Мышцы: {self.muscle}',
                                   bg='pink', font=("Helvetica", "12"), width=12
                                   )
        self.muscles_stock.grid(row=16, column=3, sticky=W)

        self.notes = Text(frame, width=53, height=4, wrap=WORD, bg='pink', font=("Helvetica", "12"))
        self.notes.insert(INSERT, "Заметки:\n")
        self.notes.grid(row=24, column=1, columnspan=6)

        self.current_panel_lbl = Label(frame,
                                       text=f'Продолжить с панели: {self.current_panel}',
                                       bg='pink', font=("Helvetica", "12"))
        self.current_panel_lbl.grid(row=25, column=2, columnspan=2)

        user_frame = Frame(self.win, bg='brown', padx=13, pady=13)
        user_frame.pack(side='bottom')

        enemy_hp_lbl = Label(user_frame,
                             text='Здоровье врага',
                             bg='brown', font=("Helvetica", "12")
                             )
        enemy_hp_lbl.grid(row=1, column=1, columnspan=2, sticky=W)

        enemy_dmg_lbl = Label(user_frame,
                              text='Урон врага',
                              bg='brown', font=("Helvetica", "12")
                              )
        enemy_dmg_lbl.grid(row=2, column=1, columnspan=2, sticky=W)

        self.enemy_hp_ent = Entry(user_frame, bg='brown')
        self.enemy_hp_ent.grid(row=1, column=3, columnspan=2)

        self.enemy_dmg_ent = Entry(user_frame, bg='brown')
        self.enemy_dmg_ent.grid(row=2, column=3, columnspan=2)

        fight_btn = Button(user_frame,
                           text='В бой',
                           command=self.who_first,
                           bg='brown', font=("Helvetica", "12")
                           )
        fight_btn.grid(row=3, column=2, columnspan=2)

        eat_btn = Button(user_frame,
                         text='Съесть труп',
                         command=self.eat_corpse,
                         bg='brown', font=("Helvetica", "12"), width=20
                         )
        eat_btn.grid(row=1, column=6, columnspan=2)

        Label(user_frame, bg='brown', text='          ').grid(row=4, column=5)

        add_item_btn = Button(user_frame,
                              text='Взять вещь',
                              bg='brown', font=("Helvetica", "12"), width=16,
                              command=self.take_item_window
                              )
        add_item_btn.grid(row=5, column=1, columnspan=3, sticky=W)

        dlt_item_btn = Button(user_frame,
                              text='Выбросить вещь',
                              bg='brown', font=("Helvetica", "12"), width=16,
                              command=self.delete_item
                              )
        dlt_item_btn.grid(row=6, column=1, columnspan=3, sticky=W)

        add_weapon_btn = Button(user_frame,
                                text='Взять оружие',
                                bg='brown', font=("Helvetica", "12"), width=16,
                                command=self.take_weapon_win
                                )
        add_weapon_btn.grid(row=7, column=1, columnspan=3, sticky=W)

        dlt_weapon_btn = Button(user_frame,
                                text='Выбросить оружие',
                                bg='brown', font=("Helvetica", "12"), width=16,
                                command=self.throw_away_win
                                )
        dlt_weapon_btn.grid(row=8, column=1, columnspan=3, sticky=W)

        change_weapon_btn = Button(user_frame,
                                   text='Поменять оружие',
                                   bg='brown', font=("Helvetica", "12"), width=16,
                                   command=self.change_weapon
                                   )
        change_weapon_btn.grid(row=9, column=1, columnspan=3, sticky=W)

        use_stock = Button(user_frame,
                           text='Использовать запасы',
                           command=self.use_stock,
                           bg='brown', font=("Helvetica", "12"), width=20
                           )
        use_stock.grid(row=5, column=6, columnspan=2, sticky=W)

        go_to = Button(user_frame,
                       text='Перейти на страницу:',
                       command=self.jump,
                       bg='brown', font=("Helvetica", "12"), width=20
                       )
        go_to.grid(row=8, column=6, columnspan=2, sticky=W)

        self.go_to_ent = Entry(user_frame, bg='brown', width=5)
        self.go_to_ent.grid(row=9, column=6, columnspan=2)

    # panel change
    def jump(self):
        # check null
        try:
            go_to = int(self.go_to_ent.get())
            self.current_panel = go_to
            self.current_panel_lbl.config(text=f'Продолжить с панели: {self.current_panel}')
        except ValueError:
            self.error()

    # choice first turn in battle
    def who_first(self):
        # death check
        if self.hp < 1:
            messagebox.showinfo('Вы мертвы', 'Вы мертвы. Начните игру с начала.')
            return
        # check null
        try:
            self.enemy_hp = int(self.enemy_hp_ent.get())
            self.enemy_dmg = int(self.enemy_dmg_ent.get())
            self.who = Toplevel(bg='pink', bd=2, height=300, width=300)
            frame = Frame(self.who, bg='pink')
            frame.pack()
            Label(frame,
                  text='Кто нападает?',
                  bg='pink', font=("Helvetica", "12")).grid(row=0, column=0, columnspan=3)
            Button(frame,
                   text='Вы',
                   command=self.fight_you,
                   bg='pink', font=("Helvetica", "12"), width=6).grid(row=1, column=0)
            Button(frame,
                   text='Враг',
                   command=self.fight_enemy,
                   bg='pink', font=("Helvetica", "12"), width=6).grid(row=1, column=2)
            Label(frame,
                  text='<==>',
                  bg='pink', font=("Helvetica", "12")).grid(row=1, column=1)
        except ValueError:
            self.error()

    @staticmethod
    def error():
        messagebox.showerror('Ошибка!', 'Вы ввели неверные данные.')

    # if first turn gamers
    def fight_you(self):
        self.who.destroy()
        while self.hp > 0:
            self.bullets()
            self.enemy_hp -= self.weapon[self.weapon1]['damage'] + self.bonus_dmg
            self.bonus_dmg = 0
            if self.enemy_hp < 1:
                self.winer()
                return
            self.hp -= self.enemy_dmg
        self.loser()

    # if first turn enemy
    def fight_enemy(self):
        self.who.destroy()
        while self.enemy_hp > 0:
            self.hp -= self.enemy_dmg
            if self.hp < 1:
                self.loser()
                return
            self.bullets()
            self.enemy_hp -= self.weapon[self.weapon1]['damage'] + self.bonus_dmg
            self.bonus_dmg = 0
        self.winer()

    # fight win message
    def winer(self):
        self.hit_points.config(text=f'Очки здоровья: {self.hp}')
        messagebox.showinfo('Победа!', f'Вы победили, у вас осталось {self.hp} очков здоровья')

    # fight lose message. game over
    def loser(self):
        messagebox.showinfo('Поражение', 'У вас не осталось здоровья. Вы умерли. Еще раз.')
        self.hit_points.config(text=f'Очки здоровья: {self.hp}')

    # change number of ammo and weapon if out of ammo
    def bullets(self):
        # check existence of ammo
        if self.weapon[self.weapon1]['ammo'] == 'нет':
            return
        if self.weapon[self.weapon1]['ammo'] > 0:
            self.weapon[self.weapon1]['ammo'] -= 1
            self.ammo_left.config(text=f'Патроны: {self.weapon[self.weapon1]["ammo"]}')
            # delete main weapon and get second weapon at main
            if self.weapon[self.weapon1]['ammo'] < 1:
                messagebox.showinfo('Патроны', f'В оружии 1 ({self.weapon1} закончились патроны')
                self.weapon1 = self.weapon2
                self.weapon2 = 'hands'
                self.weapon_left.config(text=f'Оружие 1: {self.weapon1}')
                self.weapon_right.config(text=f'Оружие 2: {self.weapon2}')
                self.ammo_left.config(text=f'Патроны: {self.weapon[self.weapon1]["ammo"]}')
                self.ammo_right.config(text=f'Патроны: {self.weapon[self.weapon2]["ammo"]}')
                self.damage_left.config(text=f'Урон: {self.weapon[self.weapon1]["damage"]}')
                self.damage_right.config(text=f'Урон: {self.weapon[self.weapon2]["damage"]}')
                self.int_left.config(text=f'Очки интеллекта: {self.weapon[self.weapon1]["intelegent"]}')
                self.int_right.config(text=f'Очки интеллекта: {self.weapon[self.weapon1]["intelegent"]}')

    # window of eat corpse
    def eat_corpse(self):
        self.eat = Toplevel(bg='pink', bd=2)
        eat_frame = Frame(self.eat, bg='pink')
        eat_frame.pack(padx=25, pady=25)

        Label(eat_frame,
              text='Введите количество:',
              bg='pink', font=("Helvetica", "12")
              ).grid(row=0, column=1)

        self.eat_number_ent = Entry(eat_frame, bg='pink')
        self.eat_number_ent.grid(row=1, column=1, pady=10)
        eat_heart_btn = Button(eat_frame,
                               text='Съесть сердце',
                               command=self.eat_heart,
                               bg='pink', font=("Helvetica", "12"), width=20
                               )
        eat_heart_btn.grid(row=2, columnspan=3)

        eat_brain_btn = Button(eat_frame,
                               text='Съесть мозги',
                               command=self.eat_brain,
                               bg='pink', font=("Helvetica", "12"), width=20
                               )
        eat_brain_btn.grid(row=3, columnspan=3)

        eat_muscles_btn = Button(eat_frame,
                                 text='Съесть мышцы',
                                 command=self.eat_muscles,
                                 bg='pink', font=("Helvetica", "12"), width=20
                                 )
        eat_muscles_btn.grid(row=4, columnspan=3)

    # add brain
    def eat_brain(self):
        try:
            eat_number = int(self.eat_number_ent.get())
            self.eat.destroy()
            self.brain += eat_number
            self.brain_stock.config(text=f'Мозги: {self.brain}')
        except ValueError:
            self.error()

    # add heart
    def eat_heart(self):
        try:
            eat_number = int(self.eat_number_ent.get())
            self.eat.destroy()
            self.heart += eat_number
            self.heart_stock.config(text=f'Сердце: {self.heart}')
        except ValueError:
            self.error()

    # add muscle
    def eat_muscles(self):
        try:
            eat_number = int(self.eat_number_ent.get())
            self.eat.destroy()
            self.muscle += eat_number
            self.muscles_stock.config(text=f'Мышцы: {self.muscle}')
        except ValueError:
            self.error()

    # use stock window
    def use_stock(self):
        self.use = Toplevel(bg='pink', bd=2)
        use_frame = Frame(self.use, bg='pink')
        use_frame.pack(padx=25, pady=25)

        Label(use_frame,
              text='Использовать одну порцию из запаса',
              bg='pink', font=("Helvetica", "12")
              ).grid(row=0, column=1, pady=10)

        use_heart_btn = Button(use_frame,
                               text='Сердце: 100г = 1 Оз',
                               command=self.use_heart,
                               bg='pink', font=("Helvetica", "12"), width=20
                               )
        use_heart_btn.grid(row=2, columnspan=3)

        use_brain_btn = Button(use_frame,
                               text='Мозги: 200г = 1 Ои',
                               command=self.use_brain,
                               bg='pink', font=("Helvetica", "12"), width=20
                               )
        use_brain_btn.grid(row=3, columnspan=3)

        use_muscles_btn = Button(use_frame,
                                 text='Мышцы: 100г = +2 урона\n на первый выстрел/удар',
                                 command=self.use_muscles,
                                 bg='pink', font=("Helvetica", "8"), width=30
                                 )
        use_muscles_btn.grid(row=4, columnspan=3)

        exit_btn = Button(use_frame,
                          text='Выход',
                          command=self.use.destroy,
                          bg='pink', font=("Helvetica", "12"), width=20
                          )
        exit_btn.grid(row=5, columnspan=3)

    # convert heart of stock at hp
    def use_heart(self):
        if self.hp >= 70:
            messagebox.showerror('Ошибка!', 'Вы полностью здоровы. Здоровье не может быть больше 70.')
            return
        if self.heart < 100:
            messagebox.showerror('Ошибка!', 'Вы съели недостаточно сердец. Необходимо не менее 100г.')
            return
        self.heart -= 100
        self.hp += 1
        self.heart_stock.config(text=f'Сердце: {self.heart}')
        self.hit_points.config(text=f'Очки здоровья: {self.hp}')

    # convert brain at intelegence
    def use_brain(self):
        if self.brain < 200:
            messagebox.showerror('Ошибка!', 'Нужно больше мозгов. Хотя бы 200г')
            return
        self.brain -= 200
        self.ip += 1
        self.brain_stock.config(text=f'Мозги: {self.brain}')
        self.int_points.config(text=f'Очки интеллекта: {self.ip}')

    # convert muscles at bonus damage
    def use_muscles(self):
        if self.muscle < 100:
            messagebox.showerror('Ошибка!', 'Недостаточно мышц. Найдите хотя бы 100г')
            return
        self.muscle -= 200
        self.bonus_dmg += 2
        self.muscles_stock.config(text=f'Мышцы: {self.muscle}')

    # take item window, insert name of item
    def take_item_window(self):
        # check numbers of item
        if len(self.inventory.get(0, END)) == 10:
            messagebox.showerror('Ошибка!', 'У вас может быть не более 10 предметов')
            return
        self.take = Toplevel(bg='pink', bd=2)
        take_frame = Frame(self.take, bg='pink')
        take_frame.pack(padx=25, pady=25)
        Label(take_frame,
              text='Какую вещь вы хотите взять?\nПомните, у вас может быть не больше 10 вещей',
              bg='pink', font=("Helvetica", "12")
              ).grid(row=0, rowspan=2, column=0, columnspan=5)
        self.take_ent = Entry(take_frame, bg='pink', width=20)
        self.take_ent.grid(row=2, column=1, columnspan=3)
        take_btn = Button(take_frame,
                          text='Взять',
                          bg='pink', font=("Helvetica", "12"), width=20,
                          command=self.take_item
                          )
        take_btn.grid(row=3, column=1, columnspan=3)

    # add insert item at listbox
    def take_item(self):
        if not self.take_ent.get().isalnum():
            messagebox.showerror('Ошибка!', 'Введите название вещи')
        else:
            self.inventory.insert(END, self.take_ent.get())
            self.take.destroy()
            return

    # delete item at listbox
    def delete_item(self):
        select = list(self.inventory.curselection())
        select.reverse()
        for i in select:
            self.inventory.delete(i)

    # window take weapon, insert weapon name and his attribute
    def take_weapon_win(self):
        self.weapon_win = Toplevel(bg='pink', bd=2)
        weapon_frame = Frame(self.weapon_win, bg='pink')
        weapon_frame.grid(padx=25, pady=25)

        Label(weapon_frame,
              text='Название оружия',
              bg='pink', font=("Helvetica", "12")
              ).grid(row=0, column=0, columnspan=2)

        self.w_name_ent = Entry(weapon_frame, bg='pink')
        self.w_name_ent.grid(row=0, column=2, columnspan=2)

        Label(weapon_frame,
              text='Урон',
              bg='pink', font=("Helvetica", "12")
              ).grid(row=1, column=0, columnspan=2)

        self.w_damage_ent = Entry(weapon_frame, bg='pink')
        self.w_damage_ent.grid(row=1, columnspan=2, column=2)

        Label(weapon_frame,
              text='Очки интеллекта',
              bg='pink', font=("Helvetica", "12")
              ).grid(row=2, column=0, columnspan=2)

        self.w_int_ent = Entry(weapon_frame, bg='pink')
        self.w_int_ent.grid(row=2, column=2, columnspan=2)

        Label(weapon_frame,
              text='Патроны',
              bg='pink', font=("Helvetica", "12")
              ).grid(row=3, column=0, columnspan=2)

        self.w_ammo_ent = Entry(weapon_frame, bg='pink')
        self.w_ammo_ent.grid(row=3, column=2, columnspan=2)

        self.rbutton(weapon_frame, 4, 0, 4,2)

        Button(weapon_frame,
               text='Взять',
               bg='pink', font=("Helvetica", "12"),
               command=self.take_weapon
               ).grid(row=5, column=1, columnspan=2)

    # take weapon on first or second slot
    def take_weapon(self):
        try:
            name = self.w_name_ent.get()
            dmg = int(self.w_damage_ent.get())
            ammo = self.w_ammo_ent.get()
            intelegent = int(self.w_int_ent.get())
        except ValueError:
            self.error()
            return
        if not name.isalnum():
            self.error()
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

    # delete weapon from first or second slot window
    def throw_away_win(self):
        self.discard = Toplevel(bg='pink', bd=2)
        discard_frame = Frame(self.discard, bg='pink', padx=25, pady=25)
        discard_frame.pack()

        Label(discard_frame,
              text='Какое оружие вы хотите выбросить?',
              bg='pink', font=("Helvetica", "12")
              ).grid(row=0, column=1, columnspan=2)

        self.rbutton(discard_frame, 2, 0, 2, 2)

        Button(discard_frame,
               text='Выбросить',
               bg='pink', font=("Helvetica", "12"),
               command=self.discard_weapon
               ).grid(row=3, column=1, columnspan=2)

    # delete weapon from first or second slot
    def rbutton(self, frame, row1, column1, row2, column2):
        self.weapon_var.set(False)
        r1 = Radiobutton(frame,
                         text='Оружие 1',
                         variable=self.weapon_var, value=False,
                         bg='pink', font=("Helvetica", "12")
                         )
        r2 = Radiobutton(frame,
                         text='Оружие 2',
                         variable=self.weapon_var, value=True,
                         bg='pink', font=("Helvetica", "12")
                         )
        r1.grid(row=row1, column=column1, columnspan=2)
        r2.grid(row=row2, column=column2, columnspan=2)

    # check slot to delete weapon
    def discard_weapon(self):
        if not self.weapon_var.get():
            self.weapon1 = 'Руки'
            self.rewrite()
        else:
            self.weapon2 = 'Руки'
            self.rewrite()
        self.discard.destroy()

    # swap weapon slot
    def change_weapon(self):
        self.weapon1, self.weapon2 = self.weapon2, self.weapon1
        self.rewrite('w')

    # rewrite label at main page. 'a' = all, 'w' = weapon only, 'p' = parameters only
    def rewrite(self, arg="a"):
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
        if arg == 'a':
            self.rewrite('p')
            self.rewrite('w')

    # save variables at file
    def save(self):
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
        with open('save game.json', 'w') as save_file:
            json.dump(data, save_file)

    # load variables from file
    def load(self):
        with open('save game.json') as load_file:
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
            for i in self.inventory.get(0, END):
                self.inventory.delete(i)
            for i in data['inventory']:
                self.inventory.insert(END, i)

            self.notes.insert(1.0, data['notes'])
            self.rewrite()

    # change variables at start parameters
    def new_game(self):
        for i in self.inventory.get(0, END):
            self.inventory.delete(i)
        self.notes.delete(1.0, END)
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

# class Judi:
#     def __init__(self, win):
#         self.win = win
#         self.win.title('Judi')
#         self.win.geometry('200x200')


window = Tk()
Ben(window).char_config()
# Judi(window)
window.mainloop()
