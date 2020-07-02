var Calendar = tui.Calendar;
var calendar = new Calendar('#calendar', {
  defaultView: 'month',
  taskView: true,
  template: {
    monthDayname: function(dayname) {
      return '<span class="calendar-week-dayname-name">' + dayname.label + '</span>';
    }
  }
});
 function onClickNavi(e) {
        var action = getDataAction(e.target);

        switch (action) {
            case 'move-prev':
                calendar.prev();
                break;
            case 'move-next':
                calendar.next();
                break;
            case 'move-today':
                calendar.today();
                break;
            default:
                return;
        }

        setRenderRangeText();
        setSchedules();
    }
 function setRenderRangeText() {
        var renderRange = document.getElementById('renderRange');
        var options = calendar.getOptions();
        var viewName = calendar.getViewName();
        var html = [];
        if (viewName === 'day') {
            html.push(moment(calendar.getDate().getTime()).format('MMM YYYY DD'));
        } else if (viewName === 'month' &&
            (!options.month.visibleWeeksCount || options.month.visibleWeeksCount > 4)) {
            html.push(moment(calendar.getDate().getTime()).format('MMM YYYY'));
        } else {
            html.push(moment(calendar.getDateRangeStart().getTime()).format('MMM YYYY DD'));
            html.push(' ~ ');
            html.push(moment(calendar.getDateRangeEnd().getTime()).format(' MMM DD'));
        }
        renderRange.innerHTML = html.join('');
    }
 $('#menu-navi').on('click', onClickNavi);