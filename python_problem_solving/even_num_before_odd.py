input_list =[1,2,3,4,5,6,7,10,12,14,17,19,20]
def get_even_num(input_list:list):
    output_list=[]
    for i in range(len(input_list)-1):
        if(input_list[i]%2==0 and input_list[i+1]%2==1):
            output_list.append(input_list[i])
    print(output_list)


get_even_num(input_list)

