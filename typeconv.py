def typeconv(newdf):
     newdf.Research = newdf.Research.apply(Research)
     return newdf

def Research(value):
    if value == "Yes":
        return 0
    elif value == "No":
        return 1