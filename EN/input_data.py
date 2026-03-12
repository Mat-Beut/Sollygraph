# importing necessaries libraries
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import hachures.custom_hatches as custom_hatches


# Mathplotlib uses inches, but I want it to use cm instead
## 1 inch = 2.54 cm
inch_to_cm = 1 * 2.54

# Creates a figure and an axis with fixed dimensions in cm using unit conversion
## The fixed dimensions are there to prevent the bars from deforming when layers are added
### They are also there to keep the same proportions on export, regardless of resolution and screen's ppi
fig, ax = plt.subplots(figsize=(4 * inch_to_cm, 8 *inch_to_cm))

# Setup the variable for later use
bar = 0

# Layers' length. It's purely for aesthetic!
bar_width = 4

# For the legend
labels = []
munsells = []
horizons = []


# Function to ask the user if they want to add a hatch to their layer
def hatch() :
    # Defines global variables for later use in the main function of the script: loopy_bar()
    global motif, ask_hatch, motif_available, motif_choice, motif_for_dict, bar_dict, poly_dict, bar_wave
    
    # .strip().lower() to avoid issues with case sensitivity and accidental spaces
    ## .strip() takes care of leading/trailing spaces, and .lower() makes everything lowercase
    ### For more information about \033 etc., it is ANSI escape code, for more intels you can check this website: https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797
    ask_hatch = input("""
        Do you want to add a pattern to your layer? \033[1;34;49m(yes/no)\033[0;0m: """).strip().lower()
    
    # Simplifies user input by accepting "y" for "yes"
    if ask_hatch in ["yes", "y"] :
        ask_hatch = "yes"
    
    if ask_hatch == "oui" :
        motif_available = ("""
            \033[4mAvailable patterns:\033[0m
              \033[1;33;49m
              1. Accumulation of hydrated iron      |  2. Alterned
              3. Sandstone                          |  4. Limestone
              5. Organic slightly decomposed        |  6. Silica
              7. Localised iron precipitation       |  8. Gley
              9. Particulate horizon                |  10. Lumpy horizon
              11. Roots                             |  12. Lime carbonate
              13. Clay 2/1 (illites, vermiculites   |  14. Clay 2/1 (kaolinite)
                  montmorillonite                   |
                  with absorbed iron oxide)         |  
              15. Free alumina                      |  16. Ferromagnetic concretion
              17. Accumulation of dehydated iron    | \033[0;0m
             """) 
        # Defines a color for "|", then replaces the "|" in the "motif_available" text with the same "|" but colored
        default_color = "\033[0;1m|\033[1;33;49m"
        if '|' in motif_available :
            motif_available = motif_available.replace('|', default_color)
        print(motif_available)
        motif_choice = input("Type here the number of the pattern you want to use: ").strip()

        # Checks if entered value is 1, 2, 4, 5, 6, 8 or 10
        ## If the value is one of them, checks which one it is and assigns to "motif" the corresponding pattern
        if motif_choice in ['1', '2', '5', '6', '8', '10', '13', '14', '17'] :
            if motif_choice == '1' :
                motif = custom_hatches.vline
            if motif_choice == '2' :
                motif = custom_hatches.reversed_t
            if motif_choice == '5' :
                motif = custom_hatches.orga_peu_decomp
            if motif_choice == '6' :
                motif = custom_hatches.plus
            if motif_choice == '8' :
                motif = custom_hatches.dashed_vline
            if motif_choice == '10' :
                motif = custom_hatches.slash
            if motif_choice == '13' :
                motif = custom_hatches.hline_full
            if motif_choice == '14' :
                motif = custom_hatches.hline
            if motif_choice == '17' :
                 motif = custom_hatches.vline
            # Converts the pattern as lines so it's useable with draw_hatch function from custom_hatches.py
            ## Is called this way because this variable may be added to bar_dict's or poly_dict's dictionaries
            motif_for_dict = custom_hatches.shape_to_lines(*motif)

        # If entered value is 3, assign to "motif" the dot pattern (the "sandstone")
        ## Since we don't want segments between points, no need to use the shape_to_line() function
        if motif_choice in ['3'] :
            motif = custom_hatches.dots
            motif_for_dict = motif

        # If entered value is 4, assign to "motif" the grid-shaped pattern
        if motif_choice in ['4'] :
           custom_hatches.grid1
           custom_hatches.grid2
           # "+" sign here isn't used to sum any values, but to draw the grid shaped pattern (vertical line + horizontal line pattern)
           motif_for_dict = custom_hatches.grid1 + custom_hatches.grid2
        
        # If entered value is 7, assign to "motif" the different variables used to create the wave-shaped pattern 
        if motif_choice in ['7'] :
           custom_hatches.line1
           custom_hatches.line2
           custom_hatches.line3
           custom_hatches.line4
           # "+" sign here is not used to sum up any values but to draw the 4 used variables for the wave-shaped pattern (the first one, not the alt one)
           motif_for_dict = custom_hatches.line1 + custom_hatches.line2 + custom_hatches.line3 + custom_hatches.line4
        
        # If entered value is 9, assign to "motif" the different variables used to create the diagonal lines patterns
        if motif_choice in ['9'] :
            custom_hatches.slash1
            custom_hatches.slash2
            # Same stuff as before, 2 variables get drawn this way
            motif_for_dict = custom_hatches.slash1 + custom_hatches.slash2

        # If entered value is 11, assign to "motif_for_dict" the roots pattern
        if motif_choice in ['11'] :
            motif = custom_hatches.racines
            # Same as shape_to_line() except that first point and last point doesn't get connected (i.e. custom_hatches.py)
            motif_for_dict = custom_hatches.open_shape(*motif)

        # If entered value is 12, assign to "motif_for_dict" the pattern of the two hlines
        if motif_choice in ['12'] :
            custom_hatches.hlineA
            custom_hatches.hlineB
            # Le signe "+" n’est ici non pas utilisé pour additionner la moindre valeur, mais pour tracer les 2 variables utilisées pour le motif 12
            motif_for_dict = custom_hatches.hlineA + custom_hatches.hlineB

        # If entered value is 15, assign to "motif" the circles pattern
        ## Just like for dots, we don't want segments, we just want the centers
        if motif_choice in ['15'] :
            motif = custom_hatches.circles
            motif_for_dict = motif

        # If entered value is 16, assign to "motif" the circles pattern but patched to also accomodate vertical lines
        ## To merge the two types of patterns, they must be defined separately in a dictionary and a type must be defined for each figure (so that the script knows how to draw them later)
        if motif_choice in ['16'] :
            motif_for_dict = [
                {"data": custom_hatches.line1_16 + custom_hatches.line2_16 + custom_hatches.line3_16 + custom_hatches.line4_16, "type": "multilines"},
                {"data": custom_hatches.circles, "type": "circles"}
            ]

        # Failsafe in case someone doesn't input a valid number
        if motif_choice not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17'] :
            print("""\033[31;49;3mInvalid choice, no pattern will be applied.
                  \033[0;0m""")
            ask_hatch = "no"
    else :
        ask_hatch = "no"

