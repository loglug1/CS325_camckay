#namesake
hello = "hello"
world = "world"
print(hello, world)

print("BATMAN")
print(r"""_____________________                              _____________________
`-._:  .:'   `:::  .:\           |\__/|           /::  .:'   `:::  .:.-'
    \      :          \          |:   |          //         :       /    
     \     ::    .     `-_______/ ::   \_______-'   .      ::   . /      
      |  :   :: ::'  :   :: ::'  :   :: ::'      :: ::'  :   :: :|       
      |     ;::         ;::         ;::         ;::         ;::  |       
      |  .:'   `:::  .:'   `:::  .:'   `:::  .:'   `:::  .:'   `:|       
      /     :           :           :           :           :    \       
     /______::_____     ::    .     ::    .     ::   _____._::____\      
                   `----._:: ::'  :   :: ::'  _.----'                    
                          `--.       ;::  .--'                           
                              `-. .:'  .-'                               
                                 \    / :F_P:                            
                                  \  /                                   
                                   \/ """)

#define your ranges
start = 2
end = 14

for n in range(1,7):
    delta_x = (end - start)/n
    sum = 0
    for i in range(0,n):
        x_sub_i = start + (delta_x * i)
        #function in terms of x_sub_i
        y = 1 - 0.5*x_sub_i
        sum += y*delta_x
    print("Using " + str(n) + " rectangles's the area under the curve is " + str(sum))