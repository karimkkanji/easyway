var today, datepicker;
today = new Date(new Date().getFullYear(), new Date().getMonth(), new Date().getDate());
$('.datepicker-home').datepicker({
    uiLibrary: 'bootstrap4',
    minDate: today,
    showOtherMonths: true,
    showOnFocus: true, 
    showRightIcon: false
});


