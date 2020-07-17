var DatePicker = tui.DatePicker;
    var container = document.getElementById('tui-date-picker-container');
var target = document.getElementById('tui-date-picker-target');


var instance = new DatePicker(container, {
    input: {
        element: target
    },

});

instance.getDate();
