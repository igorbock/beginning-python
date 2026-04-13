class DiscountMixin:
    def apply_discount(self, percent):
        # TODO: Implement the apply_discount method that calculates a discounted price
        # TODO: Calculate the discounted price using the formula: price - (price * percent / 100)
        # TODO: This method should access self.price attribute from the class that uses this mixin
        # TODO: Return the calculated discounted price
        discounted_price = self.price - (self.price * percent / 100)
        return discounted_price