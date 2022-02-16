from django.utils.translation import gettext_lazy as _


STATE_TYPES = (
    (-1, _('Deleted')),
    (1, _('Active')),
    (1, _('UnActive')),
)

SESSION_STATE = (
    (0, _('Pending')),
    (1, _('Start')),
    (2, _('Complete')),
)

MAX_CHASE_COUNT = 5
TIME_DELAY = 60
