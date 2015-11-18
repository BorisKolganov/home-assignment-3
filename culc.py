from decimal import Decimal, InvalidOperation

class Culc():
    def __init__(self):
        pass

    def sum(self, x, y):
        try:
            return float(Decimal(x) + Decimal(y))
        except InvalidOperation:
            return "No, don't use strings"

    def dif(self, x, y):
        try:
            return float(Decimal(x) - Decimal(y))
        except InvalidOperation:
            return "No, don't use strings"

    def mul(self, x, y):
        try:
            return float(Decimal(x) * Decimal(y))
        except InvalidOperation:
            return "No, don't use strings"

    def div(self, x, y):
        try:
            return float(Decimal(x) / Decimal(y))
        except InvalidOperation:
            return "No, don't use strings"
        except ZeroDivisionError:
            return "/0, really?"

    def pow(self, x, y):
        try:
            return float(Decimal(x) ** Decimal(y))
        except InvalidOperation:
            return "No, don't use strings"
