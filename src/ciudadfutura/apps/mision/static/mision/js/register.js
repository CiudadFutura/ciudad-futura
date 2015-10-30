$(document).ready(function() {
    var tpl = $($('#invite-form-tpl').html());
    var holder = $('#invites-holder');

    var maxCount = parseInt($('[name="invites"]').attr('max_count'));
    var minCount = parseInt($('[name="invites"]').attr('min_count'));


    var updateIndexes = function () {
        var total = $('#invites-holder .invite-form').each(function (i, obj) {
            $(obj).find('.invite-index').html(i + 1);
        }).length;
        $('[name="invites"]').val(total);
    };

    updateIndexes();

    // Add invite
    $('#add-invite').on('click', function (event) {
        event.preventDefault();
        var total = $('#invites-holder .invite-form').length + 1;
        if (total > maxCount) {
            return alert('La canidad de miembros no puede superar: ' + maxCount);
        }

        holder.append(tpl.clone());
        updateIndexes();
    });

    // Remove invite
    $(document).on('click', '#invites-holder .remove', function (event) {
        event.preventDefault();
        var total = $('#invites-holder .invite-form').length - 1;
        if (total < minCount) {
            return alert('La canidad de miembros no puede ser menor a: ' + minCount);
        }

        $(this).parents('.invite-form').remove();
        updateIndexes();
    });
});
