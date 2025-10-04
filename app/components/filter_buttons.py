import reflex as rx
from app.states.todo_state import TodoState, FilterType


def filter_button(text: str, filter_type: FilterType) -> rx.Component:
    return rx.el.button(
        text,
        on_click=lambda: TodoState.set_filter(filter_type),
        class_name=rx.cond(
            TodoState.current_filter == filter_type,
            "h-[44px] px-4 bg-orange-500 text-white font-medium",
            "h-[44px] px-4 bg-gray-200 text-gray-800 font-medium hover:bg-gray-300 dark:bg-gray-700 dark:text-gray-200 dark:hover:bg-gray-600",
        ),
    )


def filter_buttons() -> rx.Component:
    return rx.el.div(
        filter_button("All", "all"),
        filter_button("Active", "active"),
        filter_button("Completed", "completed"),
        class_name="flex space-x-2 mb-6",
    )