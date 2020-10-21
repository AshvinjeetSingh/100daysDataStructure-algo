arr=[1,2,2,4,5,6,7,10,2,15,80,2,0,-20];
max=0
min=0
i=0;
j=i+1;
end=len(arr)-1
while(end>=0):
	
	if(arr[i]>max):
		max=arr[i]
	if(arr[i]<arr[j]):
		min=arr[i]
	i+=1
	end-=1
print("Maximum Number",max,"\nMinimum Number",min)