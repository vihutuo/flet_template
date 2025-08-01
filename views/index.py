import flet as ft

def IndexView(page:ft.Page, params):
    def CreateAppBar():
        app_bar = ft.AppBar(
            leading=ft.Image("images/csc_logo_100.png"),
            leading_width=40,
            title=ft.Text("Flet Template"),
            #center_title=False,
            bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,
            actions=[
                ft.IconButton(ft.Icons.RESTART_ALT, on_click=restart_clicked),
                ft.IconButton(ft.Icons.FILTER_3),

            ],
        )
        return app_bar

    def restart_clicked(e):
         dlg = ft.AlertDialog(title=ft.Text("You clicked restart"))
         page.open(dlg)
    def btn_question1_clicked(e):
        page.go("/question/1")

    def btn_question2_clicked(e):
        page.go("/question/2")

    def btn_simple_clicked(e):
        page.go("/simple_view")

    txt = ft.Text("Welcome to the Flet Template", font_family="playwrite")
    col_right = ft.Row(controls=[txt], alignment=ft.MainAxisAlignment.END)
    btn_question1 = ft.ElevatedButton("Question1", on_click=btn_question1_clicked)
    btn_question2 = ft.ElevatedButton("Question2", on_click=btn_question2_clicked)
    btn_simple = ft.ElevatedButton("Simple View", on_click=btn_simple_clicked)
    img_1 = ft.Image(src="images/m1.jpg", width=300)
    appbar = CreateAppBar()

    page.views.append(ft.View(
        "/",
        [appbar, col_right, btn_question1, btn_question2, btn_simple, img_1],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,

    )
    )
    page.update()
