def rgb2hex(col):
    return '#{:02x}{:02x}{:02x}'.format(col[0],col[1],col[2])

def invert_color(hex,bw):
    if hex[0]=="#":
        hex=hex[1:]
    if len(hex)==3:
        hex= hex[0] + hex[0] + hex[1] + hex[1] + hex[2] + hex[2]
    if len(hex)!=6:
        print("INVALID color")
    r=255-int(hex[0:2],16)
    g=255-int(hex[2:4],16)
    b=255-int(hex[4:6],16)
    
    if bw:
        if (r * 0.299 + g * 0.587 + b * 0.114) > 186:
            return '#000000'
        else:
            return '#FFFFFF'
    
    return rgb2hex((r,g,b))




invert_color("#4c43b1", 0)


# xe=["#DFFF00","#FFBF00","#FF7F50","#DE3163","#9FE2BF","#40E0D0","#6495ED","#CCCCFF"]

# fi=open("test","w")


# for color in xe:
#     print(color,rgb2hex(invert_color(color,0)))
#     fi.write(color+" "+str(rgb2hex(invert_color(color,0)))+"\n")



    