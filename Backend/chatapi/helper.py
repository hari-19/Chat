def get_chat_name(user1, user2):
    if user1.id > user2.id :
        return "one2one_"+str(user2.id)+"_"+str(user1.id)
    elif user1.id < user2.id:
        return "one2one_"+str(user1.id)+"_"+str(user2.id)
    
    return None