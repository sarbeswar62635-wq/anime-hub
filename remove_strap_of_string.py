def remove_and_strip(word_list,target_word):
    result =  [word.strip() for word in word_list if word.strip()!=target_word]
    return result
list=['apple','banana','orange']
list_big = remove_and_strip(list,'apple')
print(list_big)