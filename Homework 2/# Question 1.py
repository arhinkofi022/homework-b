def compareStrings(garland, flower):
   
    garlands = set(garland)
    flowers = set(flower)

   
    common_flowers = garlands.intersection(flowers)

   
    common = len(common_flowers)

    return common