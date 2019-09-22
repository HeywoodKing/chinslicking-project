from django.utils.translation import ugettext_lazy as _
from jet.dashboard import modules
from jet.dashboard.dashboard import Dashboard, AppIndexDashboard
from django.core.urlresolvers import reverse
# from jet.dashboard.dashboard_modules import google_analytics
# from jet.dashboard.dashboard_modules import yandex_metrika


class CustomIndexDashboard(Dashboard):
    columns = 3

    def init_with_context(self, context):
        site_name = get_admin_site_name(context)

        self.available_children.append(modules.LinkList)
        self.available_children.append(modules.Feed)

        # self.available_children.append(google_analytics.GoogleAnalyticsVisitorsTotals)
        # self.available_children.append(google_analytics.GoogleAnalyticsVisitorsChart)
        # self.available_children.append(google_analytics.GoogleAnalyticsPeriodVisitors)

        # 链接列表
        self.children.append(modules.LinkList(
            _('支持列表'),
            children=[
                {
                    'title': _('Django documentation'),
                    'url': 'http://docs.djangoproject.com',
                    'external': True,
                },
                {
                    'title': _('Django "django-users" mailing list'),
                    'url': 'http://groups.google.com/group/django-users',
                    'external': True,
                },
                {
                    'title': _('Django irc channel'),
                    'url': 'irc://irc.freenode.net/django',
                    'external': True,
                },
                {
                    'title': _('Django irc channel2'),
                    'url': 'irc://irc.freenode.net/django',
                    'external': True,
                },
            ],
            column=2,
            order=1,
            layout='stacked',
            draggable=False,
            deletable=False,
            collapsible=True,
        ))
        # 快速操作
        self.children.append(modules.LinkList(
            _('快速操作'),
            layout='inline',
            draggable=False,
            deletable=False,
            collapsible=False,
            children=[
                [_('查看站点'), '/'],
                [_('修改密码'),
                 reverse('%s:password_change' % site_name)],
                [_('退出'), reverse('%s:logout' % site_name)],
            ],
            column=0,
            order=0
        ))
        # 应用
        self.children.append(modules.AppList(
            _('应用'),
            exclude=('auth.*',),
            column=1,
            order=0
        ))
        # 用户
        self.children.append(modules.AppList(
            _('用户'),
            model=('auth.*',),
            column=2,
            order=0
        ))
        # 模块
        self.children.append(modules.ModelList(
            _('模型'),
            exclude=('auth.*',),
            column=0,
            order=0
        ))
        # 最近管理操作
        self.children.append(modules.RecentActions(
            _('最近操作'),
            10,
            column=0,
            order=1
        ))
        # 展示订阅信息
        self.children.append(modules.Feed(
            _('django订阅信息'),
            feed_url='http://www.djangoproject.com/rss/weblog',
            limit=5,
            column=1,
            order=1
        ))
        # google 分析插件
        # self.children.append(google_analytics.GoogleAnalyticsVisitorsTotals)
        # self.children.append(google_analytics.GoogleAnalyticsVisitorsChart)
        # self.children.append(google_analytics.GoogleAnalyticsPeriodVisitors)

        # self.available_children.append(yandex_metrika.YandexMetrikaVisitorsTotals)
        # self.available_children.append(yandex_metrika.YandexMetrikaVisitorsChart)
        # self.available_children.append(yandex_metrika.YandexMetrikaPeriodVisitors)


# class CustomAppIndexDashboard(AppIndexDashboard):
#     def init_with_context(self, context):
#         self.available_children.append(modules.LinkList)
#
#         self.children.append(modules.ModelList(
#             title=_('Application models'),
#             models=self.models(),
#             column=0,
#             order=0
#         ))
#         self.children.append(modules.RecentActions(
#             include_list=self.get_app_content_types(),
#             column=1,
#             order=0
#         ))
