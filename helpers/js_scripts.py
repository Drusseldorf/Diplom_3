class DragAndDrop:

    JS_SCRIPT = """
    var source = arguments[0];
    var target = arguments[1];
    var event = document.createEvent('MouseEvent');
    event.initMouseEvent('dragstart', true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
    source.dispatchEvent(event);
    event = document.createEvent('MouseEvent');
    event.initMouseEvent('dragenter', true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
    target.dispatchEvent(event);
    event = document.createEvent('MouseEvent');
    event.initMouseEvent('dragover', true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
    target.dispatchEvent(event);
    event = document.createEvent('MouseEvent');
    event.initMouseEvent('drop', true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
    target.dispatchEvent(event);
    event = document.createEvent('MouseEvent');
    event.initMouseEvent('dragend', true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
    source.dispatchEvent(event);
    """
