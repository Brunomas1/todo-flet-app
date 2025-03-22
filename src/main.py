import flet as ft


def main(page: ft.Page):
    page.title = "Todo List App"
    page.padding = 16
    page.window_width = 400
    page.window_height = 800
    page.theme_mode = ft.ThemeMode.DARK

    def get_colors():
        return {
            ft.ThemeMode.DARK: {
                "background": "#121212",
                "card_bg": "#1e1e1e",
                "text": "#ffffff",
                "input_fill": "#333333",
                "input_border": "#555555",
                "hint": "#cccccc",
                "button_bg": "#333333",
                "button_text": "#ffffff",
            },
            ft.ThemeMode.LIGHT: {
                "background": "#f8f8f8",
                "card_bg": "#ffffff",
                "text": "#222222",
                "input_fill": "#ffffff",
                "input_border": "#e0e0e0",
                "hint": "#888888",
                "button_bg": "#ffffff",
                "button_text": "#222222",
            },
        }[page.theme_mode]

    colors = get_colors()

    # Lista para rastrear cards criados e atualizá-los no update_theme_colors
    todo_cards = []

    def update_theme_colors():
        nonlocal colors
        colors = get_colors()
        new_todo_field.fill_color = colors["input_fill"]
        new_todo_field.border_color = colors["input_border"]
        new_todo_field.hint_style = ft.TextStyle(color=colors["hint"])
        header_text.color = colors["text"]
        content_container.bgcolor = colors["background"]
        add_button.style = ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
            bgcolor=colors["button_bg"],
            color=colors["button_text"],
        )

        for card_data in todo_cards:
            is_checked = card_data["checkbox"].value
            card_data["edit_button"].icon_color = colors["text"]
            card_data["card"].bgcolor = colors["card_bg"]
            card_data["task_text_display"].content = card_data["build_task_text"](is_checked)

        page.update()

    def toggle_theme(e):
        page.theme_mode = ft.ThemeMode.LIGHT if page.theme_mode == ft.ThemeMode.DARK else ft.ThemeMode.DARK
        theme_toggle.icon = ft.Icons.LIGHTBULB if page.theme_mode == ft.ThemeMode.LIGHT else ft.Icons.LIGHTBULB_OUTLINE
        update_theme_colors()

    theme_toggle = ft.IconButton(icon=ft.Icons.LIGHTBULB_OUTLINE, tooltip="Alternar tema", on_click=toggle_theme)

    header_text = ft.Text("Minhas Tarefas", size=28, weight="bold", color=colors["text"])
    header = ft.Row(controls=[header_text, theme_toggle], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)

    todos_container = ft.ListView(expand=True, spacing=8, padding=8, auto_scroll=True)

    new_todo_field = ft.TextField(
        hint_text="Nova tarefa", border_radius=10, filled=True, fill_color=colors["input_fill"],
        content_padding=10, border_color=colors["input_border"], hint_style=ft.TextStyle(color=colors["hint"]), expand=True
    )

    add_button = ft.ElevatedButton(
        text="Adicionar", icon=ft.Icons.ADD, style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10))
    )

    def add_todo(e):
        texto = new_todo_field.value.strip()
        if texto:
            new_todo_field.value = ""

            def build_task_text(is_checked):
                return ft.Text(
                    texto,
                    size=16,
                    color=ft.Colors.RED if is_checked else colors["text"],
                    style=ft.TextStyle(decoration=ft.TextDecoration.LINE_THROUGH if is_checked else None)
                )

            task_text_display = ft.AnimatedSwitcher(
                build_task_text(False),
                transition=ft.AnimatedSwitcherTransition.FADE,
                duration=300
            )

            todo_checkbox = ft.Checkbox(value=False)

            edit_button = ft.IconButton(icon=ft.Icons.EDIT, icon_color=colors["text"])
            delete_button = ft.IconButton(icon=ft.Icons.DELETE, icon_color="#FF3B30")

            def on_checkbox_change(e):
                task_text_display.content = build_task_text(todo_checkbox.value)
                page.update()

            todo_checkbox.on_change = on_checkbox_change

            def edit_todo(e):
                edit_field = ft.TextField(value=texto, expand=True, fill_color=colors["input_fill"], border_color=colors["input_border"])
                save_button = ft.IconButton(icon=ft.Icons.CHECK, icon_color="#34C759")
                cancel_button = ft.IconButton(icon=ft.Icons.CLOSE, icon_color="#FF9500")

                def save_edit(ev):
                    nonlocal texto
                    texto = edit_field.value
                    task_text_display.content = build_task_text(todo_checkbox.value)
                    task_row.controls[1] = ft.Container(expand=True, content=task_text_display, padding=8)
                    task_row.controls[2] = edit_button
                    task_row.controls[3] = delete_button
                    page.update()

                def cancel_edit(ev):
                    task_row.controls[1] = ft.Container(expand=True, content=task_text_display, padding=8)
                    task_row.controls[2] = edit_button
                    task_row.controls[3] = delete_button
                    page.update()

                save_button.on_click = save_edit
                cancel_button.on_click = cancel_edit

                task_row.controls[1] = ft.Container(expand=True, content=edit_field, padding=8)
                task_row.controls[2] = save_button
                task_row.controls[3] = cancel_button
                page.update()

            edit_button.on_click = edit_todo

            task_row = ft.Row(
                controls=[todo_checkbox, ft.Container(expand=True, content=task_text_display, padding=8), edit_button, delete_button],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                spacing=8,
            )

            card = ft.Container(content=task_row, bgcolor=colors["card_bg"], border_radius=8, padding=4)

            delete_button.on_click = lambda e: todos_container.controls.remove(card) or page.update()

            todos_container.controls.append(card)
            page.update()

            todo_cards.append({
                "checkbox": todo_checkbox,
                "edit_button": edit_button,
                "card": card,
                "task_text_display": task_text_display,
                "build_task_text": build_task_text,
            })

    add_button.on_click = add_todo

    def clear_completed(e):
        to_remove = []
        for item in todos_container.controls:
            if isinstance(item.content.controls[0], ft.Checkbox) and item.content.controls[0].value:
                to_remove.append(item)
        for item in to_remove:
            todos_container.controls.remove(item)
        page.update()

    clear_completed_button = ft.ElevatedButton(
        text="Limpar Concluídas", icon=ft.Icons.CLEAR_ALL,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)),
        on_click=clear_completed
    )

    content_container = ft.Container(
        content=ft.Column(
            controls=[header, ft.Row(controls=[new_todo_field, add_button]), ft.Divider(), todos_container, ft.Divider(), clear_completed_button],
            spacing=16,
        ),
        margin=16, padding=16, bgcolor=colors["background"], border_radius=10
    )

    page.add(content_container)
    page.update()


ft.app(target=main)