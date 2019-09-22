from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import AbstractUser, PermissionsMixin, BaseUserManager, AbstractBaseUser
# from django.core.validators import RegexValidator
from django.template.defaultfilters import slugify
# from datetime import datetime
from django.db.models import BooleanField as _BooleanField
# import pytz
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class BooleanField(_BooleanField):
    def get_prep_value(self, value):
        if value in (0, '0', 'false', 'False'):
            return False
        elif value in (1, '1', 'true', 'True'):
            return True
        else:
            return super(BooleanField, self).get_prep_value(value)


# 用户,继承方式扩展
# class UserManager(BaseUserManager):
#     def create_user(self, username, email, password=None):
#         if not email:
#             raise ValueError('Users must have an email address')
#
#         if not username:
#             raise ValueError('Users must hanve a username')
#
#         user = self.model(
#             username = username,
#             email = self.normalize_email(email)
#         )
#         user.is_active = True
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_superuser(self, username, email, password=None):
#         user = self.create_user(username=username, email=email, password=password)
#
#         user.is_staff = True
#         user.is_superuser = True
#         user.save(using=self._db)
#         return user
#
# class UserProfile(AbstractBaseUser, PermissionsMixin):
#     alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', message='Only alphanumeric characters are allowed.')
#     username = models.CharField('用户名', unique=True, max_length=30, validators=[alphanumeric])
#     email = models.EmailField('邮箱', unique=True, max_length=200)
#     first_name = models.CharField(max_length=30, null=True, blank=True)
#     last_name = models.CharField(max_length=50, null=True, blank=True)
#     is_active = models.BooleanField(default=True, null=False)
#     is_staff = models.BooleanField(default=False, null=False)
#
#     avatar = models.ImageField(upload_to='avatar/%Y.%m', default='avatar/default.png', max_length=200, blank=False,
#                                null=False)
#     objects = UserManager()
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username']
#
#     class Meta:
#         verbose_name = '用户信息'
#         verbose_name_plural = verbose_name
#         ordering = ['-id']
#
#     def get_full_name(self):
#         self.fullname = self.first_name + " " + self.last_name
#         return self.fullname
#
#     def get_short_name(self):
#         return self.username
#
#     def __str__(self):
#         return self.email


# AbstractBaseUser中只含有3个field: password, last_login和is_active.
# 如果你对django user model默认的first_name, last_name不满意,
# 或者只想保留默认的密码储存方式, 则可以选择这一方式.
class ChinUserProfile(AbstractUser):
    avatar = models.ImageField(upload_to='avatar/%Y/%m', default='avatar/default.png', max_length=200,
                               verbose_name=_('用户头像'))
    qq = models.CharField(max_length=20, blank=True, null=True, verbose_name='QQ')
    phone = models.CharField(max_length=11, blank=True, null=True, unique=True, verbose_name=_('手机号'))
    nick_name = models.CharField(max_length=30, verbose_name=_('昵称'))

    # is_lock = models.BooleanField(default=False, verbose_name='是否锁定', choices=((0, '否'), (1, '是')))
    # is_enable = models.BooleanField(default=True, verbose_name='是否启用', choices=((0, '否'), (1, '是')))

    class Meta(AbstractUser.Meta):
        db_table = 'chf_userprofile'
        swappable = 'AUTH_USER_MODEL'
        verbose_name = _('用户')
        verbose_name_plural = verbose_name
        ordering = ['-id']

    # class Meta:
    #     db_table = 'chf_userprofile'
    #     verbose_name = '用户'
    #     verbose_name_plural = verbose_name
    #     ordering = ['-id']

    def __str__(self):
        return self.username

    # def create_user(self, username, nickname, password=None):
    #     # create user here
    #     pass
    #
    # def create_superuser(self, username, password):
    #     # create superuser here
    #     pass


# class ChinUserProfileBase(AbstractBaseUser):
#     identifier = models.CharField(max_length=50, unique=True)
#     nickname = models.CharField(max_length=10, unique=True)
#     data_of_birth = models.DateField()
#     height = models.FloatField()
#     is_active = models.BooleanField(default=True)
#
#     USERNAME_FIELD = 'identifier'
#     REQUIRED_FIELDS = ['date_of_birth', 'height']
#
#     def get_full_name(self):
#         return self.identifier
#
#     def get_short_name(self):
#         return self.nickname

