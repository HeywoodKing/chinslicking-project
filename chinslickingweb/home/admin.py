from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from home import models
from django.contrib.admin import SimpleListFilter
# from jet.filters import DateRangeFilter
from django.contrib.admin.models import LogEntry

# Register your models here.
admin.site.index_title = '欢迎使用秦食皇后台管理系统'
admin.site.site_title = '后台管理系统'
admin.site.site_header = '秦食皇后台管理系统'


# 是否启用过滤
class IsEnableFilter(SimpleListFilter):
    title = '是否启用'
    parameter_name = 'is_enable'

    def lookups(self, request, model_admin):
        return [(1, '是'), (0, '否')]

    def queryset(self, request, queryset):
        # pdb.set_trace()
        if self.value() == '1':
            return queryset.filter(is_enable=True)
        elif self.value() == '0':
            return queryset.filter(is_enable=False)
        else:
            return queryset.filter()


# 是否领取
class IsGetFilter(SimpleListFilter):
    title = '是否领取'
    parameter_name = 'is_get'

    def lookups(self, request, model_admin):
        return [(1, '已领取'), (0, '未领取')]

    def queryset(self, request, queryset):
        # pdb.set_trace()
        if self.value() == '1':
            return queryset.filter(is_get=True)
        elif self.value() == '0':
            return queryset.filter(is_get=False)
        else:
            return queryset.filter()


# 是否已通知
class IsInformFilter(SimpleListFilter):
    title = '是否通知'
    parameter_name = 'is_inform'

    def lookups(self, request, model_admin):
        return [(1, '已通知'), (0, '未通知')]

    def queryset(self, request, queryset):
        # pdb.set_trace()
        if self.value() == '1':
            return queryset.filter(is_inform=True)
        elif self.value() == '0':
            return queryset.filter(is_inform=False)
        else:
            return queryset.filter()


# 是否推荐
class IsRecommandFilter(SimpleListFilter):
    title = '是否推荐'
    parameter_name = 'is_recommand'

    def lookups(self, request, model_admin):
        return [(1, '是'), (0, '否')]

    def queryset(self, request, queryset):
        # pdb.set_trace()
        if self.value() == '1':
            return queryset.filter(is_recommand=True)
        elif self.value() == '0':
            return queryset.filter(is_recommand=False)
        else:
            return queryset.filter()


# 超级用户状态
class IsSuperUserFilter(SimpleListFilter):
    title = '超级用户状态'
    parameter_name = 'is_superuser'

    def lookups(self, request, model_admin):
        return [(1, '是'), (0, '否')]

    def queryset(self, request, queryset):
        # pdb.set_trace()
        if self.value() == '1':
            return queryset.filter(is_superuser=True)
        elif self.value() == '0':
            return queryset.filter(is_superuser=False)
        else:
            return queryset.filter()


# 超级用户状态
class IsActiveFilter(SimpleListFilter):
    title = '是否有效'
    parameter_name = 'is_superuser'

    def lookups(self, request, model_admin):
        return [(1, '是'), (0, '否')]

    def queryset(self, request, queryset):
        # pdb.set_trace()
        if self.value() == '1':
            return queryset.filter(is_active=True)
        elif self.value() == '0':
            return queryset.filter(is_active=False)
        else:
            return queryset.filter()


# 管理员
@admin.register(models.ChinUserProfile)
class ChinUserProfileAdmin(UserAdmin):
    list_display = ('username', 'email', 'nick_name', 'first_name', 'last_name', 'qq', 'phone',
                    'is_superuser', 'is_active', )
    list_display_links = ('username', )
    list_editable = ('nick_name', 'qq', 'phone', 'is_superuser', 'is_active', )
    list_per_page = 30
    list_filter = (IsSuperUserFilter, IsActiveFilter, 'groups')
    search_fields = ('username', 'nick_name', 'first_name', 'last_name', 'email')
    ordering = ('username',)
    filter_horizontal = ('groups', 'user_permissions',)
    exclude = ('create_uid', 'create_username', 'create_time', 'operate_uid', 'operate_username', )


