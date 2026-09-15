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
class Order:
    def add_item(self,name,price):
        self.item.append((name,price))
    def total_price(self):
        raw_total=0
        for item in self.items:
            raw_total+=item[1]
        discount_rate=self.customer.get_discount_rate()
        final_price=int(raw_total*(1-discount_rate))
        return final_price
    def pay(self):
        final_price=self.total_price()
        self.customer.add_points(final_price)
        return final_price
