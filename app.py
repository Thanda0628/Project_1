import flet as ft

def main(page: ft.Page):
    page.title = "Counter"
    page.verticle_alignment = ft.MainAxisAlignment.CENTER

    page.window_width = 200
    page.window_height = 100

    txt_number = ft.TextField(value = 0, text_align = ft.TextAlign.CENTER, width = 50)

    def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.Icons.REMOVE, on_click=minus_click),
                txt_number,
                ft.IconButton(ft.Icons.ADD, on_click=plus_click),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

ft.app(main)
    