# 导航菜单管理
@admin.register(models.SysNav)
class SysNavAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'name', 'url', 'parent', 'sort', 'is_root', 'is_enable', 'is_delete')
    list_display_links = ('id', 'name', 'url',)
    list_editable = ('code', 'sort', 'is_enable',)
    list_filter = (IsEnableFilter, )
    list_per_page = 30
    exclude = ('create_uid', 'create_username', 'create_time', 'operate_uid', 'operate_username', )
    search_fields = ('name', 'url', )


# 用户日志
@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    list_display = ('object_id', 'object_repr', 'action_flag', 'user', 'change_message', )


# Banner管理
@admin.register(models.ChinBanner)
class ChinBannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'nav', 'image_url', 'sort', 'is_enable')
    list_display_links = ('id', )
    list_editable = ('nav', 'sort', 'is_enable', )
    list_filter = (IsEnableFilter, )
    list_per_page = 30
    exclude = ('create_uid', 'create_username', 'create_time', 'operate_uid', 'operate_username', )
    search_fields = ('nav', )


# 产品列表
@admin.register(models.ChinProduct)
class ChinProductAdmin(admin.ModelAdmin):
    # fields = ()
    # inlines = ()
    list_display = ('name', 'brief_profile', 'profile', 'cover_image_url', 'read_count',
                    'product_type', 'sort', 'is_recommand', 'is_enable', 'create_time')
    list_display_links = ('name', 'brief_profile', 'profile',)
    list_editable = ('sort', 'is_recommand', 'is_enable', 'product_type')
    list_filter = ('product_type', IsRecommandFilter, IsEnableFilter, 'create_time', )
    list_per_page = 30
    exclude = ('create_uid', 'create_username', 'create_time', 'operate_uid', 'operate_username', )
    # fieldsets = (
    #     ('基本设置', {
    #         'fields': ('name', 'brief', 'product_type', )
    #     }),
    #     ('高级设置', {
    #         'classes': ('collapse', ),
    #         'fields': ('read_count', 'content', 'cover_image_url', 'sort', 'is_recommand')
    #     }),
    # )
    search_fields = ('name', 'product_type', )
    # list_max_show_all =
    # list_per_page =
    # list_select_related =
    # change_list_template =
    # sortable_by =
    # '''每页显示条目数'''
    # list_per_page = 10
    # 按日期筛选
    # date_hierarchy = 'create_time'
    # 按创建日期排序
    # ordering = ('-create_time',)
    # prepopulated_fields = {'slug': ('name',)}

    class Media:
        js = (
            '/static/plugins/kindeditor-4.1.10/kindeditor-all-min.js',
            '/static/plugins/kindeditor-4.1.10/lang/zh_CN.js',
            '/static/plugins/kindeditor-4.1.10/config.js',
        )


# 产品类型
@admin.register(models.ChinProductType)
class ChinProductTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'sort', 'is_enable', 'data_filter_name')
    list_display_links = ('name', )
    list_editable = ('is_enable', 'sort', 'data_filter_name', )
    list_filter = (IsEnableFilter, )
    list_per_page = 30
    search_fields = ('name', )
    exclude = ('create_uid', 'create_username', 'create_time', 'operate_uid', 'operate_username', )


# 合作伙伴
@admin.register(models.ChinPartner)
class ChinPartnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'logo', 'brief', 'profile', 'url', 'address', 'sort', 'is_enable', )
    list_display_links = ('name', 'profile',)
    list_editable = ('sort', 'is_enable', 'url', )
    list_filter = (IsEnableFilter, 'create_time',)
    search_fields = ('name', 'brief',)
    exclude = ('create_uid', 'create_username', 'create_time', 'operate_uid', 'operate_username', )


