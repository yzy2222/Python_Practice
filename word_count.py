content = ''' Life Like Summer Flowers
  Let life be beautiful like summer flowers and death like autumn leaves.
  I sit at my window this morning where the world like a passer-by stops for a moment, nods to me and goes.                                                                                       
  The touch of the nameless days clings to my heart like mosses round the old tree.
  My day is done, and I am like a boat drawn on the beach, listening to the dance-music of the tide in the evening.
  I think of other ages that floated upon the stream of life and love and death and are forgotten, and I feel the freedom of passing away.
  If you shed tears when you miss the sun, you also miss the stars.
  Our names are the light that glows on the sea waves at night and then dies without leaving its signature.
  The cricket’s chirp and the patter of rain come to me through the dark, like the rustle of dreams from my past youth.
 1This rainy evening the wind is restless. I look at the swaying branches and ponder over the greatness of all things.
 1“You are the big drop of dew under the lotus leaf, I am the smaller one on its upper side,” said the dewdrop to the lake.
 1“We, the rustling leaves, have a voice that answers the storms, but who are you so silent?” “I am a mere flower.”'''

list_content = content.split()
list_content_1 = []
print(list_content)
print(len(list_content))
for i in range(len(list_content)):
    lst = []
    for j in range(len(list_content[i])):
        if (ord(list_content[i].lower()[j]) >= 97) and (ord(list_content[i].lower()[j]) <= 122):
              lst.append(list_content[i][j])
    list_content[i] = ''.join([k for k in lst])

    
    

#print(list_content)
lst = []
for i in range(len(list_content)):
     if list_content[i].lower() not in lst:
          lst.append(list_content[i].lower())
lst_count = [0]*len(lst)   
print(lst)  
print(len(lst))
print(lst_count)
print(len(lst_count))

for i in range(len(lst)):
    for j in range(len(list_content)):
         if list_content[j].lower() == lst[i]:
              lst_count[i] += 1

print(lst_count)  

result = dict(zip(lst, lst_count))
print(result)
          

"""
if ((ord(list_content[i].lower()[0]) < 97) or (ord(list_content[i].lower()[0]) > 122)) and\
          ((ord(list_content[i].lower()[-1]) < 97) or (ord(list_content[i].lower()[-1]) > 122)):
        list_content[i] = list_content[i][1:-1]
    elif (ord(list_content[i].lower()[0]) < 97) or (ord(list_content[i].lower()[0]) > 122):
        list_content[i] = list_content[i][1:]
    elif ((ord(list_content[i].lower()[-1]) < 97) or (ord(list_content[i].lower()[-1]) > 122)):
        list_content[i] = list_content[i][:-1]
        """