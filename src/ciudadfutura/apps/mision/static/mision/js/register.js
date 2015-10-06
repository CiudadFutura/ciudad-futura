$(document).ready(function() {
    var tpl = $($('#invite-form-tpl').html());
    var holder = $('#invites-holder');
    $('#add-invite').on('click', function (event) {
        event.preventDefault();
        holder.append(tpl.clone());
    });
});