problem_link = 'https://jovian.ai/aakashns/python-binary-search#C5'

#1st step

#state problem
#We need to a program to find a postion of a card of a given query. Where cards are arragned in decreasing order

# cards = [8, 7, 6, 4, 3, 2, 1]
# query = 6
# output = 2

# def locate_card(cards, query):
#     pass


# result = locate_card(cards, query)
# print(result==output)


test = {
    'input' : {
        'cards' : [8, 7, 6, 4, 3, 2, 1],
        'query' : 4
    },
    'output' : 3
}

# locate_card(**test['input']) == test['output']

#covering all edge carses
#1. the query occurs somewhere in the middle
#2. The queryy occurs at first
#3. The query occurs at last
#4. The query doesn't exists
#5. The query are duplicated
#6. List is empty
#7. The cards carry just query

tests = []

#occurs at middle
tests.append({
    'input' : {
        'cards' : [8, 7, 6, 4, 3, 2, 1],
        'query' : 4
    },
    'output': 3
})

#occurs at first
tests.append({
    'input' : {
        'cards' : [8, 7, 6, 4, 3, 2, 1],
        'query' : 8
    },
    'output': 0
})

#occurs at last
tests.append({
    'input' : {
        'cards' : [8, 7, 6, 4, 3, 2, 1],
        'query' : 1
    },
    'output': 6
})

#Doesn't exist
tests.append({
    'input' : {
        'cards' : [8, 7, 6, 4, 3, 2, 1],
        'query' : 9
    },
    'output': -1
})

#query is duplicate
tests.append({
    'input' : {
        'cards' : [8, 7, 6, 6, 6, 6, 6, 4, 3, 2, 1],
        'query' : 6
    },
    'output': 2
})

#list is empty
tests.append({
    'input' : {
        'cards' : [],
        'query' : 4
    },
    'output': -1
})

#card with query
tests.append({
    'input' : {
        'cards' : [8],
        'query' : 8
    },
    'output': 0
})

#Simple function explination
# 1. Create a variable called postion
# 2. Check whether number at index position in cards is equal to query
# 3. if it does, positon is the answer and can be return funciton
# 4. else incriment the postion by 1 and repet 2-5
# 5. if number was not found return -1

# # # def locate_card(cards, query):
# # #     position = 0
# # #     print(cards)
# # #     while position < len(cards):
# # #         if cards[position] == query:
# # #             return position
        
# # #         position += 1
# # #     return -1
        
# # # result = locate_card(**test['input'])

# # # # print(result == test['output'])

# # # from jovian.pythondsa import evaluate_test_cases

# # # evaluate_test_cases(locate_card, tests)
# # # #time complexity O(N) and space complexity is O(1)



#write a program to find a card location in a minimum attempts. First get the middle cards check where its greater then or smaller then the query
#if its greater then get the right part of the list. if its smaller then the query then get its left part of the list repeate until the middle number is equal to query #

# 1. find the middle element of the cards
# 2. if it matches to query number, then return postion of the number
# 3. if its greater then the query, then search the left half of the cards
# 4. if its smaller then the query, then search the right half of the cards
# 5. if no more elements remain return -1#

def locate_cards(cards, query):
    left_pointer = 0
    right_pointer = len(cards) - 1

    while left_pointer <= right_pointer:
        mid = (left_pointer + right_pointer) // 2
        mid_num = cards[mid]


        if mid_num == query:
            if mid-1 >= 0 and cards[mid-1] == query:
                right_pointer = mid - 1
            else:
                return mid
        elif mid_num > query:
            left_pointer = mid + 1
        elif mid_num < query:
            right_pointer = mid - 1
        
        
    return -1


from jovian.pythondsa import evaluate_test_cases, evaluate_test_case
evaluate_test_cases(locate_cards, tests)

# Time complexity of BINARY SEARCH is O(log N) and Space complexity is O(1)