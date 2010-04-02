from django.conf import settings
from django.db.models import signals
from django.utils.translation import ugettext_noop as _
 
if "notification" in settings.INSTALLED_APPS:
    from notification import models as notification
    
    def create_notice_types(app, created_models, verbosity, **kwargs):
        notification.create_notice_type("blocking_add", _("Blocking"), _("you have started blocking an user"), default=1)
        notification.create_notice_type("following_add", _("Following"), _("you have started following an user"), default=1)
        
        notification.create_notice_type("blockers_add", _("Blocked"), _("an user started blocking you"), default=1)
        notification.create_notice_type("followers_add", _("Followed"), _("an user started following you"), default=2)
        
        notification.create_notice_type("blocking_remove", _("Unblocking"), _("you stopped blocking an user"), default=1)        
        notification.create_notice_type("following_remove", _("Unfollowing"), _("you have stopped following an user"), default=1)
        
        notification.create_notice_type("follower_following_add", _("Followed Started Following"), 
                                        _("an user you are following started following another user"), default=1)
        notification.create_notice_type("follower_following_remove", _("Followed Stopped Following"), 
                                        _("an user you are following stopped following another user"), default=1) 
    
    signals.post_syncdb.connect(create_notice_types, sender=notification)
else:
    print "Skipping creation of NoticeTypes as notification app not found"
 
