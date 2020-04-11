'''
Quan Nguyen

Algorithm Design
Term Project
03/05/2018

This program colors the map of the United States. We will give 
  neighbouring States different colors by using as fewest different colors as possible.
'''
import sys

'''
We will dictionary data type to represent the the map of the US in form of an undirected graph.
The 'key' represents a US state (a vertex in the graph).
The 'value' represents a list of adjacent States (adjacent vertices) to the give state (vertex).
'''
adjacency_map_of_USA = {
'AK': [],
'AL': ['MS','TN','GA','FL'],
'AR': ['MO','TN','MS','LA','TX','OK'],
'AZ': ['CA','NV','UT','CO','NM'],
'CA': ['OR','NV','AZ'],
'CO': ['WY','NE','KS','OK','NM','AZ','UT'],
'CT': ['NY','MA','RI'],
'DC': ['MD','VA'],
'DE': ['MD','PA','NJ'],
'FL': ['AL','GA'],
'GA': ['FL','AL','TN','NC','SC'],
'HI': [],
'IA': ['MN','WI','IL','MO','NE','SD'],
'ID': ['MT','WY','UT','NV','OR','WA'],
'IL': ['IN','KY','MO','IA','WI'],
'IN': ['MI','OH','KY','IL'],
'KS': ['NE','MO','OK','CO'],
'KY': ['IN','OH','WV','VA','TN','MO','IL'],
'LA': ['TX','AR','MS'],
'MA': ['RI','CT','NY','NH','VT'],
'MD': ['VA','WV','PA','DC','DE'],
'ME': ['NH'],
'MI': ['WI','IN','OH'],
'MN': ['WI','IA','SD','ND'],
'MO': ['IA','IL','KY','TN','AR','OK','KS','NE'],
'MS': ['LA','AR','TN','AL'],
'MT': ['ND','SD','WY','ID'],
'NC': ['VA','TN','GA','SC'],
'ND': ['MN','SD','MT'],
'NE': ['SD','IA','MO','KS','CO','WY'],
'NH': ['VT','ME','MA'],
'NJ': ['DE','PA','NY'],
'NM': ['AZ','UT','CO','OK','TX'],
'NV': ['ID','UT','AZ','CA','OR'],
'NY': ['NJ','PA','VT','MA','CT'],
'OH': ['PA','WV','KY','IN','MI'],
'OK': ['KS','MO','AR','TX','NM','CO'],
'OR': ['CA','NV','ID','WA'],
'PA': ['NY','NJ','DE','MD','WV','OH'],
'RI': ['CT','MA'],
'SC': ['GA','NC'],
'SD': ['ND','MN','IA','NE','WY','MT'],
'TN': ['KY','VA','NC','GA','AL','MS','AR','MO'],
'TX': ['NM','OK','AR','LA'],
'UT': ['ID','WY','CO','NM','AZ','NV'],
'VA': ['NC','TN','KY','WV','MD','DC'],
'VT': ['NY','NH','MA'],
'WA': ['ID','OR'],
'WI': ['MI','MN','IA','IL'],
'WV': ['OH','PA','MD','VA','KY'],
'WY': ['MT','SD','NE','CO','UT','ID']
}


'''
Input: 1 parameter
	map:	<dictionary>
		key: 	<string> 	(name of a State)
		value: 	<list> 		(list of adjacent States)

Output: 1 value
	colored_map:	<dictionary>
		key: 	<string> 	(name of a State)
		value: 	<int> 		(color of the State)
'''
def welsh_powell_algorithm(map):
	
	number_of_colors = 0 # number of colors used to color the map.
	
	# a dictionary with 'key' is the name of a State, and 'value' is the number of adjacent States to that State.
	valance_map = dict(zip(map.keys(), [len(map[x]) for x in map.keys()]))

	# a list of States sorted by the number of adjacent States for each State (the State with most adjacent States listed first).
	sorted_list_of_states = sorted(valance_map, key = valance_map.get, reverse = True)
	
	# suppose that we need 50 different colors for 50 different States.
	colors = []
	for i in range(50, 0, -1): # colors are named 1, 2, 3,..., 50.
		colors.append(i)
	
	# a dictionary containing all States with their colors. 
	colored_map = {}
	for key in map.keys():
		colored_map[key] = 'blank' # initially, all States' colors are blank.
		
	for index in range(len(sorted_list_of_states)): # for each State in the sorted list.
		state = sorted_list_of_states[index] # select the State with highest valence on the sorted list.
		if (colored_map[state] == 'blank'): # if this State is not colored yet.
			new_color = colors.pop() # choose a new color from the set of colors.
			colored_map[state] = new_color # color this State with this new color.
			number_of_colors += 1 # increase number of colors used.
		
			# Traverse down the list AND color every State
			#	which is not connected to the colored States above the same color.
			for other_state in sorted_list_of_states[index + 1:]:
				do_not_color = False # this variable used to decide whether or not we apply a color to a vertex.
				if(colored_map[other_state] == 'blank'): # if the State is not colored yet.
					if(map[other_state] == ''): # if a State has no neighbour.
						colored_map[other_state] = 1 # apply the color 1 to that State. In our case, Alaska and Hawaii are color 1.
					else: # if a State has at lease 1 neighbour
						for adjacent_state in map[other_state]: # for each State adjacent to the 'other_state'.
							if(colored_map[adjacent_state] == new_color): # if one of the 'adjacent_state' has the 'new_color'.
								do_not_color = True # do not color the 'other_state'.
								break
						if(do_not_color == False): # if none of the 'adjacent_state' has the 'new_color'.
							colored_map[other_state] = new_color # # color the 'other_state'.
							
	print('There are', number_of_colors, 'different colors were used!') # print out number of colors used.					
	return colored_map # return the colored version of the U.S. map.

# activate the function print() below to print out the result (a dictionary).	
print(welsh_powell_algorithm(adjacency_map_of_USA))















