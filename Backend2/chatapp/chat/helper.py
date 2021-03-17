def get_chat_name(user1, user2):
    if user1.id > user2.id :
        return "one2one-"+str(user2.id)+"-"+str(user1.id)
    elif user1.id < user2.id:
        return "one2one-"+str(user1.id)+"-"+str(user2.id)
    elif user1.id == user2.id:
        return "one2one-"+str(user1.id)+"-"+str(user1.id)

    return None

def get_chat_name_id(user1_id, user2_id):

    if user1_id > user2_id :
        return "one2one-"+str(user2_id)+"-"+str(user1_id)
    elif user1_id < user2_id:
        return "one2one-"+str(user1_id)+"-"+str(user2_id)
    elif user1_id == user2_id:
        return "one2one-"+str(user1_id)+"-"+str(user1_id)
    
    return None