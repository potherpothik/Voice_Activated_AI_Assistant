class FridgeRepairService:
    def __init__(self):
        self.name = "Refrigerator Repair"
        self.description = "Repair services for all types of refrigerators addressing cooling problems, water leakage, ice maker issues, and unusual noises."
        self.common_issues = ["not cooling", "water leaking", "ice maker not working", "unusual noises", "freezing food"]
        self.price_range = "$100-$350"

    def get_info(self):
        return {
            "name": self.name,
            "description": self.description,
            "common_issues": self.common_issues,
            "price_range": self.price_range
        } 