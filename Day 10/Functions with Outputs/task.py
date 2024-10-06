def format_name(f_name, l_name):
    formatted_f_name=f_name.title()
    formatted_l_name=l_name.title()
    #print(f"{formatted_f_name} {formatted_l_name}")
    return f"{formatted_f_name} {formatted_l_name}"

formatted_string = format_name(f_name="carlo", l_name="contardi")
print(formatted_string)
print(format_name(f_name="carlo", l_name="contardi"))
# output=len("Carlo")
# print(output)

def function_1(text):
    return text + text
def function_2(text):
    return text.title()

output = function_2(function_1("hello"))
print(output)