/**
 * Created by Development on 09/02/2017.
 */
$(function () {
    $("#register-form").submit(function () {
        var form = this;
        var card = {
            number:     $("#id_credit_card_number").val(),
            expMonth:   $("#id_expiry_month").val(),
            expYear:    $("#id_expiry_year").val(),
            vcc:        $("#id_vcc").val()
        };

        $("#validate_card_btn").attr("disable", true);
            Stripe.createToken(card, function(status, response){
                if (status === 200) {
                    console.log(status, response);
                    $("#credit-card-errors").hide();
                    $("#id_stripe_id").val(response.id);
                    form.submit();
                } else {
                    $("#stripe-error-message").text(response.error.message);
                    $("#credit-card-errors").show();
                    $("#validate_card_btn").attr("disable", false);
                }
            });
        return false;
    });
});