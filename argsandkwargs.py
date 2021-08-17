def magic(*args,**kwargs):
    print("Unamed args ", args)
    print("Keyword args ", kwargs)

magic(1,2, key="word", key2="word2")

def other_way_magic(x,y,z):
    return x + y +z

x_ylist = [1,2]
z_dict = {"z":3}

assert other_way_magic(*x_ylist,**z_dict) == 6, "1 + 2 + 3 deve ser igual a 6"