import time
import os
from cftools.tools.LIBzek import NDEC, NENC
from cftools.tools import LIBzx
import sys
try:
    import flet as ft
except:
    input('библиотека flet не установлена. нажмите enter чтобы установить.')
    os.system('pip install flet')
    input("\n \n \n \nПерезагрузите программу")

try:
    import pyperclip
except:
    input('библиотека pyperclip не установлена. нажмите enter чтобы установить.')
    os.system('pip install pyperclip')
    input("\n \n \n \nПерезагрузите программу")

from flet import TextField, Checkbox, ElevatedButton, Text, Row, Column
from flet_core.control_event import ControlEvent

os.environ["FLET_WS_MAX_MESSAGE_SIZE"] = "8000000"


def copy(nm):
    def copys(e):
        pyperclip.copy(nm)

    return ft.IconButton(icon=ft.icons.COPY_OUTLINED, on_click=copys)


def main(page: ft.Page) -> None:
    page.title = "Вход"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.DARK
    page.window_width = 400
    page.window_height = 400
    page.window_resizable = False

    text_login: TextField = TextField(label='Логин', text_align=ft.TextAlign.LEFT, width=200)
    text_pass: TextField = TextField(label='Пароль', text_align=ft.TextAlign.LEFT, width=200, password=True)
    Checkbox_login: Checkbox = Checkbox(label="Я подписан на cubefel.t.me", value=False)
    button_sub: ElevatedButton = ElevatedButton(text="Войти", width=200, disabled=True)
    regGo: ft.TextButton = ft.TextButton(text="Нет аккаунта? Зарегистроваться.")

    def vali(e: ControlEvent) -> None:

        if all([text_login.value, text_pass.value, Checkbox_login.value]):
            button_sub.disabled = False

        else:
            button_sub.disabled = True
        page.update()

    def subm(e: ControlEvent) -> None:
        call = False
        m = LIBzx.zs(path="CLients.txt", ENCODING=False)
        print(text_pass.value)
        v = m.read()
        for i in v:
            print("check", i)
            print(f"{NENC(text_login.value)}!_!{NENC(text_pass.value)}.txt")
            if NENC(text_login.value) == i:
                call = True
                print("succes")
                page.clean()
                z = LIBzx.zs(ENCODING=True, path=f"{NENC(text_login.value)}!_!{NENC(text_pass.value)}.txt")

                def find(e):
                    cu = 0
                    ind = -1

                    li = z.read()
                    text = e.control.value.lower()
                    # print(text + " sd")
                    r.controls.clear()
                    page.update()
                    found = False
                    if text != "":
                        for tab in li:
                            ind = ind + 1
                            cu = cu + 1
                            # print(tab, "TAB", str(cu),str(ind))
                            if cu == 3 and text in tab.lower():
                                create(li[ind - 2], li[ind - 1], li[ind])
                                cu = 0

                            elif cu == 3:
                                cu = 0

                        if not found:
                            r.controls.append(
                                ft.Text("Результатов нету. Попробуйте что нибудь другое", color=ft.colors.CYAN,
                                        width=150)
                            )
                    else:
                        upd()
                def logout(e):
                    text_login.value = ""
                    text_pass.value = ""
                    page.clean()
                    page.add(
                        Row(
                            controls=[
                                Column(
                                    [
                                        text_login,
                                        text_pass,
                                        Checkbox_login,
                                        button_sub,
                                        regGo]
                                )
                            ], alignment=ft.MainAxisAlignment.CENTER
                        )
                    )
                    page.window_resizable = False

                finda = ft.TextField(width=1100, hint_text="Поиск по приложениям / сайтам", on_change=find)

                page.add(ft.Row(controls=[finda]))
                page.window_width = 1335
                spc = 0
                r = ft.Row(wrap=True, scroll="always", expand=True)
                page.window_height = 800
                page.window_resizable = True
                field_1 = ft.TextField(label="Логин", value="")
                field_2 = ft.TextField(label="Пароль", value="")
                field_3 = ft.TextField(label="Приложение или сайт", value="")
                page.title = "CFpass"

                page.add(r)

                def create(id2, id1, id):
                    r.controls.append(
                        ft.Container(

                            content=(Row(
                                controls=[
                                    Text("Логин:\n\nПароль:\n\nПриложение:", size=20),
                                    Column(
                                        controls=[
                                            TextField(value=id2, width=220, height=50, text_align=ft.TextAlign.CENTER,
                                                      label="Логин", text_size=20),
                                            TextField(value=id1, width=220, height=50, text_align=ft.TextAlign.CENTER,
                                                      label="Пароль", text_size=20),
                                            TextField(value=id, width=220, height=50, text_align=ft.TextAlign.CENTER,
                                                      label="Приложение", text_size=20),

                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER
                                    ),
                                    Column(
                                        controls=[
                                            copy(id2),
                                            copy(id1),
                                            copy(id)
                                        ],
                                        alignment=ft.MainAxisAlignment.SPACE_EVENLY
                                    )
                                ],
                                alignment=ft.MainAxisAlignment.SPACE_EVENLY
                            )
                            ),

                            width=400,
                            height=200,
                            alignment=ft.alignment.center,
                            bgcolor=ft.colors.BLUE_500,
                            border=ft.border.all(5, ft.colors.CYAN),
                            border_radius=ft.border_radius.only(top_left=25, bottom_left=25, bottom_right=25)

                        )
                    )
                    page.update()

                def upd():
                    spc = 0
                    s = z.read()

                    for i in range(len(s)):
                        spc = spc + 1
                        if spc == 3:
                            spc = 0
                            create(s[i - 2], s[i - 1], s[i])

                    page.update()

                def on_clk(e):
                    z.write(field_1.value, field_2.value, field_3.value)
                    create(field_1.value, field_2.value, field_3.value)

                upd()

                send = ft.ElevatedButton(text="Добавить", on_click=on_clk, height=50, width=150, bgcolor=ft.colors.BLUE)
                but = ft.ElevatedButton(text='Выйти', on_click=logout, height=50, width=150, bgcolor=ft.colors.BLUE)

                page.add(ft.Row(controls=[field_1, field_2, field_3, send, but]))
                page.update()
        else:
            if call != True:
                FLU = Text("Такого аккаунта нету или неправильный пароль, логин.", color="red200",
                         text_align=ft.TextAlign.CENTER)
                page.add(FLU)
                page.update()
                time.sleep(2)
                page.clean()
                page.add(
                    Row(
                        controls=[
                            Column(
                                [
                                    text_login,
                                    text_pass,
                                    Checkbox_login,
                                    button_sub]
                            )
                        ], alignment=ft.MainAxisAlignment.CENTER
                    )
                )
                page.update()

    Checkbox_login.on_change = vali

    text_pass.on_change = vali
    button_sub.on_click = subm
    text_login.on_change = vali

    def regProc(e):
        login: TextField = TextField(label='Логин', text_align=ft.TextAlign.LEFT, width=200)
        passw: TextField = TextField(label='Пароль', text_align=ft.TextAlign.LEFT, width=200, password=True)
        passA: TextField = TextField(label='Потверди пароль', text_align=ft.TextAlign.LEFT, width=200, password=True)
        TG: Checkbox = Checkbox(label="Я подписан на cubefel.t.me", value=False)
        buttosub: ElevatedButton = ElevatedButton(text="Зарегистрироваться", width=200, disabled=True)
        def va(e: ControlEvent) -> None:
            if all([login.value,TG.value]) and passw.value == passA.value:
                buttosub.disabled = False

            else:
                buttosub.disabled = True
            page.update()

        def sm(e: ControlEvent) -> None:
            with open("CLients.txt","a") as lo:
                lo.write(f"{NENC(login.value)}\n")
                lo.close()
            try:
                file = open(f"{NENC(login.value)}!_!{NENC(passw.value)}.txt","r+")
                file.close()
            except IOError:
                file = open(f"{NENC(login.value)}!_!{NENC(passw.value)}.txt", "w+")
                file.close()
                page.clean()
                page.add(Row(controls=[Column(controls=[login, passw, passA, TG, Text("Перезагрузите приложение")],alignment=ft.MainAxisAlignment)],alignment=ft.MainAxisAlignment.CENTER))
        buttosub.on_click = sm
        login.on_change = va
        passA.on_change = va
        passw.on_change = va
        TG.on_change = va

        page.clean()
        page.title = "Зарегистриоваться"
        page.add(
            Row(
                controls=[
                    Column(
                        [
                            login,
                            passw,
                            passA,
                            TG,
                            buttosub]
                    )
                ], alignment=ft.MainAxisAlignment.CENTER
            )
        )
        
        
    
    regGo.on_click = regProc

    page.add(
        Row(
            controls=[
                Column(
                    [
                        text_login,
                        text_pass,
                        Checkbox_login,
                        button_sub,
                        regGo]
                )
            ], alignment=ft.MainAxisAlignment.CENTER
        )
    )


ft.app(target=main)
