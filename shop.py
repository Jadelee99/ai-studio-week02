class Customer:
    def add_points(self, amount):
        self.points += int(amount*0.05)
    def get_discount_rate(self):
        if self.grade=="vip":
            return 0.10
        else :
            return 0.03
    def summary(self):
        return f"[{self.grade}]{self.name}(포인트: {self.points:,})"
c1=Customer()
c1.name="김서강"
c1.grade="vip"
c1.points=0
c1.add_points(10000)
print(c1.summary())