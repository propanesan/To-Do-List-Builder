import reflex as rx
from typing import TypedDict, Literal

FilterType = Literal["all", "active", "completed"]


class Task(TypedDict):
    id: int
    text: str
    completed: bool


class TodoState(rx.State):
    tasks: list[Task] = []
    _next_id: int = 1
    current_filter: FilterType = "all"

    @rx.var
    def filtered_tasks(self) -> list[Task]:
        if self.current_filter == "active":
            return [task for task in self.tasks if not task["completed"]]
        if self.current_filter == "completed":
            return [task for task in self.tasks if task["completed"]]
        return self.tasks

    @rx.event
    def add_task(self, form_data: dict):
        new_task_text = form_data.get("new_task", "").strip()
        if new_task_text:
            self.tasks.append(
                {"id": self._next_id, "text": new_task_text, "completed": False}
            )
            self._next_id += 1

    @rx.event
    def toggle_completed(self, task_id: int):
        for i, task in enumerate(self.tasks):
            if task["id"] == task_id:
                self.tasks[i]["completed"] = not self.tasks[i]["completed"]
                break

    @rx.event
    def delete_task(self, task_id: int):
        self.tasks = [task for task in self.tasks if task["id"] != task_id]

    @rx.event
    def set_filter(self, new_filter: FilterType):
        self.current_filter = new_filter