import reflex as rx
from app.states.todo_state import TodoState
from app.states.theme_state import ThemeState
from app.components.task_input import task_input
from app.components.filter_buttons import filter_buttons
from app.components.task_item import task_item


def index() -> rx.Component:
    return rx.el.main(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.h1(
                        "todos",
                        class_name="text-8xl font-thin text-orange-500/80 dark:text-orange-400/80",
                    ),
                    rx.el.button(
                        rx.icon(
                            tag=rx.cond(ThemeState.theme == "light", "moon", "sun"),
                            class_name="h-6 w-6",
                        ),
                        on_click=ThemeState.toggle_theme,
                        class_name="p-2 rounded-full text-gray-500 hover:bg-gray-200 dark:text-gray-400 dark:hover:bg-gray-700",
                    ),
                    class_name="flex items-center justify-between w-full mb-8",
                ),
                rx.el.div(
                    task_input(),
                    filter_buttons(),
                    rx.el.div(
                        rx.foreach(TodoState.filtered_tasks, task_item),
                        class_name="w-full border border-[#E0E0E0] dark:border-gray-700",
                    ),
                    rx.cond(
                        TodoState.tasks.length() > 0,
                        rx.el.p(
                            f"{TodoState.filtered_tasks.length()} items",
                            class_name="mt-4 text-sm text-gray-500 dark:text-gray-400",
                        ),
                    ),
                    class_name="w-full bg-[#FAFAFA] dark:bg-gray-800 p-6 border border-[#E0E0E0] dark:border-gray-700",
                ),
                class_name="flex flex-col items-center w-full max-w-2xl",
            ),
            class_name="min-h-screen flex items-start justify-center pt-16 bg-[#FAFAFA] dark:bg-gray-900",
        ),
        class_name="font-['Lora'] bg-[#FAFAFA] dark:bg-gray-900",
    )


app = rx.App(
    theme=rx.theme(appearance="light"),
    head_components=[
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(rel="preconnect", href="https://fonts.gstatic.com", cross_origin=""),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Lora:wght@400;500;700&display=swap",
            rel="stylesheet",
        ),
    ],
)
app.add_page(index)