# searlize the data

def individual_serlarizer(todo)-> dict:
    return {
        "id": str(todo['_id']),
        "title":todo['title'],
        "description":todo['description'],
        "complete":todo['complete']
    }

def list_serlarizer(todos)->list:
    return [individual_serlarizer(todo) for todo in todos]

