# importing necessaries libraries
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import hachures.custom_hatches as custom_hatches


# Mathplotlib uses inches, but I want it to use cm instead
## 1 inch = 2.54 cm
inch_to_cm = 1 * 2.54

# Creates a figure and an axis with fixed dimensions in cm via unit conversion
## The fixed dimensions are there to prevent the bars from deforming when layers are added
### They are also there to keep the same proportions on export, regardless of resolution and screen's ppi
fig, ax = plt.subplots(figsize=(4 * inch_to_cm, 8 *inch_to_cm))

# Setup the variable for later use
bar = 0

# Layers' length. It's purely aesthetic!
bar_width = 4

# For the legend
labels = []
horizons = []


# Function to ask the user if they want to add a hatch to their layer
def hatch() :
    # Defines global variables for later use in the main function of the script: loopy_bar()
    global motif, ask_hatch, motif_choice, motif_for_dict, bar_dict, poly_dict, bar_wave
    
    # .strip().lower() to avoid issues with case sensitivity and accidental spaces
    ## .strip() takes care of leading/trailing spaces, and .lower() makes everything lowercase
    ask_hatch = input("Do you want to add a pattern to your layer? (yes/no): ").strip().lower()
    
    # Simplifies user input by accepting "y" for "yes"
    if ask_hatch in ["yes", "y"] :
        ask_hatch = "yes"
    
    if ask_hatch == "yes" :
        print("Available patterns:")
        print("1. Accumulation of iron")
        print("2. Alterned")
        print("3. Sandstone")
        print("4. Limestone")
        print("5. Organic slightly decomposed")
        print("6. Silica")
        print("7. Localised iron precipitation")
        print("8. Gley")
        print("9. Particulate horizon")
        print("10. Lumpy horizon")
        print("11. Roots")
        motif_choice = input("Type here the number of the pattern you want to use: ").strip()

        # Checks if entered value is 1, 2, 4, 5, 6, 8 or 10
        ## If the value is one of them, checks which one it is and assigns to "motif" the corresponding pattern
        if motif_choice in ['1', '2', '5', '6', '8', '10'] :
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
           # Le signe "+" n’est ici non pas utilisé pour additionner la moindre valeur, mais pour tracer les 4 variables utilisées pour le motif en forme d'onde
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

        if motif_choice in ['11'] :
            motif = custom_hatches.racines
            # Same as shape_to_line() except that first point and last point doesn't get connected (i.e. custom_hatches.py)
            motif_for_dict = custom_hatches.open_shape(*motif)

        # Failsafe in case someone doesn't input a valid number
        if motif_choice not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11'] :
            print("Invalid choice, no pattern will be applied.")
            ask_hatch = "no"
    else :
        ask_hatch = "no"

