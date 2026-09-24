from dataclasses import dataclass

@dataclass
class Plan:
    goal: str
    steps: list[str]

class Planner:
    def make_plan(self, goal: str) -> Plan:
        return Plan(goal=goal, steps=[
            "Understand the requested outcome",
            "Check required capabilities and permissions",
            "Execute safe steps",
            "Ask for approval before consequential actions",
            "Report the result and save a reusable workflow when appropriate",
        ])