class BaseModel(models.Model):
    # default=datetime.now().replace(tzinfo=pytz.utc)
    create_time = models.DateTimeField(_('创建时间'), auto_now_add=True)
    create_uid = models.IntegerField(_('创建人ID'), default=123456789, auto_created=True)
    create_username = models.CharField(_('创建人名称'), max_length=30, default='admin', auto_created=True)
    operate_time = models.DateTimeField(_('操作时间'), auto_now=True)
    operate_uid = models.IntegerField(_('操作人ID'), default=123456789, auto_created=True)
    operate_username = models.CharField(_('操作人名称'), max_length=30, default='admin', auto_created=True)

    class Meta:
        abstract = True


# 系统相关
# class SysSetting(BaseModel):
#
#     class Meta:
#         db_table = 'sys_setting'
#         verbose_name = '系统相关'
#         verbose_name_plural = verbose_name


# 系统|站点配置
class SysConfig(BaseModel):
    site_name = models.CharField(_('站点名称'), max_length=50, default='', blank=True)
    site_desc = models.CharField(_('站点描述'), max_length=150, default='', blank=True)
    site_author = models.CharField(_('作者'), max_length=100, default='', blank=True)
    site_company = models.CharField(_('公司'), max_length=100)
    address = models.CharField(_('底部显示地址'), max_length=150)
    telephone = models.CharField(_('底部显示电话'), max_length=15)
    email = models.EmailField(_('邮箱'), max_length=50, default='', blank=True)
    icp = models.CharField(_('备案号'), max_length=15, default='', blank=True)
    remark = models.CharField(_('备注'), max_length=200, default='', blank=True)
    logo_bottom = models.ImageField(_('底部logo'), default='', null=True, blank=True, upload_to='sys/%Y/%m')
    qrcode = models.ImageField(_('二维码'), default='', null=True, blank=True, upload_to='sys/%Y/%m')
    is_enable = models.BooleanField(_('是否启用'), default=True)

    class Meta:
        db_table = "sys_config"
        verbose_name = _('站点配置')
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.site_name


# 导航菜单管理
class SysNav(BaseModel):
    code = models.CharField(_('标识'), max_length=20, default='')
    name = models.CharField(_('名称(中文)'), max_length=50, default='', blank=True, null=True,)
    en_name = models.CharField(_('名称(英文)'), max_length=100, default='', blank=True, null=True,)
    url = models.CharField(_('链接'), max_length=200)
    remark = models.CharField(_('描述'), max_length=300, blank=True)
    parent = models.ForeignKey(to='self', default=0, null=True, blank=True, related_name='children',
                               verbose_name=_('父级'), limit_choices_to={'is_delete': False, 'is_root': True},
                               on_delete=models.CASCADE)
    is_root = models.BooleanField(_('是否一级菜单'), default=True)
    is_delete = models.BooleanField(_('是否删除'), default=False)
    sort = models.IntegerField(_('排序'), default=0)
    is_enable = models.BooleanField(_('是否启用'), default=True)

    class Meta:
        db_table = "sys_nav"
        ordering = ['sort', '-create_time']
        verbose_name = _('导航菜单管理')
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# # 广告位
# class SysAdPosition(BaseModel):
#     name = models.CharField('广告位名称', max_length=50)
#     target_type = models.CharField('广告位类型', max_length=20)
#     width = models.IntegerField("广告位宽度", default=0)
#     is_enable = models.BooleanField('是否启用', default=True)
#
#     class Meta:
#         db_table = "sys_adposition"
#         ordering = ['-create_time']
#         verbose_name = '广告位'
#         verbose_name_plural = 'SysAdPositions'
#
#     def __str__(self):
#         return self.name
#
# # 广告记录
# class SysAdRecord(BaseModel):
#     name = models.CharField('广告名称', max_length=30)
#     slug = models.SlugField('Slug', max_length=255, unique=True, null=True, blank=True,
#                             help_text='根据name生成的，用于生成页面URL，必须唯一')
#     path = models.CharField('广告图片路径', max_length=200)
#     image = models.ImageField('广告图片', max_length=255, null=True, blank=True, upload_to='ad/%Y/%m')
#     is_enable = models.BooleanField('是否启用', default=True)
#     sort = models.IntegerField('排序', default=0)
#     adposition = models.ForeignKey(to='SysAdPosition', to_field='id')
#
#     class Meta:
#         db_table = 'sys_adrecord'
#         ordering = ['sort', '-create_time']
#         verbose_name = '广告记录'
#         verbose_name_plural = 'SysAdRecords'
#
#     def __str__(self):
#         return self.name
#
#     def get_absolute_url(self):
#         return reverse('sys_adrecord', args=(self.slug, ))


