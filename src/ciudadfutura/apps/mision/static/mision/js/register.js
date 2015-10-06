$(document).ready(function() {
    var tpl = $($('#invite-form-tpl').html());
    var holder = $('#invites-holder');

    var maxCount = parseInt($('[name="invites"]').attr('max_count'));


    $('#add-invite').on('click', function (event) {
        event.preventDefault();
        var total = $('#invites-holder .invite-form').length + 1;
        if (total > maxCount) {
            return alert('La canidad de miembros no puede superar: ' + maxCount);
        }
        var form = tpl.clone();
        form.find('.invite-index').html(total);
        holder.append(form);

        $('[name="invites"]').val(total);
    });
});
