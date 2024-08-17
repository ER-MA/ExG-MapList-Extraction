import get_map


# ==========方法1==========
# 使用如下函数自动从 `https://list.darkrp.cn:9000/ServerList/Cs2MapList` 获取 ExG 所有地图列表
get_map.get_map_list_from_exg_map_list()

# 运行该函数后，会使用项目目录中的 `chromedriver.exe` 开启一个新的 Chrome 来读取数据。
# 读取将会持续约 10 秒左右，在此期间请勿进行其他操作。
# 运行完成后即可在项目根目录获取到地图列表:`ExG_MapList_{timestamp}.csv`
# ==========全自动 - 推荐==========


# ==========方法2==========
# 使用如下函数从 ExG 游戏菜单的预订地图菜单获取 ZE 地图列表
# get_map.get_map_list_from_exg_map_ordering()

# 该函数使用前请先打开 ExG 游戏菜单 `https://list.darkrp.cn:6514/#` 进入 `主菜单/地图系统/预定地图`
# 按 F2 进入控制台，点击左上角“元素检查”按钮进入元素选择模式，选中地图下拉菜单。
# 随后右键其对应的 html 文本。文本内容形似如下格式。
# <select class="form-select" title="nominatemap">...</select>
# 使用 `Copy -> Copy outerHTML` 复制后，覆盖粘贴到本项目根目录的 `maps_html_from_exg_menu.txt` 中。
# 最后取消注释该函数，并运行本文件即可在项目根目录获取到地图列表:`ExG_ZE_MapList_{timestamp}.csv`
# ==========半自动 - 应急用==========
