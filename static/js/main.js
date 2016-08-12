function initBuyModal() {
    $('a.add-to-cart').click(function(event) {
        var modal = $('#myModal');
        var img = $(this).parent().find('img').clone();
        var header = $(this).parent().find('h4 strong').clone();
        var price = $(this).parent().find('p span.big-price').clone();

        modal.find('.img-modal').html(img);
        modal.find('h4').text(header.text());
        modal.find('#model-price').html(price);
        modal.modal({
            'keyboard': false,
//            'backdrop': false,
            'show': true
        });
        return false;
    });
}

function increaseDecrease() {
    var input_val = $('.increase-decrease input');
    $('#decrease').click(function() {
        input_val.val(input_val.val()-1);
    });
    $('#increase').click(function() {
        input_val.val(parseInt(input_val.val(), 10)+1);
    });
}

$(document).ready(function() {
    initBuyModal();
    increaseDecrease();
});