def loopy_bar() :
    global bar_width, bar, x_wave, y_wave, labels, motif, ask_hatch, motif_choice, motif_for_dict, bar_dict, poly_dict, bar_wave
    loopy = int(input("Type here the number of layers you want to create: "))
    bottom = 0

    # Allows repeating the creation of bars depending on the wanted number of layers
    for i in range(loopy) :
        x = [0]
        # The "f" allows the usage of {i + 1} in the middle of the printed text in the input
        ## The {i + 1} shows the current loop we're in. So if that's the first loop it will display "layer 1", if it's 3rd loop it will display "layer 3"
        y = int(input(f"Type here the height of your layer {i + 1} in cm: "))
        
        bar_wave = input("Does your layer have a breach? (yes/no): ").strip().lower()
        if bar_wave in ["yes", "y"] :
            bar_wave = "yes"

    
        label = input("Type here the name of your layer: ")
        color = input("Type here the color you want among the available ones: ")


        if bar_wave == "yes" :
            dash_wave = input("Dashed line or solid line? (dashed/solid): ").strip().lower()
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
                "xy" : list(zip(poly_x, poly_y)),
                "color" : color,
                "label" : label,
                "linestyle" : 'dashed' if dash_wave == "dashed" else 'solid'
            }

            # Launch hatch() function to ask if hatches are needed, and which ones to setup
            hatch()

            if ask_hatch == "yes" :
                if motif_choice in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11'] :
                    # Adds the "motif" option in the poly's dictionary and setting it to "motif_for_dict"
                    ## Go see hatch() to know what "motif_for_dict" refers to, it changes depending on what pattern you chose
                    poly_dict["motif"] = motif_for_dict
                    if motif_choice in ['3'] :
                        # Adds and setup "motif_type" option. Will be useful later for how exactly hatches must be drawn
                        poly_dict["motif_type"] = "dots"
                    elif motif_choice in ['4'] :
                        poly_dict["motif_type"] = "grid"
                    elif motif_choice in ['7'] :
                        poly_dict["motif_type"] = "multilines"
                    elif motif_choice in ['9', '10'] :
                        poly_dict["motif_type"] = "slash"
                    elif motif_choice in ['11'] :
                        poly_dict["motif_type"] = "racines"
                    else :
                        # Same as previous comment except it's for most patterns and not special cases like the rest above
                        poly_dict["motif_type"] = "lines"
            else :
                # Setup these options as "None" so it gets ignored without breaking the script
                poly_dict["motif"] = None
                poly_dict["motif_type"] = None
            
            # Store the dictionary for later use under the name "horizons"
            horizons.append(poly_dict)

            # Update the "bottom" value to stack layers
            ## Updates it from the highest point of the last breach
            ### (higher point because the graph's y-axis is reversed)
            bottom += min(y_wave)


        else :
            dash = input("Dotted line or solid line? (dotted/solid): ").strip().lower()
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
                "color" : color,
                "linestyle" : 'dotted' if dash == "dotted" else 'solid'
            }

            # Runs hatch() function to ask if hatches are needed and which ones to setup
            hatch()

            if ask_hatch == "yes" :
                if motif_choice in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11'] :
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
                    else :
                        # Same as previous comment except it's for most patterns and not special cases like the rest above
                        bar_dict["motif_type"] = "lines"
            else :
                # Setup these options as "None" so it gets ignored without breaking the script
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
                if h["motif_type"] == "lines" :
                        ax.fill_between(h["x"], h["bottom"], h["bottom"] + h["y"], color = 'black')
                        # (what you must apply the pattern on, type of pattern (left side of the bar, right side of the bar), (top side of the bar, bottom side of the bar))
                        ## "spacing" is the space between each array. It controls both vertical and horizontal spacing (except for vertical spacing in "racines", since in custom_hatches/draw_racines, the "spacing" argument was removed for dy)
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


            # Store "labels" data for later use with "annotate" for the legend
            labels.append(h["label"])
        
        
            # Calculate the middle of the bar (adjusted for bar width)
            bar_x = h["x"][0] + (bar_width - 0.5)
            bar_y = h["bottom"] + h["y"] / 2

            # Annotate the bar with a line and the name of the bar (which is the label)
            ax.annotate(
                h["label"],
                xy = (bar_x, bar_y),
                # Position label to the right
                xytext = (bar_x + 1, bar_y),
                va = 'center',
                ha = 'left',
                # To draw the line, we must draw an arrow
                ## The arrow's type is a straight line
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
            
            
            # Find the rightmost x and average y for the label placement later
            poly_xs, poly_ys = zip(*h["xy"])

            # Get the "motif" value, if it's not None, fill the polygon with the correct hatch and draws the hatch
            if h.get("motif") is not None :
                if h["motif_type"] == "lines" :
                        xmin, xmax = min(poly_xs), max(poly_xs)
                        ymin, ymax = min(poly_ys), max(poly_ys)
                        # (what you must apply the pattern on, type of pattern, xy positions (so x et y max and min can be used just after), (left side of the bar, right side of the bar), (top side of the bar, bottom side of the bar))
                        ## "spacing" is the space between each array. It controls both vertical and horizontal spacing (except for vertical spacing in "racines", since in custom_hatches/draw_racines, the "spacing" argument was removed for dy)
                        custom_hatches.draw_hatch_clipped_for_poly(ax, h["motif"], h["xy"], (xmin, xmax), (ymin, ymax), spacing = 0.5, color = 'black')
                if h["motif_type"] == "grid" :
                        xmin, xmax = min(poly_xs), max(poly_xs)
                        ymin, ymax = min(poly_ys), max(poly_ys)
                        custom_hatches.draw_hatch_clipped_for_poly(ax, h["motif"], h["xy"], (xmin, xmax), (ymin, ymax), spacing = 0.2, color = 'black')
                if h["motif_type"] == "multilines" :
                        xmin, xmax = min(poly_xs), max(poly_xs)
                        ymin, ymax = min(poly_ys), max(poly_ys)
                        custom_hatches.draw_hatch_clipped_for_poly(ax, h["motif"], h["xy"], (xmin, xmax), (ymin, ymax), spacing = 1.2, color = 'black')
                if h["motif_type"] == "slash" :
                        xmin, xmax = min(poly_xs), max(poly_xs)
                        ymin, ymax = min(poly_ys), max(poly_ys)
                        custom_hatches.draw_hatch_clipped_for_poly(ax, h["motif"], h["xy"], (xmin, xmax), (ymin, ymax), spacing = 1.0, color = 'black')
                if h["motif_type"] == "racines" :
                        xmin, xmax = min(poly_xs), max(poly_xs)
                        ymin, ymax = min(poly_ys), max(poly_ys)
                        custom_hatches.draw_racines_clipped_for_poly(ax, h["motif"], h["xy"], (xmin, xmax), (ymin, ymax), spacing = 0.5, color = 'white')
                if h["motif_type"] == "dots" :
                        xmin, xmax = min(poly_xs), max(poly_xs)
                        ymin, ymax = min(poly_ys), max(poly_ys)
                        custom_hatches.draw_dots_clipped_for_poly(ax, h["motif"], h["xy"], (xmin, xmax), (ymin, ymax), spacing = 0.5, color = 'black')


            # Determines the x and y positions of the "label" for its placement in annotate()
            label_x = max(poly_xs) + 0.5
            label_y = sum(poly_ys) / len(poly_ys)
            

            # Use the rightmost point (- 0.5) as the start of the arrow
            arrow_start = (max(poly_xs) - 0.5, label_y)
            
            # Annotate the polygon with a line and the name of the polygon (which is the label)
            ax.annotate(
                h["label"],
                xy = arrow_start,
                # Position label to the right
                xytext = (label_x, label_y),
                va = 'center',
                ha = 'left',
                # To draw the line we must draw an arrow
                ## The arrow's type is a straight line
                arrowprops=dict(arrowstyle = '-', color = 'black')
                )
            
    # I have no clue why, but all of a sudden, my layers didn't go all the down nor up, my 0 wasn't aligned correctly and my ticks were a mess, I had to change all my code
    ## That's why I added (0, bottom) for ax.set_ylim() 
    ax.set_ylim(0, bottom)


# Runs the main function of the script
loopy_bar()



# MIT License :
    # Copyright (c) 2024 Mathys B., aka Γucky

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
