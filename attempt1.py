#dictionary of AUM of all Funds we are looking at. 
#any entry is of the form {str->'Fund name' : int->'AUM'}
Assets_under_managment = {"ICICI":27170 ,
                         "Edelweiss_Mid":7187 ,
                         "Mahindra_Large":567 ,
                         "Nippon_Small":58553 ,
                         "SBI_Small":30801 ,
                         "Canara":14333 ,
                         "DSP_Small":15634 ,
                         "Edelweiss_Large":206 ,
                         "Motilal_Midcap":12478
                         }

total_AUM = 0
for i in Assets_under_managment:
    total_AUM += Assets_under_managment[i]

Relative_AUM = {}
for i in Assets_under_managment:
    Relative_AUM[i] = Assets_under_managment[i] / total_AUM

    
sorted_Funds = []
for i in Assets_under_managment:
    sorted_Funds.append([i , Assets_under_managment[i] , Relative_AUM[i]])

sorted_Funds.sort(reverse = True, key = lambda e : e[2])
n = len(sorted_Funds)
for i in range (n):
    sorted_Funds[i].append((1.1) ** (n - 1 - i))

#dictionary of holdings of all Funds we are looking at.
#any entry if of the form {str->'Fund name' : dict->p}
#where p is a dictionary of all the holdings of a fund with any entry of the form
#{str->'holding name' : float->'a number between 0 and 100 which gives % of its AUM it has invested'}
Holdings = {"ICICI" : {"Financial" : 24.4, 
                       "Energy" : 19.4, 
                       "Others" : 12.2, 
                       "Automobile" : 12.1,
                       "Healthcare" : 8.4,
                       "Communication" : 6.8,
                       "Construction" : 5.9,
                       "Technology" : 5.5,
                       "Services" : 5.3} ,
            
            "Edelweiss_Mid" : { "Capital Goods" : 21.6,
                       "Financial" : 15.1, 
                       "Services" : 11.9,
                       "Automobile" : 11.8,
                       "Others" : 11.3,
                       "Construction" : 9.5,
                       "Metals & Mining" : 6.5,
                       "Healthcare" : 6.5,
                       "Technology" : 5.8} ,
            
            "Mahindra_Large" : { "Financial" : 32.9,
                       "Others" : 18.5, 
                       "Energy" : 13.5,
                       "Technology" : 11.2,
                       "Consumer Staples" : 9.8,
                       "Automobile" : 7.4,
                       "Construction" : 6.7} ,
            
            "Nippon_Small" : { "Capital Goods" : 21.3,
                       "Financial" : 12.5, 
                       "Services" : 10,
                       "Consumer Staples" : 8,
                       "Others" : 27.6,
                       "Construction" : 6.2,
                       "Chemicals" : 7,
                       "Healthcare" : 7.3} ,
            
            "SBI_Small" : { "Services" : 17.4,
                       "Consumer Discretionary" : 14.8,
                       "Financial" : 14.6,
                       "Others" : 3.9, 
                       "Capital Goods" : 12.5,
                       "Consumer Staples" : 10.8,
                       "Chemicals" : 10.3,
                       "Metals & Mining" : 5,
                       "Construction" : 10.6} ,   
            
            "Canara" : {"Financial" : 29.6,
                       "Others" : 14.7,
                       "Technology" : 9.8,
                       "Automobile" : 9.5,
                       "Energy" : 9.4,
                       "Healthcare" : 8.1,
                       "Construction" : 7.5,
                       "Consumer Staples" : 6,
                       "Capital Goods" : 5.5} ,
            
            "DSP_Small" : {"Chemicals" : 16.1, 
                       "Capital Goods" : 14.6,
                       "Consumer Staples" : 11.2,
                       "Healthcare" : 8.9,
                       "Consumer Discretionary" : 8.6,
                       "Others" : 8.1,
                       "Metals & Mining" : 7.6, 
                       "Services" : 7.3,    
                       "Automobile" : 6.6,    
                       "Financial" : 5.9,
                       "Construction" : 5.2} ,
            
            "Edelweiss_Large" : {"Financial" : 22.1,
                       "Others" : 10.8,
                       "Energy" : 10.3,
                       "Capital Goods" : 8.8,          
                       "Automobile" : 8.2,          
                       "Technology" : 7.5, 
                       "Healthcare" : 7.3,  
                       "Construction" : 7.3,
                       "Services" : 7.1,          
                       "Consumer Staples" : 5.4,          
                       "Chemicals" : 5} ,
            
            "Motilal_Midcap" : {"Technology" : 14.2,
                       "Automobile" : 12.3,
                       "Financial" : 12.0,
                       "Consumer Discretionary" : 11.8, 
                       "Communication" : 11,
                       "Services" : 9.1,
                       "Construction" : 8.5,
                       "Capital Goods" : 7.7,
                       "Others" : 7.1,         
                       "Healthcare" : 6.3}}

all_possible_holdings = set()
for i in Holdings:
    for j in Holdings[i]:
        all_possible_holdings.add(j)

Holdings_value = {}
for i in all_possible_holdings:
    Holdings_value[i] = 0
    for j in sorted_Funds:
        if i in Holdings[j[0]]:
            Holdings_value[i] += (Holdings[j[0]][i] / 100) * j[1] * j[3]

ranked = list(Holdings_value.keys())
ranked.sort(reverse = True, key = lambda e : Holdings_value[e])

j = 1
for i in ranked :
    print(j , ".  " , i , sep = "")
    j += 1
        
    

