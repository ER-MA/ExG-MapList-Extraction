import get_map as gm
import get_map_status_exg as gme
import data_to_file as d2f


# ==========方法1==========
# 直接 get `.../ServerList/CurrentCs2MapStatus` 中的 Doc 文档。
# 随后用与官网相同的方式处理数据，最终得到一模一样的 excel 表格。

# 下面两步处理完后 `map_status_json` 里的数据就可以直接用到自己的项目里了（Json 格式）
map_status_doc = gme.get_current_exg_map_status()  # 从ExG官网获取实时地图状态列表的完整数据（为json格式）
map_status_json = gme.preprocess_data(map_status_doc)  # 预处理获取的数据（格式化，将数据转为易读的文本）

# 当然还可以用以下函数将其保存为 excel 表格。创意工坊的超链接什么的都打好了，和官网显示内容完全一致。
d2f.json_to_excel(map_status_json, 'ExG_实时地图状态列表')  # 将处理好的数据转存为excel（文件名后会自动补时间戳）
# 要存成 `.json` 文件方便调用可以用以下函数。（为方便阅读，格式化过了）
d2f.json_to_file(map_status_json, 'ExG_CurrentCs2MapStatus')
# ==========全自动 - 推荐==========


# ==========方法2==========
# 使用 chromedriver 配合 selenium 库获取数据，最后处理为 .csv 表格。
# 恭喜你，电脑里的 Chrome 再次喜加一（雾）

# 使用如下函数自动从 `https://list.darkrp.cn:9000/ServerList/Cs2MapList` 获取 ExG 所有地图列表
# gm.get_map_list_from_exg_map_list()

# 运行该函数后，会使用项目目录中的 `chromedriver.exe` 开启一个新的 Chrome 来读取数据。
# 读取将会持续约 10 秒左右，在此期间请勿进行其他操作。
# 运行完成后即可在项目根目录的 `output` 目录中获取到地图列表:`ExG_MapList_{timestamp}.csv`
# ==========全自动 - 不推荐==========


# ==========方法3==========
# 用户手动获取 html 格式的表格，用如下函数处理为 .csv 表格。

# 使用如下函数从 ExG 游戏菜单的预订地图菜单获取 ZE 地图列表
# gm.get_map_list_from_exg_map_ordering()

# 该函数使用前请先打开 ExG 游戏菜单 `https://list.darkrp.cn:6514/#` 进入 `主菜单/地图系统/预定地图`
# 按 F2 进入控制台，点击左上角“元素检查”按钮进入元素选择模式，选中地图下拉菜单。
# 随后右键其对应的 html 文本。文本内容形似如下格式。
# <select class="form-select" title="nominatemap">...</select>
# 使用 `Copy -> Copy outerHTML` 复制后，覆盖粘贴到本项目 `input` 录下的 `maps_html_from_exg_menu.txt` 中。
# 最后取消注释该函数，并运行本文件即可在项目根目录的 `output` 目录中获取到地图列表:`ExG_ZE_MapList_{timestamp}.csv`
# ==========半自动 - 应急用==========
