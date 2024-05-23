# Assuming 'tiles' is a list of tile objects, with the top tile being the last element
tiles = []

def add_tile(tile):
    global topTile
    # Add the new tile to the stack
    tiles.append(tile)
    # Update the top tile to be the new tile
    topTile = tile

def remove_top_tile():
    global topTile
    # Remove the top tile from the stack if the stack is not empty
    if tiles:
        tiles.pop()
        # Update the top tile to be the new top of the stack, or None if the stack is empty
        topTile = tiles[-1] if tiles else None

# Example usage:
add_tile(new_tile)
remove_top_tile()
