def h_s_updater(score) :
    
    with open('high_score.txt') as f:
        recent_s = f.read()
        recent_s = int(recent_s)
        
    if recent_s < int(score) or recent_s == '' :
        with open('high_score.txt','w')  as d:
            d.write(str(score))
            

h_s_updater(555)


with open('high_score.txt') as check_s:
    print('Highest Score is : ',check_s.read())
