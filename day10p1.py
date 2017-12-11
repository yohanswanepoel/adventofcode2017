import sys
import operator

def start_game():
    #with open('day10.txt') as f:
    #    stream = f.read()
    #stream = "<><random characters><<<<><{!>}><!!>><{o\"i!a,<{i<a>"
    input="183,0,31,146,254,240,223,150,2,206,161,1,255,232,199,88"
    input_list =[]
    for i in input:
        input_list.append(ord(i))

    input_list.append(17)
    input_list.append(31)
    input_list.append(73)
    input_list.append(47)
    input_list.append(23)


    cl = Circular_List(256)
    print("Starter")
    cl.show()

    x = 0
    while x < 64:
        for i in input_list:
            cl.reverse_elements(i)
        x += 1
    print("Sparse Hash")
    cl.show()
    hash = cl.create_dense_hash(16)
    #res = hash[0] * hash[1]
    print("result",hash)
    result = ""
    for h in hash:
        result += format(h, '02x')
    print(result)



class Circular_List:
    def __init__(self,size):
        self.mylist=list(range(size))
        self.len = len(self.mylist)
        self.current_position = 0
        self.skip_size = 0

    def reverse_elements(self,length):
        to_position = self.current_position + length
        if(to_position < self.len): # No need to loop around just take a slice and reverse it
            tmp_list = self.mylist[self.current_position:to_position]
            #print("to_reverse", tmp_list)
            tmp_list.reverse()
            self.mylist[self.current_position:to_position] = tmp_list
        else:  #We now have to loop around
            tmp_list = self.mylist[self.current_position:self.len]
            split_place = len(tmp_list)
            tmp_list += self.mylist[0:self.normalise_index(to_position)]
            #print("to_reverse", tmp_list)
            tmp_list.reverse()
            # No reassemble the list
            first_set_number = self.len - self.current_position
            self.mylist[self.current_position:self.len] = tmp_list[0:first_set_number]
            self.mylist[0:self.normalise_index(to_position)] = tmp_list[split_place:len(tmp_list)]
        self.change_current_position(length)
        #print("reverse", tmp_list)
        #print(self.mylist)

    def change_current_position(self,length):
        new_pos_index = self.current_position + length + self.skip_size
        self.current_position = self.normalise_index(new_pos_index)
        self.skip_size += 1

    def show(self):
        print(self.mylist)

    def get_item(self,index):
        return self.mylist[self.normalise_index(index)]

    def normalise_index(self,index):
        return index % (self.len)

    def create_dense_hash(self,block_size):
        dense_hash = []
        counter = 0
        while counter < block_size:
            dense_hash.append(0)
            counter2 = 0
            while counter2 < block_size:
                dense_hash[counter] ^= self.mylist[(block_size * counter) + counter2]
                counter2 += 1
            counter += 1
        return dense_hash




if __name__ == '__main__':
    start_game()
