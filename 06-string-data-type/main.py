text = "text"
text = "text 'this'"
text = 'text "this"'
text = 'text\' "this"'
text = "text\nthis"
text = """
This is
a story
the end

"this"
'this'
"""
print(text)

text = "text"
print("1 " + text + " 2")

# formatted string (F-String)
new_str = f"1 {text} 2, {2 + 5}"
print(new_str)
