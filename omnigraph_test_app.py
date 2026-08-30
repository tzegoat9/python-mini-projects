
# Python Service Writing to Global Users (ts=1788100252)
class GlobalUser:
    __tablename__ = 'global_users'

def onboard_user(user_id):
    GlobalUser.objects.filter(id=user_id).update(status='onboarded')