# 合作共赢 品牌合作-0:合作政策 1:项目优势 2:经销商问答 3:支持与服务
@admin.register(models.ChinCooperation)
class ChinCooperationAdmin(admin.ModelAdmin):
    list_display = ('title', 'profile', 'type', 'sort', 'is_enable')
    list_display_links = ('title', 'profile')
    list_editable = ('type', 'sort', 'is_enable', )
    list_filter = (IsEnableFilter, 'type', )
    search_fields = ('title', 'profile', )
    exclude = ('create_uid', 'create_username', 'create_time', 'operate_uid', 'operate_username', )

    class Media:
        js = (
            '/static/plugins/kindeditor-4.1.10/kindeditor-all-min.js',
            '/static/plugins/kindeditor-4.1.10/lang/zh_CN.js',
            '/static/plugins/kindeditor-4.1.10/config.js',
        )


# # 合作共赢 品牌合作-合作政策
# @admin.register(models.ChinCooperationPolicy)
# class ChinCooperationPolicyAdmin(admin.ModelAdmin):
#     list_display = ('title', 'profile', 'is_enable')
#     list_display_links = ('title', 'profile')
#     list_editable = ('is_enable', )
#     list_filter = (IsEnableFilter, )
#     search_fields = ('title', )
#     exclude = ('create_uid', 'create_username', 'create_time', 'operate_uid', 'operate_username', )
#
#     class Media:
#         js = (
#             '/static/plugins/kindeditor-4.1.10/kindeditor-all-min.js',
#             '/static/plugins/kindeditor-4.1.10/lang/zh_CN.js',
#             '/static/plugins/kindeditor-4.1.10/config.js',
#         )
#
#
# # 合作共赢 品牌合作-项目优势
# @admin.register(models.ChinCooperationSuperiority)
# class ChinCooperationSuperiorityAdmin(admin.ModelAdmin):
#     list_display = ('title', 'profile', 'is_enable')
#     list_display_links = ('title', 'profile')
#     list_editable = ('is_enable', )
#     list_filter = (IsEnableFilter, )
#     search_fields = ('title', )
#     exclude = ('create_uid', 'create_username', 'create_time', 'operate_uid', 'operate_username', )
#
#     class Media:
#         js = (
#             '/static/plugins/kindeditor-4.1.10/kindeditor-all-min.js',
#             '/static/plugins/kindeditor-4.1.10/lang/zh_CN.js',
#             '/static/plugins/kindeditor-4.1.10/config.js',
#         )
#
#
# # 合作共赢 品牌合作-项目优势
# @admin.register(models.ChinCooperationQuestion)
# class ChinCooperationQuestionAdmin(admin.ModelAdmin):
#     list_display = ('title', 'profile', 'is_enable')
#     list_display_links = ('title', 'profile')
#     list_editable = ('is_enable', )
#     list_filter = (IsEnableFilter, )
#     search_fields = ('title', )
#     exclude = ('create_uid', 'create_username', 'create_time', 'operate_uid', 'operate_username', )
#
#     class Media:
#         js = (
#             '/static/plugins/kindeditor-4.1.10/kindeditor-all-min.js',
#             '/static/plugins/kindeditor-4.1.10/lang/zh_CN.js',
#             '/static/plugins/kindeditor-4.1.10/config.js',
#         )


# 关于我们 品牌介绍
@admin.register(models.ChinAbout)
class ChinAboutAdmin(admin.ModelAdmin):
    list_display = ('comp_name', 'title', 'profile', 'comp_image', 'is_enable')
    list_display_links = ('comp_name', 'profile', )
    list_editable = ('title', 'is_enable')
    list_filter = (IsEnableFilter, 'create_time',)
    search_fields = ('comp_name', 'title',)
    exclude = ('create_uid', 'create_username', 'create_time', 'operate_uid', 'operate_username', )

    class Media:
        js = (
            '/static/plugins/kindeditor-4.1.10/kindeditor-all-min.js',
            '/static/plugins/kindeditor-4.1.10/lang/zh_CN.js',
            '/static/plugins/kindeditor-4.1.10/config.js',
        )


# 品牌介绍图片资源
@admin.register(models.ChinAboutResource)
class ChinAboutResourceAdmin(admin.ModelAdmin):
    list_display = ('type_code', 'type_name', 'image_url', 'sort', 'is_enable')
    list_display_links = ('type_name',)
    list_editable = ('type_code', 'sort', 'is_enable')
    list_filter = ('type_name', IsEnableFilter, 'create_time',)
    list_per_page = 30
    search_fields = ('type_code', 'type_name')
    exclude = ('create_uid', 'create_username', 'create_time', 'operate_uid', 'operate_username',)


