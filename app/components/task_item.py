import reflex as rx
from app.states.todo_state import TodoState, Task


def task_item(task: Task) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.input(
                    type="checkbox",
                    checked=task["completed"],
                    on_change=lambda: TodoState.toggle_completed(task["id"]),
                    class_name="h-6 w-6 accent-orange-500 cursor-pointer",
                ),
                rx.el.p(
                    task["text"],
                    class_name=rx.cond(
                        task["completed"],
                        "ml-4 text-lg text-gray-500 line-through",
                        "ml-4 text-lg text-gray-800",
                    ),
                ),
                class_name="flex items-center",
            ),
            rx.el.button(
                rx.icon(tag="trash-2", class_name="h-5 w-5"),
                on_click=lambda: TodoState.delete_task(task["id"]),
                class_name="p-2 text-gray-400 hover:text-red-500",
            ),
            class_name="flex items-center justify-between w-full",
        ),
        class_name="flex items-center w-full p-4 h-[60px] bg-white border-b border-[#E0E0E0]",
        key=task["id"],
    )