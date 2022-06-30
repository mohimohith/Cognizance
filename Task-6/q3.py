count = 0;  
word = "";  
maxCount = 0;  
words = [];    
file = open("pandas/about.txt", "r")  
for line in file:  
    string = line.lower().replace(',','').replace('.','').split(" ");  
    for s in string:
        if len(s)>=6: #len greater than 6
            words.append(s);   
for i in range(0, len(words)):  
    count = 1;  
    for j in range(i+1, len(words)):  
        if(words[i] == words[j]):  
            count = count + 1;  
    if(count > maxCount):  
        maxCount = count;  #frequency
        word = words[i];  
          
print("Most repeated word: " + word); 
print("Frequency: " ,maxCount); 
file.close();  