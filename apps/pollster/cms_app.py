from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool

from django.utils.translation import ugettext_lazy as _

class SurveyIntakehook(CMSApp):
    name = _("Survey Intake")
    urls = ["apps.pollster.urls"]

class SurveyMonthlyhook(CMSApp):
    name = _("Survey  Monthly")
    urls = ["apps.pollster.urls"]

class SurveyResultshook(CMSApp):
    name = _("Survey Results")
    urls = ["apps.survey.urls"]
    app_name = "sublevel"

apphook_pool.register(SurveyIntakehook)
apphook_pool.register(SurveyMonthlyhook)
apphook_pool.register(SurveyResultshook)

