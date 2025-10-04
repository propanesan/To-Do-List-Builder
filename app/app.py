import reflex as rx
from app.states.todo_state import TodoState
from app.components.task_input import task_input
from app.components.filter_buttons import filter_buttons
from app.components.task_item import task_item


def index() -> rx.Component:
    return rx.el.main(
        rx.el.div(
            rx.el.div(
                rx.el.h1(
                    "todos", class_name="text-8xl font-thin text-orange-500/80 mb-8"
                ),
                rx.el.div(
                    task_input(),
                    filter_buttons(),
                    rx.el.div(
                        rx.foreach(TodoState.filtered_tasks, task_item),
                        class_name="w-full border border-[#E0E0E0]",
                    ),
                    rx.cond(
                        TodoState.tasks.length() > 0,
                        rx.el.p(
                            f"{TodoState.filtered_tasks.length()} items",
                            class_name="mt-4 text-sm text-gray-500",
                        ),
                    ),
                    class_name="w-full bg-[#FAFAFA] p-6 border border-[#E0E0E0]",
                ),
                class_name="flex flex-col items-center w-full max-w-2xl",
            ),
            class_name="min-h-screen flex items-start justify-center pt-16 bg-[#FAFAFA]",
        ),
        class_name="font-['Lora'] bg-[#FAFAFA]",
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