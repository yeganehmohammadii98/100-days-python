class Drug:
    def __init__(self, name: str, amount: int, price: int):
        self.name = name
        self.amount = amount
        self.price = price


class Pharmacy:
    def __init__(self, name: str):
        self.name = name
        self.drugs = []
        self.employees = []

    def add_drug(self, drug: Drug):
        if isinstance(drug, Drug):
            self.drugs.append(drug)
        else:
            raise ValueError("Invalid drug object")

    def add_employee(self, first_name: str, last_name: str, age: int):
        if isinstance(first_name, str) and isinstance(last_name, str) and isinstance(age, int):
            self.employees.append({
                "first_name": first_name,
                "last_name": last_name,
                "age": age
            })
        else:
            raise ValueError("Invalid employee data")

    def total_value(self) -> int:
        total = 0
        for drug in self.drugs:
            total += drug.amount * drug.price
        return total

    def employees_summary(self) -> str:
        summary = []
        for employee in self.employees:
            summary.append(f"{employee['first_name']} {employee['last_name']} ({employee['age']})")
        return ", ".join(summary)
