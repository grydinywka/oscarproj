function initBuyModal() {
    $('a.add-to-cart').click(function(event) {
        var modal = $('#myModal');
        var img = $(this).parent().find('img').clone();
        var header = $(this).parent().find('h4').clone();
        var price = $(this).parent().find('p span.big-price').clone();

        modal.find('.img').html(img);
        modal.find('.h4').html(header);
        modal.find('#model-price').html(price);
        modal.modal('show');
        return false;
    });
}

$(document).ready(function() {
    initBuyModal();
});