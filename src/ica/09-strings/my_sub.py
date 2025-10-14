def name_subst (name, text):
    if "ZZZ" in text:
        new_text = text.replace("ZZZ", name)
        return new_text

sallie = name_subst("Sallie", "Her name is ZZZ")
print(sallie)

