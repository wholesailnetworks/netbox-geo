from extras.plugins import PluginMenuButton, PluginMenuItem
from utilities.choices import ButtonColorChoices


point_buttons = [
    PluginMenuButton(
        link='plugins:netbox_geo:point_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
        color=ButtonColorChoices.GREEN
    )
]
path_buttons = [
    PluginMenuButton(
        link='plugins:netbox_geo:path_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
        color=ButtonColorChoices.GREEN
    )
]
polygon_buttons = [
    PluginMenuButton(
        link='plugins:netbox_geo:polygon_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
        color=ButtonColorChoices.GREEN
    )
]

menu_items = (
    PluginMenuItem(
        link='plugins:netbox_geo:point_list',
        link_text='Points',
        buttons=point_buttons
    ),
    PluginMenuItem(
        link='plugins:netbox_geo:path_list',
        link_text='Paths',
        buttons=path_buttons
    ),
    PluginMenuItem(
        link='plugins:netbox_geo:polygon_list',
        link_text='Polygons',
        buttons=polygon_buttons
    ),
)