# 动画类型
@admin.register(models.ChinAnimateType)
class ChinAnimateTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'class_name', 'profile', 'is_enable')
    list_display_links = ('id', )
    list_editable = ('name', 'class_name', 'is_enable', )
    list_filter = (IsEnableFilter, )
    list_per_page = 30
    search_fields = ('name', 'class_name', )
    exclude = ('create_uid', 'create_username', 'create_time', 'operate_uid', 'operate_username', )


# 首页模块
@admin.register(models.ChinIndexPlate)
class ChinIndexPlateAdmin(admin.ModelAdmin):
    # list_display = ('id', 'title', 'plate_image_url', 'front_image', 'back_image', 'descr', 'animate_type',
    #                 'is_redirect_sub_page', 'sub_page_url', 'video_source', 'sort', 'is_enable', )
    list_display = ('id', 'title', 'profile', 'animate_type',
                    'is_redirect_sub_page', 'sub_page_url', 'video_source', 'sort', 'is_enable',)
    list_display_links = ('id', 'profile')
    list_editable = ('title', 'animate_type', 'is_redirect_sub_page', 'is_enable', 'sort', )
    list_filter = (IsEnableFilter, 'create_time',)
    search_fields = ('title', 'desc', 'animate_type')
    exclude = ('create_uid', 'create_username', 'create_time', 'operate_uid', 'operate_username', )


# 发展历程
@admin.register(models.ChinCompanyHistory)
class ChinCompanyHistoryAdmin(admin.ModelAdmin):
    # exclude = ('breif', 'content', )
    list_display = ('timeline_title', 'title', 'breif', 'cover_image_url', 'sort', 'is_enable', )
    list_display_links = ('timeline_title', )
    list_editable = ('title', 'is_enable', 'sort', )
    list_filter = (IsEnableFilter, 'create_time',)
    list_per_page = 30
    search_fields = ('title', 'breif', 'timeline_title')
    exclude = ('create_uid', 'create_username', 'create_time', 'operate_uid', 'operate_username', )

    class Media:
        js = (
            '/static/plugins/kindeditor-4.1.10/kindeditor-all-min.js',
            '/static/plugins/kindeditor-4.1.10/lang/zh_CN.js',
            '/static/plugins/kindeditor-4.1.10/config.js',
        )


# 工作机会
@admin.register(models.ChinJobRecruit)
class ChinJobRecruitAdmin(admin.ModelAdmin):
    # exclude = ('job_require', 'skill_require', )
    list_display = ('job_name', 'work_year', 'education', 'work_prop', 'profile', 'sort', 'is_enable')
    list_display_links = ('job_name', 'profile', )
    list_editable = ('education', 'work_prop', 'sort', 'is_enable')
    list_filter = ('education', 'work_prop', IsEnableFilter, 'create_time',)
    list_per_page = 30
    search_fields = ('job_name', 'work_year', )
    exclude = ('create_uid', 'create_username', 'create_time', 'operate_uid', 'operate_username', )

    class Media:
        js = (
            '/static/plugins/kindeditor-4.1.10/kindeditor-all-min.js',
            '/static/plugins/kindeditor-4.1.10/lang/zh_CN.js',
            '/static/plugins/kindeditor-4.1.10/config.js',
        )


# 社会责任
# 新闻资讯
@admin.register(models.ChinNews)
class ChinNewsAdmin(admin.ModelAdmin):
    # exclude = ('content', )
    list_display = ('title', 'brief', 'profile', 'read_count', 'cover_image_url', 'type', 'sort', 'is_enable', )
    list_display_links = ('title', 'profile')
    list_editable = ('brief', 'sort', 'read_count', 'type', 'is_enable', )
    list_filter = ('type', IsEnableFilter, )
    list_per_page = 30
    search_fields = ('title', 'brief',)
    exclude = ('create_uid', 'create_username', 'create_time', 'operate_uid', 'operate_username', )

    class Media:
        js = (
            '/static/plugins/kindeditor-4.1.10/kindeditor-all-min.js',
            '/static/plugins/kindeditor-4.1.10/lang/zh_CN.js',
            '/static/plugins/kindeditor-4.1.10/config.js',
        )


