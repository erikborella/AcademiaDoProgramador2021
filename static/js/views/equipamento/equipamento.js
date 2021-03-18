// Tradução dos nomes para o dataPicker
const months = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'];
const monthsShort = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'];
const weekdays = ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabádo'];
const weekdaysShort	= ['Dom', 'Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sab'];
const weekdaysAbbrev = ['D','S','T','Q','Q','S','S'];
const cancel = "Cancelar";
const clear = "Limpar";
const done = "Ok";

// Inicialiação do dataPicker
document.addEventListener('DOMContentLoaded', function() {
    let modals = document.querySelectorAll('.modal');
    M.Modal.init(modals);

    let elems = document.querySelectorAll('.datepicker');
    let instances = M.Datepicker.init(elems, 
        {
            "maxDate": new Date(),
            "format": "dd/mm/yyyy",
            "i18n": {
                "months": months,
                "monthsShort": monthsShort,
                "weekdays": weekdays,
                "weekdaysShort": weekdaysShort,
                "weekdaysAbbrev": weekdaysAbbrev,
                "cancel": cancel,
                "clear": clear,
                "done": done
            },
        }
    );
});


// Essa função quando chamada abre o dataPicker
// Necessaria para ser utiliada com o onFocus
function openDatePicker() {
    let elem = document.getElementById("dataDeFabricacao");
    M.Datepicker.getInstance(elem).open();
}