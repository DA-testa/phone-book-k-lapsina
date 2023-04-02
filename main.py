# python3

class Query:
    def __init__(self, query):
        self.type = query[0]
        num = query[1]
        while len(num) > 1 and num[0] == '0':
            num = num[1:]
        if len(num) <=7:
            self.number = int(num)
        if self.type == 'add':
            if query[2].isalpha() and query[2] != "not found" and len(query[2])<=15 and query[2] != "":
                self.name = query[2]

def read_queries():
    n = int(input())
    if n>=1 and n<=105:
        return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    contacts = []
    for cur_query in queries:
        if cur_query.type == 'add':
            # if we already have contact with such number,
            # we should rewrite contact's name
            for contact in contacts:
                if contact.number == cur_query.number:
                    contact.name = cur_query.name
                    break
            else: # otherwise, just add it
                contacts.append(cur_query)
        elif cur_query.type == 'del':
            for j in range(len(contacts)):
                if contacts[j].number == cur_query.number:
                    contacts.pop(j)
                    break
        else:
            response = 'not found'
            for contact in contacts:
                if contact.number == cur_query.number:
                    response = contact.name
                    break
            result.append(response)
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))

