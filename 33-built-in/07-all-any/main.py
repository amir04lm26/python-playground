is_connected: bool = True
has_electricity: bool = False
has_paid: bool = True

requirements: list[bool] = [is_connected, has_electricity, has_paid]

has_internet: bool = all(requirements)
print("Internet:", has_internet)

has_any_condition: bool = any(requirements)
print("Has any requirements:", has_any_condition)
