import random
# This is the dictionary that we save values of cells.
cell_values={}
# Using x and y for save location of robot.
x=0
y=0
# The list that shows values we get from sensors.If road is open, sensors return 0.
# Else sensors return 1. This values is only for show we took this values from sensors.
# Right-Forward-Left. This is the order that I use from index 0 to 2. 
sensors=[0,0,0] 
# This is the first direction of robot. I named directions as north,south,east, and west.
# But they are doesn't have to equal to real life.
dir="North"
# This dictionary will help us at checking what is the location if robot turns right,left or move forward.
# Also will help us at updating coordinates. 
next_loc_count={
    "North":{"Left":[-1,0],"Right":[1,0],"Forward":[0,1]},
    "South":{"Left":[1,0],"Right":[-1,0],"Forward":[0,-1]},
    "West":{"Left":[0,-1],"Right":[0,1],"Forward":[-1,0]},
    "East":{"Left":[0,1],"Right":[0,-1],"Forward":[1,0]}
}
# This dictionary will help us at updating robot's direction depending on robot's move, and former direction.
dir_update={
    "North":{"Back":"South","Right":"East","Left":"West","Forward":"North"},
    "South":{"Back":"North","Right":"West","Left":"East","Forward":"South"},
    "West":{"Back":"East","Right":"North","Left":"South","Forward":"West"},
    "East":{"Back":"West","Right":"South","Left":"North","Forward":"East"}
}
# This function will help us at finding open roads depending on datas that come from sensors.
def open_roads():
    _open_roads=[]
    if sensors[0]==0:
        _open_roads.append("Right")
    if sensors[1]==0:
        _open_roads.append("Forward")
    if sensors[2]==0:
        _open_roads.append("Left")
    return _open_roads
# This function will help us at checking values of open roads, 
# and if this location's value equal the value that we are looking for adds the way to a list.
def value_checker(value):
    ways=[]
    for road in list(open_roads()):
        next_loc=(x+next_loc_count[dir][road][0],y+next_loc_count[dir][road][1])
        try:
           if cell_values[next_loc]==value:
               ways.append(road)
        except:
            if value==0:
                ways.append(road)
            else:
                pass
    return ways
# This is the function that commands robot to move right,left, or forward.
# Print parts are only for show.
def move(road):
    if road=="Forward":
        # move one step
        print("Moving")
    elif road=="Right":
            # rotate -90 degree
            # move one step
        print("Right")
    elif road=="Left":
        # rotate 90 degree
        # move one step
        print("Left")

# This is the function that commands robot to turn back.
# We will call it when we are in a dead end.
def turn_back():
    # rotate 180 degree
    dir=dir_update[dir["Back"]]


while True:
    # If we don't have any open roads,which means we are in a dead-end, we are turning back.
    if len(open_roads())==0:
        turn_back()
        dir=dir_update[dir]["Back"]
    # If we have only one open road, we are following it without checking it's value.
    # After this step we are updating our location(x,y), direction, and dictionary that keeping values of cells  .
    # First we're trying to increase value of the cell by 1.
    # If we get an error, that means that we never visited that cell.
    # So we need to add this cell to the dictionary not update it. 
    elif len(open_roads())==1:
        move(open_roads()[0])
        x=x+next_loc_count[dir][open_roads()[0]][0]
        y=y+next_loc_count[dir][open_roads()[0]][1]
        dir=dir_update[dir][open_roads()[0]]
        try:
            cell_values.update({(x,y):cell_values[(x,y)]+1})
        except:
            cell_values.update({(x,y):1})
    # If we have more than 1 open roads, we are checking the values of the cells on those roads.
    elif len(open_roads())>1:
        # First we are checking is there any cell with value 0.
        # If there is cell or cells with value 0 we're randomly choosing one of this roads and follow it.
        # After that, we are updating our location(x,y), direction, and dictionary that keeping values of cells. 
        if len(value_checker(0))>0:
            road_to_go=random.choice(value_checker(0))
            move(road_to_go)
            x=x+next_loc_count[dir][road_to_go][0]
            y=y+next_loc_count[dir][road_to_go][1]
            dir=dir_update[dir][road_to_go]
            try:
                cell_values.update({(x,y):cell_values[(x,y)]+1})
            except:
                cell_values.update({(x,y):1})                     
        # If there is not, we're looking a cell with value 1.
        # If there is cell or cells with value 1 we're randomly choosing one of this roads and follow it.
        # After that, we are updating our location(x,y), direction, and dictionary that keeping values of cells. 
        elif len(value_checker(1))>0:
            road_to_go=random.choice(value_checker(1))
            move(road_to_go)
            x=x+next_loc_count[dir][road_to_go][0]
            y=y+next_loc_count[dir][road_to_go][1]
            dir=dir_update[dir][road_to_go]
            try:
                cell_values.update({(x,y):cell_values[(x,y)]+1})
            except:
                cell_values.update({(x,y):1})                 
        # If there is no cells with value 0 or 1 we're looking a cell with value 2.
        # If there is cell or cells with value 2 we're randomly choosing one of this roads and follow it.
        # After that, we are updating our location(x,y), direction, and dictionary that keeping values of cells. 
        elif len(value_checker(2))>0:
            road_to_go=random.choice(value_checker(2))
            move(road_to_go)
            x=x+next_loc_count[dir][road_to_go][0]
            y=y+next_loc_count[dir][road_to_go][1]
            dir=dir_update[dir][road_to_go]
            try:
                cell_values.update({(x,y):cell_values[(x,y)]+1})
            except:
                cell_values.update({(x,y):1})
 























