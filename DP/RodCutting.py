class Solution:
    def rod_cutting_bottom_up( self, price_table, rod_len ):
        '''
        price_table : List[ ( len, price ) ]
        rod_len : int
        ret tyep : List[ int ]
        '''
        price_table.sort( key=lambda x:x[0] )
        if len(price_table) == 0:
            return []

        cut_price = [0] * ( rod_len + 1 )
        cut_solution = [ [] ] * (rod_len + 1)

        for i in range( rod_len + 1):
            for j in range( i+1 ):
                for l, p in price_table:
                    if l > j:
                        break

                    if cut_price[i] < p + cut_price[i-l]:
                        cut_price[i] = p + cut_price[i-l]
                        cut_solution[i] = [l] + cut_solution[i-l]

            # print( i, cut_price, cut_solution )

        return cut_price[-1], cut_solution[-1]
        
    def rod_cutting_top_down_sub( self, price_table, rod_len, cut_price, cut_solution ):
        if cut_price[rod_len]:
            return cut_solution[rod_len]

        p_max = 0
        s = []
        for i in range( rod_len + 1 ):
            for l, p in price_table:
                if l > i:
                    break

                self.rod_cutting_top_down_sub( price_table, rod_len - l, cut_price, cut_solution )

                if p_max < p + cut_price[rod_len-l]:
                    p_max = p + cut_price[rod_len-l]
                    s = [l] + cut_solution[rod_len-l]

        cut_price[rod_len] = p_max
        cut_solution[rod_len] = s

    def rod_cutting_top_down( self, price_table, rod_len ):
        '''
        price_table : List[ ( len, price ) ]
        rod_len : int
        ret tyep : List[ int ]
        '''
        price_table.sort( key=lambda x:x[0] )
        if len(price_table) == 0:
            return []
    
        cut_price = [0] * ( rod_len + 1 )
        cut_solution = [ [] ] * (rod_len + 1)

        self.rod_cutting_top_down_sub( price_table, rod_len, cut_price, cut_solution )

        return cut_price[-1], cut_solution[-1]
    
# price_table = [ (1,1), (2,5), (3,8), (4,9), (5,10), (6,17), (7, 17), (8,20), (9,24), (10,30) ]
# rod_len = 9
# print( Solution().rod_cutting_bottom_up( price_table, rod_len ) )
# print( Solution().rod_cutting_top_down( price_table, rod_len ) )