# banner图管理
class ChinBanner(BaseModel):
    """
    nav:
    """
    nav = models.ForeignKey(to='SysNav', default='', null=True, blank=True, related_name='navs',
                            related_query_name='nav_query', on_delete=models.CASCADE, verbose_name=_('Banner页面'))
    image_url = models.ImageField(_('图片'), default='', null=True, blank=True, upload_to='banner/%Y/%m')
    text = models.CharField(_('Banner上文本描述(中文)'), max_length=150, default='')
    en_text = models.CharField(_('Banner上文本描述(英文)'), max_length=300, default='')
    sort = models.IntegerField(_('排序'), default=0)
    is_enable = models.BooleanField(_('是否启用'), default=True)

    class Meta:
        db_table = 'chin_banner'
        ordering = ['nav', 'sort', '-create_time']
        verbose_name = _('Banner管理')
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.nav.name


# 品牌介绍图片资源
class ChinAboutResource(BaseModel):
    """
    type_code: 1 企业文化 2 品牌荣誉 3 企业资质 4 团队风采 5 品牌故事 6 组织架构
    """
    type_code = models.PositiveSmallIntegerField(_('图片业务类型'), default=0,
                                                 choices=(
                                                     (1, _('企业文化')),
                                                     (2, _('品牌荣誉')),
                                                     (3, _('企业资质')),
                                                     (4, _('团队风采')),
                                                     (5, _('品牌故事')),
                                                     (6, _('组织架构'))
                                                 )
                                                 )
    # type_name = models.CharField('图片业务类型名称', max_length=15, default='')
    image_url = models.ImageField(_('图片'), default='', null=True, blank=True, upload_to='company/%Y/%m')
    about = models.ForeignKey(to='ChinAbout', default='', null=True, blank=True, related_name='about_resource',
                              related_query_name='about', on_delete=models.CASCADE, verbose_name=_('品牌介绍'))
    sort = models.IntegerField(_('排序'), default=0)
    is_enable = models.BooleanField(_('是否启用'), default=True)

    class Meta:
        db_table = 'chin_aboutresource'
        ordering = ['sort', '-create_time']
        verbose_name = _('品牌介绍图片资源')
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.type_code)


# 关于我们
# 品牌介绍
class ChinAbout(BaseModel):
    comp_name = models.CharField(_('公司名称(中文)'), max_length=100, default='', blank=True, null=True,)
    en_comp_name = models.CharField(_('公司名称(英文)'), max_length=200, default='', blank=True, null=True,)
    slug = models.SlugField('Slug', max_length=255, unique=True, null=True, blank=True,
                            help_text=_('根据name生成的，用于生成页面URL，必须唯一'))
    title = models.CharField(_('公司简介标题(中文)'), max_length=100, default='', blank=True, null=True,)
    en_title = models.CharField(_('公司简介标题(英文)'), max_length=200, default='', blank=True, null=True,)
    content = models.TextField(_('公司简介(中文)'), default='', null=True, blank=True)
    en_content = models.TextField(_('公司简介(英文)'), default='', null=True, blank=True)
    comp_image = models.ImageField(_('公司简介图片'), max_length=255, null=True, blank=True, upload_to='company/%Y/%m')
    is_enable = models.BooleanField(_('是否启用'), default=True)

    class Meta:
        db_table = 'chin_about'
        verbose_name = _('品牌介绍')
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.comp_name

    def get_absolute_url(self):
        return reverse('about', args=(self.slug,))

    def profile(self):
        if len(str(self.content)) > 40:
            return '{}...'.format(str(self.content)[0:40])
        else:
            return str(self.content)

    profile.allow_tags = True
    profile.short_description = _('公司简介(中文)')

    def en_profile(self):
        if len(str(self.en_content)) > 40:
            return '{}...'.format(str(self.en_content)[0:40])
        else:
            return str(self.en_content)

    en_profile.allow_tags = True
    en_profile.short_description = _('公司简介(英文)')


