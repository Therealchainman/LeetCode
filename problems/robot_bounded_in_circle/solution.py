class Solution:
    def isRobotBounded(self, A):
        location=[0,0]
        direction_index=0
        # The directions are North, West, South, and East.
        directions=[(1,0),(0,-1),(-1,0),(0,1)]
        # These are the instructions so we move through list in forward direction mod 4 if we turn left
        # and we move through in reverse direction mod 4 if we turn right.  Note the fact that -1%4 =3 makes 
        # this work in python so the negative values will basically start it at the end of the direction list
        # and it will wrap around properly. 
        for instruction in A:
            if instruction=="L":
                direction_index=(direction_index+1)%4
            elif instruction=="R":
                direction_index=(direction_index-1)%4
            else:
                dx,dy=directions[direction_index]
                location[0]+=dx
                location[1]+=dy
        # The robot is bounded by a circle if the direction vector changes or location doesn't change.  
        return location==[0,0] or directions[direction_index]!=(1,0)
        