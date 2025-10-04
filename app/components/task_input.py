import reflex as rx
from app.states.todo_state import TodoState


def task_input() -> rx.Component:
    return rx.el.form(
        rx.el.div(
            rx.el.input(
                name="new_task",
                placeholder="What needs to be done?",
                class_name="w-full h-[44px] px-4 text-lg bg-transparent focus:outline-none placeholder:text-gray-400 text-gray-800",
            ),
            rx.el.button(
                "Add",
                type="submit",
                class_name="h-[44px] px-6 bg-orange-500 text-white font-medium hover:bg-orange-600",
            ),
            class_name="flex items-center w-full border border-[#E0E0E0] bg-white",
        ),
        on_submit=TodoState.add_task,
        reset_on_submit=True,
        class_name="w-full mb-6",
    )