# 秦始皇故事
class ChinStory(BaseModel):
    short_title = models.CharField(_('短板故事标题(中文)'), max_length=80, default='', blank=True, null=True,)
    en_short_title = models.CharField(_('短板故事标题(英文)'), max_length=160, default='', blank=True, null=True,)
    short_content = models.TextField(_('短板故事(中文)'), max_length=1000, default='', blank=True, null=True,)
    en_short_content = models.TextField(_('短板故事(英文)'), max_length=2000, default='', blank=True, null=True,)
    long_title = models.CharField(_('长板故事标题(中文)'), max_length=80, default='', blank=True, null=True,)
    en_long_title = models.CharField(_('长板故事标题(英文)'), max_length=160, default='', blank=True, null=True,)
    long_content = models.TextField(_('长板故事(中文)'), max_length=4000, default='', blank=True, null=True,)
    en_long_content = models.TextField(_('长板故事(英文)'), max_length=8000, default='', blank=True, null=True,)
    is_enable = models.BooleanField(_('是否启用'), default=True)

    class Meta:
        db_table = 'chin_story'
        ordering = ['-create_time']
        verbose_name = _('秦始皇故事')
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.short_title

    def short_profile(self):
        if len(str(self.short_content)) > 20:
            return '{}...'.format(str(self.short_content)[0:20])
        else:
            return str(self.short_content)

    short_profile.allow_tags = True
    short_profile.short_description = _('短板描述(中文)')

    def en_short_profile(self):
        if len(str(self.en_short_content)) > 20:
            return '{}...'.format(str(self.en_short_content)[0:20])
        else:
            return str(self.en_short_content)

    en_short_profile.allow_tags = True
    en_short_profile.short_description = _('短板描述(英文)')

    def long_profile(self):
        if len(str(self.long_content)) > 50:
            return '{}...'.format(str(self.long_content)[0:50])
        else:
            return str(self.long_content)

    long_profile.allow_tags = True
    long_profile.short_description = _('长板描述(中文)')

    def en_long_profile(self):
        if len(str(self.en_long_content)) > 50:
            return '{}...'.format(str(self.en_long_content)[0:50])
        else:
            return str(self.en_long_content)

    en_long_profile.allow_tags = True
    en_long_profile.short_description = _('长板描述(英文)')


# 动画类型
class ChinAnimateType(BaseModel):
    name = models.CharField(_('动画名称'), max_length=30, default='')
    class_name = models.CharField(_('class样式名'), max_length=50, default='flip')
    descr = models.CharField(_('动画描述'), max_length=100, default='', null=True, blank=True)
    is_enable = models.BooleanField(_('是否启用'), default=True)

    class Meta:
        db_table = 'chin_animatetype'
        ordering = ['-create_time']
        verbose_name = _('动画类型')
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def profile(self):
        if len(str(self.descr)) > 50:
            return '{}...'.format(str(self.descr)[0:50])
        else:
            return str(self.descr)

    profile.allow_tags = True
    profile.short_description = _('动画描述')


# 首页板块管理
class ChinIndexPlate(BaseModel):
    title = models.CharField(_('板块标题(中文)'), max_length=8, default='', blank=True, null=True,)
    en_title = models.CharField(_('板块标题(英文)'), max_length=16, default='', blank=True, null=True,)
    plate_image_url = models.ImageField(_('图标'), max_length=255, null=True, blank=True, upload_to='index_plate/%Y/%m')
    front_image = models.ImageField(_('正面图'), max_length=255, null=True, blank=True, upload_to='index_plate/%Y/%m')
    back_image = models.ImageField(_('背面图'), max_length=255, null=True, blank=True, upload_to='index_plate/%Y/%m')
    descr = models.CharField(_('简介(中文)'), max_length=100, default='', null=True, blank=True)
    en_descr = models.CharField(_('简介(英文)'), max_length=100, default='', null=True, blank=True)
    is_redirect_sub_page = models.BooleanField(_('是否跳转到子页面'), default=True)
    sub_page_url = models.CharField(_('子页面地址'), max_length=150, default='', null=True, blank=True)
    video_source = models.FileField(_('视频文件地址'), max_length=200, default='', null=True, blank=True,
                                    upload_to='media/%Y/%m')
    animate_type = models.ForeignKey(to='ChinAnimateType', null=True, blank=True, on_delete=models.CASCADE,
                                     verbose_name=_('动画类型'))
    sort = models.IntegerField(_('排序'), default=0)
    is_enable = models.BooleanField(_('是否启用'), default=True)

    class Meta:
        db_table = 'chin_indexplate'
        ordering = ['sort', '-create_time']
        verbose_name = _('首页板块')
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

    def profile(self):
        if len(str(self.descr)) > 5:
            return '{}...'.format(str(self.descr)[0:5])
        else:
            return str(self.descr)

    profile.allow_tags = True
    profile.short_description = _('简介(中文)')

    def en_profile(self):
        if len(str(self.en_descr)) > 5:
            return '{}...'.format(str(self.en_descr)[0:5])
        else:
            return str(self.en_descr)

    en_profile.allow_tags = True
    en_profile.short_description = _('简介(英文)')


