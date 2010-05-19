from django.conf import settings
from django.db.models import signals
from django.utils.translation import ugettext_noop as _
 
if "notification" in settings.INSTALLED_APPS:
    from notification import models as notification
    
    def create_notice_types(app, created_models, verbosity, **kwargs):
        notification.create_notice_type("blocking_add", _("Blocking"), _("You have started blocking an user"), default=1)
        notification.create_notice_type("following_add", _("Following"), _("You have started following an user"), default=1)
        
        notification.create_notice_type("blockers_add", _("Blocked"), _("An user started blocking you"), default=1)
        notification.create_notice_type("followers_add", _("Followed"), _("An user started following you"), default=2)
        
        notification.create_notice_type("blocking_remove", _("Unblocking"), _("You stopped blocking an user"), default=1)        
        notification.create_notice_type("following_remove", _("Unfollowing"), _("You have stopped following an user"), default=1)
        
        notification.create_notice_type("blockers_remove", _("Unblocked"), _("An user stopped blocking you"), default=1)
        notification.create_notice_type("followers_remove", _("Unfollowed"), _("An user stopped following you"), default=1)        
        
        notification.create_notice_type("follower_following_add", _("Followed Started Following"), 
                                        _("An user you are following started following another user"), default=1)
        notification.create_notice_type("follower_following_remove", _("Followed Stopped Following"), 
                                        _("An user you are following stopped following another user"), default=1) 
    
    signals.post_syncdb.connect(create_notice_types, sender=notification)
else:
    print "Skipping creation of NoticeTypes as notification app not found"
 
