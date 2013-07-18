import random

options = dict(
    items = dict(
        helm     = dict( inv=(1,5), bank=(1,9), enabled=True ),
        shoulder = dict( inv=(2,5), bank=(2,9), enabled=True ),
        chest    = dict( inv=(3,5), bank=(3,9), enabled=True ),
        neck     = dict( inv=(4,5), bank=(4,9), enabled=True ),
        belt     = dict( inv=(4,6), bank=(4,10), enabled=True ),
        hand     = dict( inv=(5,5), bank=(5,9), enabled=True ),
        wrist    = dict( inv=(6,5), bank=(6,9), enabled=True ),
        ring1    = dict( inv=(7,5), bank=(7,9), enabled=True ),
        ring2    = dict( inv=(7,6), bank=(7,10), enabled=True, mod=KeyModifier.ALT ),
        legs     = dict( inv=(8,5), bank=(7,7), enabled=True ),
        feet     = dict( inv=(9,5), bank=(6,7), enabled=True ),
        mainhand = dict( inv=(10,3), enabled=True ),
        offhand  = dict( inv=(10,5), bank=(5,7), enabled=True, mod=KeyModifier.ALT )
    ),
    hotkeys = dict(
        equipGear  = Key.F1,
        moveToBank = Key.F2,
        moveToInv  = Key.F3
    ),
    randomError = 0,
    delay = 0,
    delayError = 0,
    autoOpenCloseCharScreen = True,
    autoAbility = False # example: autoAbility = "2"
)

rect = Screen().getBounds()
screenRes = (rect.width, rect.height)

uiOffsets = {
    (1920, 1080): dict(
        stash = dict( left=65, top=221, width=400, height=573 ),
        inventory = dict( left=1413, top=587, width=483, height=285 ),
        paperdoll = dict( left=1433, top=162, width=442, height=385 )
    ),
    (2560, 1600): dict(
        stash = dict( left=96, top=328, width=593, height=849 ),
        inventory = dict( left=1809, top=870, width=714, height=422 ),
        paperdoll = dict( left=1840, top=240, width=652, height=569 )
    )
}

paperdollRelWidth, paperdollRelHeight = 442, 385
charSlotOffsets = dict(
    # (left, top, width, height)
    helm     = (277, 8, 58, 58),
    shoulder = (203, 28, 58, 77),
    neck     = (353, 48, 46, 46),
    chest    = (270, 70, 72, 101),
    hand     = (180, 117, 57, 77),
    wrist    = (374, 117, 58, 78),
    belt     = (270, 117, 72, 28),
    ring1    = (191, 208, 35, 35),
    ring2    = (386, 208, 35, 35),
    legs     = (278, 211, 56, 77),
    mainhand = (180, 256, 57, 115),
    offhand  = (375, 256, 56, 115),
    feet     = (277, 294, 57, 77)
)

def getStashSlot(x, y):
    slotsWide, slotsTall = 7, 10
    offsets = uiOffsets[screenRes]['stash']
    xx = offsets['left'] + offsets['width']*((x-0.5)/slotsWide)
    yy = offsets['top'] + offsets['height']*((y-0.5)/slotsTall)
    return (xx, yy)

def getInvSlot(x, y):
    slotsWide, slotsTall = 10, 6
    offsets = uiOffsets[screenRes]['inventory']
    xx = offsets['left'] + offsets['width']*((x-0.5)/slotsWide)
    yy = offsets['top'] + offsets['height']*((y-0.5)/slotsTall)
    return (xx, yy)

def getCharSlot(name):
    paperdoll = uiOffsets[screenRes]['paperdoll']
    left, top, width, height = charSlotOffsets[name]
    x = paperdoll['left'] + paperdoll['width']*left/paperdollRelWidth + width/2
    y = paperdoll['top'] + paperdoll['height']*top/paperdollRelHeight + height/2
    return (x, y)

def equipGear(event):
    mouseLoc = Env.getMouseLocation()
    if options['autoOpenCloseCharScreen']:
        type("c")
    if 'autoAbility' in options:
        autoAbility = options['autoAbility']
        if autoAbility:
            type(autoAbility)
    for item in options['items']:
        itemOptions = options['items'][item]
        if itemOptions['enabled']:
            slotX, slotY = itemOptions['inv']
            x, y = getInvSlot(slotX, slotY)
            randomError = options['randomError']
            delay = options['delay']
            delayError = options['delayError']
            Settings.MoveMouseDelay = delay + random.random() * delayError
            x += random.randint(-randomError, randomError)
            y += random.randint(-randomError, randomError)
            if 'mod' in itemOptions:
                rightClick(Location(x,y), itemOptions['mod'])
            else:
                rightClick(Location(x,y))
    if options['autoOpenCloseCharScreen']:
        type("c")
    mouseMove(mouseLoc)

Env.addHotkey(options['hotkeys']['equipGear'], 0, equipGear)