# 公司发展历程
class ChinCompanyHistory(BaseModel):
    timeline_title = models.CharField(_('时间标题(中文)'), max_length=20, default='', unique=True, null=True, blank=True)
    en_timeline_title = models.CharField(_('时间标题(英文)'), max_length=40, default='', unique=True, null=True, blank=True)
    title = models.CharField(_('标题(中文)'), max_length=100, default='', blank=True, null=True,)
    en_title = models.CharField(_('标题(英文)'), max_length=200, default='', blank=True, null=True,)
    breif = models.CharField(_('摘要(中文)'), max_length=50, default='', null=True, blank=True)
    en_breif = models.CharField(_('摘要(英文)'), max_length=100, default='', null=True, blank=True)
    content = models.TextField(_('描述(中文)'), default='', null=True, blank=True)
    en_content = models.TextField(_('描述(英文)'), default='', null=True, blank=True)
    cover_image_url = models.ImageField(_('图片'), max_length=255, null=True, blank=True, upload_to='company/%Y/%m')
    sort = models.IntegerField(_('排序'), default=0)
    is_enable = models.BooleanField(_('是否启用'), default=True)

    class Meta:
        db_table = 'chin_companyhistory'
        ordering = ['sort', '-create_time']
        verbose_name = _('发展历程')
        verbose_name_plural = verbose_name  # 后台管理站点显示的Model名称
        # verbose_name_plural = 'ChinCompanyHistories'

    def __str__(self):
        return self.title

    def profile(self):
        if len(str(self.content)) > 20:
            return '{}...'.format(str(self.content)[0:20])
        else:
            return str(self.content)

    profile.allow_tags = True
    profile.short_description = _('描述')

    def en_profile(self):
        if len(str(self.en_content)) > 20:
            return '{}...'.format(str(self.en_content)[0:20])
        else:
            return str(self.en_content)

    en_profile.allow_tags = True
    en_profile.short_description = _('描述')


# 产品类型
class ChinProductType(BaseModel):
    name = models.CharField(_('类型名称(中文)'), max_length=30, default='', blank=True, null=True,)
    en_name = models.CharField(_('类型名称(英文)'), max_length=30, default='', blank=True, null=True,)
    sort = models.IntegerField(_('排序'), default=0)
    is_enable = models.BooleanField(_('是否启用'), default=True)
    data_filter_name = models.CharField(_('数据类型标识'), max_length=20, default='*')

    class Meta:
        db_table = 'chin_producttype'
        ordering = ['sort', '-create_time']
        verbose_name = _('产品类型')
        # verbose_name_plural = 'ChinProductTypes'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 品牌产品
class ChinProduct(BaseModel):
    name = models.CharField(_('产品名称(中文)'), max_length=100, default='', blank=True, null=True,)
    en_name = models.CharField(_('产品名称(英文)'), max_length=200, default='', blank=True, null=True,)
    slug = models.SlugField('Slug', max_length=255, unique=True, null=True, blank=True,
                            help_text=_('根据name生成的，用于生成页面URL，必须唯一'))
    brief = models.CharField(_('产品摘要(中文)'), max_length=40, default='', blank=True, null=True,)
    en_brief = models.CharField(_('产品摘要(英文)'), max_length=80, default='', blank=True, null=True,)
    content = models.TextField(_('产品描述(中文)'), default='', null=True, blank=True)
    en_content = models.TextField(_('产品描述(英文)'), default='', null=True, blank=True)
    mall_url = models.URLField(_('在线商城地址'), default='', null=True, blank=True)
    cover_image_url = models.ImageField(_('图片'), max_length=255, null=True, blank=True, upload_to='product/%Y/%m')
    read_count = models.IntegerField(_('浏览量'), default=0)
    product_type = models.ForeignKey(to='ChinProductType', null=True, blank=True, on_delete=models.CASCADE,
                                     verbose_name=_('产品类型'))
    sort = models.IntegerField(_('排序'), default=0)
    is_recommand = models.BooleanField(_('是否推荐'), default=True)
    is_enable = models.BooleanField(_('是否启用'), default=True)

    class Meta:
        db_table = 'chin_product'
        ordering = ['sort', '-create_time']
        verbose_name = _('品牌产品')
        # verbose_name_plural = 'ChinProducts'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def get_absolute_url(self, *args, **kwargs):
        # return reverse('product', args=(self.slug, ))
        self.slug = slugify(self.name)
        super(ChinProduct, self).get_absolute_url(*args, **kwargs)

    def brief_profile(self):
        if len(str(self.brief)) > 10:
            return '{}...'.format(str(self.brief)[0:10])
        else:
            return str(self.brief)

    brief_profile.allow_tags = True
    brief_profile.short_description = _('产品简介(中文)')

    def en_brief_profile(self):
        if len(str(self.en_brief)) > 10:
            return '{}...'.format(str(self.en_brief)[0:10])
        else:
            return str(self.en_brief)

    en_brief_profile.allow_tags = True
    en_brief_profile.short_description = _('产品简介(英文)')

    def profile(self):
        if len(str(self.content)) > 40:
            return '{}...'.format(str(self.content)[0:40])
        else:
            return str(self.content)

    profile.allow_tags = True
    profile.short_description = _('产品描述(中文)')

    def en_profile(self):
        if len(str(self.en_content)) > 40:
            return '{}...'.format(str(self.en_content)[0:40])
        else:
            return str(self.en_content)

    en_profile.allow_tags = True
    en_profile.short_description = _('产品描述(英文)')


