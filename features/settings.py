from screeninfo import get_monitors

window_width = None
window_height = None

for m in get_monitors():
    window_width = m.width
    window_height = m.height
