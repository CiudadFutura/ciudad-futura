(function () {

    var getCookie = function (name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = $.trim(cookies[i]);

                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    };

    var csrfSafeMethod = function (method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    };

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                var csrftoken = getCookie('csrftoken');
                // Send the token to same-origin, relative URLs only.
                // Send the token only if the method warrants CSRF protection
                // Using the CSRFToken value acquired earlier
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    var addToCartTimeout;

    $('.js-add-to-cart').on('submit', function (event) {

        if (addToCartTimeout) {
            clearTimeout(addToCartTimeout);
            $('#js-message').hide();
        }

        event.preventDefault();
        var form = $(event.currentTarget);
        $.post(form.attr('action'), form.serialize(), function (data) {
            if (data.success) {
                $('#js-message').show().find('#js-message-product').html(data.item.name);

                addToCartTimeout = setTimeout(function () {
                    $('#js-message').hide();
                }, 2000);
            } else {
                // TODO: display error (validation)...
            }
        });
    });

})();
