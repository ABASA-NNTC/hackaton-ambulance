//Открытие файла
let state_data = 0;
function loadFile(o)
{
    var fr = new FileReader();
    fr.onload = function(e)
        {
            showDataFile(e, o);
            state_data += 1;
        };
    fr.readAsText(o.files[0]);
}

//Вывод файла
function showDataFile(e, o)
{ 
  var getCSVData = e.target.result;
  var rows = getCSVData.split("\n");
  var html = '<table border="1">';
  rows.forEach((data, index) => {
    html += "<tr>";
    var value = data.split(",");

    html += "<td>" + value[0] + "</td>";
    html += "<td>" + value[1] + "</td>";
    html += "<td>" + value[2] + "</td>";
    html += "<td>" + value[3] + "</td>";
    html += "<td>" + value[4] + "</td>";
    html += "<td>" + value[5] + "</td>";
    html += "<td>" + value[6] + "</td>";
    html += "<td>" + value[7] + "</td>";
    html += "<td>" + value[8] + "</td>";
    html += "<td>" + value[9] + "</td>";
    html += "<td>" + value[10] + "</td>";
    html += "<td>" + value[11] + "</td>";

    html += "</tr>";
  });
  html += '</table>';
  document.getElementById("data").innerHTML = html;
}

//Считывание css свойств
let data_file = document.getElementById("data");
let data_file_style = window.getComputedStyle(data_file,null).getPropertyValue("display");
let counter = 0;

//Функция считывания текущего display
function state_display() {
    if (data_file_style == 'block') {
    counter = 0;
    }
    else if (data_file_style == 'none') {
        counter = 1;
    }
}

//Кнопка, открывающая содержимое файла
function showFile() {
    warningImport();
    document.getElementsByClassName('data')[0].style.display="block";
    data_file_style = 'none';
    state_display();
    if (counter == 1 && state_data > 0) {
        document.getElementsByClassName('button_show_file')[0].style.display = "none";
        document.getElementsByClassName('button_close_file')[0].style.display = "flex";
    }
}

//Кнопка, закрывающая содержимое файла
function closeFile() {
    document.getElementsByClassName('data')[0].style.display="none";
    data_file_style = 'block';
    state_display();
    if (counter == 0) {
        document.getElementsByClassName('button_show_file')[0].style.display = "flex";
        document.getElementsByClassName('button_close_file')[0].style.display = "none";
    }
}

//Высвечивание ошибки
function warningImport() {
    if (state_data == 0) {
        document.getElementsByClassName('warning_import_file')[0].style.display = "flex";
    }
    else if (state_data > 0) {
        document.getElementsByClassName('warning_import_file')[0].style.display = "none";
    }
}