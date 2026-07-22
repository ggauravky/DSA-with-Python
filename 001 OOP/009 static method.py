class chaiutils:
    @staticmethod
    def clean_ingredients(text):
        return [items.strip() for items in text.split(",")]

raw="milk, sugar, tea leaves, cardamom, ginger"

obj=chaiutils()
# print(obj.clean_ingredients(raw))

cleaned=chaiutils.clean_ingredients(raw)
print(cleaned)