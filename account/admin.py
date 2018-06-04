import xadmin
from account.models import Address

# 全局配置
from xadmin import views


# 开启主题修改
class BaseStyleSettings:
    enable_themes = True
    use_boot_swatch = True


xadmin.site.register(views.BaseAdminView, BaseStyleSettings)


class GlobalSettings:
    site_title = '天猫后台管理系统'
    site_footer = '千锋互联科技有限公司'
    menu_style = 'accordion'  # 后台菜单样式修改


xadmin.site.register(views.CommAdminView, GlobalSettings)


class AddressAdmin:
    # 后台界面要显示的字段
    list_display = ['add_id', 'province', 'city']
    # 搜索
    search_fields = ['province', 'city']
    # 分页显示的条数
    list_per_page = 10


xadmin.site.register(Address, AddressAdmin)
