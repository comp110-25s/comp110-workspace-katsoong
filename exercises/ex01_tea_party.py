"""Items and costs for planning a tea party"""

__author__: str = "730591959"


def main_planner(guests: int) -> None:
    """Planning a tea party."""
    print(f"A Cozy Tea Party for {guests} People")
    print(f"Tea Bags: {tea_bags(guests)}")
    print(f"Treats: {treats(guests)}")
    print(f"Total Cost: ${cost(tea_bags(guests), treats(guests))}")
    return None


def tea_bags(people: int) -> int:
    """Calculate total number of tea bags."""
    return 2 * people


def treats(people: int) -> int:
    """Calculate total number of treats based on number of tea bags."""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Calculate the total cost."""
    return tea_count * 0.5 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests?")))
