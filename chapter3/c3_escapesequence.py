a="kk is a goood boy \
   who is learning python \n and he is very good in python\n\
   this is about escape sequence"
print(a)
# This code snippet demonstrates the use of escape sequences in Python strings.
# Escape sequences allow you to include special characters in strings, such as newlines (\n) and tabs (\t).
#if we use \n it will print in new line
#else it will print in same line by using \ only




# Python Escape Sequences - Quick Cheat Sheet
#  Common Escape Sequences:
#   \\    
# → Backslash
#   \'    
#   \"    
#   \n    
#   \t    
#   \r    
#   \b    
#   \f    
#   \v    
# → Single quote
#  → Double quote
#  → Newline (line break)
#  → Horizontal tab
#  → Carriage return (moves cursor to start of line)
#  → Backspace (deletes previous char)
#  → Form feed (page break, rarely used)
#  → Vertical tab (rarely used)
#  Octal & Hexadecimal Characters:
#   \ooo  → Character with octal value (e.g., "\101" → 'A')
#   \xhh  → Character with hex value (e.g., "\x41" → 'A')
#  Unicode Escape Sequences:
#   \uXXXX      
# → Unicode char (4 hex digits) (e.g., "\u03A9" → Ω)
#   \UXXXXXXXX  → Unicode char (8 hex digits) (e.g., "\U0001F600" → )
#   \N{name}    
# → Named Unicode char (e.g., "\N{GREEK CAPITAL LETTER OMEGA}" → Ω)
#  Raw Strings (Ignore Escapes):
#   r"string" → Keeps backslashes as-is
#   Example: r"C:\new\folder" → C:\new\folder
