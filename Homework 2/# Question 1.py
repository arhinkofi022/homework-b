# Question 1

def compareStrings(garland, flower):
    common_count = 0

   
    garland = garland.lower()
    flower = flower.lower()

    garland_chars = set(garland)

   
    for char in flower:
        if char in garland_chars:
            common_count += 1

    return common_count


garland_str = "garl"
flower_str = "flower"
result = compareStrings(garland_str, flower_str)
print("Number of flowers that are garlands:", result)
