def get_chat_name(user1, user2):
    if user1.id > user2.id :
        return "one2one_"+str(user2.id)+"_"+str(user1.id)
    elif user1.id < user2.id:
        return "one2one_"+str(user1.id)+"_"+str(user2.id)
    
    return None

def get_chat_name_id(user1_id, user2_id):
    if user1_id > user2_id :
        return "one2one_"+str(user2_id)+"_"+str(user1_id)
    elif user1_id < user2_id:
        return "one2one_"+str(user1_id)+"_"+str(user2_id)
    
    return None