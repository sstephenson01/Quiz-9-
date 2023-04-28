# Sarah Stephenson
# Problem 3

import dbm
dbm1 = dbm.open("houses", "c")
dbm1["house1.png"] = "A 2 bed, 3 bath house in South Bend"
dbm1["house2.png"] = "A 1 bed, 2 bath house in South Bend"
dbm1["house3.png"] = "A 3 bed, 3 bath house in South Bend"
dbm1["house4.png"] = "A 2 bed 1 bath blue house in Plymouth"
dbm1["house5.png"] = "A 4 bed, 4 bath house in Knox"
dbm1["house6.png"] = "A 3 bed, 2 bath house in Notre Dame"

#h = dbm1["house1.png"]
#print(h)
# Problem 4
dbm1["house1.png"] = "A pink 2 bed, 3 bath house in South Bend"
dbm1["house2.png"] = "A purple 1 bed, 2 bath house in South Bend"
for item in dbm1:
    print(item, dbm1[item])
