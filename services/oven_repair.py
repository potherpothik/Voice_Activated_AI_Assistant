class OvenRepairService:
    def __init__(self):
        self.name = "Oven Repair"
        self.description = "Repair services for electric and gas ovens including heating problems, temperature inconsistency, and control panel issues."
        self.common_issues = ["not heating", "uneven cooking", "temperature issues", "control panel failures", "strange odors"]
        self.price_range = "$90-$320"

    def get_info(self):
        return {
            "name": self.name,
            "description": self.description,
            "common_issues": self.common_issues,
            "price_range": self.price_range
        } 