# 合作伙伴
class ChinPartner(BaseModel):
    name = models.CharField(_('名称(中文)'), max_length=100, default='', blank=True, null=True,)
    en_name = models.CharField(_('名称(英文)'), max_length=200, default='', blank=True, null=True,)
    logo = models.ImageField(_('Logo'), max_length=255, null=True, blank=True, upload_to='partner/%Y/%m')
    brief = models.CharField(_('简介(中文)'), max_length=100, default='', blank=True, null=True,)
    en_brief = models.CharField(_('简介(英文)'), max_length=200, default='', blank=True, null=True,)
    url = models.URLField(_('链接'), max_length=255, null=True, blank=True)
    address = models.CharField(_('地址'), max_length=100)
    sort = models.IntegerField(_('排序'), default=0)
    is_enable = models.BooleanField(_('是否启用'), default=True)

    class Meta:
        db_table = 'chin_partner'
        ordering = ['sort', '-create_time']
        verbose_name = _('合作伙伴')
        # verbose_name_plural = 'ChinPartners'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def profile(self):
        if len(str(self.brief)) > 20:
            return '{}...'.format(str(self.brief)[0:20])
        else:
            return str(self.brief)

    profile.allow_tags = True
    profile.short_description = _('简介(中文)')

    def en_profile(self):
        if len(str(self.en_brief)) > 20:
            return '{}...'.format(str(self.en_brief)[0:20])
        else:
            return str(self.en_brief)

    en_profile.allow_tags = True
    en_profile.short_description = _('简介(英文)')


# 合作共赢 品牌合作
class ChinCooperation(BaseModel):
    title = models.CharField(_('名称(中文)'), max_length=100, default='', blank=True, null=True,)
    en_title = models.CharField(_('名称(英文)'), max_length=200, default='', blank=True, null=True,)
    content = models.TextField(_('内容(中文)'), default='', null=True, blank=True)
    en_content = models.TextField(_('内容(英文)'), default='', null=True, blank=True)
    type = models.CharField(
        _('类型'),
        max_length=10,
        choices=(
            ('0', _('合作政策')),
            ('1', _('项目优势')),
            ('2', _('经销商问答')),
            ('3', _('支持与服务'))
        ),
        default=0
    )
    sort = models.IntegerField(_('排序'), default=0)
    is_enable = models.BooleanField(_('是否启用'), default=True)

    class Meta:
        db_table = 'chin_cooperation'
        ordering = ['sort', '-create_time']
        verbose_name = _('合作共赢')
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

    def profile(self):
        if len(str(self.content)) > 30:
            return '{}...'.format(str(self.content)[0:30])
        else:
            return str(self.content)

    profile.allow_tags = True
    profile.short_description = _('内容(中文)')

    def en_profile(self):
        if len(str(self.en_content)) > 30:
            return '{}...'.format(str(self.en_content)[0:30])
        else:
            return str(self.en_content)

    en_profile.allow_tags = True
    en_profile.short_description = _('内容(英文)')


