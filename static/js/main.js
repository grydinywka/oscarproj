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

$(document).ready(function() {
    initBuyModal();
});