def loopy_bar() :
    global bar_width, bar, x_wave, y_wave, labels, munsells, motif, motif_available, ask_hatch, motif_choice, motif_for_dict, bar_dict, poly_dict, bar_wave
    loopy = int(input("""
        Type here the number of layers you want to create: """))
    bottom = 0

    # Allows repeating the creation of bars depending on the wanted number of layers
    for i in range(loopy) :
        x = [0]
        # The "f" allows the usage of {i + 1} in the middle of the printed text in the input
        ## The {i + 1} shows the current loop we're in. So if that's the first loop it will display "layer 1", if it's 3rd loop it will display "layer 3"
        y = int(input(f"""
        Type here the height of your layer {i + 1} in cm: """))
        
        bar_wave = input("""
        Does your layer have a breach? \033[1;34;49m(yes/no)\033[0;0m: """).strip().lower()
        if bar_wave in ["yes", "y"] :
            bar_wave = "yes"

        # Label correspond to layer's name
        ## munsell_color is a sort of second label with a different name to avoid any bug
        label = input("""
        Type here the name of your layer: """)
        munsell_color = input("""
        Type here the Munsell color code: """)


        if bar_wave == "yes" :
            dash_wave = input("""
        Dashed line or solid line? \033[1;34;49m(dashed/solid)\033[0;0m: """).strip().lower()
            # Simplifies user input by accepting "d" for "dashed"
            if dash_wave in ["dashed", "d"] :
                dash_wave = "dashed"
            # x and y values for the breach
            bar_bottom = bottom
            x_wave = [0, 1, 2, 3, 4]
            y_wave = [y - 1, y, y - 1, y, y - 1]


            # Polygon should follow the shape given by x_wave and y_wave
            bar_left = x_wave[0]
            bar_right = x_wave[-1]

            # Polygon's points
            poly_x = [bar_left] + x_wave + [bar_right, bar_left]
            # Makes it so the breach doesn't start at 0 each time you loop
            poly_y = [bar_bottom] + [bar_bottom + yw for yw in y_wave] + [bar_bottom, bar_bottom]

            # Store polygon's data
            ## Mandatory to avoid bottom bar hiding the polygon
            poly_dict = {
                "type" : "poly",
                # "xy" corresponds to a list of tuples of x and y coordinates, zip allows to associate them together
                ## List is used to have the coordinates grouped in a list and be easily usable to draw the polygon later
                "xy" : list(zip(poly_x, poly_y)),
                "label" : label,
                "munsell" : munsell_color,
                "linestyle" : 'dashed' if dash_wave == "dashed" else 'solid'
            }
            # Launch hatch() function to ask if hatches are needed, and which ones to setup
            hatch()

            if ask_hatch == "yes" :
                if motif_choice in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17'] :
                    # Adds the "motif" option in the poly's dictionary and setting it to "motif_for_dict"
                    ## Go see hatch() to know what "motif_for_dict" refers to, it changes depending on what pattern you chose
                    poly_dict["motif"] = motif_for_dict
                    if motif_choice in ['3'] :
                        # Adds and setup "motif_type" option. Will be useful later for precising how exactly hatches must be drawn
                        poly_dict["motif_type"] = "dots"
                    elif motif_choice in ['4'] :
                        poly_dict["motif_type"] = "grid"
                    elif motif_choice in ['7'] :
                        poly_dict["motif_type"] = "multilines"
                    elif motif_choice in ['9', '10'] :
                        poly_dict["motif_type"] = "slash"
                    elif motif_choice in ['11'] :
                        poly_dict["motif_type"] = "racines"
                    elif motif_choice in ['12'] :
                        poly_dict["motif_type"] = "double_hline"
                    elif motif_choice in ['15'] :
                        poly_dict["motif_type"] = "circles"
                    elif motif_choice in ['16'] :
                        # Since motif 16 corresponds to two different predefined types of patterns
                        ## We assign a none value here so that motif_type is recorded in the poly_dict dictionary
                        ### While getting both types of patterns in "motif_for_dict"
                        poly_dict["motif_type"] = None
                    else :
                        # Adds and sets up "motif_type" option, except that it's for most patterns and not special cases like the ones just above
                        poly_dict["motif"] = motif_for_dict
                        poly_dict["motif_type"] = "lines"
            else :
                # Sets up these options as "None" so it gets ignored without breaking the script
                poly_dict["motif"] = None
                poly_dict["motif_type"] = None
            
            # Store the dictionary for later use under the name "horizons"
            horizons.append(poly_dict)

            # Update the "bottom" value to stack layers
            ## Updates it from the highest point of the last breach
            ### (higher point because the graph's y-axis is reversed)
            bottom += min(y_wave)


        else :
            dash = input("""
        Dotted line or solid line? \033[1;34;49m(dotted/solid)\033[0;0m: """).strip().lower()
            # Simplifies user input by accepting "d" for "dotted"
            if dash in ["dotted", "d"] :
                dash = "dotted"


            # Store bar's data
            bar_dict = {
                "type" : "bar",
                "x" : x,
                "y" : y,
                "bottom" : bottom,
                "label" : label,
                "munsell" : munsell_color,
                "linestyle" : 'dotted' if dash == "dotted" else 'solid'
            }

            # Runs hatch() function to ask if hatches are needed and which ones to setup
            hatch()

            if ask_hatch == "yes" :
                if motif_choice in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17'] :
                    # Adds the "motif" option in the bar's dictionary and setting it to "motif_for_dict"
                    ## Go see hatch() to know what "motif_for_dict" refers to, it changes depending on what pattern you chose
                    bar_dict["motif"] = motif_for_dict
                    if motif_choice in ['3'] :
                        # Adds and setup "motif_type" option. Will be useful later for how exactly hatches must be drawn
                        bar_dict["motif_type"] = "dots"
                    elif motif_choice in ['4'] :
                        bar_dict["motif_type"] = "grid"
                    elif motif_choice in ['7'] :
                        bar_dict["motif_type"] = "multilines"
                    elif motif_choice in ['9', '10'] :
                        bar_dict["motif_type"] = "slash"
                    elif motif_choice in ['11'] :
                        bar_dict["motif_type"] = "racines"
                    elif motif_choice in ['12'] :
                        bar_dict["motif_type"] = "double_hline"
                    elif motif_choice in ['15'] :
                        bar_dict["motif_type"] = "circles"
                    elif motif_choice in ['16'] :
                        # Since motif 16 corresponds to two different predefined types of patterns
                        ## We assign a none value here so that motif_type is recorded in the bar_dict dictionary
                        ### While getting both types of patterns in "motif_for_dict"
                        bar_dict["motif_type"] = None
                    else :
                        # Adds and sets up "motif_type" option, except that it's for most patterns and not special cases like the ones just above
                        bar_dict["motif"] = motif_for_dict
                        bar_dict["motif_type"] = "lines"
            else :
                # Sets up these options as "None" so it gets ignored without breaking the script
                bar_dict["motif"] = None
                bar_dict["motif_type"] = None

            # Store the dictionary for later use under the name "horizons"
            horizons.append(bar_dict)
            
            # Update the "bottom" value to stack layers
            ## Adds the y value to be sure the next layer doesn't get drawn over the first one
            bottom += y


    # "reversed" here makes the layers being drawn from last to first. That is also why we needed to store the data first
    ## This avoids layer overlapping issues
    for h in reversed(horizons) :
        if h["type"] == "bar" :
            bar = ax.bar(
                h["x"], 
                h["y"],
                bar_width,
                # Since h means "horizons" (but reversed), the following line means "bottom" = the bottom setting from, here, bar_dict 
                bottom = h["bottom"],
                # Same here for "label", then "color", etc.
                ## "label" is for the legend
                label = h["label"],
                # "facecolor" is the color of the bar
                facecolor = h["color"],
                # "edgecolor" is the color of the bar's outline
                edgecolor = 'black',
                # "linestyle" is the style of the outline ("dotted" or "line")
                linestyle = h["linestyle"],
                # Align the left edges of the bar with the x positions
                align = 'edge',
                # "zorder" determines the order in which bars, polygons, etc., must get drawn
                ## The higher the number is, the later the object will be drawn
                zorder = 1
            )
            # Get the "motif" value, if it's not None, fill the bar with the correct hatch and draws the hatch
            if h.get("motif") is not None :
                # Verifies if it's a dicts list (multi-pattern) or just data (single-pattern)
                ## More precisely, isinstance checks if h["motif"] is a dictionary or not
                ### If yes, then we go on with the for loop for m in h["motif"]
                if h["motif"] and isinstance(h["motif"][0], dict) :
                    # Multiple patterns : each element is a dictionnary with "data" and "type"
                    for m in h["motif"] :
                        # Depending on pattern's type, use the appropriate drawing function
                        if m["type"] == "multilines" :
                            custom_hatches.draw_hatch(ax, m["data"], (h["x"][0], h["x"][0] + bar_width), (h["bottom"], h["bottom"] + h["y"]), spacing = 0.5, color = 'black')
                        elif m["type"] == "circles" :
                            custom_hatches.draw_circles_patches(ax, m["data"], (h["x"][0], h["x"][0] + bar_width), (h["bottom"], h["bottom"] + h["y"]), spacing = 0.5, color = 'black', radius = 0.08)
                else :
                    # Single pattern : h["motif"] directly contains the pattern's data
                    if h["motif_type"] == "lines" :
                        ax.fill_between(h["x"], h["bottom"], h["bottom"] + h["y"], color = 'black')
                        # If motif 17 is chosen, then we add linewidth = 2 so that the lines are thicker
                        if motif_choice in ['17'] :
                        # (what you must apply the pattern on, type of pattern (left side of the bar, right side of the bar), (top side of the bar, bottom side of the bar))
                        ## "spacing" is the space between each array. It controls both vertical and horizontal spacing (except for vertical spacing in "racines", since in custom_hatches/draw_racines, the "spacing" argument was removed for dy)
                            custom_hatches.draw_hatch(ax, h["motif"], (h["x"][0], h["x"][0] + bar_width), (h["bottom"], h["bottom"] + h["y"]), spacing = 0.5, color = 'black', linewidth = 2)
                        else :
                            custom_hatches.draw_hatch(ax, h["motif"], (h["x"][0], h["x"][0] + bar_width), (h["bottom"], h["bottom"] + h["y"]), spacing = 0.5, color = 'black')
                    
                    if h["motif_type"] == "grid" :
                            ax.fill_between(h["x"], h["bottom"], h["bottom"] + h["y"], color = 'black')
                            custom_hatches.draw_hatch(ax, h["motif"], (h["x"][0], h["x"][0] + bar_width), (h["bottom"], h["bottom"] + h["y"]), spacing = 0.2, color = 'black')
                    if h["motif_type"] == "multilines" :
                            ax.fill_between(h["x"], h["bottom"], h["bottom"] + h["y"], color = 'black')
                            custom_hatches.draw_hatch(ax, h["motif"], (h["x"][0], h["x"][0] + bar_width), (h["bottom"], h["bottom"] + h["y"]), spacing = 1.2, color = 'black')
                    if h["motif_type"] == "slash" :
                            ax.fill_between(h["x"], h["bottom"], h["bottom"] + h["y"], color = 'black')
                            custom_hatches.draw_hatch(ax, h["motif"], (h["x"][0], h["x"][0] + bar_width), (h["bottom"], h["bottom"] + h["y"]), spacing = 1.0, color = 'black')
                    if h["motif_type"] == "racines" :
                            ax.fill_between(h["x"], h["bottom"], h["bottom"] + h["y"], color = "white")
                            custom_hatches.draw_racines(ax, h["motif"], (h["x"][0], h["x"][0] + bar_width), (h["bottom"], h["bottom"] + h["y"]), spacing = 0.5, color = 'white')
                    if h["motif_type"] == "dots" :
                            ax.fill_between(h["x"], h["bottom"], h["bottom"] + h["y"], color = 'black')
                            custom_hatches.draw_dots(ax, h["motif"], (h["x"][0], h["x"][0] + bar_width), (h["bottom"], h["bottom"] + h["y"]), spacing = 0.5, color = 'black')
                    if h["motif_type"] == "double_hline" :
                            ax.fill_between(h["x"], h["bottom"], h["bottom"] + h["y"], color = 'black')
                            custom_hatches.draw_hatch(ax, h["motif"], (h["x"][0], h["x"][0] + bar_width), (h["bottom"], h["bottom"] + h["y"]), spacing = 0.5, color = 'black')
                    if h["motif_type"] == "circles" :
                            ax.fill_between(h["x"], h["bottom"], h["bottom"] + h["y"], color = 'black')
                            custom_hatches.draw_circles_patches(ax, h["motif"], (h["x"][0], h["x"][0] + bar_width), (h["bottom"], h["bottom"] + h["y"]), spacing = 0.5, color = 'black', radius = 0.08)
                            
                            ax.set_aspect('equal')

            
            # Store "labels" data for later use with "annotate" for the legend
            labels.append(h["label"])
            # h.get and not h["munsell"] to avoid issues if "munsell" is not defined in the dictionary (it avoids a KeyError)
            munsells.append(h.get("munsell"))
        
        
            # Calculate the middle of the bar (adjusted for bar width)
            bar_x = h["x"][0] + (bar_width - 0.5)
            bar_y = h["bottom"] + h["y"] / 2

            # Annotate the bar with a line and the name of the bar (which is the label)
            ax.annotate(
                h["label"],
                xy = (bar_x, bar_y),
                # Position label to the right
                ## VA : Vertical Alignment, HA : Horizontal Alignment
                xytext = (bar_x + 1, bar_y),
                va = 'center',
                ha = 'left',
                # To draw the line, we must draw an arrow
                ## The arrow's type is a straight line
                arrowprops = dict(arrowstyle = '-', color = 'black')
            )

            # Annotate the bar with a line and the Munsell code below the label
            ax.annotate(
                h["munsell"] + "*",
                xy = (bar_x, bar_y + 0.5),
                # Places the Munsell code to the right of the line
                ## VA : Vertical Alignment, HA : Horizontal Alignment
                xytext = (bar_x + 1, bar_y + 0.5),
                va = 'center',
                ha = 'left',
                # To draw a line, we must in fact draw an arrow
                ## Arrow's type is a straight line
                arrowprops = dict(arrowstyle = '-', color = 'black')
            )

    # "reversed" here makes the layers being drawn from last to first. That is also why we needed to store the data first
    ## This avoids layer overlapping issues
    for h in reversed(horizons) :
        if h["type"] == "poly" :
            poly = patches.Polygon(
                # Since h means "horizons" (but reversed), the following line means "xy" = the xy setting from, here, poly_dict 
                xy = h["xy"],
                # "closed" being True means the first and last points are connected
                ## That's how we got a polygon that looks like a bar but with a v wave-shaped breach at the bottom
                closed = True,
                # Same as "xy" but for "label", then "color", etc.
                ## "label" is for the legend
                label = h["label"],
                # "facecolor" is the color of the polygon
                facecolor = h["color"],
                # "edgecolor" is the color of the polygon's outline
                edgecolor = 'black',
                # "linestyle" is the style of the outline ("dashed" or "line")
                linestyle = h['linestyle'],
                # Honestly, I don't remember what it does, I'm sorry...
                clip_on = True,
                # "zorder" determines the order in which bars, polygons, etc., must get drawn
                ## The higher the number is, the later the object will be drawn
                zorder = 3
            )
            # Draws the polygon
            ax.add_patch(poly)

            # Store "labels" data for later use with "annotate" for the legend
            labels.append(h["label"])
            # h.get and not h["munsell"] to avoid issues if "munsell" is not defined in the dictionary (it avoids a KeyError)
            munsells.append(h.get("munsell"))
            
            
            # Find the rightmost x and average y for the label placement later
            poly_xs, poly_ys = zip(*h["xy"])

            # Calculate x and y limits once for all patterns
            xmin, xmax = min(poly_xs), max(poly_xs)
            ymin, ymax = min(poly_ys), max(poly_ys)

            # Get the "motif" value, if it's not None, fill the polygon with the correct hatch and draws the hatch
            if h.get("motif") is not None :
                # Verifies if it's a dicts list (multi-pattern) or just data (single-pattern)
                ## More precisely, isinstance checks if h["motif"] is a dictionary or not
                ### If yes, then we go on with the for loop for m in h["motif"]
                if h["motif"] and isinstance(h["motif"][0], dict) :
                    # Multiple patterns : each element is a dictionnary with "data" and "type"
                    for m in h["motif"] :
                        # Depending on pattern's type, use the appropriate drawing function
                        if m["type"] == "multilines" :
                            custom_hatches.draw_hatch_clipped_for_poly(ax, m["data"], h["xy"], (xmin, xmax), (ymin, ymax), spacing=0.5, color='black')
                        elif m["type"] == "circles" :
                            custom_hatches.draw_circles_patches_clipped_for_poly(ax, m["data"], h["xy"], (xmin, xmax), (ymin, ymax), spacing=0.5, color='black', radius= 0.05)
                else :
                    # Single pattern : h["motif"] directly contains the pattern's data
                    if h.get("motif_type") == "lines" :
                            # If motif 17 is chosen, then we add linewidth = 2 so that the lines are thicker
                            if motif_choice in ['17'] :
                                # (what you must apply the pattern on, type of pattern (left side of the poly, right side of the poly), (top side of the poly, bottom side of the poly))
                                ## "spacing" is the space between each array. It controls both vertical and horizontal spacing (except for vertical spacing in "racines", since in custom_hatches/draw_racines, the "spacing" argument was removed for dy)
                                custom_hatches.draw_hatch_clipped_for_poly(ax, h["motif"], h["xy"], (xmin, xmax), (ymin, ymax), spacing = 0.5, linewidth = 2, color = 'black')
                            else :
                                custom_hatches.draw_hatch_clipped_for_poly(ax, h["motif"], h["xy"], (xmin, xmax), (ymin, ymax), spacing = 0.5, color = 'black')
                    if h.get("motif_type") == "grid" :
                            custom_hatches.draw_hatch_clipped_for_poly(ax, h["motif"], h["xy"], (xmin, xmax), (ymin, ymax), spacing = 0.2, color = 'black')
                    if h.get("motif_type") == "multilines" :
                            custom_hatches.draw_hatch_clipped_for_poly(ax, h["motif"], h["xy"], (xmin, xmax), (ymin, ymax), spacing = 1.2, color = 'black')
                    if h.get("motif_type") == "slash" :
                            custom_hatches.draw_hatch_clipped_for_poly(ax, h["motif"], h["xy"], (xmin, xmax), (ymin, ymax), spacing = 1.0, color = 'black')
                    if h.get("motif_type") == "racines" :
                            custom_hatches.draw_racines_clipped_for_poly(ax, h["motif"], h["xy"], (xmin, xmax), (ymin, ymax), spacing = 0.5, color = 'white')
                    if h.get("motif_type") == "dots" :
                            custom_hatches.draw_dots_clipped_for_poly(ax, h["motif"], h["xy"], (xmin, xmax), (ymin, ymax), spacing = 0.5, color = 'black')
                    if h.get("motif_type") == "double_hline" :
                            custom_hatches.draw_hatch_clipped_for_poly(ax, h["motif"], h["xy"], (xmin, xmax), (ymin, ymax), spacing = 0.5, color = 'black')
                    if h.get("motif_type") == "circles" :
                            custom_hatches.draw_circles_patches_clipped_for_poly(ax, h["motif"], h["xy"], (xmin, xmax), (ymin, ymax), spacing = 0.5, color = 'black', radius = 0.08)

            # Determines the x and y positions of the "label" and "munsell" for their placement in annotate()
            label_x = max(poly_xs) + 0.5
            label_y = sum(poly_ys) / len(poly_ys)
            munsell_x = max(poly_xs) + 0.5
            munsell_y = (sum(poly_ys) / len(poly_ys)) + 0.5

            
            # Annotate the polygon with a line and the name of the polygon (which is the label)
            ax.annotate(
                h["label"],
                xy = (max(poly_xs) - 0.5, label_y),
                # Position label to the right
                xytext = (label_x, label_y),
                ## VA : Vertical Alignment, HA : Horizontal Alignment
                va = 'center',
                ha = 'left',
                # To draw the line we must draw an arrow
                ## The arrow's type is a straight line
                arrowprops=dict(arrowstyle = '-', color = 'black')
                )
            
            # Annotate the bar with a line and the Munsell code below the label
            ax.annotate(
                h["munsell"] + "*",
                xy = (max(poly_xs) - 0.5, munsell_y),
                # Places the Munsell code to the right of the line
                xytext = (munsell_x, munsell_y),
                ## VA : Vertical Alignment, HA : Horizontal Alignment
                va = 'center',
                ha = 'left',
                # To draw the line we must draw an arrow
                ## The arrow's type is a straight line
                arrowprops=dict(arrowstyle = '-', color = 'black')
                )
            
    # I have no clue why, but all of a sudden, my layers didn't go all the way down nor up, my 0 wasn't aligned correctly and my ticks were a mess, I had to change all my code
    ## That's why I added (0, bottom) for ax.set_ylim() 
    ax.set_ylim(0, bottom)


# Runs the main function of the script
loopy_bar()


# Script by Mathys B.
## Some parts of the script are inspired by a script from Bogdan S.

# MIT License :
    # Copyright (c) 2025-2026 Mathys B.

    # Permission is hereby granted, free of charge, to any person obtaining a copy
    # of this software and associated documentation files (the "Software"), to deal
    # in the Software without restriction, including without limitation the rights
    # to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    # copies of the Software, and to permit persons to whom the Software is
    # furnished to do so, subject to the following conditions:

    # The above copyright notice and this permission notice shall be included in all
    # copies or substantial portions of the Software.

    # THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    # IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    # FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    # AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    # LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    # OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    # SOFTWARE.