# 社会责任
# 新闻资讯
class ChinNews(BaseModel):
    title = models.CharField(_('标题(中文)'), max_length=64, default='', blank=True, null=True,)
    en_title = models.CharField(_('标题(英文)'), max_length=128, default='', blank=True, null=True,)
    slug = models.SlugField('Slug', max_length=255, unique=True, null=True, blank=True,
                            help_text=_('根据title生成的，用于生成页面URL，必须唯一'))
    brief = models.CharField(_('摘要(中文)'), max_length=120, default='', blank=True, null=True,)
    en_brief = models.CharField(_('摘要(英文)'), max_length=240, default='', blank=True, null=True,)
    content = models.TextField(_('内容(中文)'), default='', null=True, blank=True)
    en_content = models.TextField(_('内容(英文)'), default='', null=True, blank=True)
    read_count = models.IntegerField(_('浏览量'), default=0)
    cover_image_url = models.ImageField(_('图片'), max_length=255, null=True, blank=True, upload_to='news/%Y/%m')
    sort = models.IntegerField(_('排序'), default=0)
    type = models.CharField(
        _('类型'),
        max_length=10,
        choices=(
            ('0', _('新闻资讯')),
            ('1', _('社会责任'))
        ),
        default=0
    )
    is_enable = models.BooleanField(_('是否启用'), default=True)

    class Meta:
        db_table = 'chin_news'
        ordering = ['sort', '-create_time']
        verbose_name = _('新闻资讯|社会责任')
        # verbose_name_plural = 'ChinProducts'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('news', args=(self.slug, ))

    def get_absolute_url(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(ChinNews, self).get_absolute_url(*args, **kwargs)

    def profile(self):
        if len(str(self.content)) > 20:
            return '{}...'.format(str(self.content)[0:20])
        else:
            return str(self.content)

    profile.allow_tags = True
    profile.short_description = _('内容(中文)')

    def en_profile(self):
        if len(str(self.en_content)) > 20:
            return '{}...'.format(str(self.en_content)[0:20])
        else:
            return str(self.en_content)

    en_profile.allow_tags = True
    en_profile.short_description = _('内容(英文)')


# 工作机会
class ChinJobRecruit(BaseModel):
    job_name = models.CharField(_('职位名称(中文)'), max_length=50, default='', blank=True, null=True,)
    en_job_name = models.CharField(_('职位名称(英文)'), max_length=100, default='', blank=True, null=True,)
    slug = models.SlugField('Slug', max_length=255, unique=True, null=True, blank=True,
                            help_text=_('根据job_name生成的，用于生成页面URL，必须唯一'))
    work_year = models.CharField(_('工作经验'), max_length=20, default='', null=True, blank=True)
    education = models.CharField(
        _('学历'),
        max_length=10,
        choices=(
            ('0', _('请选择')),
            ('1', _('博士导师')),
            ('2', _('博士后')),
            ('3', _('博士')),
            ('4', _('硕士')),
            ('5', _('研究生')),
            ('6', _('本科')),
            ('7', _('大专')),
            ('8', _('高中')),
            ('9', _('初中')),
            ('10', _('小学')),
            ('11', _('其他')),
        ),
        default=0
    )
    work_prop = models.CharField(
        _('工作性质'),
        max_length=5,
        choices=(
            ('0', _('全职')),
            ('1', _('兼职')),
            ('2', _('自由职业')),
            ('3', _('其他')),
        ),
        default=0
    )
    # job_require = models.TextField('岗位要求', default='', null=True, blank=True)
    # skill_require = models.TextField('技能要求', default='', null=True, blank=True)
    content = models.TextField(_('招聘要求(中文)'), default='', null=True, blank=True)
    en_content = models.TextField(_('招聘要求(英文)'), default='', null=True, blank=True)
    sort = models.IntegerField(_('排序'), default=0)
    is_enable = models.BooleanField(_('是否启用'), default=True)

    class Meta:
        db_table = 'chin_jobrecruit'
        ordering = ['sort', '-create_time']
        verbose_name = _('工作机会')
        # verbose_name_plural = 'ChinJobRecruits'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.job_name

    # def get_absolute_url(self):
    #     return reverse('jobrecruit', args=(self.slug, ))

    def get_absolute_url(self, *args, **kwargs):
        self.slug = slugify(self.job_name)
        super(ChinJobRecruit, self).get_absolute_url(*args, **kwargs)

    def profile(self):
        if len(str(self.content)) > 80:
            return '{}...'.format(str(self.content)[0:80])
        else:
            return str(self.content)

    # 如何将一个TextField字段设为safe
    profile.allow_tags = True
    profile.short_description = _('招聘要求(中文)')

    def en_profile(self):
        if len(str(self.en_content)) > 80:
            return '{}...'.format(str(self.en_content)[0:80])
        else:
            return str(self.en_content)

    # 如何将一个TextField字段设为safe
    en_profile.allow_tags = True
    en_profile.short_description = _('招聘要求(英文)')


# 用户抢购优惠券表
class ChinApplyRecord(BaseModel):
    name = models.CharField(_('姓名'), max_length=100, default='', null=True, blank=True)
    sex = models.CharField(
        _('性别'),
        max_length=5,
        choices=(
            ('0', _('男')),
            ('1', _('女')),
            ('2', _('保密')),
            ('3', _('未知')),
        ),
        default=0
    )
    birthday = models.DateField(_('生日'), default='', null=True, blank=True)
    phone = models.CharField(_('电话'), max_length=11)
    email = models.EmailField(_('邮箱'), max_length=50, default='', null=True, blank=True)
    is_get = models.BooleanField(_('是否已领取'), default=False)
    is_inform = models.BooleanField(_('是否已通知'), default=False)
    state = models.SmallIntegerField(
        _('是否中奖'), default=0,
        choices=(
            (0, _('未中奖')),
            (1, _('中奖')),
        )
    )
    sort = models.IntegerField(_('排序'), default=1)

    class Meta:
        db_table = "chin_applyrecord"
        ordering = ['sort', '-create_time']
        verbose_name = _('用户抢券记录')
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 用户浇水记录
class ChinUserWateringRecord(BaseModel):
    client_ip = models.GenericIPAddressField(_('客户端IP'), default='127.0.0.1', protocol='both')
    client_host = models.CharField(_('客户端主机名'), default='', max_length=100)
    client_port = models.IntegerField(_('客户端端口'), default=0)
    client_user_agent = models.CharField(_('客户端浏览器'), default='', max_length=255)
    server_ip = models.GenericIPAddressField(_('服务器IP'), default='127.0.0.1', protocol='both')
    server_host = models.CharField(_('服务器主机名'), default='', max_length=100)
    server_port = models.IntegerField(_('服务器端口'), default=0)
    init_amount = models.IntegerField(_('期初水量'), default=0)
    amount = models.IntegerField(_('本次水量'), default=0)
    final_amount = models.IntegerField(_('期末水量'), default=0)

    class Meta:
        db_table = "chin_userwateringrecord"
        ordering = ['-create_time']
        verbose_name = _('用户浇水记录')
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.client_ip

    def profile(self):
        if len(str(self.client_user_agent)) > 60:
            return '{}...'.format(str(self.client_user_agent)[0:60])
        else:
            return str(self.client_user_agent)

    profile.allow_tags = True
    profile.short_description = _('客户端浏览器')


# 浇水量余额表
class ChinWateringQty(BaseModel):
    amount = models.IntegerField(_('水量余额'), default=0)
    total_amount = models.IntegerField(_('浇水总量'), default=0)

    class Meta:
        db_table = "chin_wateringqty"
        ordering = ['-create_time']
        verbose_name = _('浇水量余额表')
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.amount)


