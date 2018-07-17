function blindioShowAlert(content, alert_class, hide_delay = 2000) {
    $("#blindio__alert_message__content").text(content);
    $("#blindio__alert_message").addClass(alert_class)
    $("#blindio__alert_message").show();
    setTimeout(function() {
        $("#blindio__alert_message").hide();
        $("#blindio__alert_message").removeClass(alert_class)
    }, hide_delay);
};

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
};

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});
