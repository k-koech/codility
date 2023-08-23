def solution(S, C):
    names = S.split(', ')
    print(names)
    email_map = {}
    result = []

    for name in names:
        first_name, *middle_name, last_name = name.split(' ')

        middle_initial = middle_name[0][0].lower() if middle_name else ''
        sanitized_last_name = last_name.replace('-', '').lower()[:8]
        
        email = f"{first_name[0].lower()}{middle_initial}{sanitized_last_name}"

        # [:8]
        
        if email in email_map:
            count = email_map[email]
            email_map[email] = count + 1
            email = email + str(count)
            print(email_map)
        else:
            email_map[email] = 2
        
        
        email = email +  f"@{C.lower()}.com"

        result.append(f"{name} <{email}>")
        # print(email)


    return ', '.join(result)

C = "Example"
S = "John Doe, Peter Parker, Mary Jane Watson-Parker, James Doe, John Elvis Doe, Jane Doe, Penny Parker"

email_addresses = solution(S, C)
print(email_addresses)