# 用户抢购优惠券表
@admin.register(models.ChinApplyRecord)
class ChinApplyRecordAdmin(admin.ModelAdmin):
    list_display = ('name', 'sex', 'birthday', 'phone', 'email', 'is_get', 'is_inform', 'state', 'sort', 'create_time')
    list_display_links = ('name', )
    list_editable = ('is_get', 'is_inform', 'state', 'sort', )
    list_filter = (IsGetFilter, IsInformFilter, 'state')
    list_per_page = 30
    search_fields = ('name', 'sex', 'phone', 'email', )
    exclude = ('create_uid', 'create_username', 'create_time', 'operate_uid', 'operate_username', )

    # 屏蔽增加功能按钮
    def has_add_permission(self, request):
        return False

    # 屏蔽删除功能按钮
    def has_delete_permission(self, request, obj=None):
        return False

    # def get_list_filter(self, request):
    #     return [('1', '是'), ('0', '否')]


# 用户浇水记录
@admin.register(models.ChinUserWateringRecord)
class ChinUserWateringRecordAdmin(admin.ModelAdmin):
    list_display = ('client_ip', 'client_host', 'client_port', 'profile', 'server_ip', 'server_host', 'server_port',
                    'init_amount', 'amount', 'final_amount', 'create_time')
    list_filter = ('client_ip', 'create_time')
    list_per_page = 30
    search_fields = ('client_ip', 'client_host', 'client_port', 'client_user_agent', 'server_ip', 'server_host', 'server_port', )
    exclude = ('create_uid', 'create_username', 'create_time', 'operate_uid', 'operate_username', )

    # 屏蔽增加功能按钮
    def has_add_permission(self, request):
        return False

    # 屏蔽删除功能按钮
    def has_delete_permission(self, request, obj=None):
        return False

    # 屏蔽修改功能按钮
    def has_change_permission(self, request, obj=None):
        return False


# 浇水量余额表
@admin.register(models.ChinWateringQty)
class ChinWateringQtyAdmin(admin.ModelAdmin):
    list_display = ('amount', 'total_amount', 'operate_time')
    list_display_links = ('amount', 'total_amount', )
    exclude = ('create_uid', 'create_username', 'create_time', 'operate_uid', 'operate_username', )

    # 屏蔽增加功能按钮
    def has_add_permission(self, request):
        return True

    # 屏蔽删除功能按钮
    def has_delete_permission(self, request, obj=None):
        return False


# 申请模板表
@admin.register(models.ChinTableTemplate)
class ChinTableTemplateAdmin(admin.ModelAdmin):
    list_display = ('name', 'profile', 'is_enable', 'operate_time')
    list_display_links = ('name', 'profile', )
    list_editable = ('is_enable', )
    list_filter = (IsEnableFilter, )
    list_per_page = 30
    search_fields = ('name', 'is_enable',)
    exclude = ('create_uid', 'create_username', 'create_time', 'operate_uid', 'operate_username',)


# 问题列表
@admin.register(models.ChinQuestion)
class ChinQuestionAdmin(admin.ModelAdmin):
    list_display = ('name', 'profile', 'type', 'state', 'operate_time')
    list_display_links = ('name', 'profile', )
    list_editable = ('type', 'state', )
    list_filter = ('type', 'state', )
    list_per_page = 30
    search_fields = ('name', 'type', 'state')
    exclude = ('create_uid', 'create_username', 'create_time', 'operate_uid', 'operate_username',)

    class Media:
        js = (
            '/static/plugins/kindeditor-4.1.10/kindeditor-all-min.js',
            '/static/plugins/kindeditor-4.1.10/lang/zh_CN.js',
            '/static/plugins/kindeditor-4.1.10/config.js',
        )