# 申请模板表
class ChinTableTemplate(BaseModel):
    name = models.CharField(_('名称'), max_length=30, default='')
    file = models.FileField(_('文件'), max_length=255, upload_to='file/%Y/%m')
    is_enable = models.BooleanField(_('是否启用'), default=True)

    class Meta:
        db_table = 'chin_tabletemplate'
        ordering = ['-create_time']
        verbose_name = _('申请表格')
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def profile(self):
        if len(str(self.file)) > 20:
            return '{}...'.format(str(self.file)[0:20])
        else:
            return str(self.file)

    profile.allow_tags = True
    profile.short_description = _('文件')


# 问题汇总列表
class ChinQuestion(BaseModel):
    name = models.CharField(_('问题标题'), max_length=200)
    content = models.TextField(_('问题描述'), default='', null=True, blank=True)
    type = models.SmallIntegerField(
        _('问题类型'),
        default=-1,
        choices=(
            (-1, _('不是问题')),
            (0, _('浏览器问题')),
            (1, _('操作系统问题')),
            (2, _('bug')),
            (3, _('其他问题')),
            (4, _('重复问题')),
            (5, _('第三方问题')),
        )
    )
    state = models.SmallIntegerField(
        _('问题状态'),
        default=-1,
        choices=(
            (-1, _('待解决')),
            (0, _('未解决')),
            (1, _('已解决')),
            (2, _('延期处理')),
            (3, _('不予处理')),
            (4, _('需第三方处理')),
        )
    )
    remark = models.CharField(_('备注'), max_length=200, default='', null=True, blank=True)

    class Meta:
        db_table = "chin_question"
        ordering = ['-create_time']
        verbose_name = _('问题汇总列表')
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.name)

    def profile(self):
        if len(str(self.content)) > 60:
            return '{}...'.format(str(self.content)[0:60])
        else:
            return str(self.content)

    profile.allow_tags = True
    profile.short_description = _('问题描述')

    def profile_remark(self):
        if len(str(self.remark)) > 60:
            return '{}...'.format(str(self.remark)[0:60])
        else:
            return str(self.remark)

    profile_remark.allow_tags = True
    profile_remark.short_description = _('备注')
