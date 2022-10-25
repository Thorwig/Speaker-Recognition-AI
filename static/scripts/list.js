navigator
    .mediaDevices

function refreshList(){
    var form = new FormData();
    $.ajax({
        type: 'POST',
        url: '/getlist',
        data: form,
        cache: false,
        processData: false,
        contentType: false
    }).done(function(data) {
        console.log(data);
    });
    window.location.reload();
}
//Refresh button 
trigger.onclick = e => {
    refreshList()
};

//Radio button click 
$('#table').on('click', 'input[name="radio"]',function() { 
    var form = new FormData();
    let value = this.getAttribute('id');
    form.append('user_id',value);
    $.ajax({
        type: 'POST',
        url: '/delete',
        data: form,
        cache: false,
        processData: false,
        contentType: false
    }).done(function(data) {
        console.log(data);
    });
    refreshList()
});

//Filter table
$('#search').keyup(function() {
    var $rows = $('.row');
    var val = '^(?=.*\\b' + $.trim($(this).val()).split(/\s+/).join('\\b)(?=.*\\b') + ').*$',
        reg = RegExp(val, 'i'),
        text;

    $rows.show().filter(function() {
        text = $(this).text().replace(/\s+/g, ' ');
        return !reg.test(text);
    }).hide();
});

//Sort table
function sortTable() {
    var table, rows, switching, i, x, y, shouldSwitch;
    table = document.getElementById("table");
    switching = true;
    while (switching) {
        switching = false;
        rows = table.rows;
        for (i = 1; i < (rows.length - 1); i++) {
            shouldSwitch = false;
            x = rows[i].getElementsByTagName("td")[0];
            y = rows[i + 1].getElementsByTagName("td")[0];
            if (x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase()) {
                shouldSwitch = true;
                break;
            }
        }
        if (shouldSwitch) {
        rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
        switching = true;
        }
    }
};

$(document).ready(function(){
    setTimeout(() => {sortTable() }, 100);
});

